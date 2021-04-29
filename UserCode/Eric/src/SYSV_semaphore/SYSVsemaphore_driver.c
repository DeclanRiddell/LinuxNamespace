#include "SYSVsemaphore_driver.h"



int SYS_V_semaphore_execute(int iteration_count, int native)
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

   SYSVmax = SYSVtimes[0];
   SYSVmin = SYSVtimes[0];
   SYSVsum = 0;
   SYSVvariance = 0;

   //Loop to find the max, min, and sum of the times
   for(int i = 0; i < SYSVcount; i++)
   {
       if(SYSVtimes[i] < SYSVmin)
       {
           SYSVmin = SYSVtimes[i];
       }
       if(SYSVtimes[i] > SYSVmax)
       {
           SYSVmax = SYSVtimes[i];
       }

       SYSVsum += SYSVtimes[i];
   }

   SYSVmean = SYSVsum/SYSVcount;

   //Loop to calculate variance
   for (int i = 0; i < SYSVcount; i++)
   {
       SYSVvariance += (SYSVtimes[i] - SYSVmean) * (SYSVtimes[i] - SYSVmean);
   }

   SYSVvariance = SYSVvariance / SYSVcount;

   SYSVstandard_deviation = sqrt(SYSVvariance);


    LOG("\n");
    LOG("SYSV Semaphore findings\n");
    LOG("-----------------------------\n");
    LOG("Number of Iterations: %d\n", iteration_count);
    LOG("Average time for System Calls: %f\n", SYSVmean);
    LOG("Minumum system calls time: %f\n", SYSVmin < MIN_TIME_EXE ? MIN_TIME_EXE : SYSVmin);
    LOG("Maximum system calls time: %f\n", SYSVmax);
    LOG("Varaince in system call times: %f\n", SYSVvariance);
    LOG("Standard Deviation of system call times: %f\n", SYSVstandard_deviation);
    if(native == 0)write_to_file_("semaphore", "sysv", "native", SYSVmean, iteration_count);
    else write_to_file_("semaphore", "sysv", "namespace", SYSVmean, iteration_count);


   
   


    return 0;
}