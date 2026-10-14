"""
Läser in och bearbetar data
"""
import csv


def load_data(filename="Data/ecommerce_sales.csv"):
    """Läser in data från en fil och konverterar värdena till lämpliga datatyper.
    Returns:
        list[dict]
        dict: Ett felmeddelande om filen inte hittas.
    """
    try:
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=",")

            data = []

            for row in reader:
                row["price"] = float(row["price"])
                row["units"] = int(row["units"])
                row["revenue"] = float(row["revenue"])
                data.append(row)

        return data

    except FileNotFoundError:
        print("Hittar inte filen")


if __name__ == "__main__":
    print(load_data()[:10])
