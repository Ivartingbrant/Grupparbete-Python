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
import collections
from io_utils import load_data

data = load_data()
def category_analysis(data):
    category_counts = collections.Counter()
    revenue_per_category = collections.defaultdict(float)

    for row in data:
        category = row["category"]
        category_counts[category] += 1
        revenue_per_category[category] += row["revenue"]

    return category_counts, revenue_per_category

category_counts, revenue_per_category = category_analysis(data)
print(category_counts)

for category, revenue in revenue_per_category.items():
    print(f"{category}: {revenue:.2f}")
def revenue_by_city(data):
    """Summerar intäkterna per stad, avrundat till två decimaler."""
    city_revenue = {}

    for row in data:
        city = row["city"]
        revenue = row["revenue"]

        if city not in city_revenue:
            city_revenue[city] = 0

        city_revenue[city] += revenue

    for city in city_revenue:
        city_revenue[city] = round(city_revenue[city], 2)

    return city_revenue
# Srilatha - start
def top_categories(data):
    #Calculates total revenue per category and returns the top 3.
    category_totals = {}
    
    for row in data:
        category = row.get("category", "")
        try:
            revenue = float(row.get("revenue", 0))
        except ValueError:
            continue
            
        category_totals[category] = category_totals.get(category, 0.0) + revenue
        
    # Sort from highest revenue to lowest
    sorted_categories = sorted(
        category_totals.items(), key=lambda item: item[1], reverse=True
    )
    
    # Return only the top 3 items
    return sorted_categories[:3]


print("\nTop 3 categories by revenue:")
for category, revenue in top_categories(data):
    print(f"{category}: {revenue:.2f}")

# Srilatha - end
def total_revenue(data): #Räknar ut den totala intäkten
    return sum(row["revenue"] for row in data)

def total_units(data): #Räknar ut totala antal enheter sålda
    return sum(row["units"] for row in data)
