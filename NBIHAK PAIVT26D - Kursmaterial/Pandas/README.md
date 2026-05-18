# Pandas Tutorial: `Pandas_Terese.ipynb`

This folder contains the `Pandas_Terese.ipynb` notebook with a beginner-friendly Pandas exercise using the `cars_data.csv` dataset.

## What this notebook covers

- Importing `pandas` and setting up the notebook environment
- Loading a CSV file into a `DataFrame`
- Inspecting the data with `head()`, `tail()`, and `info()`
- Cleaning data by removing rows with missing values using `dropna(..., inplace=True)`
- Calculating summary statistics like the mean of numeric columns
- Filtering rows by column values and membership tests
- Sorting data without modifying the original `DataFrame`
- Grouping data and computing aggregated values

## Dataset

- `cars_data.csv` is the dataset used in the notebook.
- The notebook loads it using `pd.read_csv("cars_data.csv")`.
- If the CSV is stored in a different folder, update the path accordingly.

## Notebook structure

1. Introduction and prerequisite reading
2. Importing Pandas
3. Exercise: explain what a CSV file is
4. Load `cars_data.csv` into `cars`
5. View the first 10 rows with `cars.head(10)`
6. View the last 5 rows with `cars.tail(5)`
7. Use `cars.info()` to inspect non-null values and column types
8. Remove rows with missing values using `cars.dropna(..., inplace=True)`
9. Calculate means for numeric columns
10. Filter rows where `company == "honda"`
11. Sort by `price` in descending order (non-inplace)
12. Select rows where `company` is one of `audi`, `bmw`, or `porsche`
13. Count cars per company
14. Find the maximum price for each company

## How to run

1. Open `Pandas_Terese.ipynb` in Jupyter or VS Code Notebook view.
2. Make sure `pandas` is installed in your active Python environment.
3. Run the first cell to import Pandas.
4. Run the remaining cells in order.

## Notes

- The notebook uses the alias `pd` for `pandas`.
- If you see `NameError: name 'pd' is not defined`, it means the import cell was not executed. Run:

```python
import pandas as pd
```

- The `dropna` operation in the notebook is performed with `inplace=True`, so it modifies `cars` directly.

