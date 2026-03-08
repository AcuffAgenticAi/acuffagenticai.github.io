import pandas as pd
import os

class AttributionAgent:
    def __init__(self, filename):
        self.data_path = os.path.join(os.path.dirname(__file__), filename)
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.data_path)
            print(f"--- Data Loaded: {len(self.df)} transactions ---\n")
        except FileNotFoundError:
            print(f"Error: {self.data_path} not found.")

    def analyze_performance(self):
        if self.df is None: return
        
        # Group by channel to sum Revenue and Cost
        metrics = self.df.groupby('channel').agg({
            'revenue': 'sum',
            'cost': 'sum'
        })

        # Calculate ROAS: Revenue / Cost
        # We use fillna(0) for Organic channels where cost might be 0
        metrics['roas'] = (metrics['revenue'] / metrics['cost']).fillna(float('inf'))
        
        print(metrics.sort_values(by='roas', ascending=False))
        return metrics

if __name__ == "__main__":
    agent = AttributionAgent('marketing_data.csv')
    agent.load_data()
    agent.analyze_performance()
