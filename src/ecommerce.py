"""EcommerceAnalyzer class: Analyzes sales data by calculating total revenue, 
total units sold, average order value, median revenue, revenue by city 
and product category, and the top three categories by revenue.
"""

from src.metrics import (
    total_revenue,
    total_units,
    average_order_value,
    calc_median,
    category_analysis,
    revenue_by_city,
    top_categories
)


class EcommerceAnalyzer:
    """Analyzes sales data and calculates key business metrics"""

    def __init__(self, data):
        """Initialize the analyzer"""
        self.__data = data

    @property
    def data(self):
        """Return sales data."""
        return self.__data

    def __str__(self):
        """Return a human-readable description"""
        return f"EcommerceAnalyzer med {len(self.__data)} rader data"

    def __repr__(self):
        """Return a string representation"""
        return f"EcommerceAnalyzer(d={self.__data!r})"

    def total_revenue(self):
        """Calculate the total revenue from sales"""
        return total_revenue(self.__data)

    def total_units(self):
        """Calculate the total number of units"""
        return total_units(self.__data)

    def average_order_value(self):
        """Calculate the average revenue per order"""
        return average_order_value(self.__data)

    def calc_median(self):
        """Calculate the median revenue"""
        return calc_median(self.__data)

    def category_analysis(self):
        """Calculate revenue by product category"""
        return category_analysis(self.__data)

    def revenue_by_city(self):
        """Calculate total revenue for each city"""
        return revenue_by_city(self.__data)

    def top_categories(self):
        """Return the top three product categories by revenue"""
        return top_categories(self.__data)
