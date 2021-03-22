#include "semaphore_driver.h"


int psemaphore_execute(int argc, char* argv[])
{
    //create the semaphore
    sem_init(&semaphore, 0, 1);
    pthread_t thread1, thread2;
    

    //spawn two processes with pthreads that will use the semaphore, both threads will run the thread function
    
    //thread1
    pthread_create(&thread1, NULL, thread, NULL);
   
    //thread2
    pthread_create(&thread2,NULL, thread, NULL);
  


    sleep(5);
    //ensures the processes have time to finish running


    sem_destroy(&semaphore);
   
    
    max = times[0];
    min = times[0];
    sum = 0;
    variance = 0;

    //This loops finds the max, min, and sum of the times
    for (int i = 0; i < count; i++)
    {
        if (times[i] < min) 
        {
            min = times[i];
        }

        if(times[i] > max)
        {
            max = times[i];
        }

        sum += times[i];
    }

    mean = sum/count;

    
    //calculate variance
    for (int i = 0; i < count; i++)
    {
        variance += (times[i] - mean) * (times[i] - mean);
    }
    variance = variance / count;

    standard_deviation = sqrtf(variance);

    printf("Posix Semaphore Stats:\n");
    printf("Number of Iterations: %d\n", count);
    printf("Average wait()/post() Time: %f\n", mean);
    printf("Minimum wait()/post() Time: %f\n", min);
    printf("Maximum wait()/post() Time: %f\n", max);
    printf("Variance of wait()/post() Times: %f\n", variance);
    printf("Standard Deviation of wait()/post() Times: %f\n", standard_deviation);



    

    return 0;
}