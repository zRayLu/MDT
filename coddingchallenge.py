import json

f1=open('resources/sensorMetadata.json')
sensorDict = json.load(f1)


f2=open('resources/all_cloud_sensors.json')
cloudDict=json.load(f2)

cloudSensorsAlias=[k["alias"] for k in cloudDict["data"]["activeSensors"]]
sensorNames=[k["name"] for k in sensorDict["sensors"]]

#QUESTION 3
print("==========================")
print("QUESTION3")
seenName=set()
seenAlias=set()
duplicateAlias=set()
duplicateNames=set()
for n in sensorNames:
    if n in seenName:
        duplicateNames.add(n)
    else:
        seenName.add(n)

for n in cloudSensorsAlias:
    if n in seenAlias:
        duplicateAlias.add(n)
    else:
        seenAlias.add(n)

print("duplicate names\n" , duplicateNames)
print("duplicate alias\n" , duplicateAlias)


invalidKeys=[]
withDuplicatedAlias=[]
# QUESTION 1
print("==========================")
print("QUESTION1")
for n in sensorNames:
    if n in duplicateAlias:
        withDuplicatedAlias.append(n)
    if n not in cloudSensorsAlias:
        invalidKeys.append(n)


print("Names with duplicate alias: \n",withDuplicatedAlias)
print("Names don't have alias: \n",invalidKeys)
# QUESTION 2
print("==========================")
print("QUESTION2")
invalidCfg=[]
newSensorDict={e["name"]:e for e in sensorDict["sensors"]}
newCloudDict={e["alias"]:e for e in cloudDict["data"]["activeSensors"]}
for k in newSensorDict.keys():
    if k not in invalidKeys:
        if newSensorDict[k]["unitOfMeasure"] != newCloudDict[k]["uom"]:
            invalidCfg.append(k)

print("invalid uom config: \n", invalidCfg)







