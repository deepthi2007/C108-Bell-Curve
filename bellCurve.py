import pandas as pd
import plotly.figure_factory as pf 

df = pd.read_csv("data.csv")
data = df["Avg Rating"]

fig = pf.create_distplot([data],["rating"],show_hist=False)
fig.show()