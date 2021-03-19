#include "server.h"

 
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
    shmdt(shm);
    shmdt(shm);

    return 0;
}
