import pandas as pd
from marketing_attribution_agt import MarketingAttributionAgent

# 1. Setup Sample Marketing Spend (The Investment)
spend_data = pd.DataFrame({
    'Channel': ['LinkedIn', 'Google Ads', 'TikTok', 'Email'],
    'Spend': [2000, 1500, 1000, 200]
})

# 2. Setup Customer Journeys (The Paths to Revenue)
conversion_data = pd.DataFrame({
    'user_id': [101, 102, 103, 104],
    'channel_path': [
        'LinkedIn > Google Ads > Email', # Multi-touch
        'TikTok > Google Ads',            # Multi-touch
        'LinkedIn',                       # Single-touch
        'Google Ads > Email'              # Multi-touch
    ],
    'revenue': [5000, 3000, 1500, 2000]
})

# 3. Initialize and Run the Agent
agent = MarketingAttributionAgent(spend_data, conversion_data)

print("--- U-Shaped Attribution Breakdown ---")
print(agent.calculate_u_shaped_attribution())

print("\n--- ROI/ROAS Performance Report ---")
print(agent.calculate_roi())

print("\n--- Executive Summary ---")
print(agent.get_attribution_summary())
