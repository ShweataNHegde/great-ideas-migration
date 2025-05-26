import matplotlib.pyplot as plt
import pandas as pd
import plotly
import plotly.express as px

df_01 = pd.read_csv('government-id.csv')
df_02 = pd.read_csv('migration-reason.csv')

# Make a stacked bar chart of all the ration-card, voter-id, passport and aadhar migration

fig_01 = px.bar(df_01, x="state-ut", y=["ration-card", 'voter-id', 'passport', 'aadhar'], color_discrete_sequence=["#be95c4", "#2a9d8f", "#e9c46a", "#eda4b8"], title="Migration Analysis of Government IDs by State")
plotly.offline.plot(fig_01, filename='migration-government-id.html')

fig_02 = px.bar(df_02, x="reason", y=["employed", 'unemployed', 'out-of-labour-force'], color_discrete_sequence=["#be95c4", "#2a9d8f", "#e9c46a"], title="Migration Reasons Analysis by Employment Status")
plotly.offline.plot(fig_02, filename='migration-reason.html')