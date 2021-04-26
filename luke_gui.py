from tkinter import *

c_width = 720; c_height = 480;
root = Tk(className="Linux IPC Metrics")
canvas = Canvas(root, width = c_width, height = c_height)
canvas.pack()

def change_size_callback(event):
    print(event.width,event.height)
    c_width = event.width;
    c_height = event.height
def init():
    print(canvas['width'])

    root.bind('<Configure>',change_size_callback)

    picker_w = 0.4; picker_h = 1;
    picker_frame = Frame(root, bg="#4F4776")
    picker_frame.place(width = 720 * picker_w, relheight=picker_h)

    matplot_frame = Frame(root, bg="#475E76")
    matplot_frame.place(relwidth = 1.0 , relheight = picker_h, x=720 * picker_w, )
    ipc_label = Label(picker_frame, text="IPC\tSup").pack()
    semaphore_label = Label(picker_frame, text="Semaphores").pack()
    message_queue_label = Label(picker_frame, text="Message Queue").pack()
    shared_memory_label = Label(picker_frame, text="Shared Memory").pack()
    posix_label = Label(picker_frame, text="Posix").pack()
    sysv_label = Label(picker_frame, text="SysV").pack()


    
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