import numpy as np
import pandas as pd 

data = np.random.random((3, 4))
df = pd.DataFrame(data)

df.to_csv("data/test_2.csv", index=False)