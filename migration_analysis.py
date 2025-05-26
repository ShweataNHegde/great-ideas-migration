import matplotlib.pyplot as plt
import pandas as pd
import plotly
import plotly.express as px

df_01 = pd.read_csv('multiple-indicator-survey/government-id.csv')
df_02 = pd.read_csv('multiple-indicator-survey/migration-reason.csv')

# Make a stacked bar chart of all the ration-card, voter-id, passport and aadhar migration

fig_01 = px.bar(df_01, x="state-ut", y=["ration-card", 'voter-id', 'passport', 'aadhar'], color_discrete_sequence=["#be95c4", "#2a9d8f", "#e9c46a", "#eda4b8"], title="Migration Analysis of Government IDs by State")
plotly.offline.plot(fig_01, filename='migration-government-id.html')

fig_02 = px.bar(df_02, x="reason", y=["employed", 'unemployed', 'out-of-labour-force'], color_discrete_sequence=["#be95c4", "#2a9d8f", "#e9c46a"], title="Migration Reasons Analysis by Employment Status")
plotly.offline.plot(fig_02, filename='migration-reason.html')

# Load your data
df_03 = pd.read_csv('multiple-indicator-survey/state-migration.csv')

# Create the scatter map
fig = px.scatter_mapbox(
    df_03,
    lat='Latitude',
    lon='Longitude',
    hover_name='State/UT',
    hover_data={'Rural': True, 'Urban': True, 'All': True, 'Latitude': False, 'Longitude': False},
    size='All',  # Bubble size by 'All' column
    color='All', # Bubble color by 'All' column
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
