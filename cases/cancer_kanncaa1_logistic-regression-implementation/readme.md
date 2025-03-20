# Logistic Regression Implementation

## Overview

This project demonstrates the implementation of logistic regression from scratch and compares its performance with `sklearn`'s logistic regression model. The dataset used is the **Breast Cancer Wisconsin (Diagnostic) Data Set**, where the goal is to predict whether a tumor is malignant (M) or benign (B) based on given features.

## Dataset

The dataset is located in `input/data.csv` and contains the following:

- The `diagnosis` column represents the classification target:
  - `M` = Malignant
  - `B` = Benign

## Steps in the Notebook

The Jupyter Notebook `logistic-regression-implementation.ipynb` follows these steps:

1. **Load the Data**: Read `data.csv` into a Pandas DataFrame.
2. **Normalize Features**: Perform manual normalization of feature matrix `X`.
3. **Train/Test Split**: Split the dataset into training and testing sets.
4. **Implement Key Functions**:
   - Initialize **weights** and **biases**.
   - Define the **sigmoid function** to ensure `y` values remain between 0 and 1.
   - Implement **forward and back propagation**.
   - Update learning parameters using gradient descent.
   - Implement a **prediction function**.
   - Build the complete **logistic regression model**.
5. **Train and Evaluate the Model**:
   - Train the logistic regression model and estimate its cost.
   - Compute **train/test accuracy** for the custom implementation (\~94%).
   - Compare performance with `sklearn`'s logistic regression (\~97%).

## Results

- **Custom Logistic Regression**: \~94% accuracy
- **Scikit-learn Logistic Regression**: \~97% accuracy

## How to Run

1. Install necessary dependencies (if not already installed):
   ```bash
   pip install numpy pandas scikit-learn matplotlib
   ```
2. Open and run the Jupyter Notebook:
   ```bash
   jupyter notebook logistic-regression-implementation.ipynb
   ```

## Dependencies

- Python 3.x
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Author

Based on the original implementation by [kanncaa1](https://www.kaggle.com/kanncaa1) on Kaggle.

---

This README provides a structured guide to understand and execute the project effectively. 🚀

