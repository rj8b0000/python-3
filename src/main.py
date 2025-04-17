import numpy as np
import tkinter as tk
from tkinter import ttk

# Load data from CSV file
data = np.loadtxt('../data/sample_data.csv', delimiter=',', skiprows=1)

# Basic analysis
mean_value = np.mean(data)
median_value = np.median(data)
std_dev = np.std(data)

# GUI Setup
root = tk.Tk()
root.title("NumPy Data Analysis")
root.geometry("300x200")

# Labels for results
ttk.Label(root, text="Data Analysis Results").grid(row=0, column=0, columnspan=2, pady=10)
ttk.Label(root, text=f"Mean: {mean_value:.2f}").grid(row=1, column=0, padx=10, pady=5)
ttk.Label(root, text=f"Median: {median_value:.2f}").grid(row=2, column=0, padx=10, pady=5)
ttk.Label(root, text=f"Standard Deviation: {std_dev:.2f}").grid(row=3, column=0, padx=10, pady=5)

# Start GUI
root.mainloop()