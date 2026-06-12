# Python ML - Housing EDA

This repository contains a Jupyter Notebook for exploratory data analysis of a housing dataset. The notebook loads `housing.csv`, inspects the data, checks summary statistics, and visualizes selected housing features with Pandas and Matplotlib.

## Repository Structure

```text
.
├── README.md
└── NBIHAK PAIVT26D - Kursmaterial/
    ├── eda_housing.ipynb
    └── housing.csv
```

## Files

- `NBIHAK PAIVT26D - Kursmaterial/eda_housing.ipynb` contains the housing exploratory data analysis workflow.
- `NBIHAK PAIVT26D - Kursmaterial/housing.csv` is the dataset used by the notebook.
- `README.md` explains the repository and how to run the notebook.

## Dataset

The housing dataset contains 20,640 rows and these columns:

- `longitude`
- `latitude`
- `housing_median_age`
- `total_rooms`
- `total_bedrooms`
- `population`
- `households`
- `median_income`
- `median_house_value`
- `ocean_proximity`

## Requirements

Use Python 3 with these packages:

- `notebook`
- `pandas`
- `matplotlib`

## Getting Started

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
pip install notebook pandas matplotlib
```

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open this notebook:

```text
NBIHAK PAIVT26D - Kursmaterial/eda_housing.ipynb
```

Run the notebook cells from top to bottom.

## Notes

- `housing.csv` should stay in the same folder as `eda_housing.ipynb`.
- If the dataset is moved, update the notebook's `DATA_FILE` path.
- The local `.venv/` folder is only for your machine and should not be committed.
