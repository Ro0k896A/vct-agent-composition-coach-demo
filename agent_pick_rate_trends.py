# Agent Pick Rate Trends by Map (2021–2025) with Role-Based Analysis

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load All Cleaned Data
data_path = 'cleaned_data'
all_data = pd.concat([
    pd.read_csv(os.path.join(data_path, file))
    for file in os.listdir(data_path)
    if file.endswith('.csv')
], ignore_index=True)

# Step 2: Explode Agents Played into Separate Rows
all_data['Agents Played'] = all_data['Agents Played'].str.split(', ')
exploded_data = all_data.explode('Agents Played')


# Step 3: Add Agent Roles (Define Static Role Mapping)
# You may need to adjust this dictionary based on your dataset and meta
agent_roles = {
    'Jett': 'Duelist',
    'Reyna': 'Duelist',
    'Raze': 'Duelist',
    'Phoenix': 'Duelist',
    'Yoru': 'Duelist',
    'Neon': 'Duelist',
    'Sova': 'Initiator',
    'Skye': 'Initiator',
    'KAY/O': 'Initiator',
    'Breach': 'Initiator',
    'Fade': 'Initiator',
    'Gekko': 'Initiator',
    'Omen': 'Controller',
    'Brimstone': 'Controller',
    'Viper': 'Controller',
    'Astra': 'Controller',
    'Harbor': 'Controller',
    'Killjoy': 'Sentinel',
    'Cypher': 'Sentinel',
    'Sage': 'Sentinel',
    'Chamber': 'Sentinel',
    'Deadlock': 'Sentinel'
}

exploded_data['Role'] = exploded_data['Agents Played'].map(agent_roles)

# Step 5: Calculate Pick Rate by Agent and Map per Year
agent_map_counts = (
    exploded_data
    .groupby(['Year', 'Map', 'Agents Played'])
    .size()
    .reset_index(name='Pick Count')
)

total_picks_per_map = (
    exploded_data
    .groupby(['Year', 'Map'])
    .size()
    .reset_index(name='Total Picks')
)

pick_rate_data = pd.merge(agent_map_counts, total_picks_per_map, on=['Year', 'Map'])
pick_rate_data['Pick Rate (%)'] = (pick_rate_data['Pick Count'] / pick_rate_data['Total Picks']) * 100

# Step 6: Role-Based Pick Rates
role_map_counts = (
    exploded_data
    .groupby(['Year', 'Map', 'Role'])
    .size()
    .reset_index(name='Pick Count')
)

total_picks_per_map_role = (
    exploded_data
    .groupby(['Year', 'Map'])
    .size()
    .reset_index(name='Total Picks')
)

role_pick_rate_data = pd.merge(role_map_counts, total_picks_per_map_role, on=['Year', 'Map'])
role_pick_rate_data['Pick Rate (%)'] = (role_pick_rate_data['Pick Count'] / role_pick_rate_data['Total Picks']) * 100

# Step 7: Visualize Pick Rate Trends for Top 5 Agents on a Specific Map
map_name = 'Ascent'
ascent_data = pick_rate_data[pick_rate_data['Map'] == map_name]
top_agents = ascent_data.groupby('Agents Played')['Pick Count'].sum().nlargest(5).index
plot_data = ascent_data[ascent_data['Agents Played'].isin(top_agents)]

plt.figure(figsize=(10, 6))
sns.lineplot(data=plot_data, x='Year', y='Pick Rate (%)', hue='Agents Played', marker='o')
plt.title(f'Agent Pick Rates on {map_name} (2021–2025)')
plt.ylabel('Pick Rate (%)')
plt.xlabel('Year')
plt.grid(True)
plt.legend(title='Agent')
plt.tight_layout()
plt.show()

# Step 8: Visualize Role Pick Rates on the Same Map
role_plot_data = role_pick_rate_data[role_pick_rate_data['Map'] == map_name]

plt.figure(figsize=(10, 6))
sns.lineplot(data=role_plot_data, x='Year', y='Pick Rate (%)', hue='Role', marker='o')
plt.title(f'Role Pick Rates on {map_name} (2021–2025)')
plt.ylabel('Pick Rate (%)')
plt.xlabel('Year')
plt.grid(True)
plt.legend(title='Role')
plt.tight_layout()
plt.show()

# Optional: Save Full Pick Rate Tables
pick_rate_data.to_csv('agent_pick_rates_by_map_year.csv', index=False)
role_pick_rate_data.to_csv('role_pick_rates_by_map_year.csv', index=False)
