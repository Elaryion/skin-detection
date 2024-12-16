import uvicorn
import cv2
from load import device, model
from image_loader import load_image_base64
import torch
from present import BoundingBoxPlotter
import numpy as np
import nms
import base64

# TODO: Better logging
# TODO: Print qr for ip address to connect
# TODO: buildfile to fetch model

async def run_job(base64_img):
    print("About to load the image")
    image, image_tensor = load_image_base64(base64_img)
    print("Image loaded successfully.")
    print(f"Image shape: {image.shape}")
    print(f"Image tensor shape: {image_tensor.shape}")
    # Perform inference
    image_tensor = image_tensor.to(device)
    with torch.no_grad():
        preds = model([image_tensor.squeeze()])

    # Extract predictions
    preds = [{k: v.to('cpu') for k, v in t.items()} for t in preds]
    pred_boxes = preds[0]['boxes']
    pred_scores = preds[0]['scores']
    pred_labels = preds[0]['labels']

    # Apply NMS
    keep_indices, count = nms.nms(pred_boxes, pred_scores, 0.3)
    nms_boxes, nms_labels = pred_boxes[keep_indices[:count]], pred_labels[keep_indices[:count]]

    # Plot the results
    BoundingBoxPlotter.plot_with_bbox(image, nms_boxes.numpy().astype(np.int32), nms_labels.numpy()) 
    # Save the results
    img = BoundingBoxPlotter.encode_image_with_bbox(image, nms_boxes.numpy().astype(np.int32), nms_labels.numpy())

    jpg_img = cv2.imencode('.jpg', img)
    return base64.b64encode(jpg_img[1]).decode('utf-8')


async def read_body(receive):
    """
    Read and return the entire body from an incoming ASGI message.
    """
    body = b''
    more_body = True

    while more_body:
        message = await receive()
        body += message.get('body', b'')
        more_body = message.get('more_body', False)

    return body
    
async def app(scope, receive, send):
    assert scope['type'] == 'http'

    body = await read_body(receive)

    # print(body)
    img = await run_job(body)
    print(img)

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': img.encode('utf-8'),
    })

if __name__ == "__main__":
    uvicorn.run("serv:app", port=5000, log_level="info")
