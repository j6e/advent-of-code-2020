import pandas as pd

df = pd.read_csv('advent_of_code/10_adapter_array/input.txt', header=None, names=['jolts'])

df.loc[-1, :] = [0] #Base adapter
df = df.sort_values(by='jolts', ascending=True)
df.loc[df.shape[0], :] = [df.iloc[-1] + 3] #phone adapter
df['diff'] = df['jolts'].diff(1)
# print(df.tail())
values = df['diff'].value_counts()
print(values)
print(values[1.0] * values[3.0])
