#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include "client.h"

/**
 * Shared Memory SystemV Client side
 * 
 * The Client is able to read the data from Shared Memory
 * that was used as an argument in server.c
 */


#define SHM_SIZE 1024

int shmid;
key_t key;
char *shm;

// Reads/Prints the message in memory that was placed by server.c
int receive(){

    key = 30821;

    //Create or get block of memory associated with the key
    shmid = shmget(key, SHM_SIZE, IPC_CREAT | 0666);
    if(shmid < 0){
        perror("shmget error in client\n");
        exit(1);
    }

    //Attach the block to the process's address space and return a pointer
    shm = shmat(shmid, NULL, 0);

    if(shm == (char *) -1){
        perror("shmat error in client\n");
        exit(1);
    }

    return 0;
}

//Reads the data associated from the shared memory
void print_msg(){
    
    printf("The data read from memory is: %s\n", shm);
}

// Removes IPC
void clean_ipc(){

    //Cleaning
    shmdt(shm);
    shmctl(shmid, IPC_RMID, NULL);
}