#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <stdio.h>
#include <pthread.h>
#include <debug_utils.h>
#include "SYSV_message_queue_driver.h"


//Creates threads for the message send and message receive operations and then
int SYS_V_message_queue_execute()
{
    inc_msg = __msg;

    int index = 0;
    clock_t start, end;
    double execution_time;
    double snd_times[ITERATION_COUNT];
    double rcv_times[ITERATION_COUNT];
    double min, max, avg;
    min = max = avg = MIN_POSSIBLE_EXE_TIME;
    while(index < ITERATION_COUNT)
    {
        pthread_t thread1, thread2;
        start = clock();
        pthread_create(&thread1, NULL, sysv_msgq_send, NULL);
        pthread_join(thread1,NULL);
        end = clock();
        execution_time = ((double)(end - start))/CLOCKS_PER_SEC;
        snd_times[index] = ((double)(end - start))/CLOCKS_PER_SEC;
        
        //create pthread for receive operation
        start = clock();
        pthread_create(&thread2, NULL, sysv_msgq_rcv, NULL);
        pthread_join(thread2,NULL);
        end = clock();
        execution_time = ((double)(end - start))/CLOCKS_PER_SEC;
        execution_time = MIN_POSSIBLE_EXE_TIME > execution_time ? MIN_POSSIBLE_EXE_TIME : execution_time;
        rcv_times[index] = execution_time;
        min = execution_time < min ? execution_time : min;
        max = execution_time > max ? execution_time : max;
        avg += execution_time;

        index++;
    }       
    avg /= ITERATION_COUNT;
    double variance, standard_deviation;
    variance = standard_deviation = 0;
    for(int i = 0; i < ITERATION_COUNT; i++) variance += (rcv_times[i] - avg) * (rcv_times[i] - avg);
    variance /= ITERATION_COUNT;
    standard_deviation = sqrt(variance);

    SYSV_msgq_outputDataFile(snd_times, "System V Message Queue Send", ITERATION_COUNT);
    SYSV_msgq_outputDataFile(rcv_times, "System V Message Queue Receive", ITERATION_COUNT);

   LOG("SysV Metrics\nMinimum:\t\t%f\nMaximum:\t\t%f\nAverage:\t\t%f\nVariance:\t\t%f\nStandard Deviation:\t%f\n", min, max, avg, variance, standard_deviation);
    return 0;
}