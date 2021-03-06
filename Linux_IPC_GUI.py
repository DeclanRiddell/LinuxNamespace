from tkinter import *
import tkinter.ttk
import subprocess
from PIL import ImageTk, Image
import os, signal
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import csv
c_width = 1120; c_height = 1000;
root = Tk(className="- ASRC Linux Namespace Performance Project -")
root.resizable(False, False)
canvas = Canvas(root, width = c_width, height = c_height, bg='skyblue')
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

def create_table():
    title_text = 'Average runtimes'
    footer_text = 'ASRC Federal'
    fig_background_color = 'skyblue'
    fig_border = 'steelblue'
    data = pd.read_csv("data.csv")
    count = 0

    while count < len(data):
        val = my_map_data[data['ENVIRONMENT'][count]][data['LIBRARY'][count]][data['IPC'][count]][0]
        c = my_map_data[data['ENVIRONMENT'][count]][data['LIBRARY'][count]][data['IPC'][count]][1]
        my_map_data[data['ENVIRONMENT'][count]][data['LIBRARY'][count]][data['IPC'][count]] = [val + data['AVG_TIME'][count], c + 1]
        count += 1

    avg_native_posix_semaphore = my_map_data['native']['posix']['semaphore'][0] / float(my_map_data['native']['posix']['semaphore'][1] + 1)
    avg_native_posix_mq = my_map_data['native']['posix']['message_queue'][0] / float(my_map_data['native']['posix']['message_queue'][1] + 1)
    avg_native_posix_sm = my_map_data['native']['posix']['shared_memory'][0] / float(my_map_data['native']['posix']['shared_memory'][1] + 1)
    avg_native_sysv_semaphore = my_map_data['native']['sysv']['semaphore'][0] / float(my_map_data['native']['sysv']['semaphore'][1] + 1)
    avg_native_sysv_mq = my_map_data['native']['sysv']['message_queue'][0] / float(my_map_data['native']['sysv']['message_queue'][1] + 1)
    avg_native_sysv_sm = my_map_data['native']['sysv']['shared_memory'][0] / float(my_map_data['native']['sysv']['shared_memory'][1] + 1)
    avg_namespace_posix_semaphore = my_map_data['namespace']['posix']['semaphore'][0] / float(my_map_data['namespace']['posix']['semaphore'][1] + 1)
    avg_namespace_posix_mq = my_map_data['namespace']['posix']['message_queue'][0] / float(my_map_data['namespace']['posix']['message_queue'][1] + 1)
    avg_namespace_posix_sm = my_map_data['namespace']['posix']['shared_memory'][0] / float(my_map_data['namespace']['posix']['shared_memory'][1] + 1)
    avg_namespace_sysv_semaphore = my_map_data['namespace']['sysv']['semaphore'][0] / float(my_map_data['namespace']['sysv']['semaphore'][1] + 1)
    avg_namespace_sysv_mq = my_map_data['namespace']['sysv']['message_queue'][0] / float(my_map_data['namespace']['sysv']['message_queue'][1] + 1)
    avg_namespace_sysv_sm = my_map_data['namespace']['sysv']['shared_memory'][0] / float(my_map_data['namespace']['sysv']['shared_memory'][1] + 1)
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
        cell_text.append(["{0:0.5f}".format(x) for x in row])# Get some lists of color specs for row and column headers
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
    #plt.show()
    plt.savefig('Resources/table.png',
                #bbox='tight',
                edgecolor=fig.get_edgecolor(),
                facecolor=fig.get_facecolor(),
                dpi=150
                )

    plt.close('all')
    plt.clf()

def create_graph():
    filename = 'data.csv'
    search = "semaphore"
    semaphore_list = []
    semaphore_field = ['IPC','LIBRARY','ENVIRONMENT','AVG_TIME','ITERATIONS']

    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            if search in row:
                semaphore_list.append(row)

    with open("semaphore.csv",'w') as semaphore_file:
        csvwriter = csv.writer(semaphore_file)
        csvwriter.writerow(semaphore_field)
        csvwriter.writerows(semaphore_list)

    semaphore_data = pd.read_csv("semaphore.csv")
    if(semaphore_data.empty):
        plt.draw()
    else:
        fig = sns.catplot(x = "AVG_TIME", y = "ENVIRONMENT" , data = semaphore_data, kind = "strip", hue = "LIBRARY", dodge = True, palette = sns.color_palette(['orange', 'blue']))
        plt.title('Semaphore Graph')
        fig.set_xticklabels(rotation=40, ha='right')
        plt.tight_layout()
        plt.savefig('Resources/semaphore_graph.png', dpi = 200)

    search = "message_queue"
    msgq_list = []
    msgq_field = ['IPC','LIBRARY','ENVIRONMENT','AVG_TIME','ITERATIONS']

    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            if search in row:
                msgq_list.append(row)

    with open("msgq.csv",'w') as msgq_file:
        csvwriter = csv.writer(msgq_file)
        csvwriter.writerow(msgq_field)
        csvwriter.writerows(msgq_list)

    msgq_data = pd.read_csv("msgq.csv")
    if(msgq_data.empty):
        plt.draw()
    else:
        fig = sns.catplot(x = "AVG_TIME", y = "ENVIRONMENT" , data = msgq_data, kind = "strip", hue = "LIBRARY", dodge = True, palette = sns.color_palette(['orange', 'blue']))
        plt.title('Message Queue Graph')
        fig.set_xticklabels(rotation=40, ha='right')
    plt.tight_layout()
    plt.savefig('Resources/msgq_graph.png', dpi = 200)




    search = "shared_memory"
    shared_memory_list = []
    shared_memory_field = ['IPC','LIBRARY','ENVIRONMENT','AVG_TIME','ITERATIONS']

    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            if search in row:
                shared_memory_list.append(row)

    with open("shared_memory.csv",'w') as shared_memory_file:
        csvwriter = csv.writer(shared_memory_file)
        csvwriter.writerow(shared_memory_field)
        csvwriter.writerows(shared_memory_list)

    shared_memory_data = pd.read_csv("shared_memory.csv")
    if(shared_memory_data.empty):
        plt.draw()
    else:
        fig = sns.catplot(x = "AVG_TIME", y = "ENVIRONMENT" , data = shared_memory_data, kind = "strip", hue = "LIBRARY", dodge = True, palette = sns.color_palette(['orange', 'blue']))
        plt.title('Shared Memory Graph')
        fig.set_xticklabels(rotation=40, ha='right')
        plt.tight_layout()
        plt.savefig('Resources/shared_memory_graph.png', dpi = 200)
    plt.cla()
    plt.clf()

p_col = '#ccccff'
font_type= 'Arial'
font_size = 12
picker_frame = Frame(root, bg=p_col)
matplot_frame = Frame(root, bg="#e6ffff")
log_frame = Frame(root, bg = 'skyblue')
log = []
def change_size_callback(event):
    c_width = event.width
    c_height = event.height


img_size = 350
#bar_img = ImageTk.PhotoImage(Image.open('Resources/shared_memory_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
#hist_img = ImageTk.PhotoImage(Image.open('Resources/msgq_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
img_tbl = ImageTk.PhotoImage(Image.open('Resources/table.png').resize((img_size, img_size), Image.ANTIALIAS))
img_sm = ImageTk.PhotoImage(Image.open('Resources/shared_memory_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
img_mq = ImageTk.PhotoImage(Image.open('Resources/msgq_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
img_sem = ImageTk.PhotoImage(Image.open('Resources/semaphore_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
# img_sm.resize((img_size, img_size), Image.ANTIALIAS)
# img_mq.resize((img_size, img_size), Image.ANTIALIAS)
# img_sem.resize((img_size, img_size), Image.ANTIALIAS)
padding = [10, 100]
panel_sm = Label(matplot_frame, image = img_sm)
panel_mq = Label(matplot_frame, image = img_mq)
panel_sem = Label(matplot_frame, image = img_sem)
panel_sem.grid(row= 0, column = 2, padx=padding[0], pady = padding[1])
panel_mq.grid(row= 0, column = 0, padx=padding[0], pady = padding[1])
panel_sm.grid(row= 0, column = 1, padx=padding[0], pady = padding[1])

panel_table = Label(log_frame, image = img_tbl)
#panel_table.pack(fill = BOTH, expand = True)
panel_table.grid(row= 0, column = 0,padx=50)

iteration_argument = StringVar()
loop_argument = StringVar()
def draw_updated():
    img_tbl = ImageTk.PhotoImage(Image.open('Resources/table.png').resize((img_size, img_size), Image.ANTIALIAS))
    img_sm = ImageTk.PhotoImage(Image.open('Resources/shared_memory_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
    img_mq = ImageTk.PhotoImage(Image.open('Resources/msgq_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
    img_sem = ImageTk.PhotoImage(Image.open('Resources/semaphore_graph.png').resize((img_size, img_size), Image.ANTIALIAS))


    panel_table = Label(log_frame, image = img_tbl)
    panel_sem = Label(matplot_frame, image = img_sem)
    panel_mq = Label(matplot_frame, image = img_mq)
    panel_sm = Label(matplot_frame, image = img_sm)
    panel_mq.grid(row= 0, column = 0, padx=padding[0], pady = padding[1])
    panel_sm.grid(row= 0, column = 1, padx=padding[0], pady = padding[1])
    panel_sem.grid(row= 0, column = 2, padx=padding[0], pady = padding[1])
    panel_table.grid(row=0,column=0)
    panel_sem.image = img_sem
    panel_mq.image = img_mq
    panel_sm.image = img_sm
    panel_table.image=img_tbl

    count = 0
    matplot_frame.update()
    log_frame.update()




def init():
    print(canvas['width'])

    root.bind('<Configure>',change_size_callback)
    root.photo1 = ImageTk.PhotoImage(Image.open('Resources/shared_memory_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
    root.photo2 = ImageTk.PhotoImage(Image.open('Resources/msgq_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
    root.photo3 = ImageTk.PhotoImage(Image.open('Resources/semaphore_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
    #root.bind('<Return>',change_image_callback)
    picker_w = 0.6; picker_h = 1;
    ypos = (c_height - (c_height / 3)) * picker_h
    picker_frame.place(width = c_width * picker_w, relheight=picker_h-0.1, y = ypos )
    matplot_frame.place(relwidth = 1.0 , height= ypos, x=0)
    log_frame.place(width = c_width - c_width * picker_w, relheight=picker_h-0.1, y = ypos, x= c_width * picker_w)
    root.update()
    #Label(log_frame, text="Log", bg="lightgray", font=(font_type, font_size)).pack()
    update_graph('echo starting')

   
    #run_button = Button(picker_frame, text="Run", padx=picker_frame.winfo_width() / 2, pady=5, anchor='c').grid(row=0,column=0,rowspan=10);
    Button(picker_frame, text="Run", command = execute, anchor='c', padx=15, bg='#ccffe6').grid(row=10,column=0, columnspan=1);
    Button(picker_frame, text="Abort", command = abort, anchor='c', padx=15, bg='red').grid(row=10,column=1, columnspan=1);
    rando = "" + str(iteration_count)
    iteration_label = Label(picker_frame, text="Iterations:", bg=p_col,font=(font_type, font_size)).grid(row=11, column=0)
    loop_label = Label(picker_frame, text="Loop amount:", bg=p_col,font=(font_type, font_size)).grid(row=12, column=0)
    Entry(picker_frame, width = 10, textvariable = iteration_argument).grid(row = 11, column = 1)
    Entry(picker_frame, width = 10, textvariable = loop_argument).grid(row = 12, column = 1)
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



    

    tkinter.ttk.Separator(picker_frame, orient=VERTICAL).grid(column=0, row=3, rowspan=7, sticky='ens') 
    tkinter.ttk.Separator(picker_frame, orient=VERTICAL).grid(column=2, row=3, rowspan=7, sticky='ns') 
    tkinter.ttk.Separator(picker_frame, orient=VERTICAL).grid(column=4, row=3, rowspan=7, sticky='ns') 
    tkinter.ttk.Separator(picker_frame, orient=VERTICAL).grid(column=6, row=3, rowspan=7, sticky='ns') 
    tkinter.ttk.Separator(picker_frame, orient=VERTICAL).grid(column=8, row=3, rowspan=7, sticky='ns') 

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

driver = 'build/LNDriver/LNDriver'
#pro = subprocess.Popen('sudo ' +  driver + ' 5 0', shell=True, preexec_fn=os.setsid)
processes = []
def abort():
    print("Aborting")
    if(len(processes) != 0):
        for i in processes:
            os.killpg(os.getpgid(i.pid), signal.SIGTERM)

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



def sub_p(command):
    pro = subprocess.Popen(command, stdout=subprocess.PIPE, env=os.environ, shell=True, preexec_fn=os.setsid)  
    processes.append(pro)
    #proc_stdout = pro.communicate()[0].strip()

def update_graph(command):
    print(command)
    sub_p(command)
    create_graph()
    create_table()
    draw_updated()
    canvas.update()
    
msg = StringVar()
msg.set("")
error = Label(picker_frame, textvariable=msg, bg=p_col, fg='red')
error.grid(row=11,column=2, columnspan = 10, rowspan=2, sticky='w')
def execute():
    msg.set("")
    f = 0
    failed = False
    try:
        iteration_count = int(iteration_argument.get())
        if(iteration_count <= 0):
            f+=1
            msg.set('Please enter a valid positive \ninteger for iteration')
            failed = True
    except:
        failed = True #default
        msg.set('Please enter a valid positive \ninteger for iteration')
        f += 1
    try:
        loop_count = int(loop_argument.get())
        if(loop_count <= 0):
            msg.set('Please enter a valid positive \ninteger for loop')
            if(f == 1):
                msg.set('Please enter a valid positive \ninteger for iteration and loop')
            failed = True
        

    except:
        msg.set('Please enter a valid positive \ninteger for the loop')
        if(f == 1):
            msg.set('Please enter a valid positive \ninteger for iteration and loop')
        failed = True #default

    if(not failed):
        #Native POSIX IPCs
        if(my_map['native']['posix']['semaphore'].get()): update_graph('sudo ' +  driver + ' 5 0 ' + str(iteration_count) + ' ' + str(loop_count))
        if(my_map['native']['posix']['messagequeue'].get()): update_graph('sudo ' +  driver + ' 6 0 ' + str(iteration_count) + ' ' + str(loop_count))
        if(my_map['native']['posix']['sharedmemory'].get()): update_graph('sudo ' +  driver + ' 7 0 ' + str(iteration_count) + ' ' + str(loop_count))

        #Native SysV IPCs
        if(my_map['native']['sysv']['semaphore'].get()): update_graph('sudo ' +  driver + ' 9 0 ' + str(iteration_count) + ' ' + str(loop_count))
        if(my_map['native']['sysv']['messagequeue'].get()): update_graph('sudo ' +  driver + ' 10 0 ' + str(iteration_count) + ' ' + str(loop_count))
        if(my_map['native']['sysv']['sharedmemory'].get()): update_graph('sudo ' +  driver + ' 11 0 ' + str(iteration_count) + ' ' + str(loop_count))

        #Namespace POSIX IPCs
        if(my_map['namespace']['posix']['semaphore'].get()): update_graph('sudo ' +  driver + ' 5 1 ' + str(iteration_count) + ' ' + str(loop_count))
        if(my_map['namespace']['posix']['messagequeue'].get()): update_graph('sudo ' +  driver + ' 6 1 ' + str(iteration_count) + ' ' + str(loop_count))
        if(my_map['namespace']['posix']['sharedmemory'].get()): update_graph('sudo ' +  driver + ' 7 1 ' + str(iteration_count) + ' ' + str(loop_count))

        #Namespace SysV IPCs
        if(my_map['namespace']['sysv']['semaphore'].get()): update_graph('sudo ' +  driver + ' 9 1 ' + str(iteration_count) + ' ' + str(loop_count))
        if(my_map['namespace']['sysv']['messagequeue'].get()): update_graph('sudo ' +  driver + ' 10 1 ' + str(iteration_count) + ' ' + str(loop_count))
        if(my_map['namespace']['sysv']['sharedmemory'].get()): update_graph('sudo ' +  driver + ' 11 1 ' + str(iteration_count) + ' ' + str(loop_count))

        update_log()

def update_log():
    #label = Label(log_frame, text="Native", bg="lightgrey").pack()
    for i in log:
        print(i)

if __name__ == '__main__':
    init()