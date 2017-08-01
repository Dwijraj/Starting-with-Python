import pandas as pd
data={
    "Students":["Maina","Dwijraj","Dinku"],
    "Maths":[95,96,94],
    "Computer":[91,92,93],
    "Science":[89,90,91]
    }
Dataframe=pd.DataFrame(data,columns=["Students","Maths","Computer","Science"])
print(Dataframe)
