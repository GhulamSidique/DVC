import pandas as pd
import os  

# create a data frame
data = {"Name": ["Haji", "Ali", "hussain"], "Age":[25, 20, 18], "City": ["Khi", "Lrk", "Hyd"]}
df = pd.DataFrame(data)

# add a new row
new_data = {"Name":"GS", "Age":32, "City":"Isl"}
df.loc[len(df.index)] = new_data

# add another new row
new_data2 = {"Name":"GD", "Age":32, "City":"Isl"}
df.loc[len(df.index)] = new_data2

# make a folder and save this dataframe inside it
folder = "Data"
os.makedirs(folder, exist_ok=True)
file_path = os.path.join(folder, "sample.csv")

df.to_csv(file_path, index=False)
print(f"The file {file_path} saved to folder {folder} succesfully")