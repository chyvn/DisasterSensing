from sklearn.svm import SVC
import load_data
import numpy as np

clf = SVC(gamma='auto')

X = np.array([[], [], [], []])
x_hum = np.array([])
x_press = np.array([])
x_temp = np.array([])
x_win = np.array([])

for i in range(len(load_data.df_humidity['datetime'])):
    x_hum = np.append(x_hum, load_data.df_humidity[load_data.df_humidity['datetime'] == load_data.df_humidity['datetime'][i]].values)
    x_temp = np.append(x_temp,
                      load_data.df_temperature[load_data.df_temperature['datetime'] == load_data.df_temperature['datetime'][i]].values)
    x_press = np.append(x_press,
                      load_data.df_pressure[load_data.df_pressure['datetime'] == load_data.df_pressure['datetime'][i]].values)
    x_win = np.append(x_win, load_data.df_wind_speed[load_data.df_wind_speed['datetime'] == load_data.df_wind_speed['datetime'][i]].values)

print('break')