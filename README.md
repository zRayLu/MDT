# This is a python script helping me with solving MDT assignment. 
# Here are my ideas and answers to the questions.  

I solved the third question first. If there are sensors with the same name, there should be sensors having the same alias in All Cloud Sensors.json. Then the number of sensors with the same name in sensorMetadata.json should match the number of sensors with the same alias in All Cloud Sensor.json. In this case, there are no 2 sensors with the same name in sensorMetadata.json.

1. Base on the finding for question 3,  I went through records in sensorMetadata.json to find all records whose Name don't match any Alias from  All Cloud Sensors.json. Here are the Names.
'ENGINE1_AWL', 'ENGINE1_RSL', 'ENGINE1_MIL', 'ENGINE1_PRO', 'TRANS_OIL_DIFF_PRESS'

I also found 2 sensors have more than 1 records from All Cloud Sensors.json with the same Alias.
'POWERTRAIN1.TRANS_CURRENT_GEAR', 'DISCHARGE_PRESS_SENSOR'

2. In the question, I found 3 records from sensorMetadata.json (besides those 5 records from question) whose value of filed units of measure are incorrect.
ENGINE1.HOURS.ETHO
DIRTY_POWER
POWERTRAIN1.PUMP_HHP

For those 2 sensors have more than 1 records from All Cloud Sensors.json with the same Alias, they have the same UOM configuration. 

3. There are no 2 sensors in sensorMetadata.json with the same name.
