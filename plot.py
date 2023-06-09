import pandas as pd
import os
import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px

df = pd.read_csv("./assign2_wastedata.csv")


df['Stream'] = df['Stream'].str.split().str[-1]
df['Date'] = "20"+ df['Date'].str.split("/").str[-1]
df['Volume'].fillna(0)

# fig = make_subplots(
#     rows=1,
#     cols=2,
#     subplot_titles=("Sunburst Chart 1", "Sunburst Chart 2")
# )
# fig.add_trace(
#     go.Sunburst
# )

fig = px.sunburst(df, path=["Date",'Building', 'Stream'], values='Weight')
fig.update_traces(hovertemplate='<b>The total weight is: %{value} pounds</b>')
fig.update_layout(title_text = "<b>Total Wastage as per Streams<b>", 
                  title_x = 0.5,
                  plot_bgcolor="black",  # Set the plot background color to black
                paper_bgcolor="black",  # Set the paper (outside the plot) background color to black
                font=dict(color="white"),)

# fig1 = px.sunburst(df, path=["Date",'Building', 'Stream'], values='Volume')
# fig1.update_traces(hovertemplate='<b>The total volume is: %{value} </b>')
# fig1.update_layout(title_text = "<b>Total Wastage as per Streams<b>", 
#                   title_x = 0.5,
#                   plot_bgcolor="black",  # Set the plot background color to black
#                 paper_bgcolor="black",  # Set the paper (outside the plot) background color to black
#                 font=dict(color="white"),)
st.plotly_chart(fig, use_container_width=False)# fig1.show()
