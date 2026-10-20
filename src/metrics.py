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