dataList = ['Emmanuel', 'Aji', 'Sadewa']
dataDict = {
    'first':'Emmanuel',
    'middle':'Aji',
    'last':'Sadewa',
    'full':dataList
}
print(dataDict['first'])
print(dataDict['middle'])
print(dataDict['full'])
print(dataDict)

# Operator Dictionary
p = len(dataDict)
print(p)
Key1 = 'middle'
Key2 = 'Middle'
checkKey = Key1 in dataDict
print(checkKey)
checkKey = Key2 in dataDict
print(checkKey)

# Looping Dictionary
# for i in dataDict.keys():
#     print(dataDict.get(i))