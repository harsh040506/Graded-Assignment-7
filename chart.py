# chart.py

# 1. Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 2. Generate synthetic data
# Create a predictable random number generator for reproducibility
np.random.seed(42)

# Define months and customer segments
months = range(1, 13)
segments = ['New Customers', 'Returning Customers', 'VIP Customers']

# Generate data points
data = []
for month in months:
    for segment in segments:
        # Define base revenue and growth for each segment
        if segment == 'New Customers':
            base_revenue = 15000 + month * 500
        elif segment == 'Returning Customers':
            base_revenue = 30000 + month * 300
        else:  # VIP Customers
            base_revenue = 50000 + month * 200

        # Add seasonality (peak in Q4) using a sine wave
        seasonality_factor = 1 + (0.3 * np.sin((month - 1) * (np.pi / 6) + np.pi / 2))

        # Apply seasonality and add random noise
        seasonal_revenue = base_revenue * seasonality_factor
        noise = np.random.normal(0, seasonal_revenue * 0.05)  # 5% noise
        revenue = seasonal_revenue + noise
        
        data.append([month, segment, revenue])

# Create a pandas DataFrame
df = pd.DataFrame(data, columns=['Month', 'Customer Segment', 'Revenue'])

# 3. Create and Style the lineplot
# Set professional style and context for presentation
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.8)

# Set figure size for 512x512 output (8 inches * 64 dpi = 512 pixels)
plt.figure(figsize=(8, 8))

# Create the lineplot with distinct markers for each segment
lineplot = sns.lineplot(
    data=df,
    x='Month',
    y='Revenue',
    hue='Customer Segment',
    style='Customer Segment',
    markers=True,
    dashes=False,
    palette='viridis',
    linewidth=2.5
)

# 4. Set professional titles, labels, and ticks
plt.title('Monthly Revenue Trend by Customer Segment', fontsize=16, weight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue (USD)', fontsize=12)
plt.xticks(months)
plt.legend(title='Customer Segment')
plt.tight_layout()

# 5. Save the chart with specified dimensions
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

print("Chart 'chart.png' (512x512) generated successfully.")
