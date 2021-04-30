import numpy as np
import matplotlib.pyplot as plt
import pandas

import numpy as np
import matplotlib.pyplot as plt

my_map_data = {"native" : 
                    {"sysv" :  
                            {"message_queue" : [0, 0], 
                             "shared_memory" : [0, 0], 
                             "semaphore" : [0, 0]}, 

                    "posix" : {"message_queue" : [0, 0], 
                               "shared_memory" : [0, 0], 
                               "semaphore" : [0, 0]
                               }
                    }, 
          "namespace" : 
                    {"sysv" :  {"message_queue" : [0, 0], 
                                "shared_memory" : [0, 0], 
                                "semaphore" : [0, 0]
                                }, 

                    "posix" :  {"message_queue" : [0, 0], 
                                "shared_memory" : [0, 0], 
                                "semaphore" : [0, 0]
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
    val = my_map_data[data['ENVIRONMENT'][count]][data['LIBRARY'][count]][data['IPC'][count]][0]
    c = my_map_data[data['ENVIRONMENT'][count]][data['LIBRARY'][count]][data['IPC'][count]][1]
    my_map_data[data['ENVIRONMENT'][count]][data['LIBRARY'][count]][data['IPC'][count]] = [val + data['AVG_TIME'][count], c + 1]
    count += 1

avg_native_posix_semaphore = my_map_data['native']['posix']['semaphore'][0] / float(my_map_data['native']['posix']['semaphore'][1])
avg_native_posix_mq = my_map_data['native']['posix']['message_queue'][0] / float(my_map_data['native']['posix']['message_queue'][1])
avg_native_posix_sm = my_map_data['native']['posix']['shared_memory'][0] / float(my_map_data['native']['posix']['shared_memory'][1])
avg_native_sysv_semaphore = my_map_data['native']['sysv']['semaphore'][0] / float(my_map_data['native']['sysv']['semaphore'][1])
avg_native_sysv_mq = my_map_data['native']['sysv']['message_queue'][0] / float(my_map_data['native']['sysv']['message_queue'][1])
avg_native_sysv_sm = my_map_data['native']['sysv']['shared_memory'][0] / float(my_map_data['native']['sysv']['shared_memory'][1])
avg_namespace_posix_semaphore = my_map_data['namespace']['posix']['semaphore'][0] / float(my_map_data['namespace']['posix']['semaphore'][1])
avg_namespace_posix_mq = my_map_data['namespace']['posix']['message_queue'][0] / float(my_map_data['namespace']['posix']['message_queue'][1])
avg_namespace_posix_sm = my_map_data['namespace']['posix']['shared_memory'][0] / float(my_map_data['namespace']['posix']['shared_memory'][1])
avg_namespace_sysv_semaphore = my_map_data['namespace']['sysv']['semaphore'][0] / float(my_map_data['namespace']['sysv']['semaphore'][1])
avg_namespace_sysv_mq = my_map_data['namespace']['sysv']['message_queue'][0] / float(my_map_data['namespace']['sysv']['message_queue'][1])
avg_namespace_sysv_sm = my_map_data['namespace']['sysv']['shared_memory'][0] / float(my_map_data['namespace']['sysv']['shared_memory'][1])
amount = 1
data =  [
            ['Namespace\nPOSIX', 'Namespace\nSysV', 'Native\nPOSIX', 'Native\nSysV'],
            [ 'Semaphore',  avg_namespace_posix_semaphore * (float)(amount), avg_namespace_sysv_semaphore * (float)(amount),   avg_native_posix_semaphore * (float)(amount),  avg_native_sysv_semaphore * (float)(amount)],
            ['Message Queue',  avg_namespace_posix_mq, avg_namespace_sysv_mq * (float)(amount),   avg_native_posix_mq * (float)(amount), avg_native_sysv_mq * (float)(amount) ],
            ['Shared Memory',  avg_namespace_posix_sm, avg_namespace_sysv_sm * (float)(amount),   avg_native_posix_sm * (float)(amount),  avg_native_sysv_sm * (float)(amount)],
        ]


column_headers = data.pop(0)
row_headers = [x.pop(0) for x in data]# Table data needs to be non-numeric text. Format the data
# while I'm at it.
cell_text = []
for row in data:
    cell_text.append(["{0:0.8f}".format(x) for x in row])# Get some lists of color specs for row and column headers
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
the_table.scale(1, 5)# Hide axes
the_table.auto_set_font_size(False)
the_table.set_fontsize(12)

ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)# Hide axes border
plt.box(on=None)# Add title
plt.suptitle(title_text)# Add footer
plt.figtext(0.95, 0.05, footer_text, horizontalalignment='right', size=6, weight='light')# Force the figure to update, so backends center objects correctly within the figure.
# Without plt.draw() here, the title will center on the axes and not the figure.
plt.draw()# Create image. plt.savefig ignores figure edge and face colors, so map them.
fig = plt.gcf()
plt.savefig('Resources/table.png',
            #bbox='tight',
            edgecolor=fig.get_edgecolor(),
            facecolor=fig.get_facecolor(),
            dpi=450
            )
plt.show()