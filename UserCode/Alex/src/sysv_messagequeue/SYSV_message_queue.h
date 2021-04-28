#ifndef MSG_Q_H
#define MSG_Q_H
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <string.h>
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include "SYSV_message_queue_driver.h"
#include <debug_utils.h>

//Message buffer for message being sent and received
struct sysv_msgbuf{
        long msgtype;
        char text[1024];
    }msg;

//Receives and removes message from message queue
void * sysv_msgq_rcv();

//Adds message to message queue
void * sysv_msgq_send();


#endif