import torch

class Model:
    def __init__(self, model_path: str, device: str = "cuda:0"):
        self.device = torch.device(device if torch.cuda.is_available() else 'cpu')
        self.model = self._load_model(model_path)

    def _load_model(self, model_path: str):
        try:
            model = torch.load(model_path, map_location=self.device)
            model.eval()  # Set the model to evaluation mode
            model.to(self.device)  # Move the model to the specified device
            return model
        except Exception as e:
            raise RuntimeError(f"Failed to load the model from {model_path}: {e}")
