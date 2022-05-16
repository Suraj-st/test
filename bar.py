import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def stackedbar(data, predictor, target):
    count = data[predictor].nunique()
    sorter = data[target].value_counts().index[-1]
    tabl = pd.crosstab(data[predictor], data[target], margins=True).sort_values(by=sorter, ascending=False)
    print(tabl)
    print("*"*120)
    tab = pd.crosstab(data[predictor], data[target], normalize='index').sort_values(by=sorter, ascending=False)
    tab.plot(kind='bar', stacked=True, figsize=(count+1, 5))
    plt.legend(
    loc="lower left",
    frameon=False,
    )
    plt.legend(loc='upper left', bbox_to_anchor=(1,1))
    plt.show()
