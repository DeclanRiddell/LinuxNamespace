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
        #ifdef DEBUG
        printf("Running %d times\n", count);
        #endif
        //wait grabs hold of semaphore
        sem_wait(&semaphore);
        #ifdef DEBUG
        printf("\nGrabbed Semaphore\n");
        #endif



        //release semaphore
        #ifdef DEBUG
        printf("\nReleasing Semaphore\n");
        #endif
        sem_post(&semaphore);
        
        #ifdef DEBUG
        printf("\Destroying Semaphore\n");
        #endif
        sem_destroy(&semaphore);
        #ifdef DEBUG
        printf("Destroyed\n");
        #endif
        //stop timer
        gettimeofday(&t2, NULL);
        count++;

        elapsedTime += (t2.tv_sec - t1.tv_sec) * 1000.0; //converts seconds to milliseconds
        elapsedTime += (t2.tv_usec - t1.tv_usec) / 1000.0; //converts microseconds to milliseconds
        if(elapsedTime <= MIN_TIME_EXE) elapsedTime = MIN_TIME_EXE;
        loopTime+= elapsedTime;

        times[(count - 1)%SIZE_TIMES] = elapsedTime; //Add the elapsed time to the array
        #ifdef DEBUG
        printf("%d : %f\n", count, elapsedTime);
        #endif

    }
    
    
}




