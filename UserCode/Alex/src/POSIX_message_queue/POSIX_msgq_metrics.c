#include <time.h>
#include <pthread.h>
#include <sys/ipc.h>
#include "POSIX_msgq_metrics.h"

void POSIX_msgq_outputDataFile(double times[], char methodName[], int iterations)
{
    FILE *metrics;

    metrics = fopen("./POSIX_msgq_metrics.txt", "a");

    fprintf(metrics, "Operation %s:\n", methodName);
    fprintf(metrics,"\t%d Iterations: \n", iterations);
    fprintf(metrics,"\tAverage Access Time: %f\n", POSIX_msgq_averageTime(times,iterations));
    fprintf(metrics,"\tMinimum Access Time: %f\n", POSIX_msgq_minimum(times,iterations));
    fprintf(metrics,"\tMaximum Access Time: %f\n\n", POSIX_msgq_maximum(times,iterations));

    fclose(metrics);
}

double POSIX_msgq_averageTime(double times[], int iterations)
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

double POSIX_msgq_minimum(double times[], int iterations)
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

double POSIX_msgq_maximum(double times[], int iterations)
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