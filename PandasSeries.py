import pandas as pd
DataList=pd.Series([1,2,3,4,5,6,7,8,9])
dictionary={"Student1":"Maina","Student2":"Dwijraj","Student3":"Dinku"}
DataDictionary=pd.Series(dictionary)
print(DataDictionary.isnull())
print(DataDictionary)
print(DataDictionary[DataDictionary=="Maina"])

