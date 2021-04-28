import matplotlib.pyplot as plt
import random
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
types = ['POSIX Semaphore','SysV Semaphore','POSIX Shared Memory','SysV Shared Memory', 'POSIX Message queue']
times = [random.uniform(0,1), random.uniform(0,1), random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)]
ax.bar(types, times)
plt.savefig('bar_graph.png')#, dpi = 400)