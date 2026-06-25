df.replace('?', np.nan, inplace=True)

df.dropna(inplace=True)

print("New Shape:", df.shape)

##Output
New Shape: (30162, 15)
