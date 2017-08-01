import pandas as pd
#pd.read_csv("CsvData.csv",names=["Pizza","Cats","Dogs","Cheese"],header=None)
#print(pd.read_csv('CsvData.csv',usecols=[1,2,3]))
newCsv=pd.read_csv("CsvData.csv",header=0,names=["Food","Price","Quantity"])
newCsv.to_csv("TestData.csv")
print(pd.read_csv("TestData.csv"))
