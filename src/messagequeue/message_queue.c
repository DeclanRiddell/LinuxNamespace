#include "message_queue.h"


/*Takes a messge key as a parameter, and determines if a message queue exists. If it does not exist, 
the method returns -1. Otherwise, the message queue id is returned.
*/
int msgq_get(key_t key)
{
    int qid = msgget(key, 0666 | IPC_CREAT);

    if(qid == -1)
    {
        printf("Message queue does not exist");
        return -1;
    }
    
    return qid;
}


/*
    Adds message to message queue by taking the message as a parameter and returns the message key
*/
key_t msgq_send(char *message)
{
    printf("a\n");
    struct msgbuf msg;
    printf("a\n");

    key_t key = ftok(".", 0);
    printf("a\n");

    int msgqid = msgget(key, 0666 | IPC_CREAT);
    printf("a\n");

    msg.msgtype = 1;
    printf("a\n");
    msg.text = message;

    printf("a\n");
    msgsnd(msgqid, &msg, sizeof(message), 0);
    printf("a\n");
    
    return key;
}