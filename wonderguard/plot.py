import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    fmri = sns.load_dataset("fmri")
    ax = sns.lineplot(x="timepoint", y="signal", data=fmri)
    plt.show()


