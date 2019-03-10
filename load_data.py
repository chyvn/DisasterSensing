import os
import pandas as pd

files = os.listdir('./data/')
# print(files)

files_paths = []
for file in files:
    files_paths.append('./data/' + file)
print(files_paths)

df_humidity = pd.read_csv('./data/humidity.csv').fillna(-1111)
df_temperature = pd.read_csv('./data/temperature.csv').fillna(-1111)
df_wind_speed = pd.read_csv('./data/wind_speed.csv').fillna(-1111)
df_pressure = pd.read_csv('./data/pressure.csv').fillna(-1111)
df_cities = pd.read_csv('./data/city_attributes.csv').fillna(-1111)

# print(df_temperature.head())
# print(df_humidity['Haifa'])

#
# master_df = pd.DataFrame(columns=['datetime', 'Humidity', 'Temperature', 'Pressure', 'Wind_speed'])
# for city in df_cities['City']:
#     master_df.append(df_humidity['datetime'])
#     # master_df['datetime'].append(df_humidity['datetime'])
#     master_df.append(df_humidity[city])
#     master_df.append(df_temperature[city])
#     # master_df['Pressure'].append(df_pressure[city])
#     # master_df['Wind_speed'].append(df_wind_speed[city])

# print(master_df.info(verbose=True))
# print(df_humidity[df_cities['City'][0]].values)
import numpy as np

Y_values = df_humidity['datetime'].values
Y = np.array([0] * len(Y_values))

from dateutil import parser

disaster_from_us = ['16/09/2017', '30/08/2017', '17/08/2017', '28/09/2016', '19/01/2016', '26/11/2014', '07/02/2013',
                    '22/10/2012']
disaster_to_us = ['02/10/2017', '13/09/2017', '02/09/2017', '10/10/2016', '29/11/2014', '26/11/2014', '18/02/2013',
                  '02/11/2012']

from_array = [parser.parse(date) for date in disaster_from_us]
to_array = [parser.parse(date) for date in disaster_to_us]

for j in range(len(Y_values)):
    today = parser.parse(Y_values[j])
    for i in range(len(from_array)):
        if from_array[i] < today < to_array[i]:
            Y[j] = 1

X = np.array([df_humidity['Vancouver'].values, df_temperature['Vancouver'].values, df_pressure['Vancouver'].values,
             df_wind_speed['Vancouver'].values])
X = X.transpose()
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.8, random_state=42)

from sklearn.svm import SVC

# clf = SVC(gamma='auto')
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(X_train, y_train)

print('break')

y_out = []
for x in X_test:
    y_out.append(clf.predict([x]))

from sklearn.metrics import accuracy_score

print(accuracy_score(y_out, y_test))
