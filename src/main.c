#include "shmem/shared_mem_driver.h"
#include "semaphore/semaphore_driver.h"

int main(int argc, char* argv[]){

    for(int i = 0; i < 100; i ++){
        //shared_mem_execute(argc, argv);
        semaphore_execute(argc, argv);
    }
    return 0;

}