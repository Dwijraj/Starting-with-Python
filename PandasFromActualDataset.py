import pandas as pd
users=pd.read_csv('ml-100k/ml-100k/u.user',sep='|',names=['UserId','Age','Gender','Occupation','Zip Code'])
#print(users.head())
#print(users.tail(3))
"""
Head and Tail helps visualise data
"""
#print(users[10:15]) 
"""
Slicing data just like in list
"""
#print(users["Gender"].head(10)) #First 10 Genders Single Column
columnsreq=["Gender","Zip Code"]
#print(users[columnsreq].head(10))
"""
Multiple Attributes require lists ^
"""
#"""------------Boolean Indexing----------------------"""
#print(users[users.Age>25].head())
users=pd.read_csv('ml-100k/ml-100k/u.user',sep='|',names=['UserId','Age','Gender','Occupation','Zip_Code'])
#print(users.Zip_Code)
#print(users[(users.Age<35) & (users.Gender=="M")] )
#print(users[(users.Age>60) | (users.Gender=="M")].head())

#print(users.dtypes)  # Gives the data Types
#print(users.describe())  #Describes count of each mean std min 25% 50%...
#print(users.set_index('UserId').head())# Temporarily removes default pandas index
users.set_index('UserId',inplace=True)  #Permanently removes default Pandas index
rows=[1,2,3,4,5]
#print(users.ix[[1,12,13]])   #Selects Particular Rows double square bracket
print(users.ix[rows])         #Selects Particular Rows from Array square bracket
