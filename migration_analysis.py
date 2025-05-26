import matplotlib.pyplot as plt
import pandas as pd
import plotly
import plotly.express as px
import json

df_01 = pd.read_csv('multiple-indicator-survey/government-id.csv')
df_02 = pd.read_csv('multiple-indicator-survey/migration-reason.csv')

# Make a stacked bar chart of all the ration-card, voter-id, passport and aadhar migration

fig_01 = px.bar(df_01, x="state-ut", y=["ration-card", 'voter-id', 'passport', 'aadhar'], color_discrete_sequence=["#be95c4", "#2a9d8f", "#e9c46a", "#eda4b8"], title="Migration Analysis of Government IDs by State")
plotly.offline.plot(fig_01, filename='migration-government-id.html')

fig_02 = px.bar(df_02, x="reason", y=["employed", 'unemployed', 'out-of-labour-force'], color_discrete_sequence=["#be95c4", "#2a9d8f", "#e9c46a"], title="Migration Reasons Analysis by Employment Status")
plotly.offline.plot(fig_02, filename='migration-reason.html')

# Load your data
df_03 = pd.read_csv('multiple-indicator-survey/migration-reasons-detailed.csv')
df_04 = pd.read_csv('multiple-indicator-survey/state-migration.csv')

df_05 = pd.merge(df_03, df_04[['State/UT','Rural','Urban']], on='State/UT', how='left')

with open('multiple-indicator-survey/migration-reasons.json') as f:
    reason_map = json.load(f)

# Rename columns using the JSON mapping
df_05 = df_05.rename(columns=reason_map)
print(df_05.head())

# List of readable reason names (after renaming)
reason_cols = list(reason_map.values())

def top3_reasons(row):
    top = row[reason_cols].dropna().sort_values(ascending=False).head(3)
    return ', '.join([f"{reason} ({row[reason]:.1f}%)" for reason in top.index])

df_05['top-three-reasons'] = df_05.apply(top3_reasons, axis=1)


# Create the scatter map
fig = px.scatter_mapbox(
    df_05,
    lat='Latitude',
    lon='Longitude',
    hover_name='State/UT',
    hover_data={ 'Rural':True, 'Urban': True,'top-three-reasons':True,'migrant-percent': True, 'Latitude': False, 'Longitude': False},
    size='migrant-percent',  # Bubble size by 'All' column
    color='migrant-percent', # Bubble color by 'All' column
    color_continuous_scale='Viridis',
    size_max=30,
    zoom=4,
    mapbox_style='carto-positron'  # Free Mapbox style
)

fig.update_layout(
    title='India States/UTs Data Visualization',
    margin={'r':0, 't':40, 'l':0, 'b':0}
)
fig.show()