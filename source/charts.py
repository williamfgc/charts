

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.signal import savgol_filter


dtype={'names':('date','weight'), 'formats':('datetime64[s]', 'float32')}
date, weight = np.loadtxt('../data/william.dat', dtype, usecols=(0,1), unpack=True, skiprows=1)

print(date)
print(weight)
yhat = savgol_filter(weight, 7, 1)

plt.title("William's weight ")
plt.plot(date, weight, 'green')
plt.yticks(np.arange(min(date), max(date), np.timedelta64(7, 'D')))
plt.xlabel('date (yyyy-mm-dd)')

plt.plot(date, yhat, 'blue')
plt.yticks(np.arange(min(weight), max(weight)+1, 1.))
plt.ylabel('weight (lbs)')

plt.gca().xaxis.grid(True)
plt.gca().yaxis.grid(True)

daily_legend = mpatches.Patch(color='green', label='Daily')
weekly_legend = mpatches.Patch(color='blue', label='Weekly')
plt.legend(handles=[daily_legend, weekly_legend])
plt.show()