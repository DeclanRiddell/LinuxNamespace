import matplotlib.pyplot as plt
import random
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
types = ['POSIX Semaphore','SysV Semaphore','POSIX Shared Memory','SysV Shared Memory', 'POSIX Message queue']
times = [random.uniform(0,1), random.uniform(0,1), random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)]
ax.bar(types, times)
ax.set_xlabel = "IPCS"
ax.set_ylabel = "Time"
plt.savefig('Resources/bar_graph.png')#, dpi = 400)


plt.show()