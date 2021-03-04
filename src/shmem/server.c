#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include "server.h"

/**
 * Shared Memory SystemV Server Side
 */

#define SHM_SIZE 4096

int send(){
    int shmid;
    key_t key;
    char *shm;

    key = 3821;

    //Create or get block of memory associated with the key
    shmid = shmget(key, SHM_SIZE, IPC_CREAT | 0666);
    if(shmid < 0){
        perror("shmget error in server");
        exit(1);
    }

    //Attach to the key's address space
    shm = shmat(shmid, NULL, 0);

    if(shm == (char *) -1){
        perror("shmat error in server");
        exit(1);
    }

    memcpy(shm, "Shared Memory Benchmark", 24);
    shmdt(shm);
    
    return 0;
}
