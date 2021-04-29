#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <stdio.h>
#include <pthread.h>
#include <limits.h>
#include <debug_utils.h>
#include "POSIX_message_queue_driver.h"


//Creates threads for the message send and message receive operations and then
int POSIX_message_queue_execute(int iteration_count, int native)
{
   LOG("Starting POSIX msg queue\n");

    int index = 0;
    clock_t start, end;
    double execution_time;
    double snd_times[iteration_count];
    double rcv_times[iteration_count];
    double min, max, avg;
    min = max = avg = MIN_POSSIBLE_EXE_TIME;
    
    while(index < iteration_count)
    {
        pthread_t thread1, thread2;

        inc_msg = __msg;

        start = clock();
        pthread_create(&thread1, NULL, posix_message_queue_send, NULL);
        pthread_join(thread1,NULL);
        end = clock();
        execution_time = ((double)(end - start))/CLOCKS_PER_SEC;
        snd_times[index] = ((double)(end - start))/CLOCKS_PER_SEC;
        
        //create pthread for receive operation
        start = clock();
        pthread_create(&thread2, NULL, posix_message_queue_receive, NULL);
        pthread_join(thread2,NULL);
        end = clock();
        execution_time = ((double)(end - start))/CLOCKS_PER_SEC;
        rcv_times[index] = execution_time;



        min = execution_time < min ? execution_time : min;
        max = execution_time > max ? execution_time : max;
        avg += execution_time;

        index++; 
    } 


    avg /= iteration_count;
    double variance, standard_deviation;
    variance = standard_deviation = 0;
    for(int i = 0; i < iteration_count; i++) variance += (rcv_times[i] - avg) * (rcv_times[i] - avg);
    variance /= iteration_count;
    //standard_deviation = sqrt(variance);
    LOG("Writing\n");
    //if(native == 0)write_to_file_pathed_("data.csv", "message_queue", "sysv", "native", avg, iteration_count);
    //else write_to_file_pathed_("data.csv", "message_queue", "sysv", "namespace", avg, iteration_count);
    if(native == 0)write_to_file_("message_queue", "posix", "native", avg, iteration_count);
    else write_to_file_("message_queue", "posix", "namespace", avg, iteration_count);
    LOG("SysV Metrics\nMinimum:\t\t%f\nMaximum:\t\t%f\nAverage:\t\t%f\nVariance:\t\t%f\nStandard Deviation:\t%f\n", min, max, avg, variance, standard_deviation);
    return 0;
}
