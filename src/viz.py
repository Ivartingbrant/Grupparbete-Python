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
