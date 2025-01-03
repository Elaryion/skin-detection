# Skin Detection

This repository contains a skin detection project. Below are the instructions for setting up the environment and running the project.

## Environment Setup

To reproduce the environment used in this project, make sure you have [uv](https://docs.astral.sh/uv/getting-started/installation/#installation-methods)

## Important Note

- **Model File**:  
  The `models` directory does not contain the trained model by default.  
  You will need to obtain the model file from the project maintainer and place it inside the `models` directory.
  
## Running the Code

To run the skin detection server, use the following command:

```bash
uv run src/serv.py
```

## Testing
To run the skin detection code, use the following command:

```bash
uv run src/pred.py
```

This will execute the script located in the `src` folder to perform skin detection.


---
