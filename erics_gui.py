
from tkinter import *
import tkinter.ttk
window = Tk()
my_map = {"native" : {"sysv" :  {"mq" : IntVar(), "sm" : IntVar(), "s" : IntVar()}, "posix" :  {"mq" : IntVar(), "sm" : IntVar(), "s" : IntVar()}}, "namespace" : {"sysv" :  {"mq" : IntVar(), "sm" : IntVar(), "s" : IntVar()}, "posix" :  {"mq" : IntVar(), "sm" : IntVar(), "s" : IntVar()}} }
def run():
    window.update( );
        
    if(my_map['native']['posix']['s'].get()):
        print("native posix semaphore")    
    if(my_map['native']['posix']['mq'].get()):
        print("native posix message queue")    
    if(my_map['native']['posix']['sm'].get()):
        print("native posix shared memory")    

    if(my_map['namespace']['posix']['s'].get()):
        print("namespace posix semaphore")    
    if(my_map['namespace']['posix']['mq'].get()):
        print("namespace posix message queue")    
    if(my_map['namespace']['posix']['sm'].get()):
        print("namespace posix shared memory")    


    if(my_map['native']['sysv']['s'].get()):
        print("native sysv semaphore")    
    if(my_map['native']['sysv']['mq'].get()):
        print("native sysv message queue")    
    if(my_map['native']['sysv']['sm'].get()):
        print("native sysv shared memory")    

    if(my_map['namespace']['sysv']['s'].get()):
        print("namespace sysv semaphore")    
    if(my_map['namespace']['sysv']['mq'].get()):
        print("namespace sysv message queue")    
    if(my_map['namespace']['sysv']['sm'].get()):
        print("namespace sysv shared memory")   

def abort():
    print("AHHHHH!!!! ABORT!!!")


        
    
    
    


w_height  = 480
w_width = 720
window.geometry(''+ str(w_width) +  'x' + str(w_height))

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
abort_button = Button(window, text = "ABORT", command = abort, fg = "red",  padx=40, bg='green')

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
for i in range(3, spanner) :
    window.grid_rowconfigure(i,weight=1)

run_button.grid(row = 0, column = 0, columnspan = 1, rowspan = 1, sticky = 'nwse')
abort_button.grid(row = 1, column = 0, columnspan = 1, rowspan = 1, sticky = 'nwse')



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

tkinter.ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=2, columnspan=3, sticky='ews')
tkinter.ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=3, columnspan=3, sticky='ews')
tkinter.ttk.Separator(window, orient=HORIZONTAL).grid(column=0, row=4, columnspan=3, sticky='ews')





window.mainloop()
