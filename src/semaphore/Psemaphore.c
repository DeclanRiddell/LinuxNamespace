#include "Psemaphore.h"


//This process grabs the semaphore, then releases it and prints the time it took to do so
void* thread1_function(void* arg)
{
    struct timeval t1, t2;
    double elapsedTime;

    //start timer
    gettimeofday(&t1, NULL);

    //wait grabs hold of semaphore
    sem_wait(&semaphore);
   

   //release semaphore
    sem_post(&semaphore);

    //stop timer
    gettimeofday(&t2, NULL);

    //compute and print elapsed time in milliseconds

    //converting elapsed seconds to milliseconds
    elapsedTime = (t2.tv_sec - t1.tv_sec) * 1000.0;

    //converting microseconds to milliseconds
    elapsedTime += (t2.tv_usec - t1.tv_usec)/1000.0;
    printf("%f ms.\n", elapsedTime);
}

//This process just grabs and releases the semaphore
void* thread2_function(void* arg)
{
    //grabs hold of semaphore
    sem_wait(&semaphore);
    
  
    //releases semaphore
    sem_post(&semaphore);
}


