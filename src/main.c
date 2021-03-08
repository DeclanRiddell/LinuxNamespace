#include "shmem/shared_mem_driver.h"
#include "semaphore/semaphore_driver.h"

int main(int argc, char* argv[]){

    //shared_mem_execute(argc, argv);
    for(int i = 0; i < 100; i ++)
        semaphore_execute(argc, argv);
    return 0;

}