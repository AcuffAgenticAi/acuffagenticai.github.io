import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

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
        
        # Group by channel
        metrics = self.df.groupby('channel').agg({
            'revenue': 'sum',
            'cost': 'sum'
        }).reset_index()

        # Calculate ROAS (Handle zero cost for organic)
        metrics['roas'] = metrics.apply(
            lambda x: x['revenue'] / x['cost'] if x['cost'] > 0 else x['revenue'], 
            axis=1
        )
        
        print(metrics.sort_values(by='roas', ascending=False))
        self.create_visual(metrics)
        return metrics

    def create_visual(self, metrics):
        plt.figure(figsize=(10, 6))
        sns.barplot(x='channel', y='roas', data=metrics, palette='viridis')
        plt.title('Marketing Channel Performance (ROAS)')
        plt.ylabel('Return on Ad Spend (ROAS)')
        plt.xlabel('Channel')
        
        # Save the report to your folder
        report_path = os.path.join(os.path.dirname(__file__), 'roas_report.png')
        plt.savefig(report_path)
        print(f"\n--- Visual Report Saved: {report_path} ---")

if __name__ == "__main__":
    agent = AttributionAgent('marketing_data.csv')
    agent.load_data()
    agent.analyze_performance()
