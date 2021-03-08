#include "shmem/shared_mem_driver.h"
#include "semaphore/semaphore_driver.h"

int main(int argc, char* argv[]){

    shared_mem_execute(argc, argv);
    semaphore_execute(argc, argv);
    return 0;

}