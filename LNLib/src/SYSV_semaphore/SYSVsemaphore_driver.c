#include "SYSVsemaphore_driver.h"



int sysvsemaphore_execute(int argc, char* argv[])
{
    //This struct will be used as a paramter in semop for grabbing the semaphore
    lock.sem_num = 13;
    lock.sem_op = -1;
    lock.sem_flg = 0;

    //This struct will be used as a paramter in semop for releasing the semaphore

    unlock.sem_num = 13;
    unlock.sem_op =  1;
    unlock.sem_flg = 0;
    
    int id;
    if ( (semaphore = semget( (key_t) 22345, 1, 0666 | IPC_CREAT) == -1)) //creates a semaphore set with one semaphore in it
     {
         perror("Error: semget");
         exit(1);
     }

     if ( (id = semop(semaphore, &unlock, 1)) == -1)     //Unlock semaphore because it is initially locked upon creation
     {
         perror("Error: Unlock in main");
         printf("Error code %d for semid %d\t %d=%s\n", id, unlock.sem_num, errno, strerror(errno));
         exit(1);
     }

     //Spawn two processes that will use the semaphore
    pthread_t thread1, thread2;
    pthread_create(&thread1, NULL, sysv_thread, NULL);
    pthread_create(&thread2, NULL, sysv_thread, NULL);

    sleep(10);  //Ensure that both threads finish executing

    if ( (semctl(semaphore, 0, IPC_RMID)) == -1)    //remove semaphore
    {
        perror("semctl");
        exit(1);
    }
    
    
    printf("semaphore removed\n");


    return 0;
}