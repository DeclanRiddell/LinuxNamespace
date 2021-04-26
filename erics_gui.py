
from tkinter import *
import tkinter.ttk
import subprocess

window = Tk()
my_map = {"native" : 
                    {"sysv" :  
                            {"mq" : IntVar(), 
                             "sm" : IntVar(), 
                             "s" : IntVar()}, 

                    "posix" : {"mq" : IntVar(), 
                               "sm" : IntVar(), 
                               "s" : IntVar()
                               }
                    }, 
          "namespace" : 
                    {"sysv" :  {"mq" : IntVar(), 
                                "sm" : IntVar(), 
                                "s" : IntVar()
                                }, 

                    "posix" :  {"mq" : IntVar(), 
                                "sm" : IntVar(), 
                                "s" : IntVar()
                                }
                    } 
        }

def execute(command):
    subprocess.run([command], shell = True, timeout = 5)
    subprocess.run('python3 yet_another_data.py', shell = True)
    #update_graph();
    

def run():
    window.update( );
        
#Native POSIX IPCs
    if(my_map['native']['posix']['s'].get()):
        execute('sudo ./run_eric_native_posix.script')    
    if(my_map['native']['posix']['mq'].get()):
        execute('sudo ./run_alex_native_posix.script')    
    if(my_map['native']['posix']['sm'].get()):
        execute('sudo ./run_vincent_native_posix.script')    

#Namespace POSIX IPCs
    if(my_map['namespace']['posix']['s'].get()):
        execute('sudo ./run_eric_namespace_posix.script')    
    if(my_map['namespace']['posix']['mq'].get()):
        execute('sudo ./run_alex_namespace_posix.script')    
    if(my_map['namespace']['posix']['sm'].get()):
        execute('sudo ./run_vincent_namespace_posix.script')    

#Native SYSV IPCs
    if(my_map['native']['sysv']['s'].get()):
        execute('sudo ./run_eric_native_sysv.script')    
    if(my_map['native']['sysv']['mq'].get()):
        #SEGMENTATION FAULT
        execute('sudo ./run_alex_native_sysv.script')    
    if(my_map['native']['sysv']['sm'].get()):
        execute('sudo ./run_vincent_native_sysv.script')    
  
#Namespace SYSV IPCs
    if(my_map['namespace']['sysv']['s'].get()): 
        execute('sudo ./run_eric_namespace_sysv.script')    
    if(my_map['namespace']['sysv']['mq'].get()):
        execute('sudo ./run_alex_namespace_sysv.script')    
    if(my_map['namespace']['sysv']['sm'].get()):
        execute('sudo ./run_vincent_namespace_sysv.script')   

#BUTTON MIGHT BE A BUST
def abort():
    print("AHHHHH!!!! ABORT!!!")
    #execute('$$')
    #execute('kill -2 $$')
    
    


w_height  = 480
w_width = 720
window.geometry(''+ str(w_width) +  'x' + str(w_height))

iteration_label = Label(window, text = "Runs:", fg = "blue",)
native_label = Label(window, text = "Native", fg = "blue",)
sem_label = Label(window, text = "Semaphore", fg = "blue",)
sm_label = Label(window, text = "Shared Memory", fg = "blue",)
mq_label = Label(window, text = "Message Queue", fg = "blue",)
namespace_label = Label(window, text = "Namespace", fg = "blue", )
posix_label = Label(window, text = "POSIX", justify=LEFT, anchor='w')
posix_label2 = Label(window, text = "POSIX")
sysv_label = Label(window, text = "SYSV")
sysv_label2 = Label(window, text = "SYSV")

#define buttons

run_button = Button(window, text = "RUN", command = run, fg = "spring green",  padx=40, bg='green')
#abort_button = Button(window, text = "ABORT", command = abort, fg = "red",  padx=40, bg='green')
iteration_argument = Entry(window, width = 10)

native_posix_semaphore_button = Checkbutton(window,  var = my_map['native']['posix']['s'], text = "             ", onvalue = 1, offvalue = 0)
native_posix_messagequeue_button = Checkbutton(window,  var = my_map['native']['posix']['mq'], onvalue = 1, offvalue = 0)
native_posix_sharedmem_button = Checkbutton(window,  var = my_map['native']['posix']['sm'], onvalue = 1, offvalue = 0)
native_sysv_semaphore_button = Checkbutton(window,  var = my_map['native']['sysv']['s'], onvalue = 1, offvalue = 0)
native_sysv_messagequeue_button = Checkbutton(window,  var = my_map['native']['sysv']['mq'], onvalue = 1, offvalue = 0)
native_sysv_sharedmem_button = Checkbutton(window,  var = my_map['native']['sysv']['sm'], onvalue = 1, offvalue = 0)

namespace_posix_semaphore_button = Checkbutton(window,  var = my_map['namespace']['posix']['s'], onvalue = 1, offvalue = 0)
namespace_posix_messagequeue_button = Checkbutton(window, var = my_map['namespace']['posix']['mq'], onvalue = 1, offvalue = 0)
namespace_posix_sharedmem_button = Checkbutton(window, var = my_map['namespace']['posix']['sm'], onvalue = 1, offvalue = 0)
namespace_sysv_semaphore_button = Checkbutton(window, var = my_map['namespace']['sysv']['s'], onvalue = 1, offvalue = 0)
namespace_sysv_messagequeue_button = Checkbutton(window, var = my_map['namespace']['sysv']['mq'], onvalue = 1, offvalue = 0)
namespace_sysv_sharedmem_button = Checkbutton(window, var = my_map['namespace']['sysv']['sm'], onvalue = 1, offvalue = 0)





#Posistion elements 
spanner = 10
window.grid_columnconfigure(0,weight=1)
window.grid_columnconfigure(1,weight=1)
window.grid_columnconfigure(2,weight=1)
window.grid_columnconfigure(3,weight=1)
window.grid_columnconfigure(10,weight=50)
for i in range(2, spanner) :
    window.grid_rowconfigure(i,weight=1)

run_button.grid(row = 0, column = 0, columnspan = 1, rowspan = 1, sticky = 'nwse')
iteration_argument.grid(row = 1, column = 0, columnspan = 1, rowspan = 1, sticky = 'nse')
iteration_label.grid(row = 1, column = 0, columnspan = 1, rowspan = 1, sticky = 'nsw')


native_label.grid(row = 0, column = 1)
namespace_label.grid(row = 0, column = 2)



posix_label.grid(row = 1, column = 1, sticky='w')
sysv_label.grid(row = 1, column = 1, sticky='e')

posix_label2.grid(row = 1, column = 2, sticky='w')
sysv_label2.grid(row = 1, column = 2, sticky='e')

sem_label.grid(row = 2, column = 0, sticky='w')
sm_label.grid(row = 3, column = 0, sticky='w')
mq_label.grid(row = 4, column = 0, sticky='w')

native_posix_semaphore_button.grid(row = 2, column = 1, sticky='w')
native_sysv_semaphore_button.grid(row = 2, column = 1, sticky='e')
namespace_posix_semaphore_button.grid(row = 2, column = 2, sticky='w')
namespace_sysv_semaphore_button.grid(row = 2, column = 2, sticky='e')



native_posix_sharedmem_button.grid(row = 3, column = 1, sticky='w')
native_sysv_sharedmem_button.grid(row = 3, column = 1, sticky='e')
namespace_posix_sharedmem_button.grid(row = 3, column = 2, sticky='w')
namespace_sysv_sharedmem_button.grid(row = 3, column = 2, sticky='e')

native_posix_messagequeue_button.grid(row = 4, column = 1, sticky='w')
native_sysv_messagequeue_button.grid(row = 4, column = 1, sticky='e')
namespace_sysv_messagequeue_button.grid(row = 4, column = 2, sticky='w')
namespace_posix_messagequeue_button.grid(row = 4, column = 2, sticky='e')

tkinter.ttk.Separator(window, orient=VERTICAL).grid(column=1, row=0, rowspan=5, sticky='ens') #middle separator line
tkinter.ttk.Separator(window, orient=VERTICAL).grid(column=1, row=0, rowspan=5, sticky='wns') #left separator line

tkinter.ttk.Separator(window, orient=VERTICAL).grid(column=2, row=0, rowspan=5, sticky='wns') #middle separator line
tkinter.ttk.Separator(window, orient=VERTICAL).grid(column=2, row=0, rowspan=5, sticky='ens') #right separator line

tkinter.ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=1, columnspan=3, sticky='ews')
tkinter.ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=2, columnspan=3, sticky='ews')
tkinter.ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=3, columnspan=3, sticky='ews')
tkinter.ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=4, columnspan=3, sticky='ews')





window.mainloop()
