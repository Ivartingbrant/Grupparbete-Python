from io_utils import load_data
import statistics

def average_order_value(data):
    total_revenue = 0
    
    for row in data:
        total_revenue += row["revenue"]

    if len(data) > 0:
        aov = total_revenue / len(data)
        return aov

    else:
        return 0

def median (data):
    revenues = []
    for row in data:
        revenues.append(row["revenue"])

        return statistics.median(revenues)

    
data = load_data()
print(f"AOV för hela året är: {round(average_order_value(data), 2)} kr")
print(f"Medianförsäljningen ligger på: {median(data)} kr under året.")