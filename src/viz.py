import matplotlib.pyplot as plt



def plot_monthly_data(ax, monthly_stats):
    # Denna rad ritar AOV-staplarna på exakt ditt sätt!
    ax.bar(monthly_stats.index.astype(str), monthly_stats["mean"])
    ax.plot(monthly_stats.index.astype(str), monthly_stats["median"], color="black")

    # Här bor alla dina egna inställningar från bilden:
    ax.set_title("Genomsnittligt ordervärde (AOV) vs median per månad")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Belopp (kr)")
    ax.grid(True, axis="y")

    plt.tight_layout()
    plt.setp(ax.get_xticklabels(), rotation=60)


