import pickle
import pandas as pd

with open('regression_model_max85.pkl', 'rb') as f:
     reg = pickle.load(f)

Inp_Arr=[]

for elem in [11, 9, 4, 12, 14]:
     print("Enter Value for Sensor_" + str(elem))
     sensor_val = input()
     Inp_Arr.append(float(sensor_val))

data_f = pd.DataFrame(columns = ['Sensor_11', 'Sensor_9', 'Sensor_4', 'Sensor_12', 'Sensor_14'])
data_f.loc[len(data_f)] = Inp_Arr
prediction = reg.predict(data_f)

if prediction > 25:
     cond = 'Healthy'
else:
     cond = 'Faulty'

print("Predicted RUL is {}, Engine Condition is {}".format(int(prediction[0]), cond))

