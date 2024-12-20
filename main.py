import numpy as np
import matplotlib.pyplot as plt

# Data for polynomial regression
sleep_hours = np.linspace(4, 10, 100)  # sleep duration from 4 to 10 hours
gpa = -0.03 * (sleep_hours - 7.5)**2 + 3.5  # quadratic relationship, max GPA at 7.5 hours

# Plotting the graph
plt.figure(figsize=(8, 6))
plt.plot(sleep_hours, gpa, label="Polynomial Regression Model", color="b", linewidth=2)
plt.scatter(7.5, 3.5, color="r", zorder=5)  # Marking the optimal point at 7.5 hours
plt.text(7.5, 3.5, "Optimal GPA", color="r", ha="center", va="bottom")

# Adding titles and labels
plt.title("Optimal Sleep Duration and GPA Trends", fontsize=14)
plt.xlabel("Sleep Duration (hours per night)", fontsize=12)
plt.ylabel("GPA", fontsize=12)
plt.grid(True)
plt.legend()

# Show the plot
plt.show()


###############################################################################################

# Simulated Data
students = 600
np.random.seed(42)
sleep_durations = np.random.normal(6.37, 0.85, students)  # Sleep durations for histogram
sleep_scatter = np.random.uniform(5, 8, students)  # Sleep durations for scatter plot
gpa_scatter = 3.0 + 0.07 * (sleep_scatter - 6.37) + np.random.normal(0, 0.1, students)  # GPA values for scatter
bins = [0, 6, 7, 10]  # Bins for GPA grouping
gpa_values = [3.25, 3.48, 3.51]  # Average GPA for <6h, 6-7h, >7h

# Plot 1: Histogram for Sleep Distribution
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.hist(sleep_durations, bins=15, color='skyblue', edgecolor='black')
plt.axvline(np.mean(sleep_durations), color='red', linestyle='dashed', linewidth=1, label="Mean Sleep Duration")
plt.title("Distribution of Nightly Sleep Duration Among Students")
plt.xlabel("Sleep Duration (hours)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Plot 2: Bar Chart for GPA by Sleep Duration Group
plt.subplot(3, 1, 2)
bars = plt.bar(["<6h", "6-7h", ">7h"], gpa_values, color=['orange', 'green', 'blue'])
for bar, gpa in zip(bars, gpa_values):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01, f"{gpa:.2f}",
             ha='center', va='bottom', fontsize=10, color='black')
plt.ylim(3.2, 3.6)  # Adjust y-axis for better visibility
plt.title("GPA by Sleep Duration Group (Enhanced)")
plt.xlabel("Sleep Duration Group")
plt.ylabel("Average GPA")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Plot 3: Scatter Plot for Sleep Duration vs GPA
plt.subplot(3, 1, 3)
plt.scatter(sleep_scatter, gpa_scatter, alpha=0.6, color='purple', edgecolors='black', label="Student Data")
z = np.polyfit(sleep_scatter, gpa_scatter, 1)  # Trend line
p = np.poly1d(z)
plt.plot(sleep_scatter, p(sleep_scatter), color='red', linestyle='--', linewidth=2, label="Trend Line")
min_gpa_idx = np.argmin(gpa_scatter)
max_gpa_idx = np.argmax(gpa_scatter)
plt.annotate("Lowest GPA", (sleep_scatter[min_gpa_idx], gpa_scatter[min_gpa_idx]),
             xytext=(sleep_scatter[min_gpa_idx] - 0.5, gpa_scatter[min_gpa_idx] - 0.1),
             arrowprops=dict(arrowstyle="->", color='blue'), color='blue', fontsize=10)
plt.annotate("Highest GPA", (sleep_scatter[max_gpa_idx], gpa_scatter[max_gpa_idx]),
             xytext=(sleep_scatter[max_gpa_idx] + 0.5, gpa_scatter[max_gpa_idx] + 0.1),
             arrowprops=dict(arrowstyle="->", color='green'), color='green', fontsize=10)
plt.title("Sleep Duration vs. GPA (Enhanced)")
plt.xlabel("Sleep Duration (hours)")
plt.ylabel("GPA")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Adjust layout and show plots
plt.tight_layout()
plt.show()