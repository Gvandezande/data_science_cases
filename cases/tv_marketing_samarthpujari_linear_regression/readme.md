# Linear Regression Implementation

## Overview
This project demonstrates the implementation of linear regression using multiple approaches: NumPy, Scikit-learn, and Gradient Descent. The dataset used is `tvmarketing.csv`, which contains information on **marketing costs** and **sales**.

## Dataset
The dataset is located in `tvmarketing.csv` and contains:
- A column for **marketing costs**.
- A column for **sales**, which serves as the target variable.

## Steps in the Notebook
The Jupyter Notebook `Optimization_Using_Gradient_Descent_in_Linear_Regression.ipynb` follows these steps:

1. **Load the Data**: Read `tvmarketing.csv` into a Pandas DataFrame.
2. **Apply Linear Regression**:
   - Using **NumPy**.
   - Using **Scikit-learn**.
   - Using **Gradient Descent**.
3. **Testing and Validation**:
   - Pre-written tests from `w2_unittest.py` are used for validation.

## Testing Functions (`w2_unittest.py`)
The testing functions ensure correctness at different stages:

- **`test_load_data(target_adv)`**: Validates that the dataset is correctly loaded as a Pandas DataFrame with 200 rows and 2 columns.
- **`test_pred_numpy(target_pred_numpy)`**: Checks if the NumPy-based linear regression prediction function produces correct values.
- **`test_sklearn_fit(target_lr_sklearn)`**: Ensures that a Scikit-learn `LinearRegression` model has been correctly trained and contains the expected coefficients.
- **`test_sklearn_predict(target_pred_sklearn, input_lr_sklearn)`**: Verifies that predictions from a trained Scikit-learn model match expected values.
- **`test_partial_derivatives(target_dEdm, target_dEdb, input_X_norm, input_Y_norm)`**: Tests the correctness of the computed partial derivatives for gradient descent.
- **`test_gradient_descent(target_gradient_descent, input_dEdm, input_dEdb, input_X_norm, input_Y_norm)`**: Validates the gradient descent implementation by comparing optimized values of `m` and `b` with expected results.

## How to Run
1. Install necessary dependencies (if not already installed):
   ```bash
   pip install numpy pandas scikit-learn matplotlib
   ```
2. Open and run the Jupyter Notebook:
   ```bash
   jupyter notebook Optimization_Using_Gradient_Descent_in_Linear_Regression.ipynb
   ```

## Dependencies
- Python 3.x
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Author
Based on the original implementation by [samarthpujari](https://www.kaggle.com/samarthpujari) on Kaggle.

---
This README provides a structured guide to understand and execute the project effectively. 🚀

