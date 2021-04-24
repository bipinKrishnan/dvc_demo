import numpy as np
import pandas as pd 

import json

data = np.random.random((3, 4))
df = pd.DataFrame(data)

df.to_csv("data/test_2.csv", index=False)
params = {"test_2_param": 55}

with open("reports/params_2.json", "w") as f:
    json.dump(params, f)