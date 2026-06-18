"""
EDA - Housing Dataset

Kör scriptet från samma mapp som housing.csv:
python eda_housing.py
"""

import pandas as pd
import matplotlib.pyplot as plt


def find_price_column(df):
    """Försök hitta en rimlig priskolumn i datasetet."""
    possible_price_columns = ["price", "Price", "median_house_value", "SalePrice", "sale_price"]

    for col in possible_price_columns:
        if col in df.columns:
            return col

    return None


def main():
    # ------------------------------
    # 1. Läs in datasetet
    # ------------------------------

    # Byt filnamn om din fil heter något annat.
    df = pd.read_csv("housing.csv")

    print("De första 5 raderna i datasetet:")
    print(df.head())

    print("\nAntal rader och kolumner:")
    print(df.shape)

    print("\nInformation om datasetet:")
    print(df.info())

    print("\nStatistisk sammanfattning:")
    print(df.describe())

    # ------------------------------
    # 2. Kontrollera saknade värden
    # ------------------------------

    print("\nSaknade värden per kolumn:")
    print(df.isnull().sum())

    missing_values = df.isnull().sum()

    plt.figure(figsize=(10, 5))
    missing_values[missing_values > 0].plot(kind="bar")
    plt.title("Saknade värden i datasetet")
    plt.xlabel("Kolumner")
    plt.ylabel("Antal saknade värden")
    plt.tight_layout()
    plt.show()

    # ------------------------------
    # 3. Kontrollera datatyper
    # ------------------------------

    print("\nDatatyper:")
    print(df.dtypes)

    # ------------------------------
    # 4. Undersök priskolumnen
    # ------------------------------

    price_column = find_price_column(df)

    if price_column is None:
        print("\nIngen tydlig priskolumn hittades.")
        print("Kolumner i datasetet är:")
        print(df.columns)
    else:
        print(f"\nPriskolumn som används: {price_column}")

        print("\nStatistik för priser:")
        print(df[price_column].describe())

        plt.figure(figsize=(8, 5))
        plt.hist(df[price_column].dropna(), bins=30)
        plt.title("Fördelning av huspriser")
        plt.xlabel("Pris")
        plt.ylabel("Antal hus")
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(8, 5))
        plt.boxplot(df[price_column].dropna(), vert=False)
        plt.title("Boxplot över huspriser")
        plt.xlabel("Pris")
        plt.tight_layout()
        plt.show()

        print("\nDe 10 billigaste husen:")
        print(df.sort_values(by=price_column).head(10))

        print("\nDe 10 dyraste husen:")
        print(df.sort_values(by=price_column, ascending=False).head(10))

    # ------------------------------
    # 5. Undersök numeriska kolumner
    # ------------------------------

    numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

    print("\nNumeriska kolumner:")
    print(numeric_columns)

    df[numeric_columns].hist(figsize=(14, 10), bins=30)
    plt.suptitle("Histogram för numeriska kolumner")
    plt.tight_layout()
    plt.show()

    correlations = None

    # ------------------------------
    # 6. Samband mellan variabler
    # ------------------------------

    if price_column is not None:
        correlations = df[numeric_columns].corr()

        print("\nKorrelation med pris:")
        print(correlations[price_column].sort_values(ascending=False))

        price_corr = correlations[price_column].sort_values(ascending=False)

        plt.figure(figsize=(10, 5))
        price_corr.plot(kind="bar")
        plt.title("Korrelation mellan pris och andra numeriska variabler")
        plt.xlabel("Variabel")
        plt.ylabel("Korrelation")
        plt.tight_layout()
        plt.show()

    # ------------------------------
    # 7. Scatter plots
    # ------------------------------

    if price_column is not None:
        for col in numeric_columns:
            if col != price_column:
                plt.figure(figsize=(7, 5))
                plt.scatter(df[col], df[price_column], alpha=0.5)
                plt.title(f"Samband mellan {col} och {price_column}")
                plt.xlabel(col)
                plt.ylabel(price_column)
                plt.tight_layout()
                plt.show()

    # ------------------------------
    # 8. Hantera saknade värden
    # ------------------------------

    print("\nAntal saknade värden innan bearbetning:")
    print(df.isnull().sum())

    for col in numeric_columns:
        df[col] = df[col].fillna(df[col].median())

    categorical_columns = df.select_dtypes(include=["object"]).columns

    for col in categorical_columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    print("\nAntal saknade värden efter bearbetning:")
    print(df.isnull().sum())

    # ------------------------------
    # 9. Undersök kategoriska variabler
    # ------------------------------

    print("\nKategoriska kolumner:")
    print(categorical_columns)

    for col in categorical_columns:
        print(f"\nAntal unika värden i {col}:")
        print(df[col].value_counts())

        plt.figure(figsize=(8, 5))
        df[col].value_counts().head(10).plot(kind="bar")
        plt.title(f"De vanligaste värdena i {col}")
        plt.xlabel(col)
        plt.ylabel("Antal")
        plt.tight_layout()
        plt.show()

    # ------------------------------
    # 10. Slutsats
    # ------------------------------

    print("\nSLUTSATS:")
    print("Denna EDA undersöker datasetets struktur, saknade värden, prisfördelning,")
    print("samband mellan variabler och vilka faktorer som kan påverka om ett hus är dyrare eller billigare.")

    if price_column is not None and correlations is not None:
        strongest_corr = correlations[price_column].sort_values(ascending=False)
        print("\nVariabler som verkar ha starkast samband med priset:")
        print(strongest_corr.head(5))

        print("\nTolkning:")
        print("Hus med högre värden på variabler som har stark positiv korrelation med priset")
        print("tenderar att vara dyrare. Variabler med negativ korrelation kan däremot")
        print("hänga ihop med lägre huspriser.")


if __name__ == "__main__":
    main()
