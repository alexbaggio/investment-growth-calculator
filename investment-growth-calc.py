import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------- WINDOW ----------

root = tk.Tk()
root.title("Investment Growth Calculator")
root.geometry("1200x700")
root.configure(bg="#1e1e1e")

# ---------- LAYOUT ----------

controls = tk.Frame(root, bg="#1e1e1e")
controls.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=20)

graph_frame = tk.Frame(root, bg="#1e1e1e")
graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# ---------- TITLE ----------

title = tk.Label(
    controls,
    text="Investment Growth",
    font=("Helvetica", 22, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title.pack(pady=(0, 20))

result_label = tk.Label(
    controls,
    text="$0",
    font=("Helvetica", 20),
    fg="#4ade80",
    bg="#1e1e1e"
)
result_label.pack(pady=(0, 20))

# ---------- GRAPH ----------

fig = Figure(figsize=(8, 5), dpi=100)
ax = fig.add_subplot(111)

fig.patch.set_facecolor("#1e1e1e")
ax.set_facecolor("#2b2b2b")

canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# ---------- UPDATE ----------

def update_graph(value=None):

    PV = principal_slider.get()
    C = contribution_slider.get()
    r = rate_slider.get() / 100
    years = years_slider.get()

    values = []

    current = PV

    for year in range(years + 1):
        values.append(current)
        current = current * (1 + r) + C

    final_value = values[-1]

    result_label.config(
        text=f"${final_value:,.0f}"
    )

    ax.clear()

    ax.plot(
        range(years + 1),
        values,
        linewidth=3
    )

    ax.set_title(
        "Portfolio Value Over Time",
        color="white",
        fontsize=14
    )

    ax.set_xlabel("Years", color="white")
    ax.set_ylabel("Value ($)", color="white")

    ax.tick_params(colors="white")

    for spine in ax.spines.values():
        spine.set_color("white")

    ax.grid(alpha=0.3)

    canvas.draw()

# ---------- SLIDER HELPER ----------

def create_slider(text, start, end, step, default):

    label = tk.Label(
        controls,
        text=text,
        fg="white",
        bg="#1e1e1e",
        font=("Helvetica", 11)
    )
    label.pack(anchor="w")

    slider = tk.Scale(
        controls,
        from_=start,
        to=end,
        resolution=step,
        orient=tk.HORIZONTAL,
        length=300,
        bg="#1e1e1e",
        fg="white",
        highlightthickness=0,
        troughcolor="#444",
        command=update_graph
    )

    slider.set(default)
    slider.pack(pady=(0, 15))

    return slider

# ---------- SLIDERS ----------

principal_slider = create_slider(
    "Starting Amount ($)",
    0,
    100000,
    100,
    1000
)

contribution_slider = create_slider(
    "Annual Contribution ($)",
    0,
    50000,
    100,
    5000
)

rate_slider = create_slider(
    "Annual Return (%)",
    0,
    15,
    0.1,
    7
)

years_slider = create_slider(
    "Years",
    0,
    50,
    1,
    30
)

update_graph()

root.mainloop()