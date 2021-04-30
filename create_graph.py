import numpy as np
import matplotlib.pyplot as plt
import pandas

import numpy as np
import matplotlib.pyplot as plt

my_map = {"native" : 
                    {"sysv" :  
                            {"message_queue" : 0, 
                             "shared_memory" : 0, 
                             "semaphore" : 0}, 

                    "posix" : {"message_queue" : 0, 
                               "shared_memory" : 0, 
                               "semaphore" : 0
                               }
                    }, 
          "namespace" : 
                    {"sysv" :  {"message_queue" : 0, 
                                "shared_memory" : 0, 
                                "semaphore" : 0
                                }, 

                    "posix" :  {"message_queue" : 0, 
                                "shared_memory" : 0, 
                                "semaphore" : 0
                                }
                    } 
        }


title_text = 'Average runtimes'
footer_text = 'ASRC Federal'
fig_background_color = 'skyblue'
fig_border = 'steelblue'
data = pandas.read_csv("data.csv")
count = 0

print(data['IPC'][0])
while count < len(data):
    print(count)
    print(data['ENVIRONMENT'][count], data['LIBRARY'][count], data['IPC'][count])
    my_map[data['ENVIRONMENT'][count]][data['LIBRARY'][count]][data['IPC'][count]] += data['AVG_TIME'][count]
    count += 1

print(my_map['native']['posix']['shared_memory'] / float(count))
avg_native_posix_semaphore = my_map['native']['posix']['semaphore'] / float(count) * float(100000)
avg_native_posix_mq = my_map['native']['posix']['message_queue'] / float(count) * float(100000)
avg_native_posix_sm = my_map['native']['posix']['shared_memory'] / float(count) * float(1000)
avg_native_sysv_semaphore = my_map['native']['sysv']['semaphore'] / float(count) * float(100000)
avg_native_sysv_mq = my_map['native']['sysv']['message_queue'] / float(count) * float(100000)
avg_native_sysv_sm = my_map['native']['sysv']['shared_memory'] / float(count) * float(100000) 
print(avg_native_posix_semaphore)
print(avg_native_posix_mq)
print(avg_native_posix_sm)
print(avg_native_sysv_semaphore)
print(avg_native_sysv_mq)
print(avg_native_sysv_sm)

avg_namespace_posix_semaphore = my_map['namespace']['posix']['semaphore'] / float(count)
avg_namespace_posix_mq = my_map['namespace']['posix']['message_queue'] / float(count)
avg_namespace_posix_sm = my_map['namespace']['posix']['shared_memory'] / float(count)
avg_namespace_sysv_semaphore = my_map['namespace']['sysv']['semaphore'] / float(count)
avg_namespace_sysv_mq = my_map['namespace']['sysv']['message_queue'] / float(count)
avg_namespace_sysv_sm = my_map['namespace']['sysv']['shared_memory'] / float(count)
data =  [
            ['Namespace POSIX', 'Namespace SysV', 'Native POSIX', 'Native SysV'],
            [ 'Semaphore',  avg_namespace_posix_semaphore, avg_namespace_sysv_semaphore,   avg_native_posix_semaphore,  avg_native_sysv_semaphore],
            ['Message Queue',  avg_namespace_posix_mq, avg_namespace_sysv_mq,   avg_native_posix_mq, avg_native_sysv_mq ],
            ['Shared Memory',  avg_namespace_posix_sm, avg_namespace_sysv_sm,   avg_native_posix_sm,  avg_native_sysv_sm],
        ]# Pop the headers from the data array
column_headers = data.pop(0)
row_headers = [x.pop(0) for x in data]# Table data needs to be non-numeric text. Format the data
# while I'm at it.
cell_text = []
for row in data:
    cell_text.append([f'{x/1000:1.1f}' for x in row])# Get some lists of color specs for row and column headers
rcolors = plt.cm.BuPu(np.full(len(row_headers), 0.1))
ccolors = plt.cm.BuPu(np.full(len(column_headers), 0.1))# Create the figure. Setting a small pad on tight_layout
# seems to better regulate white space. Sometimes experimenting
# with an explicit figsize here can produce better outcome.
plt.figure(linewidth=2,
           edgecolor=fig_border,
           facecolor=fig_background_color,
           tight_layout={'pad':1},
           #figsize=(5,3)
          )# Add a table at the bottom of the axes
the_table = plt.table(cellText=cell_text,
                      rowLabels=row_headers,
                      rowColours=rcolors,
                      rowLoc='right',
                      colColours=ccolors,
                      colLabels=column_headers,
                      loc='center')# Scaling is the only influence we have over top and bottom cell padding.
# Make the rows taller (i.e., make cell y scale larger).
the_table.scale(1, 1.5)# Hide axes
ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)# Hide axes border
plt.box(on=None)# Add title
plt.suptitle(title_text)# Add footer
plt.figtext(0.95, 0.05, footer_text, horizontalalignment='right', size=6, weight='light')# Force the figure to update, so backends center objects correctly within the figure.
# Without plt.draw() here, the title will center on the axes and not the figure.
plt.draw()# Create image. plt.savefig ignores figure edge and face colors, so map them.
fig = plt.gcf()
plt.show()
plt.savefig('pyplot-table-demo.png',
            #bbox='tight',
            edgecolor=fig.get_edgecolor(),
            facecolor=fig.get_facecolor(),
            dpi=150
            )