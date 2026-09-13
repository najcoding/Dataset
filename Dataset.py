"""
Exploratory Data Analysis (EDA) - Spread & Visualization
Author: Your Name
Description:
    This script loads a dataset, checks the spread of numerical features,
    and visualizes them using histograms, boxplots, and violin plots.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# -------------------------------
# 1. Load Dataset
# -------------------------------
def load_dataset(file_path):
    """Load CSV dataset with error handling."""
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Dataset loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        sys.exit(1)

# -------------------------------
# 2. Display Spread Statistics
# -------------------------------
def display_spread(df):
    """Show descriptive statistics for numerical columns."""
    print("\n📊 Spread of Numerical Features:")
    print(df.describe().T)  # Transpose for better readability

# -------------------------------
# 3. Visualize Spread
# -------------------------------
def visualize_spread(df, output_dir="plots"):
    """Generate histograms, boxplots, and violin plots for numerical features."""
    os.makedirs(output_dir, exist_ok=True)
    numeric_cols = df.select_dtypes(include=['number']).columns

    if numeric_cols.empty:
        print("No numerical columns found for visualization.")
        return

    for col in numeric_cols:
        plt.figure(figsize=(12, 4))

        # Histogram
        plt.subplot(1, 3, 1)
        sns.histplot(df[col].dropna(), kde=True, color='skyblue')
        plt.title(f"Histogram - {col}")

        # Boxplot
        plt.subplot(1, 3, 2)
        sns.boxplot(x=df[col], color='lightgreen')
        plt.title(f"Boxplot - {col}")

        # Violin plot
        plt.subplot(1, 3, 3)
        sns.violinplot(x=df[col], color='lightcoral')
        plt.title(f"Violin Plot - {col}")

        plt.tight_layout()
        save_path = os.path.join(output_dir, f"{col}_spread.png")
        plt.savefig(save_path)
        plt.close()
        print(f"📁 Saved plot for '{col}' → {save_path}")

# -------------------------------
# 4. Main Execution
# -------------------------------
if __name__ == "__main__":
    # Example: Replace with your dataset path
    dataset_path = "students_scores.csv"  # <-- Change this to your CSV file

    df = load_dataset(dataset_path)
    display_spread(df)
    visualize_spread(df)

    print("\n✅ EDA completed. Check the 'plots' folder for visualizations.")
