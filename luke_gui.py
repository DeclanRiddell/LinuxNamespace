from tkinter import *
import tkinter.ttk
c_width = 1080; c_height = 480;
root = Tk(className="Linux IPC Metrics")
canvas = Canvas(root, width = c_width, height = c_height)
canvas.pack()


def method2():
    distro_label = Label(picker_frame, text="Namespace\t\tNative", bg=p_col).pack()
    namespace_lib_label = Label(picker_frame, text="POSIX\t\tSysv\tPOSIX\t\tSysv", bg=p_col).pack()
   
   
    semaphore_label = Label(picker_frame, text="Semaphores", bg=p_col, justify=LEFT, anchor='w')
    message_queue_label = Label(picker_frame, text="Message Queue", bg=p_col).pack()
    shared_memory_label = Label(picker_frame, text="Shared Memory", bg=p_col).pack()
    posix_label = Label(picker_frame, text="Posix", bg=p_col).pack()
    sysv_label = Label(picker_frame, text="SysV", bg=p_col).pack()
    run_button = Button(picker_frame, text="Run", padx=picker_frame.winfo_width() / 2, pady=5, anchor='c').grid(row=0,column=0,rowspan=10);

def change_size_callback(event):
    print(event.width,event.height)
    c_width = event.width;
    c_height = event.height

p_col = '#ccccff'
font_type= 'Arial'
font_size = 12
def init():
    print(canvas['width'])

    root.bind('<Configure>',change_size_callback)
    picker_w = 0.5; picker_h = 1;
    picker_frame = Frame(root, bg=p_col)
    picker_frame.place(width = c_width * picker_w, relheight=picker_h)
    matplot_frame = Frame(root, bg="#e6ffff")
    matplot_frame.place(relwidth = 1.0 , relheight = picker_h, x=c_width * picker_w, )
    root.update()



   
    #run_button = Button(picker_frame, text="Run", padx=picker_frame.winfo_width() / 2, pady=5, anchor='c').grid(row=0,column=0,rowspan=10);
    Button(picker_frame, text="Run", anchor='c', padx=15, bg='#ccffe6').grid(row=0,column=0, columnspan=1);
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
    message_queue_label = Label(picker_frame, text="Me Queue", bg=p_col,font=(font_type, font_size)).grid(row=4+offset, column=0, sticky='w')
    Label(picker_frame, text="\t", bg=p_col,font=(font_type, font_size)).grid(row=5+offset, column=0)
    shared_memory_label = Label(picker_frame, text="Shared Memory", bg=p_col,font=(font_type, font_size)).grid(row=6+offset, column=0, sticky='w')

    tkinter.ttk.Separator(picker_frame, orient=VERTICAL).grid(column=0, row=3, rowspan=8, sticky='ens') 
    tkinter.ttk.Separator(picker_frame, orient=VERTICAL).grid(column=2, row=3, rowspan=8, sticky='ns') 
    tkinter.ttk.Separator(picker_frame, orient=VERTICAL).grid(column=4, row=3, rowspan=8, sticky='ns') 
    tkinter.ttk.Separator(picker_frame, orient=VERTICAL).grid(column=6, row=3, rowspan=8, sticky='ns') 
    tkinter.ttk.Separator(picker_frame, orient=VERTICAL).grid(column=8, row=3, rowspan=8, sticky='ns') 

    tkinter.ttk.Separator(picker_frame, orient=HORIZONTAL).grid(column=1, row=3, columnspan=8, sticky='ew') 
    tkinter.ttk.Separator(picker_frame, orient=HORIZONTAL).grid(column=1, row=5, columnspan=8, sticky='ew') 
    tkinter.ttk.Separator(picker_frame, orient=HORIZONTAL).grid(column=1, row=7, columnspan=8, sticky='ew') 
    tkinter.ttk.Separator(picker_frame, orient=HORIZONTAL).grid(column=1, row=9, columnspan=8, sticky='ew') 

    
    # ipc_label.grid(row=0, column=0)
    # semaphore_label.grid(row=2, column=0)
    # message_queue_label.grid(row=3, column=0)
    # shared_memory_label.grid(row=4, column=0)

    # spacer = 1
    # posix_label.grid(row=1, column=2)
    # sysv_label.grid(row=1, column=7)
    root.mainloop()


if __name__ == '__main__':
    init()