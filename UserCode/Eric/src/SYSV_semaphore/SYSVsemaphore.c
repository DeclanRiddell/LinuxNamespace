#include "SYSVsemaphore.h"


void* sysv_thread(void* arg) //This is the function that both pthreads will execute
    {
        struct timeval t1, t2;
        double loopTime = 0;

        //Loop for SIZE_TIMES
        while (count < SIZE_TIMES)
        {
            double elapsedTime = 0;
            //start timer
            gettimeofday(&t1, NULL);

            if ( (semop(semaphore, &lock, 1)) == -1)    //Grab semaphore if it is available or wait until it is available
            {
                perror("semop - lock");
                exit(1);
            }

            LOG("Grabbed Semaphore\n");


            LOG("Releasing Semaphore\n");

            if ( (semop(semaphore, &unlock, 1)) == -1)  //release semaphore
            {
                perror("semop - unlock");
                exit(1);
            }

            //stop timer
            gettimeofday(&t2, NULL);
            count++;

            elapsedTime += (t2.tv_sec - t1.tv_sec) * 1000.0;
            elapsedTime += (t2.tv_usec - t1.tv_usec) / 1000.0;
            if(elapsedTime <= MIN_TIME_EXE) elapsedTime = MIN_TIME_EXE;
            
            times[(count -1) %SIZE_TIMES] = elapsedTime;
        }



        

    }