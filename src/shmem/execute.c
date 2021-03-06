#include "server.h"
#include "client.h"
#include <sys/time.h>
#include <string.h>
#include <stdio.h>

int main(int argc, char* argv[]){

    struct timeval t1, t2;
    float elapsedTime = 0;
    int count = 0;
    int total = 0;

    if(argc != 2){
        printf("This program requires an argument in quotes with a maximum size of 1024 bytes\n");
        return 0;
    }

    gettimeofday(&t1, NULL);

    //1 second = 1000 milliseconds
    while(elapsedTime < 1000){
        count++;

        send(argv[1]);
        receive();

        gettimeofday(&t2, NULL);
        elapsedTime = (t2.tv_sec - t1.tv_sec) * 1000; //sec to ms
    }
    printf("The number of times this has executed is %d\n", count);
    print_msg();
    clean_ipc();
    return 0;
}

