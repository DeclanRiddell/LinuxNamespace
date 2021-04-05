#include "SYSVsemaphore_driver.h"



int SYS_V_semaphore_execute()
{
    //This struct will be used as a paramter in semop for grabbing the semaphore
    lock.sem_num = 0;
    lock.sem_op = -1;
    lock.sem_flg = 0;

    //This struct will be used as a paramter in semop for releasing the semaphore

    unlock.sem_num = 0;
    unlock.sem_op =  1;
    unlock.sem_flg = 0;
    
    int id;
    if ((semaphore = semget( (key_t) 22345, 1, 0666 | IPC_CREAT)) == -1) //creates a semaphore set with one semaphore in it
     {
         perror("Error: semget");
         exit(1);
     }

     if ( (id = semop(semaphore, &unlock, 1)) == -1)     //Unlock semaphore because it is initially locked upon creation
     {
         perror("Error: Unlock in main");
        LOG("Error code %d for semid %d\t %d=%s\n", id, unlock.sem_num, errno, strerror(errno));
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
    
    
   LOG("semaphore removed\n");

   sleep(2); //ensure threads have time to finish execution

   max = times[0];
   min = times[0];
   sum = 0;
   variance = 0;

   //Loop to find the max, min, and sum of the times
   for(int i = 0; i < count; i++)
   {
       if(times[i] < min)
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

   //Loop to calculate variance
   for (int i = 0; i < count; i++)
   {
       variance += (times[i] - mean) * (times[i] - mean);
   }

   variance = variance / count;

   standard_deviation = sqrt(variance);

   LOG("SYSV Semaphore Stats:\n");
   LOG("Number of Iterations: %d\n", count);
   LOG("Average time for System Class: %f\n", mean);
   LOG("Minumum system calls time: %f\n", min);
   LOG("Maximum system calls time: %f\n", max);
   LOG("Varaince in system call times: %f\n", variance);
   LOG("Standard Deviation of system call times: %f\n", standard_deviation);


    return 0;
}