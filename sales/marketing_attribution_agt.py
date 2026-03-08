import pandas as pd
import numpy as np

class MarketingAttributionAgent:
    def __init__(self, spend_data, conversion_data):
        """
        Initialize with spend and conversion DataFrames.
        spend_data: [Channel, Spend]
        conversion_data: [UserID, channel_path, revenue]
        """
        self.spend = spend_data
        self.conversions = conversion_data

    def calculate_u_shaped_attribution(self):
        """
        U-Shaped Logic: 40% First, 40% Last, 20% distributed in middle.
        """
        attributed_results = []
        
        for index, row in self.conversions.iterrows():
            touches = row['channel_path'].split(' > ')
            revenue = row['revenue']
            num_touches = len(touches)

            if num_touches == 1:
                attributed_results.append({touches[0]: revenue})
            elif num_touches == 2:
                attributed_results.append({touches[0]: revenue * 0.5, touches[1]: revenue * 0.5})
            else:
                # 40% to first and last, 20% split among the rest
                middle_weight = 0.20 / (num_touches - 2)
                weights = [0.40] + [middle_weight] * (num_touches - 2) + [0.40]
                
                for i, channel in enumerate(touches):
                    attributed_results.append({channel: revenue * weights[i]})

        # Aggregate all results into a single series
        df_results = pd.DataFrame(attributed_results).sum()
        return df_results

    def calculate_roi(self):
        """
        Maps spend against attributed revenue to calculate ROAS.
        """
        attributed_rev = self.calculate_u_shaped_attribution()
        roi_report = []

        for channel, rev in attributed_rev.items():
            # Match spend to the channel
            channel_spend = self.spend[self.spend['Channel'] == channel]['Spend'].sum()
            roas = rev / channel_spend if channel_spend > 0 else 0
            
            roi_report.append({
                "Channel": channel,
                "Attributed_Revenue": round(rev, 2),
                "Spend": channel_spend,
                "ROAS": round(roas, 2)
            })

        return pd.DataFrame(roi_report).sort_values(by="ROAS", ascending=False)

    def get_attribution_summary(self):
        """Returns a high-level summary of the top performing channel."""
        roi_df = self.calculate_roi()
        if not roi_df.empty:
            top_channel = roi_df.iloc[0]['Channel']
            return f"Strategic Insight: {top_channel} is your highest performing channel based on U-Shaped ROAS."
        return "No data available."

# --- Example of how to run the agent ---
# spend_df = pd.DataFrame({'Channel': ['LinkedIn', 'Google Ads'], 'Spend': [1000, 500]})
# conv_df = pd.DataFrame({'channel_path': ['LinkedIn > Google Ads'], 'revenue': [2000]})
# agent = MarketingAttributionAgent(spend_df, conv_df)
# print(agent.calculate_roi())
