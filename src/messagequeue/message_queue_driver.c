#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <sys/time.h>
#include <stdio.h>
#include "message_queue.h"

//Measures the time it takes for the message queue to send a message and recieve a message
void message_queue_execute(int argc, char* argv[])
{
    if(argc != 2){
        printf("This program requires a message in quotes with a max size of 1024 bytes\n");
        exit(1);
    }
    double elapsedTime = 0;
    int count = 0;
    char* message = argv[1];

    struct timeval start, end;
    
    gettimeofday(&start,NULL); //starts timer
    while(elapsedTime < 1000)
    {
        count++; 
        key_t key = msgq_send(message);
        msgq_get(key);
        gettimeofday(&end, NULL);//ends timer
        elapsedTime += ((end.tv_sec - start.tv_sec)/1000.0); //converts from seconds to milliseconds
    }

    printf("Message count: %d messages per second\n", count);
}