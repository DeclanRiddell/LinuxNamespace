#include <time.h>
#include <pthread.h>
#include <sys/ipc.h>
#include "SYSV_msgq_metrics.h"

void SYSV_msgq_outputDataFile(double avg, char methodName[], int iterations)
{
    FILE *metrics;

    metrics = fopen(DATA_LOC, "a");

    fclose(metrics);
}

double SYSV_msgq_averageTime(double times[], int iterations)
{
    int i = 0;
    double sum = 0.0;
    double average = 0.0;

    while(i < iterations)
    {
        sum += times[i];
        i++;
    }

    average = sum/iterations;

    return average;
}

double SYSV_msgq_minimum(double times[], int iterations)
{
    double minimum = times[0];
    int i = 1;

    while(i < iterations)
    {
        if(times[i] < minimum)
        {
            minimum = times[i];
        }
        i++;
    }

    return minimum;
}

double SYSV_msgq_maximum(double times[], int iterations)
{
    double maximum = times[0];
    int i = 1;

    while(i < iterations)
    {
        if(times[i] > maximum)
        {
            maximum = times[i];
        }
        i++;
    }

    return maximum;
}