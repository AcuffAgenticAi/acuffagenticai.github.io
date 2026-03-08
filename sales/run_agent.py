import pandas as pd
import os

class AttributionAgent:
    def __init__(self, filename):
        self.data_path = os.path.join(os.path.dirname(__file__), filename)
        self.df = None

    def load_data(self):
        try:
            # Attempt to load your marketing data
            self.df = pd.read_csv(self.data_path)
            print(f"Successfully loaded {len(self.df)} rows from {self.data_path}")
        except FileNotFoundError:
            print(f"Error: {self.data_path} not found. Please ensure your CSV is in the sales folder.")

    def run_last_touch_analysis(self):
        if self.df is None: return
        
        # Simple logic: Group by channel and sum conversions/revenue
        # Assumes your CSV has 'channel' and 'revenue' columns
        if 'channel' in self.df.columns and 'revenue' in self.df.columns:
            attribution = self.df.groupby('channel')['revenue'].sum().sort_values(ascending=False)
            print("\n--- Last-Touch Revenue Attribution ---")
            print(attribution)
            return attribution
        else:
            print("CSV missing 'channel' or 'revenue' columns.")

if __name__ == "__main__":
    # Change 'marketing_data.csv' to your actual data filename
    agent = AttributionAgent('marketing_data.csv') 
    agent.load_data()
    agent.run_last_touch_analysis()
