# Skin Detection

This repository contains a skin detection project. Below are the instructions for setting up the environment and running the project.

## Environment Setup

To reproduce the environment used in this project, make sure you have the following:

- **Python Version**: `3.12.7`
- **PyTorch with CUDA Support**:

  Install PyTorch and its dependencies using the following command:

  ```bash
  uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
  ```

## Important Note

- **Model File**:  
  The `models` directory does not contain the trained model by default.  
  You will need to obtain the model file from the project maintainer and place it inside the `models` directory.

## Running the Code

To run the skin detection code, use the following command:

```bash
uv run ./src/pred.py
```

This will execute the script located in the `src` folder to perform skin detection.

---

Now the `README.md` file includes clear instructions to run the code using `uv run ./src/pred.py`.
