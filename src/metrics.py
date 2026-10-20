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
def total_revenue(data): #Räknar ut den totala intäkten
    return sum(row["revenue"] for row in data)

def total_units(data): #Räknar ut totala antal enheter sålda
    return sum(row["units"] for row in data)

