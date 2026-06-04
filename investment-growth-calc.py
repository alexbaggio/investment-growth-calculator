# This program will calculate future value of an investment
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create window
root = tk.Tk()
root.title("Investment Growth Calculator")
root.geometry("900x700")

# Title
title = tk.Label(
    root,
    text="Investment Growth Calculator",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

# Future value label
result_label = tk.Label(
    root,
    text="Future Value: $0.00",
    font=("Arial", 14)
)
result_label.pack(pady=10)

# Create figure for graph
fig = Figure(figsize=(7, 4), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


def update_graph(value=None):
    PV = principal_slider.get()
    r = rate_slider.get() / 100
    years = years_slider.get()

    values = []

    for year in range(years + 1):
        FV = PV * (1 + r) ** year
        values.append(FV)

    final_value = values[-1]

    result_label.config(
        text=f"Future Value: ${final_value:,.2f}"
    )

    ax.clear()
    ax.plot(range(years + 1), values)

    ax.set_title("Investment Growth Over Time")
    ax.set_xlabel("Years")
    ax.set_ylabel("Value ($)")
    ax.grid(True)

    canvas.draw()


# Starting Amount Slider
principal_label = tk.Label(
    root,
    text="Starting Amount ($)"
)
principal_label.pack()

principal_slider = tk.Scale(
    root,
    from_=0,
    to=100000,
    resolution=100,
    orient=tk.HORIZONTAL,
    length=500,
    command=update_graph
)
principal_slider.set(1000)
principal_slider.pack()

# Return Slider
rate_label = tk.Label(
    root,
    text="Annual Return (%)"
)
rate_label.pack()

rate_slider = tk.Scale(
    root,
    from_=0,
    to=15,
    resolution=0.1,
    orient=tk.HORIZONTAL,
    length=500,
    command=update_graph
)
rate_slider.set(7)
rate_slider.pack()

# Years Slider
years_label = tk.Label(
    root,
    text="Years"
)
years_label.pack()

years_slider = tk.Scale(
    root,
    from_=0,
    to=50,
    resolution=1,
    orient=tk.HORIZONTAL,
    length=500,
    command=update_graph
)
years_slider.set(10)
years_slider.pack()

# Initial graph
update_graph()

root.mainloop()