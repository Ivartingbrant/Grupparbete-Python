"""EcommerceAnalyzer class analyzes e-commerce sales data by calculating total revenue,
units sold, average order value, revenue by city and category,
and the top three categories by revenue.
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
    """Analyze e-commerce sales data and calculate key business metrics."""

    def __init__(self, data):
        """Initialize the analyzer"""
        self.data = data

    def __str__(self):
        """Return a human-readable description"""
        return f"EcommerceAnalyzer med {len(self.data)} rader data"

    def __repr__(self):
        """Return a string representation"""
        return f"EcommerceAnalyzer(d={self.data!r})"

    def total_revenue(self):
        """Calculate the total revenue from sales"""
        return total_revenue(self.data)

    def total_units(self):
        """Calculate the total number of units sold"""
        return total_units(self.data)

    def average_order_value(self):
        """Calculate the average revenue per order"""
        return average_order_value(self.data)

    def calc_median(self):
        """Calculate the median revenue"""
        return calc_median(self.data)

    def category_analysis(self):
        """Calculate revenue by product category"""
        return category_analysis(self.data)

    def revenue_by_city(self):
        """Calculate total revenue for each city"""
        return revenue_by_city(self.data)

    def top_categories(self):
        """Return the top three product categories by revenue."""
        return top_categories(self.data)
