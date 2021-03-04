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
 * When this code is executed, it reads data from the shared memory
 */

#define SHM_SIZE 4096

int receive(){
    int shmid;
    key_t key;
    char *shm;

    key = 3821;

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

    //Reads the data associated from the shared memory
    //printf("The data read from memory is: %s\n", shm);

    //Cleaning
    shmdt(shm);
    shmctl(shmid, IPC_RMID, NULL);

    return 0;
}