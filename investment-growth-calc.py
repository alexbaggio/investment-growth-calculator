# This program will calculate future value of an investment
import tkinter as tk

def calculate():
    PV = float(entry_pv.get())
    r = float(entry_r.get())
    t = float(entry_t.get())

    FV = PV * (1 + r) ** t

    result_label.config(text=f"Future Value: ${FV:.2f}")

root = tk.Tk()
root.title("Investment Calculator")
root.geometry("400x250")

tk.Label(root, text="Starting Amount").pack()
entry_pv = tk.Entry(root)
entry_pv.pack()

tk.Label(root, text="Annual Return (decimal)").pack()
entry_r = tk.Entry(root)
entry_r.pack()

tk.Label(root, text="Years").pack()
entry_t = tk.Entry(root)
entry_t.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()


