from tkinter import *
import subprocess

window = Tk()
my_map = {"native" : 
                    {"sysv" :  
                            {"mq" : IntVar(), 
                             "sm" : IntVar(), 
                             "s" : IntVar()}, 

                    "posix" : {"mq" : IntVar(), 
                               "sm" : IntVar(), 
                               "s" : IntVar()}}, 
          "namespace" : 
                    {"sysv" :  {"mq" : IntVar(), 
                                "sm" : IntVar(), 
                                "s" : IntVar()}, 

                    "posix" :  {"mq" : IntVar(), 
                                "sm" : IntVar(), 
                                "s" : IntVar()}} 
        }

def run():
    window.update( );
    #print( window.winfo_width());
    sum = my_map['native']['posix']['s'].get() + my_map['native']['posix']['mq'].get() + my_map['native']['posix']['sm'].get() + my_map['native']['posix']['s'].get() + my_map['native']['posix']['mq'].get() + my_map['native']['posix']['sm'].get() + my_map['native']['posix']['s'].get() + my_map['native']['posix']['mq'].get() + my_map['native']['posix']['sm'].get()
    print(sum)

        
#Native POSIX IPCs
    if(my_map['native']['posix']['s'].get()):
        print("native posix semaphore")
        subprocess.run(['sudo make eric'], shell = True)    
    if(my_map['native']['posix']['mq'].get()):
        print("native posix message queue")    
        subprocess.run(['sudo make alex'], shell = True)    
    if(my_map['native']['posix']['sm'].get()):
        print("native posix shared memory")    
        subprocess.run(['sudo make vincent'], shell = True)    

#Namespace POSIX IPCs
    if(my_map['namespace']['posix']['s'].get()):
        print("namespace posix semaphore")    
        subprocess.run(['sudo make eric_namespace'], shell = True)    
    if(my_map['namespace']['posix']['mq'].get()):
        print("namespace posix message queue")    
        subprocess.run(['sudo make alex_namespace'], shell = True)    
    if(my_map['namespace']['posix']['sm'].get()):
        print("namespace posix shared memory")    
        subprocess.run(['sudo make vincent_namespace'], shell = True)    

#Native SYSV IPCs
    if(my_map['native']['sysv']['s'].get()):
        print("native sysv semaphore")    
        subprocess.run(['sudo make eric'], shell = True)    
    if(my_map['native']['sysv']['mq'].get()):
        print("native sysv message queue")    
        subprocess.run(['sudo make alex'], shell = True)    
    if(my_map['native']['sysv']['sm'].get()):
        print("native sysv shared memory")  
        subprocess.run(['sudo make vincent'], shell = True)    
  
#Namespace SYSV IPCs
    if(my_map['namespace']['sysv']['s'].get()):
        print("namespace sysv semaphore")    
        subprocess.run(['sudo make eric_namespace'], shell = True)    
    if(my_map['namespace']['sysv']['mq'].get()):
        print("namespace sysv message queue")    
        subprocess.run(['sudo make alex_namespace'], shell = True)    
    if(my_map['namespace']['sysv']['sm'].get()):
        print("namespace sysv shared memory")   
        subprocess.run(['sudo make vincent_namespace'], shell = True)    




        
    
    
    


w_height  = 480
w_width = 720
window.geometry(''+ str(w_width) +  'x' + str(w_height))

native_label = Label(window, text = "Native", fg = "blue",)
sem_label = Label(window, text = "Semaphore", fg = "blue",)
sm_label = Label(window, text = "Shared Memory", fg = "blue",)
mq_label = Label(window, text = "Message Queue", fg = "blue",)
namespace_label = Label(window, text = "Name Space", fg = "blue", )
posix_label = Label(window, text = "POSIX", justify=LEFT, anchor='w')
posix_label2 = Label(window, text = "POSIX")
sysv_label = Label(window, text = "SYSV")
sysv_label2 = Label(window, text = "SYSV")

#define buttons

run_button = Button(window, text = "RUN", command = run, fg = "spring green", anchor="w", padx=100, bg='green')

native_posix_semaphore_button = Checkbutton(window, text = "", var = my_map['native']['posix']['s'], onvalue = 1, offvalue = 0)
native_posix_messagequeue_button = Checkbutton(window, text = "", var = my_map['native']['posix']['mq'], onvalue = 1, offvalue = 0)
native_posix_sharedmem_button = Checkbutton(window, text = "", var = my_map['native']['posix']['sm'], onvalue = 1, offvalue = 0)
native_sysv_semaphore_button = Checkbutton(window, text = "", var = my_map['native']['sysv']['s'], onvalue = 1, offvalue = 0)
native_sysv_messagequeue_button = Checkbutton(window, text = "", var = my_map['native']['sysv']['mq'], onvalue = 1, offvalue = 0)
native_sysv_sharedmem_button = Checkbutton(window, text = "", var = my_map['native']['sysv']['sm'], onvalue = 1, offvalue = 0)

namespace_posix_semaphore_button = Checkbutton(window, text = "", var = my_map['namespace']['posix']['s'], onvalue = 1, offvalue = 0)
namespace_posix_messagequeue_button = Checkbutton(window, text = "", var = my_map['namespace']['posix']['mq'], onvalue = 1, offvalue = 0)
namespace_posix_sharedmem_button = Checkbutton(window, text = "", var = my_map['namespace']['posix']['sm'], onvalue = 1, offvalue = 0)
namespace_sysv_semaphore_button = Checkbutton(window, text = "", var = my_map['namespace']['sysv']['s'], onvalue = 1, offvalue = 0)
namespace_sysv_messagequeue_button = Checkbutton(window, text = "", var = my_map['namespace']['sysv']['mq'], onvalue = 1, offvalue = 0)
namespace_sysv_sharedmem_button = Checkbutton(window, text = "", var = my_map['namespace']['sysv']['sm'], onvalue = 1, offvalue = 0)




#window.configure(bg='gray');
#Posistion elements 
spanner = 10
window.grid_columnconfigure(0,weight=1)
window.grid_columnconfigure(1,weight=1)
window.grid_columnconfigure(2,weight=1)
window.grid_columnconfigure(3,weight=1)
window.grid_columnconfigure(10,weight=50)
for i in range(3, spanner) :
    window.grid_rowconfigure(i,weight=1)

mover = 1
run_button.grid(row = 0, column = 0, columnspan = 2, rowspan = 1)

span = 1;
native_label.grid(row = 1, column = 0+mover, columnspan=span)
namespace_label.grid(row = 1, column = 1+mover , columnspan=span)



# sysv_label.grid(row = 2, column = 1)
# posix_label.grid(row = 3, column = 1)
posix_label.grid(row = 2, column = 0+mover, sticky='w')
sysv_label.grid(row = 2, column = 0+mover, sticky='e')

posix_label2.grid(row = 2, column = 1+mover, sticky='w')
sysv_label2.grid(row = 2, column = 1+mover, sticky='e')

sem_label.grid(row = 3, column = 0, sticky='w')
sm_label.grid(row = 4, column = 0, sticky='w')
mq_label.grid(row = 5, column = 0, sticky='w')

native_posix_semaphore_button.grid(row = 3, column = 1, sticky='w')
native_sysv_semaphore_button.grid(row = 3, column = 1, sticky='e')
namespace_posix_semaphore_button.grid(row = 3, column = 2, sticky='w')
namespace_sysv_semaphore_button.grid(row = 3, column = 2, sticky='e')



native_posix_sharedmem_button.grid(row = 4, column = 1, sticky='w')
native_sysv_sharedmem_button.grid(row = 4, column = 1, sticky='e')
namespace_posix_sharedmem_button.grid(row = 4, column = 2, sticky='w')
namespace_sysv_sharedmem_button.grid(row = 4, column = 2, sticky='e')

native_posix_messagequeue_button.grid(row = 5, column = 1, sticky='w')
native_sysv_messagequeue_button.grid(row = 5, column = 1, sticky='e')
namespace_sysv_messagequeue_button.grid(row = 5, column = 2, sticky='w')
namespace_posix_messagequeue_button.grid(row = 5, column = 2, sticky='e')




window.mainloop()
