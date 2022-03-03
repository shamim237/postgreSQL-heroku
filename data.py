import pandas as pd

df = pd.DataFrame()
names = []
emails = []
mobiles = []
ages = []
weights = []
temps = []
dates = []


with open("profile.txt", "r") as f:
    profile = f.readlines()
    for line in profile:
        line = line.split(",")
        name = line[0]
        
        mobile = line[1]
        email = line[2]
        age = line[3]
        weight = line[4]
        temp = line[5]
        date = line[6]
        #print(date)
        names.append(name)
        emails.append(email)
        mobiles.append(mobile)
        ages.append(age)
        weights.append(weight)
        temps.append(temp)
        dates.append(date)

df['name'] = names
df['mobile'] = mobiles
df['email'] = emails
df['age'] = ages
df['weight'] = weights
df['temp'] = temps
#df['date'] = dates

#print(df.head())

df.to_csv("dataset.csv", index=False)
print(df.head())



