#include "shmem/shared_mem_driver.h"
//#include "semaphore/semaphore_driver.h"
#include "SYSV_semaphore/SYSVsemaphore_driver.h"
#include "messagequeue/message_queue_driver.h"
#include "debug_utils.h"

int main(int argc, char* argv[]){

    printf("Starting main driver\n");
    DBG_WRAP_DRIVER(sysvsemaphore_execute(argc, argv));
    //DBG_WRAP_DRIVER(psemaphore_execute(argc, argv));
    //DBG_WRAP_DRIVER(message_queue_execute(argc, argv));
    //DBG_WRAP_DRIVER(shared_mem_execute(argc, argv));
    return 0;

}