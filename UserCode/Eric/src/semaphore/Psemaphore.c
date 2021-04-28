#include "Psemaphore.h"

//This process grabs the semaphore, then releases it and prints the time it took to do so
void* thread(void* arg)
{ 
    struct timeval t1, t2;
    double loopTime = 0;

    //loop for 3000ms = 3s
    while(count < p_iteration_count)
    {
        double elapsedTime = 0;
        //start timer
        gettimeofday(&t1, NULL);
        sem_t semaphore;
        sem_init(&semaphore, 0, 1);
        //wait grabs hold of semaphore
        sem_wait(&semaphore);



        //release semaphore
        sem_post(&semaphore);
        
        sem_destroy(&semaphore);
        //stop timer
        gettimeofday(&t2, NULL);
        count++;

        elapsedTime += (t2.tv_sec - t1.tv_sec) * 1000.0; //converts seconds to milliseconds
        elapsedTime += (t2.tv_usec - t1.tv_usec) / 1000.0; //converts microseconds to milliseconds
        if(elapsedTime <= MIN_TIME_EXE) elapsedTime = MIN_TIME_EXE;
        loopTime+= elapsedTime;

        //times[(count - 1)%iteration_count] = elapsedTime; //Add the elapsed time to the array
        avg_time += elapsedTime;

    }
    
    
}




