#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <sys/time.h>
#include <stdio.h>
#include "message_queue.h"

//Measures the time it takes for the message queue to send a message and recieve a message
void message_queue_execute(int argc, char argv[])
{
    float elapsedTime = 0;
    int count = 0;
    char *message = &argv[0];

    struct timeval start, end;
    
    gettimeofday(&start,NULL); //starts timer
    
    while(elapsedTime < 1000)
    {
        count++; 

        key_t key = msgq_send(message);
        msgq_get(key);

        elapsedTime += ((end.tv_sec - start.tv_sec)/1000); //converts from seconds to milliseconds

        gettimeofday(&end, NULL);//ends timer
    }

    printf("Message count: %d messages per second\n", count);
}