#include "SYSVsemaphore_driver.h"



int sysvsemaphore_execute(int argc, char* argv[])
{
    lock = {0, -1, 0};      //This struct will be used as a paramter in semop for grabbing the semaphore
    unlock = {0, 1, 0};  //This struct will be used as a paramter in semop for releasing the semaphore

    if ( (semaphore = semget( (key_t) 22345, 1, 0666 | IPC_CREAT) == -1)) //creates a semaphore set with one semaphore in it
     {
         perror("semget");
         exit(1);
     }

     if ( (semop(semaphore, &unlock, 1)) == -1)     //Unlock semaphore because it is initially locked upon creation
     {
         perror("Unlock in main");
         exit(1);
     }

     //Spawn two processes that will use the semaphore
    pthread_t thread1, thread2;
    pthread_create(&thread1, NULL, thread, NULL);
    pthread_create(&thread2, NULL, thread, NULL);

    sleep(10);  //Ensure that both threads finish executing

    if ( (semctl(semaphore, 0, IPC_RMID)) == -1)    //remove semaphore
    {
        perror("semctl");
        exit(1);
    }
    
    
    printf("semaphore removed\n");


    return 0;
}