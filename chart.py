import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def create_visualization():
    # 1. Professional Styling
    sns.set_style("whitegrid")
    sns.set_context("talk")  # Larger font for presentations

    # 2. Generate Synthetic Data
    np.random.seed(42)  # For reproducibility
    
    segments = ['Bronze', 'Silver', 'Gold', 'Platinum']
    # Define distinct behaviors for each segment
    segment_params = {
        'Bronze': {'mean': 45, 'std': 15, 'n': 100},
        'Silver': {'mean': 120, 'std': 30, 'n': 100},
        'Gold': {'mean': 280, 'std': 60, 'n': 100},
        'Platinum': {'mean': 550, 'std': 120, 'n': 100}
    }

    data = []
    for segment in segments:
        params = segment_params[segment]
        # Generate realistic purchase amounts
        amounts = np.random.normal(params['mean'], params['std'], params['n'])
        # Clean data: no negative purchases
        amounts = np.maximum(amounts, 0)
        
        for amount in amounts:
            data.append({
                'Customer Segment': segment,
                'Purchase Amount ($)': amount
            })

    df = pd.DataFrame(data)

    # 3. Create Figure (8x8 inches @ 64 DPI = 512x512 pixels)
    plt.figure(figsize=(8, 8))

    # 4. Create Boxplot
    # Using a professional color palette
    custom_palette = sns.color_palette("viridis", n_colors=4)
    
    chart = sns.boxplot(
        x='Customer Segment', 
        y='Purchase Amount ($)', 
        data=df, 
        palette=custom_palette,
        linewidth=2
    )

    # 5. Add Titles and Labels
    plt.title('Customer Purchase Distribution by Segment', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Customer Loyalty Tier', fontsize=14, labelpad=10)
    plt.ylabel('Purchase Amount ($)', fontsize=14, labelpad=10)

    # 6. Save Chart
    # Using tight_layout to fit content within the fixed figure size without changing dimensions
    plt.tight_layout()
    
    # Saving with dpi=64 to ensure 512x512 output (8*64 = 512)
    plt.savefig('chart.png', dpi=64)
    print("Chart saved successfully as chart.png (512x512)")

if __name__ == "__main__":
    create_visualization()
