# from .io_utils import load_data
import statistics


# Ivar - start
def total_revenue(data):  # Räknar ut den totala intäkten
    return sum(row["revenue"] for row in data)


def total_units(data):  # Räknar ut totala antal enheter sålda
    return sum(row["units"] for row in data)
# Ivar - end

# Fredrik - start


def average_order_value(data):
    total_revenue_aov = 0

    for row in data:
        total_revenue_aov += row["revenue"]

    if len(data) > 0:
        aov = total_revenue_aov / len(data)
        return aov

    else:
        return 0


def calc_median(data):
    revenues = []
    for row in data:
        revenues.append(row["revenue"])

    return statistics.median(revenues)

# print(f"AOV för årets första sex månader är: {round(average_order_value(data), 2)} kr") #Kan vara bra att ha med i report sen
# print(f"Medianförsäljningen ligger på: {median(data)} kr under första halvåret.") #Kan vara bra att ha med i report sen
# Fredrik - end

# Casper - start


def category_analysis(data):
    category_counts = {}
    revenue_per_category = {}

    for row in data:
        category = row["category"]

        if category not in category_counts:
            category_counts[category] = 0
            revenue_per_category[category] = 0

        category_counts[category] += 1
        revenue_per_category[category] += row["revenue"]

    return category_counts, revenue_per_category
# Casper - end

# Mustafa - start


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
# Mustafa - end

# Srilatha - start


def top_categories(data):
    # Calculates total revenue per category and returns the top 3.
    category_totals = {}

    for row in data:
        category = row.get("category", "")
        try:
            revenue = float(row.get("revenue", 0))
        except ValueError:
            continue

        category_totals[category] = category_totals.get(
            category, 0.0) + revenue

    # Sort from highest revenue to lowest
    sorted_categories = sorted(
        category_totals.items(), key=lambda item: item[1], reverse=True
    )

    # Return only the top 3 items
    return sorted_categories[:3]


# print("\nTop 3 categories by revenue:") #Kan vara bra att ha med i report sen
# for category, revenue in top_categories(data): #Kan vara bra att ha med i report sen
#    print(f"{category}: {revenue:.2f}") #Kan vara bra att ha med i report sen
# Srilatha - end
# if __name__ == "__main__":
#     data = load_data()
#     print(f"Total revenue: {total_revenue(data)}")
#     print(f"Total units sold: {total_units(data)}")
#     print(f"Average order value: {average_order_value(data)}")
#     print(f"Median revenue: {calc_median(data)}")
#     print(f"Category analysis: {category_analysis(data)}")
#     print(f"Revenue by city: {revenue_by_city(data)}")
#     print(f"Top categories by revenue: {top_categories(data)}")
