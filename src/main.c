#include "shmem/shared_mem_driver.h"
#include "semaphore/semaphore_driver.h"
#include "messagequeue/message_queue_driver.h"
#include "debug_utils.h"

int main(int argc, char* argv[]){

    printf("Starting main driver\n");
    for(int i = 0; i < 100; i ++){
        DBG_WRAP_DRIVER(semaphore_execute(argc, argv));
        DBG_WRAP_DRIVER(message_queue_execute(argc, argv));
        DBG_WRAP_DRIVER(shared_mem_execute(argc, argv));
    }
    return 0;

}