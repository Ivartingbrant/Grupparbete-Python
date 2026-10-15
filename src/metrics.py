def total_revenue(data): #Räknar ut den totala intäkten
    return sum(row["revenue"] for row in data)

def total_units(data): #Räknar ut totala antal enheter sålda
    return sum(row["units"] for row in data)

