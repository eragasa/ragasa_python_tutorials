import matplotlib.pyplot as plt
import matplotlib.lines as mlines

import pandas as pd

from pandas.plotting import parallel_coordinates
data = pd.read_csv('data/iris.data')
print(data)
plt.figure()
parallel_coordinates(data,"Name")
plt.show()
exit()
from pandas.plotting import andrews_curves
data = pd.read_csv('data/iris.data')

lowColorList=["k","k","y","y"]
midColorList=["c","b","g"]
topColorList=["r"]

plt.close()
plt.gcf().clear()
fig, ax = plt.subplots()

parallel_coordinates(lowDf, "Cat",color=lowColorList, alpha=0.1)
parallel_coordinates(midDf, "Cat", color=midColorList, alpha=0.4)
parallel_coordinates(topDf, "Cat", color=topColorList, alpha=0.9)
# remove the pandas legend
plt.gca().legend_.remove()

plt.xlabel("Each Component of X is Shown on its Own Vertical Axis")
plt.ylabel("Values")
plt.title("Finding the Optimal Value of X")
# add new legend
topHandle =    mlines.Line2D([],[], color='red',   ls="-", label="Best")
midHandleOne = mlines.Line2D([],[], color='blue',  ls="-", label="Next Best")
lowHandle =    mlines.Line2D([],[], color='black', ls="-", label="Worst")
plt.legend(handles=[topHandle, midHandleOne,lowHandle],loc=1, prop={'size':10})
plt.show()
