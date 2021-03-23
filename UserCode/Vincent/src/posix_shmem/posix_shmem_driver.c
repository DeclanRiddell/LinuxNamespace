#include "posix_shmem_driver.h"

/**
 * This program is used to demonstrate Shared Memory using POSIX API
 */

int POSIX_shared_memory_execute(int argc, char* argv[]){

    if(argc < 2){
        printf("This program requires a message in quotes with a max size of 1024 bytes\n");
        exit(1);
    }

    gettimeofday(&startPosix, NULL);
    //1 second = 1000 milliseconds
    while(elapsedTimePosix < 1000.0){
        
        //Create pthread and send the message
        pthread_create(&thread1Posix, NULL, posix_send, argv[1]);
        pthread_join(thread1Posix, NULL);

        //Create pthread and read the message
        pthread_create(&thread2Posix, NULL, posix_receive, NULL);
        pthread_join(thread2Posix, NULL);

        gettimeofday(&endPosix, NULL); //end timer
        
        elapsedTimePosix += ((endPosix.tv_usec - startPosix.tv_usec) / 1000.0); //converts from microseconds to milliseconds
    }

    //Averages time spent for Server and Client
    averageClientPosix = totalClientTimePosix/clientCountPosix;
    averageServerPosix = totalServerTimePosix/serverCountPosix;
    
    //Print results and append results to file
    posix_results();
    posix_append_results(argv[1]);

    return 0;
}

//prints results
void posix_results(){        
    printf("\n");
    printf("Shared Memory POSIX findings\n");
    printf("-----------------------------------\n");
    printf("Operation: Shared Memory Read\n");
    printf("Number of iterations in 1 second: %d\n", clientCountPosix);
    printf("Average Access Time : %f ms\n", averageClientPosix);
    printf("Minimum Access Time : %f ms\n", shortestClientPosix);
    printf("Longest Access Time : %f ms\n", longestClientPosix);
    printf("\n");

    printf("Operation: Shared Memory Write\n");
    printf("Number of iterations in 1 second: %d\n", serverCountPosix);
    printf("Average Access Time : %f ms\n", averageServerPosix);
    printf("Minimum Access Time : %f ms\n", shortestServerPosix);
    printf("Longest Access Time : %f ms\n", longestServerPosix);
    printf("\n");
}

/**
 * Write results to file
 * The file is located in the "build" folder
 */
int posix_append_results(){
    
    FILE *store_results;
    store_results = fopen("SHM_POSIX_Output.txt", "a");
    fprintf(store_results, "\n");
    fprintf(store_results,"Shared Memory POSIX findings\n");
    fprintf(store_results, "The size of the shared memory is %d\n", SHM_SIZE);
    fprintf(store_results,"-----------------------------------\n");
    fprintf(store_results,"Operation: Shared Memory Read\n");
    fprintf(store_results, "Number of iterations in 1 second: %d\n", clientCountPosix);
    fprintf(store_results,"Average Access Time : %f ms\n", averageClientPosix);
    fprintf(store_results,"Minimum Access Time : %f ms\n", shortestClientPosix);
    fprintf(store_results,"Longest Access Time : %f ms\n", longestClientPosix);
    fprintf(store_results,"\n");

    fprintf(store_results,"Operation: Shared Memory Write\n");
    fprintf(store_results, "Number of iterations in 1 second: %d\n", serverCountPosix);
    fprintf(store_results,"Average Access Time : %f ms\n", averageServerPosix);
    fprintf(store_results,"Minimum Access Time : %f ms\n", shortestServerPosix);
    fprintf(store_results,"Longest Access Time : %f ms\n", longestServerPosix);
    fprintf(store_results, "------------------------------------\n");
    fprintf(store_results, "\n");

    fclose(store_results);

}