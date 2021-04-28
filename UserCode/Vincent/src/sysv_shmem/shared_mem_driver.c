#include "shared_mem_driver.h"
#include "client.h"
#include "server.h"


/**
 * This program is used to demonstrate Shared Memory using System V
 */

int SYS_V_shared_memory_execute(int iteration_count){  


    
    gettimeofday(&start,NULL); //starts timer
    while(counterSYSV < iteration_count){
        counterSYSV++;

        //Create a pthread and run the send function with the message
        pthread_create(&thread1, NULL, send, __msg);
        pthread_join(thread1, NULL);
        
        //Create a pthread to read the message
        pthread_create(&thread2, NULL, receive, NULL);
        pthread_join(thread2, NULL);
    }
    gettimeofday(&end, NULL);//ends timer
    elapsedTime += abs(((end.tv_usec - start.tv_usec) / 1000.0)); //converts from microseconds to milliseconds

    //Averages time spent for Server and Client
    averageClient = totalClientTime/clientCount;
    averageServer = totalServerTime/serverCount;
    msgPerSecondSYSV = counterSYSV/(elapsedTime/1000.0); //Go from millisecond to second

    //print results, append results to file, clean the ipc off of the ipcs list
    results();
    append_results(__msg);
    clean_ipc();

    return 0;
}

//prints results
void results(){        
   LOG("\n");
   LOG("Shared Memory System V findings\n");
   LOG("-----------------------------------\n");
   LOG("Operation: Shared Memory Read\n");
   LOG("Number of iterations : %d\n", counterSYSV);
   LOG("Total time spent : %f ms\n", elapsedTime);
   LOG("Message rate : %f messages per second\n", msgPerSecondSYSV);
   LOG("\n");
   LOG("Average Access Time : %f ms\n", averageClient);
   LOG("Minimum Access Time : %f ms\n", shortestClient);
   LOG("Longest Access Time : %f ms\n", longestClient);
   LOG("\n");

   LOG("Operation: Shared Memory Write\n");
   LOG("Average Access Time : %f ms\n", averageServer);
   LOG("Minimum Access Time : %f ms\n", shortestServer);
   LOG("Longest Access Time : %f ms\n", longestServer);
   LOG("\n");
}

/**
 * Write results to file
 * The file is located in the "build" folder
 * Time is in ms
 * First value is Read Average
 * Second value is Write Average
 */
int append_results(char* message){
    
    FILE *store_results;
    store_results = fopen("../UserCode/Vincent/src/sysv_shmem/SHM_SYSV_Output.txt", "a");
    fprintf(store_results,"%f\n", averageClient);
    fprintf(store_results,"%f\n", averageServer);
    fprintf(store_results, "\n");
    fclose(store_results);

}