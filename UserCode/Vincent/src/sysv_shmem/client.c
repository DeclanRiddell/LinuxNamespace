#include "client.h"

/**
 * Client System V
 * 
 * Reads what was written on the memory
 */

// Reads and Prints the message in memory that was placed by server.c
void * receive(){

    clientCount++;

    key = ftok(".", 0);
    if(key < 0){
        perror("Error in ftok in Client");
        exit(1);
    }

    //Start timer for when reading
    gettimeofday(&startClient, NULL);

    //Create or get block of memory associated with the key
    shmid = shmget(key, SHM_SIZE, IPC_CREAT | 0666);
    if(shmid < 0){
        perror("Shared Memory Get (shmget) error in client\n");
        exit(1);
    }

    //Attach the block to the process's address space and return a pointer
    shm = shmat(shmid, NULL, 0);
    if(shm == (char *) -1){
        perror("Shared Memory Attach (shmat) error in client\n");
        exit(1);
    }

    //Goal: Calculate the delta when accessing the memory
    //Once the message is attached, we stop the timer
    gettimeofday(&endClient, NULL);

    //Calculate the time for reading the memory in milliseconds
    readDelta = ((endClient.tv_usec - startClient.tv_usec) / 1000.0); //microsecond to millisecond  

    //Set min and max values for first iteration
    if(clientCount == 1){
        set_varClient();
    }
    //Set min and max for iterations beyond 1
    if(readDelta < shortestClient){
        if(readDelta < 0){
            readDelta = 0.000010;
        }
        shortestClient = readDelta;
    }
    if(readDelta > longestClient){
        longestClient = readDelta;
    }

    //Total time spent reading
    totalClientTime += readDelta;

    //Print the message
    if(clientCount == 1){
        print_msg();
    }

    return NULL;
}

//Reads the data associated from the shared memory
void print_msg(){
   LOG("The data read from memory is: %s\n", shm);
}

// Removes IPC
void clean_ipc(){

    //Detach and destroy the shared memory
    shmdt(shm);
    shmctl(shmid, IPC_RMID, NULL);
}

//Set first iteration min and max
int set_varClient(){
    shortestClient = readDelta;
    longestClient = readDelta;
    return 0;
}