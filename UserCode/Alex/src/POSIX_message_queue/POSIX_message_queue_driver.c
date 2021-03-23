#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <stdio.h>
#include <pthread.h>
#include <limits.h>
#include <debug_utils.h>
#include "POSIX_message_queue_driver.h"


//Creates threads for the message send and message receive operations and then
int POSIX_message_queue_execute(int argc, char* argv[])
{
    printf("Starting POSIX msg queue\n");
    if(argc != 2){
        printf("This program requires a message in quotes with a max size of 1024 bytes\n");
        exit(1);
    }

    int index = 0;
    clock_t start, end;
    double execution_time;
    double snd_times[ITERATION_COUNT];
    double rcv_times[ITERATION_COUNT];
    double min, max, avg;
    min = max = avg = MIN_POSSIBLE_EXE_TIME;
    
    while(index < ITERATION_COUNT)
    {
        printf("Loop iterating\n");
        pthread_t thread1, thread2;
        start = clock();
        pthread_create(&thread1, NULL, posix_message_queue_send, NULL);
        pthread_join(thread1,NULL);
        end = clock();
        execution_time = ((double)(end - start))/CLOCKS_PER_SEC;
        printf("Posix Message Send executed in %f seconds\n", execution_time);
        snd_times[index] = ((double)(end - start))/CLOCKS_PER_SEC;
        
        //create pthread for receive operation
        start = clock();
        pthread_create(&thread2, NULL, posix_message_queue_receive, NULL);
        pthread_join(thread2,NULL);
        end = clock();
        execution_time = ((double)(end - start))/CLOCKS_PER_SEC;
        printf("Posix Message Receive executed in %f seconds\n", execution_time);
        rcv_times[index] = execution_time;



        min = execution_time < min ? execution_time : min;
        max = execution_time > max ? execution_time : max;
        avg += execution_time;

        printf("Iterated %d times\n", index);
        index++; 
    } 


    avg /= ITERATION_COUNT;
    double variance, standard_deviation;
    variance = standard_deviation = 0;
    for(int i = 0; i < ITERATION_COUNT; i++) variance += (rcv_times[i] - avg) * (rcv_times[i] - avg);
    variance /= ITERATION_COUNT;
    standard_deviation = sqrt(variance);

    POSIX_msgq_outputDataFile(snd_times, "POSIX Message Queue Send", ITERATION_COUNT);
    POSIX_msgq_outputDataFile(rcv_times, "POSIX Message Queue Receive", ITERATION_COUNT);
    
    printf("SysV Metrics\nMinimum:\t\t%f\nMaximum:\t\t%f\nAverage:\t\t%f\nVariance:\t\t%f\nStandard Deviation:\t%f\n", min, max, avg, variance, standard_deviation);
    return 0;
}