#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <pthread.h>
#include "SYSV_message_queue.h"

//Recceives message from message queue
void * sysv_msgq_rcv()
{
    key_t key = ftok(".", 0);
    
    int qid = msgget(key, 0666 | IPC_CREAT);

    if(qid == -1)
    {
        perror("Message queue does not exist");
    }
    
    msgrcv(qid,&msg, sizeof(msg.text), msg.msgtype, IPC_NOWAIT);

    printf("Data received: %s\n", msg.text);
    
    msgctl(qid, IPC_RMID, NULL);
}

/*
    Adds message to message queue by taking the message as a parameter and returns the message key
*/
void * sysv_msgq_send()
{
    key_t key = ftok(".", 0);

    char* message = inc_msg;
    int msgqid = msgget(key, 0666 | IPC_CREAT);

    msg.msgtype = 1;
    strcpy(msg.text, message);
    printf("cur message: '%s'\nmsg is: '%s'\n", message, msg.text);

    int id = msgsnd(msgqid, &msg, sizeof(msg.text), IPC_NOWAIT);
    //if(id != 0)
        //printf("Error: %d, %d=%s\n", id, errno, strerror(errno));
}
