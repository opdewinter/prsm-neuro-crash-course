import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt

# write a for loop
some_list = ["dmt", "psilcybin", "DTP"]
for i, something in enumerate(some_list):
    print(f"tryptamine {i}: {something}")

rand_nrs = np.random.rand(25, 5)

data = pd.DataFrame(rand_nrs)
data.columns = ["dmt", "psilcybin", "DPT", "MDMA", "LSD"]
print(data)
plt.plot(data)
plt.show()