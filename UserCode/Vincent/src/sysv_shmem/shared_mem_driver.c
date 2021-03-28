#include "shared_mem_driver.h"
#include "client.h"
#include "server.h"


/**
 * This program is used to demonstrate Shared Memory using System V
 */

int SYS_V_shared_memory_execute(int argc, char* argv[]){  

    if(argc < 2){
        printf("This program requires a message in quotes with a max size of 1024 bytes\n");
        exit(1);
    }
    
    gettimeofday(&start,NULL); //starts timer
    while(counterSYSV < 1000.0){
        counterSYSV++;

        //Create a pthread and run the send function with the message
        pthread_create(&thread1, NULL, send, argv[1]);
        pthread_join(thread1, NULL);
        
        //Create a pthread to read the message
        pthread_create(&thread2, NULL, receive, NULL);
        pthread_join(thread2, NULL);

        gettimeofday(&end, NULL);//ends timer
        //Add to the elapsed time to make sure we are still under the 1 second threshold
        elapsedTime += abs(((end.tv_usec - start.tv_usec) / 1000.0)); //converts from microseconds to milliseconds
    }

    //Averages time spent for Server and Client
    averageClient = totalClientTime/clientCount;
    averageServer = totalServerTime/serverCount;
    msgPerSecondSYSV = elapsedTime/counterSYSV;

    //print results, append results to file, clean the ipc off of the ipcs list
    results();
    append_results(argv[1]);
    clean_ipc();

    return 0;
}

//prints results
void results(){        
    printf("\n");
    printf("Shared Memory System V findings\n");
    printf("-----------------------------------\n");
    printf("Operation: Shared Memory Read\n");
    printf("Number of iterations : %d\n", counterSYSV);
    printf("Total time spent : %f ms\n", elapsedTime);
    printf("Message rate : %f messages per second\n", msgPerSecondSYSV);
    printf("\n");
    printf("Average Access Time : %f ms\n", averageClient);
    printf("Minimum Access Time : %f ms\n", shortestClient);
    printf("Longest Access Time : %f ms\n", longestClient);
    printf("\n");

    printf("Operation: Shared Memory Write\n");
    printf("Average Access Time : %f ms\n", averageServer);
    printf("Minimum Access Time : %f ms\n", shortestServer);
    printf("Longest Access Time : %f ms\n", longestServer);
    printf("\n");
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
    store_results = fopen("SHM_SYSV_Output.txt", "a");
    fprintf(store_results,"%f\n", averageClient);
    fprintf(store_results,"%f\n", averageServer);
    fprintf(store_results, "\n");
    fclose(store_results);

}