from pylab import rcParams
from plotly import tools
import plotly.plotly as py

#%%
import pandas as pd
import os
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

files = os.listdir('./data/')

files_paths = []
for file in files:
    files_paths.append('./data/' + file)
print(files_paths)

humidity = pd.read_csv('./data/humidity.csv', index_col='datetime', parse_dates=['datetime'])

humidity["Vancouver"].asfreq('M').plot()
humidity = humidity.iloc[1:]
humidity = humidity.fillna(method='ffill')
plt.title('Humidity in Vancover')
plt.show()

#%%
plt.savefig('Vanc_hum.png')

#%%
humidity = pd.read_csv('./data/pressure.csv', index_col='datetime', parse_dates=['datetime'])

humidity["Vancouver"].asfreq('M').plot()
humidity = humidity.iloc[1:]
humidity = humidity.fillna(method='ffill')
plt.title('Pressure in Vancover')
plt.show()