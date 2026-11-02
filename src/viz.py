import matplotlib.pyplot as plt



def plot_monthly_data(ax, monthly_stats):
   # Två visualiseringar i samma diagram, AOV vs median
    ax.bar(monthly_stats.index.astype(str), monthly_stats["mean"], label="AOV - genomsnittligt ordervärde")
    ax.plot(monthly_stats.index.astype(str), monthly_stats["median"], color="black", label="Medianordervärde")
    
    ax.set_title("Genomsnittligt ordervärde (AOV) vs median per månad")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Belopp (kr/köp)")
    ax.grid(True, axis="y")
    ax.legend()

    plt.tight_layout()
    plt.setp(ax.get_xticklabels(), rotation=60)
    return ax
import matplotlib.ticker as ticker
import pandas as pd

from src.metrics import top_categories


def plot_category_analysis(category_counts, revenue_per_category):
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))

    # Revenue per category
    ax[0].bar(revenue_per_category.keys(), revenue_per_category.values())
    ax[0].set_title("Intäkt per kategori", fontsize=15)

    # ax[0].set_xlabel("Kategori")
    ax[0].set_ylabel("Intäkt", fontsize=12)
    ax[0].tick_params(axis="x", rotation=0)
    ax[0].grid(True, axis="y", linestyle="--", alpha=0.6)
    ax[0].tick_params(axis="both", labelsize=10)

    # Category counts
    ax[1].bar(category_counts.keys(), category_counts.values())
    ax[1].set_title("Antal per kategori", fontsize=15)
    # ax[1].set_xlabel("Kategori")
    ax[1].set_ylabel("Antal", fontsize=12)
    ax[1].tick_params(axis="x", rotation=0)
    ax[1].grid(True, axis="y", linestyle="--", alpha=0.6)

    ax[1].tick_params(axis="both", labelsize=10)

    # Show numbers instead of 1e6
    ax[0].yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

    plt.tight_layout()

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
