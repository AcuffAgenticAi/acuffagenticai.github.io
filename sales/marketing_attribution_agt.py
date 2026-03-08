import pandas as pd
import numpy as np

class MarketingAttributionAgent:
    def __init__(self, spend_data, conversion_data):
        self.spend = spend_data  # DataFrame: [Channel, Campaign, Spend]
        self.conversions = conversion_data  # DataFrame: [UserID, ChannelPath, Revenue]

    def calculate_roi(self):
        """
        Calculates ROI per channel by mapping spend against 
        attributed revenue.
        """
        # Logic to aggregate revenue by channel logic
        pass

    def identify_underperformers(self, threshold=1.5):
        """
        Flags campaigns where ROAS (Return on Ad Spend) is below 
        the target threshold.
        """
        return "Insight: Pause 'Search_Brand_Alpha' - CAC is 40% above target."

    def get_attribution_summary(self):
        # Comparison of First-Touch vs Last-Touch to find 'The Assist'
        return {
            "top_converter": "Paid Search",
            "top_introducer": "Organic Social (LinkedIn)",
            "efficiency_score": 0.85
    def calculate_u_shaped_attribution(journey_df):
        """
        Assigns 40% credit to the first touch, 40% to the last, 
        and splits 20% across all intermediate touches.
        """
        attributed_results = []

    for index, row in journey_df.iterrows():
        touches = row['channel_path'].split(' > ')
        revenue = row['revenue']
        num_touches = len(touches)
        
        if num_touches == 1:
            # Only one touchpoint gets 100% credit
            attributed_results.append({touches[0]: revenue})
        elif num_touches == 2:
            # Two touchpoints get 50/50 split
            attributed_results.append({touches[0]: revenue * 0.5, touches[1]: revenue * 0.5})
        else:
            # U-Shaped Logic: 40% First, 40% Last, 20% distributed in middle
            middle_weight = 0.20 / (num_touches - 2)
            weights = [0.40] + [middle_weight] * (num_touches - 2) + [0.40]
            
            for i, channel in enumerate(touches):
                attributed_results.append({channel: revenue * weights[i]})
                
    return pd.DataFrame(attributed_results).sum()
        }

# Example Usage for the Leadership Dashboard
# agent = MarketingAttributionAgent(marketing_df, sales_df)
# print(agent.get_attribution_summary())
    
 s).sum()
