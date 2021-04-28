from tkinter import *
import tkinter.ttk
import subprocess
from PIL import ImageTk, Image

c_width = 1080; c_height = 480;
root = Tk(className="Linux IPC Metrics")
canvas = Canvas(root, width = c_width, height = c_height)
canvas.pack()
iteration_count = 444;

my_map = {"native" : 
                    {"sysv" :  
                            {"messagequeue" : IntVar(), 
                             "sharedmemory" : IntVar(), 
                             "semaphore" : IntVar()}, 

                    "posix" : {"messagequeue" : IntVar(), 
                               "sharedmemory" : IntVar(), 
                               "semaphore" : IntVar()
                               }
                    }, 
          "namespace" : 
                    {"sysv" :  {"messagequeue" : IntVar(), 
                                "sharedmemory" : IntVar(), 
                                "semaphore" : IntVar()
                                }, 

                    "posix" :  {"messagequeue" : IntVar(), 
                                "sharedmemory" : IntVar(), 
                                "semaphore" : IntVar()
                                }
                    } 
        }




def method2():
    distro_label = Label(picker_frame, text="Namespace\t\tNative", bg=p_col).pack()
    namespace_lib_label = Label(picker_frame, text="POSIX\t\tSysv\tPOSIX\t\tSysv", bg=p_col).pack()
   
   
    semaphore_label = Label(picker_frame, text="Semaphores", bg=p_col, justify=LEFT, anchor='w')
    message_queue_label = Label(picker_frame, text="Message Queue", bg=p_col).pack()
    shared_memory_label = Label(picker_frame, text="Shared Memory", bg=p_col).pack()
    posix_label = Label(picker_frame, text="Posix", bg=p_col).pack()
    sysv_label = Label(picker_frame, text="SysV", bg=p_col).pack()
    run_button = Button(picker_frame, text="Run", padx=picker_frame.winfo_width() / 2, pady=5, anchor='c').grid(row=0,column=0,rowspan=10);
p_col = '#ccccff'
font_type= 'Arial'
font_size = 12
picker_frame = Frame(root, bg=p_col)
matplot_frame = Frame(root, bg="#e6ffff")

def change_size_callback(event):
    print(event.width,event.height)
    c_width = event.width;
    c_height = event.height


def change_image_callback(event):
    img2 = ImageTk.PhotoImage(Image.open('bar_graph.png').resize((200, 200), Image.ANTIALIAS))
    panel = Label(matplot_frame, image = img2).grid(row= 0, column = 0)
    panel.configure(image=img2)
    panel.image=img2


img = ImageTk.PhotoImage(Image.open('bar_graph.png').resize((200, 200), Image.ANTIALIAS))
panel = Label(matplot_frame, image = img).grid(row= 0, column = 0)
def init():
    print(canvas['width'])

    root.bind('<Configure>',change_size_callback)
    root.bind('<Return>',change_image_callback)
    picker_w = 0.6; picker_h = 1;
    picker_frame.place(width = c_width * picker_w, relheight=picker_h)
    matplot_frame.place(relwidth = 1.0 , relheight = picker_h, x=c_width * picker_w, )
    root.update()



   
    #run_button = Button(picker_frame, text="Run", padx=picker_frame.winfo_width() / 2, pady=5, anchor='c').grid(row=0,column=0,rowspan=10);
    Button(picker_frame, text="Run", command = execute, anchor='c', padx=15, bg='#ccffe6').grid(row=1,column=0, columnspan=1);
    #Label(picker_frame, text="Namespace", bg=p_col).grid(row=0, column=0)
    offset = 2
    namespace_label = Label(picker_frame, text="Namespace",font=(font_type, font_size), bg=p_col).grid(row=0+(int)(offset/2), column=2)
    native_label = Label(picker_frame, text="Native",font=(font_type, font_size), bg=p_col).grid(row=0+(int)(offset/2), column=6)
    blank_label = Label(picker_frame, text="\t", bg=p_col,font=(font_type, font_size)).grid(row=0+(int)(offset/2), column=4)
    namespace_posix_label = Label(picker_frame, text="POSIX", bg=p_col,font=(font_type, font_size)).grid(row=1+(int)(offset/2), column=1)
    namespace_sysv_label = Label(picker_frame, text="SysV", bg=p_col,font=(font_type, font_size)).grid(row=1+(int)(offset/2), column=3)
    native_posix_label = Label(picker_frame, text="POSIX", bg=p_col,font=(font_type, font_size)).grid(row=1+(int)(offset/2), column=5)
    native_sysv_label = Label(picker_frame, text="SysV", bg=p_col,font=(font_type, font_size)).grid(row=1+(int)(offset/2), column=7)
   
   
    blank_label2 = Label(picker_frame, text="\t", bg=p_col,font=(font_type, font_size)).grid(row=offset, column=0)
    semaphore_label = Label(picker_frame, text="Semaphores", bg=p_col, justify=LEFT, anchor='w',font=(font_type, font_size)).grid(row=2+offset, column=0, sticky='w')
    Label(picker_frame, text="\t", bg=p_col,font=(font_type, font_size)).grid(row=3+offset, column=0)
    message_queue_label = Label(picker_frame, text="Message Queue", bg=p_col,font=(font_type, font_size)).grid(row=4+offset, column=0, sticky='w')
    Label(picker_frame, text="\t", bg=p_col,font=(font_type, font_size)).grid(row=5+offset, column=0)
    shared_memory_label = Label(picker_frame, text="Shared Memory", bg=p_col,font=(font_type, font_size)).grid(row=6+offset, column=0, sticky='w')


    rando = "" + str(iteration_count)
    iteration_label = Label(picker_frame, text="Iterations:", bg=p_col,font=(font_type, font_size)).grid(row=0, column=0)
    iteration_argument = Entry(picker_frame, width = 10, textvariable = rando).grid(row = 0, column = 1)
    

    tkinter.ttk.Separator(picker_frame, orient=VERTICAL).grid(column=0, row=3, rowspan=8, sticky='ens') 
    tkinter.ttk.Separator(picker_frame, orient=VERTICAL).grid(column=2, row=3, rowspan=8, sticky='ns') 
    tkinter.ttk.Separator(picker_frame, orient=VERTICAL).grid(column=4, row=3, rowspan=8, sticky='ns') 
    tkinter.ttk.Separator(picker_frame, orient=VERTICAL).grid(column=6, row=3, rowspan=8, sticky='ns') 
    tkinter.ttk.Separator(picker_frame, orient=VERTICAL).grid(column=8, row=3, rowspan=8, sticky='ns') 

    tkinter.ttk.Separator(picker_frame, orient=HORIZONTAL).grid(column=1, row=3, columnspan=8, sticky='ew') 
    tkinter.ttk.Separator(picker_frame, orient=HORIZONTAL).grid(column=1, row=5, columnspan=8, sticky='ew') 
    tkinter.ttk.Separator(picker_frame, orient=HORIZONTAL).grid(column=1, row=7, columnspan=8, sticky='ew') 
    tkinter.ttk.Separator(picker_frame, orient=HORIZONTAL).grid(column=1, row=9, columnspan=8, sticky='ew') 
    setup_map_checkboxes()


    
    
    # ipc_label.grid(row=0, column=0)
    # semaphore_label.grid(row=2, column=0)
    # message_queue_label.grid(row=3, column=0)
    # shared_memory_label.grid(row=4, column=0)


    # spacer = 1
    # posix_label.grid(row=1, column=2)
    # sysv_label.grid(row=1, column=7)
    root.mainloop()


def setup_map_checkboxes():
    native_posix_semaphore_button = Checkbutton(picker_frame,  var = my_map['native']['posix']['semaphore'], bg=p_col, onvalue = 1, offvalue = 0).grid(row = 4, column = 5)
    native_posix_messagequeue_button = Checkbutton(picker_frame,  var = my_map['native']['posix']['messagequeue'], bg=p_col, onvalue = 1, offvalue = 0).grid(row = 6, column = 5)
    native_posix_sharedmem_button = Checkbutton(picker_frame,  var = my_map['native']['posix']['sharedmemory'], bg=p_col, onvalue = 1, offvalue = 0).grid(row = 8, column = 5)
    native_sysv_semaphore_button = Checkbutton(picker_frame,  var = my_map['native']['sysv']['semaphore'], bg=p_col, onvalue = 1, offvalue = 0).grid(row = 4, column = 7)
    native_sysv_messagequeue_button = Checkbutton(picker_frame,  var = my_map['native']['sysv']['messagequeue'], bg=p_col, onvalue = 1, offvalue = 0).grid(row = 6, column = 7)
    native_sysv_sharedmem_button = Checkbutton(picker_frame,  var = my_map['native']['sysv']['sharedmemory'], bg=p_col, onvalue = 1, offvalue = 0).grid(row = 8, column = 7)

    namespace_posix_semaphore_button = Checkbutton(picker_frame,  var = my_map['namespace']['posix']['semaphore'], bg=p_col, onvalue = 1, offvalue = 0).grid(row = 4, column = 1)
    namespace_posix_messagequeue_button = Checkbutton(picker_frame, var = my_map['namespace']['posix']['messagequeue'], bg=p_col, onvalue = 1, offvalue = 0).grid(row = 6, column = 1)
    namespace_posix_sharedmem_button = Checkbutton(picker_frame, var = my_map['namespace']['posix']['sharedmemory'], bg=p_col, onvalue = 1, offvalue = 0).grid(row = 8, column = 1)
    namespace_sysv_semaphore_button = Checkbutton(picker_frame, var = my_map['namespace']['sysv']['semaphore'], bg=p_col, onvalue = 1, offvalue = 0).grid(row = 4, column = 3)
    namespace_sysv_messagequeue_button = Checkbutton(picker_frame, var = my_map['namespace']['sysv']['messagequeue'], bg=p_col, onvalue = 1, offvalue = 0).grid(row = 6, column = 3)
    namespace_sysv_sharedmem_button = Checkbutton(picker_frame, var = my_map['namespace']['sysv']['sharedmemory'], bg=p_col, onvalue = 1, offvalue = 0).grid(row = 8, column = 3)

def execute():
        #Native POSIX IPCs
    if(my_map['native']['posix']['semaphore'].get()):
        print("native posix semaphore")
        #subprocess.call(['sudo ./IPC_EXE 5 0 ' + str(iteration_count)], shell = True, timeout=1)    
        subprocess.call(['python3 create_graph.py '], shell = True)   
        matplot_frame.update() 
        canvas.update()
        #subprocess.run(['sudo make eric'], shell = True)    
    if(my_map['native']['posix']['messagequeue'].get()):
        print("native posix message queue")    
        #subprocess.run(['sudo make alex'], shell = True)    
    if(my_map['native']['posix']['sharedmemory'].get()):
        print("native posix shared memory")    
        #subprocess.run(['sudo make vincent'], shell = True)    

#Namespace POSIX IPCs
    if(my_map['namespace']['posix']['semaphore'].get()):
        print("namespace posix semaphore")    
        #subprocess.run(['sudo make eric_namespace'], shell = True)    
    if(my_map['namespace']['posix']['messagequeue'].get()):
        print("namespace posix message queue")    
        #subprocess.run(['sudo make alex_namespace'], shell = True)    
    if(my_map['namespace']['posix']['sharedmemory'].get()):
        print("namespace posix shared memory")    
        #subprocess.run(['sudo make vincent_namespace'], shell = True)    

#Native SYSV IPCs
    if(my_map['native']['sysv']['semaphore'].get()):
        print("native sysv semaphore")    
        #subprocess.run(['sudo make eric'], shell = True)    
    if(my_map['native']['sysv']['messagequeue'].get()):
        print("native sysv message queue")    
        #subprocess.run(['sudo make alex'], shell = True)    
    if(my_map['native']['sysv']['sharedmemory'].get()):
        print("native sysv shared memory")  
        #subprocess.run(['sudo make vincent'], shell = True)    
  
#Namespace SYSV IPCs
    if(my_map['namespace']['sysv']['semaphore'].get()):
        print("namespace sysv semaphore")    
        #subprocess.run(['sudo make eric_namespace'], shell = True)    
    if(my_map['namespace']['sysv']['messagequeue'].get()):
        print("namespace sysv message queue")    
        #subprocess.run(['sudo make alex_namespace'], shell = True)    
    if(my_map['namespace']['sysv']['sharedmemory'].get()):
        print("namespace sysv shared memory")   
        #subprocess.run(['sudo make vincent_namespace'], shell = True)

if __name__ == '__main__':
    init()