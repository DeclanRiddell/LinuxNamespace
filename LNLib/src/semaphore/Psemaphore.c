#include "Psemaphore.h"


//This process grabs the semaphore, then releases it and prints the time it took to do so
void* thread(void* arg)
{ 
    struct timeval t1, t2;
    double loopTime = 0;

    //loop for 3000ms = 3s
    while(count < SIZE_TIMES)
    {
        double elapsedTime = 0;
        //start timer
        gettimeofday(&t1, NULL);
        sem_t semaphore;
        sem_init(&semaphore, 0, 1);
        //printf("Running %d times\n", count);
        //wait grabs hold of semaphore
        sem_wait(&semaphore);
        //printf("\nGrabbed Semaphore\n");



        //release semaphore
        //printf("\nReleasing Semaphore\n");
        sem_post(&semaphore);
        

        //printf("\Destroying Semaphore\n");
        sem_destroy(&semaphore);
        //printf("Destroyed\n");
        //stop timer
        gettimeofday(&t2, NULL);
        count++;

        elapsedTime += (t2.tv_sec - t1.tv_sec) * 1000.0; //converts seconds to milliseconds
        elapsedTime += (t2.tv_usec - t1.tv_usec) / 1000.0; //converts microseconds to milliseconds

        loopTime+= elapsedTime;

        times[(count - 1)%SIZE_TIMES] = elapsedTime; //Add the elapsed time to the array
        printf("%d : %f\n", count, elapsedTime);

    }
    
    
}




