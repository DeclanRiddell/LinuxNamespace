#include "server.h"

/**
 * System V server side
 * 
 * Allows user to write message that is to be read by the client
 */

 // The message that was entered as a parameter is copied into memory
void * send(void * message){

    serverCount++;

    //Generate random key with ftok
    key = ftok(".", 0);
    if(key < 0){
        perror("Error in ftok in Server");
        exit(1);
    }

    if(sizeof(message) > SHM_SIZE){
        printf("The message entered is too large\n");
        printf("The size of message cannot be longer than 1024 characters\n");
        exit(1);
    }

    //Create or get block of memory associated with the key
    shmid = shmget(key, SHM_SIZE, IPC_CREAT | 0666);
    if(shmid < 0){
        perror("Shared Memory Get (shmget) error in server\n");
        exit(1);
    }

    //Start timer right after message is entered to see how long it takes to write to memory
    gettimeofday(&startServer, NULL); 

    //Attach Shared Memory segment to the key's address space
    shm = shmat(shmid, NULL, 0);

    if(shm == (char *) -1){
        perror("Shared Memory Attach (shmat) error in server\n");
        exit(1);
    }

    //Message to be shared
    memcpy(shm, message, SHM_SIZE);

    //end timer for when the message reaches to memory
    gettimeofday(&endServer, NULL); 
    
    //Calculate write time in milliseconds
    writeDelta = ((endServer.tv_usec - startServer.tv_usec) / 1000.0); //microsecond to millisecond

    //Set min and max for first iteration
    if(serverCount == 1){
        set_varServer();
    }
    //Set the min and max values for iterations beyond the first
    if(writeDelta < shortestServer){
        shortestServer = writeDelta;
    }
    if(writeDelta > longestServer){
        longestServer = writeDelta;
    }

    //Total Time spent writing
    totalServerTime += writeDelta;

    //Detach from shared memory
    shmdt(shm);

    return NULL;
}

//Set first iteration min and max
int set_varServer(){
    shortestServer = writeDelta;
    longestServer = writeDelta;
    return 0;
}