# Unsupervised Learning Capstone

## Project Title
Wholesale Customers Unsupervised Learning Capstone

## Installation Instructions
**Important note for Windows users:** Please ensure you are using a standard Python installation from [python.org](https://www.python.org/downloads/) rather than MSYS2 or minimal environments, as those may lack pre-compiled packages and fail during installation.

To set up the environment and install dependencies, run the following commands in your terminal:
```bash
# Create a virtual environment using the Windows Python Launcher
py -m venv venv

# Activate the environment
.\venv\Scripts\activate

# Install the dependencies
pip install -r requirements.txt
```

## Usage
1. Download the `wholesale_customers.csv` file from the UCI Machine Learning Repository.
2. Place the dataset in the `data/` folder.
3. With your virtual environment activated, run the main pipeline script by executing:
```bash
python main.py
```

## Team Members
- Person 1: Initialization (.gitignore & README)
- Person 2: Data Loader (Error Handling)
- Person 3: EDA (Summary stats & Heatmap)
- Person 4: Preprocessing (Scikit-Learn Pipeline)
- Person 5: Dimensionality Reduction (PCA)
- Person 6: Clustering (K-Means)
- Person 7: Clustering (Hierarchical)
- Person 8: Clustering (DBSCAN)
- Person 9: Evaluation (Metrics & Visuals)