#include "SYSVsemaphore.h"


void* sysv_thread(void* arg) //This is the function that both pthreads will execute
    {
        if ( (semop(semaphore, &lock, 1)) == -1)    //Grab semaphore if it is available or wait until it is available
        {
            perror("semop - lock");
            exit(1);
        }

       LOG("Grabbed\n");

        sleep(2);

       LOG("Releasing\n");

        if ( (semop(semaphore, &unlock, 1)) == -1)  //release semaphore
        {
            perror("semop - unlock");
            exit(1);
        }

    }