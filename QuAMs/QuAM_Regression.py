import pickle
import pandas as pd

with open('regression_model.pkl', 'rb') as f:
     reg = pickle.load(f)

Inp_Arr=[]

for elem in ["Cycle#", 11, 9, 12, 4]:
     if elem == "Cycle#":
        print("Enter " + str(elem))
        cycle_num = input()
        Inp_Arr.append(int(cycle_num))
     else:
        print("Enter Value for Sensor_" + str(elem))
        sensor_val = input()
        Inp_Arr.append(float(sensor_val))

data_f = pd.DataFrame(columns = ["Cycle#", 'Sensor_11', 'Sensor_9', 'Sensor_12', 'Sensor_4'])
data_f.loc[len(data_f)] = Inp_Arr
prediction = reg.predict(data_f)

if prediction > 25:
     cond = 'Healthy'
else:
     cond = 'Faulty'

print("Predicted RUL is {}, Engine Condition is {}".format(int(prediction[0]), cond))

