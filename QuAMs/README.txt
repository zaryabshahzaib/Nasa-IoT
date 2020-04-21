Welcome to the QuAM for RUL Estimation. 


I have provided three QuAMs as part of this project. Their description and details about
how to run them are as follows:

QuAM_Classification: 
run: python QuAM_Classification.py
Once the program runs, input can be given on the terminal:
Input: Cycle#, Sensor_11, Sensor_9, Sensor_12, and Sensor_4

This QuAM does binary classification and classifies the engine as Healthy or Faulty.


QuAM_Regression: 
run: python QuAM_Regression.py
Once the program runs, input can be given on the terminal:
Input: Cycle#, Sensor_11, Sensor_9, Sensor_12, and Sensor_4

This QuAM does regression, returns the predicted RUL and classifies the engine as Healthy or Faulty.



QuAM_Regression_Max85: 
run: python QuAM_Regression_Max85.py
Once the program runs, input can be given on the terminal:
Input: Sensor_11, Sensor_9, Sensor_4, Sensor_12, and Sensor_14

This QuAM does regression, however, the MAX predicted RUL is set to 85. This 
returns the predicted RUL and classifies the engine as Healthy or Faulty.