import pandas as pd
import matplotlib.pyplot as plt

def analyze_and_visualize_efficiency():
    """
    Analyzes and visualizes the quarterly equipment efficiency data.
    """
    # Data provided in the business case
    data = {
        'Quarter': ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024'],
        'EfficiencyRate': [70.1, 71.68, 79.77, 81.05]
    }
    df = pd.DataFrame(data)

    # --- Analysis ---
    average_efficiency = df['EfficiencyRate'].mean()
    industry_target = 90.0
    performance_gap = industry_target - average_efficiency

    print("--- Equipment Efficiency Analysis ---")
    print(f"Calculated Average Equipment Efficiency Rate: {average_efficiency:.2f}%")
    print(f"Industry Benchmark Target: {industry_target}%")
    print(f"Performance Gap to Target: {performance_gap:.2f} points")
    print("-----------------------------------")


    # --- Visualization ---
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the quarterly efficiency data
    ax.plot(df['Quarter'], df['EfficiencyRate'], marker='o', linestyle='-', color='royalblue', label='Quarterly Efficiency Rate')
    ax.plot([], [], ' ', label=f'2024 Average: {average_efficiency:.2f}%') # Add average to legend
    
    # Plot the industry target line
    ax.axhline(y=industry_target, color='red', linestyle='--', linewidth=2, label=f'Industry Target: {industry_target}%')

    # Add value labels to the data points
    for i, txt in enumerate(df['EfficiencyRate']):
        ax.annotate(f'{txt}%', (df['Quarter'][i], df['EfficiencyRate'][i]), textcoords="offset points", xytext=(0,10), ha='center')

    # Formatting the chart
    ax.set_title('Equipment Efficiency Rate Trend vs. Industry Target (2024)', fontsize=16, weight='bold')
    ax.set_ylabel('Efficiency Rate (%)', fontsize=12)
    ax.set_xlabel('Quarter', fontsize=12)
    ax.set_ylim(65, 95)
    ax.legend(loc='lower right')

    # Save the figure
    plt.tight_layout()
    plt.savefig('equipment_efficiency_chart.png', dpi=300)
    print("Chart saved as equipment_efficiency_chart.png")

if __name__ == '__main__':
    analyze_and_visualize_efficiency()
