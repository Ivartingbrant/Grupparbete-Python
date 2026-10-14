"""
Läser in och bearbetar data
"""
import os
import csv


def load_data(filename="Data/ecommerce_sales.csv"):
    """Läser in data från en fil och konverterar värdena till lämpliga datatyper.
    Returns:
        list[dict]
        dict: Ett felmeddelande om filen inte hittas.
    """

    if os.path.exists(filename):
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=",")

            data = [
                {
                    "order_id": row["order_id"],
                    "date": row["date"],
                    "city": row["city"],
                    "category": row["category"],
                    "price": float(row["price"]),
                    "units": int(row["units"]),
                    "revenue": float(row["revenue"])
                }
                for row in reader
            ]

        return data
    return {"message": "No data found"}


if __name__ == "__main__":
    print(load_data()[-10:])
