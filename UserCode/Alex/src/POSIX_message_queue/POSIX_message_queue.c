#include "POSIX_message_queue.h"
#include <pthread.h>
#include <debug_utils.h>

void * posix_message_queue_send()
{   
    char text[1024];
    char* message = inc_msg;
    strcpy(text, message);
    printf("cur message: '%s'\nmsg is: '%s'\n", message, text);
    mqdes = mq_open(QUEUE_NAME, O_RDWR|O_CREAT, S_IRUSR | S_IWUSR, NULL);

    if(mqdes == -1)
    {
        perror("mq_open");
    }
    
    int send = mq_send(mqdes,text,1025,0);
    if(send == -1)
    {
        perror("mq_send");
        exit(1);
    }
    mq_close(mqdes);
    
}

void * posix_message_queue_receive() 
{
    int prio;

    char message[1024];
    mqdes = mq_open(QUEUE_NAME, O_RDWR, S_IRUSR | S_IWUSR, NULL);

    if(mqdes == -1)
    {
        perror("mq_open");
    }
    
    mq_receive(mqdes, message, 1025, &prio);

    printf("Message received: %s\n", message);

    mq_close(mqdes);
    mq_unlink(QUEUE_NAME);
        
}
