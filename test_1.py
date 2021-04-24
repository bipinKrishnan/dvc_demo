import numpy as np
import pandas as pd 

import json

data = np.random.random((3, 4))
df = pd.DataFrame(data)

df.to_csv("data/test_1.csv", index=False)
params = {"test_1_param": 4}

with open("reports/params_1.json", "w") as f:
    json.dump(params, f)