# Python ML

Course material and notebooks for learning core Python data analysis tools, including NumPy, Pandas, and Matplotlib.

## Repository Structure

```text
NBIHAK PAIVT26D - Kursmaterial/
├── Data/
│   └── cars_data.csv
├── Doc/
│   ├── ai_heretic_acemoglu.pdf
│   └── commodification_of_education_AI_monett_paquett.pdf
├── Matplotlib/
│   ├── matplotlib.ipynb
│   └── matplotlib_Terese.ipynb
├── NumPy/
│   ├── NumPy.ipynb
│   └── NumPy_Terese.ipynb
└── Pandas/
    ├── Pandas.ipynb
    ├── Pandas_Terese.ipynb
    └── README.md
```

## Contents

- `NumPy/` contains notebooks for working with arrays and numerical operations.
- `Pandas/` contains notebooks for loading, cleaning, filtering, sorting, and grouping tabular data.
- `Matplotlib/` contains notebooks for plotting and data visualization.
- `Data/cars_data.csv` is the sample dataset used by the Pandas exercises.
- `Doc/` contains supporting reading material.

## Getting Started

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the common notebook dependencies:

```bash
pip install notebook numpy pandas matplotlib
```

Start Jupyter Notebook:

```bash
jupyter notebook
```

Then open one of the `.ipynb` files from `NBIHAK PAIVT26D - Kursmaterial/`.

## Notes

- Run notebook cells in order so imports and variables are available.
- If a notebook cannot find `cars_data.csv`, update the file path to point to `NBIHAK PAIVT26D - Kursmaterial/Data/cars_data.csv`.
- The local `.venv/` folder is for your machine only and should not be committed.
