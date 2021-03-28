#include "posix_client.h"

/**
 *  POSIX Shared Memory Client side (reader)
 * 
 *  The Client is able to read the message that was sent from the Server 
 */

void * posix_receive(){

    clientCountPosix++;

    gettimeofday(&startClientPosix, NULL);

    //Open shared memory segment
    shm_fd = shm_open(NAME, O_RDONLY, 0666);
    if(shm_fd < 0){
        perror("Error with shm_open in Posix Client\n");
        exit(1);
    }

    //Memory Map the shared object
    ptr = mmap(NULL, SHM_SIZE, PROT_READ, MAP_SHARED, shm_fd, 0);
    if(ptr == MAP_FAILED){
        perror("Error with mmap in Posix Client\n");
        exit(1);
    }
    
    gettimeofday(&endClientPosix, NULL);

    //Print the message
    if(clientCountPosix == 1){
        posix_print_msg();
    }

    //Memory Unmap, Close Memory Segment, Delete Shared Memory Segment
    munmap(ptr, SHM_SIZE);
    close(shm_fd);
    shm_unlink(NAME);

    //Calculate the time for reading the memory in milliseconds
    readDeltaPosix = ((endClientPosix.tv_usec - startClientPosix.tv_usec) / 1000.0); //microsecond to millisecond  

    //Set min and max values for first iteration
    if(clientCountPosix == 1){
        posix_set_varClient();
    }
    //Set min and max for iterations beyond 1
    if(readDeltaPosix < shortestClientPosix){
        shortestClientPosix = readDeltaPosix;
    }
    if(readDeltaPosix > longestClientPosix){
        longestClientPosix = readDeltaPosix;
    }

    //Total time spent reading
    totalClientTimePosix += readDeltaPosix;
    return NULL;
}

//Prints message
void posix_print_msg(){
    printf("The data read from memory is: %s\n", (char*)ptr);
}

//Set first iteration min and max
int posix_set_varClient(){
    shortestClientPosix = readDeltaPosix;
    longestClientPosix = readDeltaPosix;
    return 0;
}