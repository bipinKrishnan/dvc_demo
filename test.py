import numpy as np 
import pandas as pd 

data = np.random.random((100, 4))
df = pd.DataFrame(data)

df.to_csv('data.csv')