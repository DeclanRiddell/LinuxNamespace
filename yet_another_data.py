import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *
sns.set_theme(style="ticks", color_codes=True)

#   Graphs and stuff are here
#
#   https://seaborn.pydata.org/tutorial.html
#   https://seaborn.pydata.org/introduction.html
#   https://seaborn.pydata.org/tutorial/categorical.html
#
sprint_data = pd.read_csv("UserCode/Vincent/sprint_speed.csv")

root = Tk()
root.geometry('800x600')

def graph():
    sns.lmplot(x="sprint_speed", y="age", col = "position", data=sprint_data)
    plt.show()

data_visualize = Button(root, text="graph it", command=graph)
data_visualize.pack()

root.mainloop()