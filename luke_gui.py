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
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    types = ['POSIX Semaphore','SysV Semaphore','POSIX Shared Memory','SysV Shared Memory', 'POSIX Message queue']
    times = [random.uniform(0,1), random.uniform(0,1), random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)]
    ax.bar(types, times)
    ax.set_xlabel = "IPCS"
    ax.set_ylabel = "Time"
    plt.savefig('Resources/bar_graph.png')#, dpi = 400)


    sns.set(style = "ticks", color_codes = True)

    ipc_data = pd.read_csv("data.csv")
    fig = sns.catplot(x = "AVG_TIME", y = "IPC", data = ipc_data, kind = "strip", hue = "ENVIRONMENT", dodge=True)
    plt.savefig('test_pic.png', dpi = 100)
    #plt.show()
    plt.savefig('Resources/xd_graph.png')
    plt.cla()
    plt.clf()
    plt.close()
    sns.set(style = "ticks", color_codes = True)

    fig = sns.catplot(x = "AVG_TIME", y = "IPC", data = ipc_data, kind = "strip", hue = "LIBRARY", dodge=True)
    plt.savefig('test_pic.png', dpi = 100)
    #plt.show()
    plt.savefig('Resources/bar_graph.png')
    plt.cla()
    plt.clf()
    plt.close()

    filename = 'data.csv'
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
        fig = sns.catplot(x = "AVG_TIME", y = "ENVIRONMENT" , data = msgq_data, kind = "strip", hue = "LIBRARY", dodge = True, palette = sns.color_palette(['red', 'blue']))
        plt.title('Message Queue Graph')
    plt.savefig('Resources/msgq_graph.png', dpi = 100)
    plt.cla()
    plt.clf()

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
log_frame = Frame(root, bg = 'green')
log = []
def change_size_callback(event):
    c_width = event.width
    c_height = event.height


img_size = 350
#bar_img = ImageTk.PhotoImage(Image.open('Resources/bar_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
#hist_img = ImageTk.PhotoImage(Image.open('Resources/msgq_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
img1 = ImageTk.PhotoImage(Image.open('Resources/table.png').resize((img_size, img_size), Image.ANTIALIAS))
img2 = ImageTk.PhotoImage(Image.open('Resources/bar_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
img3 = ImageTk.PhotoImage(Image.open('Resources/msgq_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
img4 = ImageTk.PhotoImage(Image.open('Resources/xd_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
# img2.resize((img_size, img_size), Image.ANTIALIAS)
# img3.resize((img_size, img_size), Image.ANTIALIAS)
# img4.resize((img_size, img_size), Image.ANTIALIAS)
am = 10
panel_bar = Label(matplot_frame, image = img2)
panel_hist = Label(matplot_frame, image = img3)
panel_xd = Label(matplot_frame, image = img4)
panel_xd.grid(row= 0, column = 2, padx=am, pady = 50)
panel_hist.grid(row= 0, column = 0, padx=am, pady = am)
panel_bar.grid(row= 0, column = 1, padx=am, pady = am)

panel_table = Label(log_frame, image = img1)
panel_table.pack(fill = BOTH, expand = True)

iteration_argument = StringVar()
loop_argument = StringVar()
def draw_updated():
    img1 = ImageTk.PhotoImage(Image.open('Resources/table.png').resize((img_size, img_size), Image.ANTIALIAS))
    img2 = ImageTk.PhotoImage(Image.open('Resources/bar_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
    img3 = ImageTk.PhotoImage(Image.open('Resources/msgq_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
    img4 = ImageTk.PhotoImage(Image.open('Resources/xd_graph.png').resize((img_size, img_size), Image.ANTIALIAS))


    panel_xd = Label(matplot_frame, image = img4)
    panel_hist = Label(matplot_frame, image = img3)
    panel_bar = Label(matplot_frame, image = img2)
    panel_xd.grid(row= 0, column = 2, padx=am, pady = 50)
    panel_hist.grid(row= 0, column = 0, padx=am, pady = am)
    panel_bar.grid(row= 0, column = 1, padx=am, pady = am)
    panel_xd.image = img4
    panel_hist.image = img3
    panel_bar.image = img2

    panel_table = Label(log_frame, image = img1)
    panel_table.pack(fill = BOTH)
    panel_table.image=img1
    # if(panel_xd != None):
    #     panel_xd.image =img4
    # if(panel_hist != None):
    #     panel_hist.image=img2
    # if(panel_bar != None):
    #     panel_bar.image= img3
    count = 0
    log_frame.update()
    matplot_frame.update()




def init():
    print(canvas['width'])

    root.bind('<Configure>',change_size_callback)
    root.photo1 = ImageTk.PhotoImage(Image.open('Resources/bar_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
    root.photo2 = ImageTk.PhotoImage(Image.open('Resources/msgq_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
    root.photo3 = ImageTk.PhotoImage(Image.open('Resources/xd_graph.png').resize((img_size, img_size), Image.ANTIALIAS))
    #root.bind('<Return>',change_image_callback)
    picker_w = 0.6; picker_h = 1;
    ypos = (c_height - (c_height / 3)) * picker_h
    picker_frame.place(width = c_width * picker_w, relheight=picker_h-0.1, y = ypos )
    matplot_frame.place(relwidth = 1.0 , height= ypos, x=0)
    log_frame.place(relwidth = 1.0 - picker_w, height =c_height - ypos, y = ypos, x= c_width * picker_w)
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
    #sub_p('sudo python3 create_graph.py')   
    #sub_p('sudo python3 bell_curve.py')   
    draw_updated()
    canvas.update()
    
msg = StringVar()
msg.set("")
error = Label(picker_frame, textvariable=msg, bg=p_col, fg='red')
error.grid(row=11,column=2, columnspan = 10, rowspan=2, sticky='w')
def execute():
    msg.set("")
    f = 0
    try:
        iteration_count = int(iteration_argument.get())
        if(iteration_count <= 0):
            f+=1
            msg.set('Please enter a valid positive \ninteger for iteration')
            iteration_count = 100
        #msg.set('nips')
    except:
        iteration_count = 100 #default
        msg.set('Please enter a valid positive \ninteger for iteration')
        f += 1
    try:
        loop_count = int(loop_argument.get())
        if(loop_count <= 0):
            msg.set('Please enter a valid positive \ninteger for loop')
            if(f == 1):
                msg.set('Please enter a valid positive \ninteger for iteration and loop')
            loop_count = 1
        

    except:
        msg.set('Please enter a valid positive \ninteger for the loop')
        if(f == 1):
            msg.set('Please enter a valid positive \ninteger for iteration and loop')
        loop_count = 1 #default

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