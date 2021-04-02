#include "semaphore_driver.h"


int POSIX_semaphore_execute()
{
    //create the semaphore
    pthread_t thread1, thread2;
    

    //spawn two processes with pthreads that will use the semaphore, both threads will run the thread function
    
    //thread1
    pthread_create(&thread1, NULL, thread, NULL);
   
    //thread2
    pthread_create(&thread2,NULL, thread, NULL);
  


    sleep(5);
    //ensures the processes have time to finish running


    //sem_destroy(&semaphore);
   
    
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

    standard_deviation = sqrt(variance);

   LOG("Posix Semaphore Stats:");
   LOG("Number of Iterations: %d", count);
   LOG("Average wait()/post() Time: %f", mean);
   LOG("Minimum wait()/post() Time: %f", min < MIN_TIME_EXE ? MIN_TIME_EXE : min);
   LOG("Maximum wait()/post() Time: %f", max);
   LOG("Variance of wait()/post() Times: %f", variance);
   LOG("Standard Deviation of wait()/post() Times: %f", standard_deviation);



    

    return 0;
}