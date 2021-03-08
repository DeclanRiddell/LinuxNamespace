#include "client.h"

// Reads/Prints the message in memory that was placed by server.c
int receive(){

    key = 30821;

    //Create or get block of memory associated with the key
    shmid = shmget(key, SHM_SIZE, IPC_CREAT | 0666);
    if(shmid < 0){
        perror("SharedMemory: shmget error in client\n");
        exit(1);
    }

    //Attach the block to the process's address space and return a pointer
    shm = shmat(shmid, NULL, 0);

    if(shm == (char *) -1){
        perror("SharedMemory: shmat error in client\n");
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
    shmdt(shm);
    shmdt(shm);

    shmctl(shmid, IPC_RMID, NULL);
}