#include "shared_mem_driver.h"
#include "client.h"
#include "server.h"


/**
 * This program is used to demonstrate Shared Memory using System V
 */

int shared_mem_execute(int argc, char* argv[]){  

    if(argc != 2){
        printf("This program requires a message in quotes with a max size of 1024 bytes\n");
        exit(1);
    }
    
    //1 second = 1000 milliseconds
    gettimeofday(&start,NULL); //starts timer
    while(elapsedTime < 1000.0){

        //Create a pthread and run the send function with the message
        pthread_create(&thread1, NULL, send, argv[1]);
        pthread_join(thread1, NULL);
        
        //Create a pthread to read the message
        pthread_create(&thread2, NULL, receive, NULL);
        pthread_join(thread2, NULL);

        gettimeofday(&end, NULL);//ends timer
        //Add to the elapsed time to make sure we are still under the 1 second threshold
        elapsedTime += ((end.tv_usec - start.tv_usec) / 1000.0); //converts from microseconds to milliseconds
    }

    //Averages time spent for Server and Client
    averageClient = totalClientTime/clientCount;
    averageServer = totalServerTime/serverCount;

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
    printf("Number of iterations in 1 second: %d\n", clientCount);
    printf("Average Access Time : %f ms\n", averageClient);
    printf("Minimum Access Time : %f ms\n", shortestClient);
    printf("Longest Access Time : %f ms\n", longestClient);
    printf("\n");

    printf("Operation: Shared Memory Write\n");
    printf("Number of iterations in 1 second: %d\n", serverCount);
    printf("Average Access Time : %f ms\n", averageServer);
    printf("Minimum Access Time : %f ms\n", shortestServer);
    printf("Longest Access Time : %f ms\n", longestServer);
    printf("\n");
}

/**
 * Write results to file
 * The file is located in the "build" folder
 */
int append_results(char* message){
    
    FILE *store_results;
    store_results = fopen("SHM_SYSV_Output.txt", "a");
    fprintf(store_results, "\n");
    fprintf(store_results,"Shared Memory System V findings\n");
    fprintf(store_results, "The size of the shared memory is %d\n", SHM_SIZE);
    fprintf(store_results,"-----------------------------------\n");
    fprintf(store_results,"Operation: Shared Memory Read\n");
    fprintf(store_results, "Number of iterations in 1 second: %d\n", clientCount);
    fprintf(store_results,"Average Access Time : %f ms\n", averageClient);
    fprintf(store_results,"Minimum Access Time : %f ms\n", shortestClient);
    fprintf(store_results,"Longest Access Time : %f ms\n", longestClient);
    fprintf(store_results,"\n");

    fprintf(store_results,"Operation: Shared Memory Write\n");
    fprintf(store_results, "Number of iterations in 1 second: %d\n", serverCount);
    fprintf(store_results,"Average Access Time : %f ms\n", averageServer);
    fprintf(store_results,"Minimum Access Time : %f ms\n", shortestServer);
    fprintf(store_results,"Longest Access Time : %f ms\n", longestServer);
    fprintf(store_results, "------------------------------------\n");
    fprintf(store_results, "\n");

    fclose(store_results);

}