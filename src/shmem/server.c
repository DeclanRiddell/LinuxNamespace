#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include "server.h"

/**
 * Shared Memory SystemV Server Side
 * 
 * When running the program, it takes a parameter (a message) and copies it
 * into memory so that Client can read it. Running this program will give no
 * output unless there is an error. In order to read the message, run client.c
 */

#define SHM_SIZE 1024

 
 // The message that was entered as a parameter is copied into memory
int send(char* message){
    int shmid;
    key_t key;
    char *shm;

    key = 30821;

    if(sizeof(message) > SHM_SIZE){
        printf("The message entered is too large\n");
        printf("The size of message cannot be longer than 1024 characters\n");
        exit(1);
    }

    //Create or get block of memory associated with the key
    shmid = shmget(key, SHM_SIZE, IPC_CREAT | 0666);
    if(shmid < 0){
        perror("shmget error in server\n");
        exit(1);
    }

    //Attach to the key's address space
    shm = shmat(shmid, NULL, 0);

    if(shm == (char *) -1){
        perror("shmat error in server\n");
        exit(1);
    }

    //Message to be shared
    memcpy(shm, message, SHM_SIZE);
    
    //Detach
    shmdt(shm);

    return 0;
}
