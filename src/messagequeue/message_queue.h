
#ifndef MSG_Q_H
#define MSG_Q_H
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Message buffer for message being sent and received
struct msgbuf{
        long msgtype;
        char *text;
    };

//Takes message key as parameter and gets the message queue associated with that message
int msgq_get(key_t);

//Adds message to message queue
key_t msgq_send(char[]);


#endif