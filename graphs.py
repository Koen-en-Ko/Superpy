from matplotlib import pyplot as plt
from datetime import date

#add export date to name pdf
today = date.today()

def get_graph(x_list, y_list, type):
    plt.bar(x_list, y_list, zorder=3)
    plt.xticks(rotation=90)
    plt.xlabel("Days")
    plt.ylabel(type)
    plt.title(f"{type} over last week")
    plt.tight_layout()
    plt.grid(zorder=0)
    plt.savefig(f"{today}-{type}_Graphic.pdf")
    plt.show()
