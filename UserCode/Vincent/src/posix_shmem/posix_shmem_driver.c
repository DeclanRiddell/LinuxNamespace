#include "posix_shmem_driver.h"

/**
 * This program is used to demonstrate Shared Memory using POSIX API
 */

int POSIX_shared_memory_execute(){


    gettimeofday(&startPosix, NULL);
    //1 second = 1000 milliseconds
    while(posixCounter < 1000){
        posixCounter++;
        
        //Create pthread and send the message
        pthread_create(&thread1Posix, NULL, posix_send, __msg);
        pthread_join(thread1Posix, NULL);

        //Create pthread and read the message
        pthread_create(&thread2Posix, NULL, posix_receive, NULL);
        pthread_join(thread2Posix, NULL);
    }
    gettimeofday(&endPosix, NULL); //end timer
    elapsedTimePosix += abs(((endPosix.tv_usec - startPosix.tv_usec) / 1000.0)); //converts from microseconds to milliseconds

    //Averages time spent for Server and Client
    averageClientPosix = totalClientTimePosix/clientCountPosix;
    averageServerPosix = totalServerTimePosix/serverCountPosix;
    msgPerSecondPosix = posixCounter/(elapsedTimePosix/1000.0); //Go from millisecond to second

    
    //Print results and append results to file
    posix_results();
    posix_append_results(__msg);

    return 0;
}

//prints results
void posix_results(){        
   LOG("\n");
   LOG("Shared Memory POSIX findings\n");
   LOG("-----------------------------------\n");
   LOG("Number of Iterations : %d\n", posixCounter);
   LOG("Total time spent : %f ms\n", elapsedTimePosix);
   LOG("Message rate : %f messages per second\n", msgPerSecondPosix);
   LOG("\n");
   LOG("Operation: Shared Memory Read\n");
   LOG("Average Access Time : %f ms\n", averageClientPosix);
   LOG("Minimum Access Time : %f ms\n", shortestClientPosix);
   LOG("Longest Access Time : %f ms\n", longestClientPosix);
   LOG("\n");

   LOG("Operation: Shared Memory Write\n");
   LOG("Average Access Time : %f ms\n", averageServerPosix);
   LOG("Minimum Access Time : %f ms\n", shortestServerPosix);
   LOG("Longest Access Time : %f ms\n", longestServerPosix);
   LOG("\n");
}

/**
 * Write results to file
 * The file is located in the "build" folder
 * Time is recorded in ms
 * First value is Read Average
 * Second value is Write Average
 */
int posix_append_results(){
    
    FILE *store_results;
    store_results = fopen("../UserCode/Vincent/src/posix_shmem/SHM_POSIX_Output.txt", "a");
    fprintf(store_results,"%f\n", averageClientPosix);
    fprintf(store_results,"%f\n", averageServerPosix);
    fprintf(store_results, "\n");

    fclose(store_results);

}