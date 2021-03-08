int main()
{
    //create the semaphore
    sem_init(&semaphore, 0, 1);
    pthread_t thread1, thread2;
    

    //spawn two processes with pthreads that will us the semaphore
    
    pthread_create(&thread1, NULL, thread1_function, NULL);
    //this thread will run the thread1_function
    
    sleep(1);
    //makes sure thread one grabs semaphore first
    pthread_create(&thread2,NULL, thread2_function, NULL);
    //this thread will run the thread2_function


    sleep(2);
    //ensures the processes have time to finish running

    sem_destroy(&semaphore);
   
    

    return 0;
}