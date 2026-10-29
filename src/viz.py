import pandas as pd
import matplotlib.pyplot as plt

from metrics import top_categories

# Srilatha_start
def plot_revenue_by_category(top_categories_by_revenue):
    """Plot the three product categories with the highest revenue."""
    chart_data = pd.DataFrame(
        top_categories_by_revenue, columns=["category", "revenue"]
    )

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(chart_data["category"], chart_data["revenue"], color="steelblue")
    ax.set_title("Top 3 Categories by Revenue")
    ax.set_xlabel("Category")
    ax.set_ylabel("Revenue")
    ax.grid(True, axis="y")
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
    plt.tight_layout()


def main():
    """Load data and display the top categories by revenue."""
    data = pd.read_csv("Data/ecommerce_sales.csv")
    category_revenues = top_categories(data.to_dict(orient="records"))
    plot_revenue_by_category(category_revenues)
    plt.show()
# Srilatha_end

if __name__ == "__main__":
    main()
