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
def total_revenue(data): #Räknar ut den totala intäkten
    return sum(row["revenue"] for row in data)

def total_units(data): #Räknar ut totala antal enheter sålda
    return sum(row["units"] for row in data)

