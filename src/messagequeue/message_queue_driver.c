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
    printf("argument: '%s'\n", argv[1]);
    printf("Sup\n");
    char* message = argv[1];

    struct timeval start, end;
    
    gettimeofday(&start,NULL); //starts timer
    printf("Beginning\n");
    while(elapsedTime < 1000)
    {
        printf("start loop\n");
        count++; 

        key_t key = msgq_send(message);
        printf("End send\n");
        msgq_get(key);
        printf("End get\n");

        elapsedTime += ((end.tv_sec - start.tv_sec)/1000.0); //converts from seconds to milliseconds
        printf("%f\n", elapsedTime);
        gettimeofday(&end, NULL);//ends timer
    }

    printf("Message count: %d messages per second\n", count);
}