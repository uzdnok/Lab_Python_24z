import pandas as pd
import openpyxl as opx
import plotly.express as px
from plotly.offline import plot

df = pd.read_excel("Statystyki.xlsx", sheet_name='PM2,5')
print(df.columns)
filtrowane = df[(df['Kod stacji'] == "PdBialWarsza") | (df['Kod stacji'] == "WmOlsPuszkin")]
fig = px.line(filtrowane, x="Rok", y="Średnia", color="Kod stacji", title="Stezenie pylow")
plot(fig, auto_open=False)

avg_pm25 = df.groupby(["Rok"])["Średnia"]
fig2 = px.box(df, x="Rok", y="Średnia", title="Rozklad stezen PM2.5")
plot(fig2, auto_open=False)


