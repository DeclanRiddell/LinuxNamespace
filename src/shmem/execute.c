#include "server.h"
#include "client.h"
#include <sys/time.h>
#include <stdio.h>

int main(){

    struct timeval t1, t2;
    float elapsedTime = 0;
    int count = 0;
    int total = 0;
    
    //1 second = 1000 milliseconds
    while(elapsedTime < 1000){
        count++;
        gettimeofday(&t1, NULL);

        send();
        receive();

        gettimeofday(&t2, NULL);
        elapsedTime = (t2.tv_sec - t1.tv_sec) * 1000; //sec to ms
    }
    printf("The number of times this has executed is %d\n", count);

    return 0;
}

