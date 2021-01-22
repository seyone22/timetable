# %%
import pandas as pd

print("Hello world")
f = open("demofile.txt", "w")
f.write("Now this file has more content!")
f.write("Testing out file with github, I think i sdfsdsdfneed it to be main!")
f.close()

f = open("demofile.txt", "r")
print(f.read())

df = pd.read_excel('C:/folder/file.xlsx')
df.head()
print(df.head())