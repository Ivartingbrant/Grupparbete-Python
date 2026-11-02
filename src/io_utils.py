"""
Reads and processes data from a CSV file.
"""
import csv


def load_data(filename="Data/ecommerce_sales.csv"):
    """Reads data from a file and converts the values to data types
    Returns:
        list[dict]

    Raises:
        FileNotFoundError: An error message if the file is not found
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
        print("File not found")


if __name__ == "__main__":
    print(load_data()[:10])
