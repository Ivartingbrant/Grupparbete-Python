import matplotlib.pyplot as plt



def plot_monthly_data(ax, monthly_stats):
   # Två visualiseringar i samma diagram, AOV vs median
    ax.bar(monthly_stats.index.astype(str), monthly_stats["mean"])
    ax.plot(monthly_stats.index.astype(str), monthly_stats["median"], color="black")

    
    ax.set_title("Genomsnittligt ordervärde (AOV) vs median per månad")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Belopp (kr)")
    ax.grid(True, axis="y")

    plt.tight_layout()
    plt.setp(ax.get_xticklabels(), rotation=60)
    return ax


def plot_of_aov_and_median(ax, x, y, title, xlabel, ylabel, grid: bool = True):)
    x = _cat_for_plot(x)
    y = _num_for_plot(y)
    ax.bar(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis="y")
    return ax