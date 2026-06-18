# Run `eda_housing.py`

This document explains how to run the Python EDA script in this repository.

The script is located at the project root:

```text
eda_housing.py
```

The dataset is located in:

```text
Kunskapskontroll-Python_och_AI-strategi/housing.csv
```

Because `eda_housing.py` reads the file as `housing.csv`, you should run the script from the folder that contains the CSV file.

## Prerequisites

Use the existing virtual environment in the project:

```bash
cd /Users/stephenucheosedumme/PythonML
source .venv/bin/activate
```

The script uses:

- `pandas`
- `matplotlib`

## Run The Script

From the project root, run these commands:

```bash
cd /Users/stephenucheosedumme/PythonML
source .venv/bin/activate
cd Kunskapskontroll-Python_och_AI-strategi
MPLCONFIGDIR=/tmp/matplotlib python ../eda_housing.py
```

## What The Script Does

The script performs exploratory data analysis on `housing.csv`:

1. Loads the dataset with `pandas`.
2. Prints the first five rows.
3. Prints the number of rows and columns.
4. Shows dataset information and summary statistics.
5. Checks missing values.
6. Finds the price column, usually `median_house_value`.
7. Creates histograms, boxplots, correlation charts, and scatter plots.
8. Fills missing numeric values with the median.
9. Fills missing categorical values with the most common value.
10. Prints a short conclusion about which variables appear related to price.

## Expected Behavior

The terminal will print dataset information and analysis results.

Matplotlib chart windows will open during the run. Close each chart window to continue to the next plot.

## Troubleshooting

If you see this error:

```text
FileNotFoundError: [Errno 2] No such file or directory: 'housing.csv'
```

you are probably running the script from the wrong folder. Move into the dataset folder first:

```bash
cd /Users/stephenucheosedumme/PythonML/Kunskapskontroll-Python_och_AI-strategi
python ../eda_housing.py
```

If Matplotlib shows a warning about `.matplotlib` not being writable, use:

```bash
MPLCONFIGDIR=/tmp/matplotlib python ../eda_housing.py
```
