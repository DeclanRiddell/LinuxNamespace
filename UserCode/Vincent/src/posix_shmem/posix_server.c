#include "posix_server.h"

/**
 * POSIX Shared Memory Server side (writer)
 * 
 * The Server is able to write a message to shared memory that will be read by the Client 
 */

void * posix_send(void * msg){

    serverCountPosix++;

    if(sizeof(msg) > SHM_SIZE){
       LOG("The message entered is too large (Posix)\n");
       LOG("The size of message cannot be longer than 1024 characters\n");
        exit(1);
    }

    //Open shared memory segment
    shm_fd = shm_open(NAME, O_CREAT | O_RDWR, 0666);
    if(shm_fd < 0){
        perror("shm_open error in Server (Posix)");
        exit(1);
    }

    //Configure size of shared memory segment
    ftruncate(shm_fd, SHM_SIZE);

    //Memory map the shared object
    ptr = mmap(NULL, SHM_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
    if(ptr == MAP_FAILED){
        perror("mmap error in Server (Posix)");
        exit(1);
    }

    //Start
    gettimeofday(&startServerPosix, NULL);

    //Write message into memory
    memcpy(ptr, msg, SHM_SIZE);

    //End
    gettimeofday(&endServerPosix, NULL);

    writeDeltaPosix = ((endServerPosix.tv_usec - startServerPosix.tv_usec) / 1000.0); //microsecond to millisecond

    //Set min and max for first iteration
    if(serverCountPosix == 1){
        posix_set_varServer();
    }
    //Set the min and max values for iterations beyond the first
    if(writeDeltaPosix < shortestServerPosix){
        if(writeDeltaPosix < 0){
            writeDeltaPosix = 0.000010;
        }
        shortestServerPosix = writeDeltaPosix;
    }
    if(writeDeltaPosix > longestServerPosix){
        longestServerPosix = writeDeltaPosix;
    }

    //Total Time spent writing
    totalServerTimePosix += writeDeltaPosix;

    //Memory Unmap, Close Memory Segment
    munmap(ptr, SHM_SIZE);
    close(shm_fd);

    return NULL;
}

//Set first iteration min and max
int posix_set_varServer(){
    shortestServerPosix = writeDeltaPosix;
    longestServerPosix = writeDeltaPosix;
    return 0;
}