#include "shared_mem_driver.h"

int shared_mem_execute(int argc, char* argv[]){

    struct timeval t1, t2;
    float elapsedTime = 0;
    float sample = 0;
    int count = 0;
    int total = 0;

    if(argc != 2){
        printf("This program requires a message in quotes with a max size of 1024 bytes\n");
        exit(1);
    }

    gettimeofday(&t1, NULL);

    //1 second = 1000 milliseconds
    while(elapsedTime < 1000){
        count++;

        send(argv[1]);
        receive();

        gettimeofday(&t2, NULL);
        elapsedTime = (t2.tv_sec - t1.tv_sec) * 1000; //sec to ms
        sample = elapsedTime;
    }
    printf("In one second, POSIX SharedMemory IPC has executed is %d times.\n", count);
    print_msg();
    clean_ipc();
    return 0;
}

