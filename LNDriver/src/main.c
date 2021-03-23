#include <POSIX_message_queue/POSIX_message_queue_driver.h>
#include <sysv_shmem/shared_mem_driver.h>
#include <posix_shmem/posix_shmem_driver.h>
#include <debug_utils.h>

int main(int argc, char* argv[]){

    printf("Starting main driver\n");
    DBG_WRAP_DRIVER(shmem_driver_posix(argc, argv));
    //DBG_WRAP_DRIVER(POSIX_message_queue_execute(argc, argv));
    //DBG_WRAP_DRIVER(semaphore_execute(argc, argv));
    //DBG_WRAP_DRIVER(shared_mem_execute(argc, argv));
    return 0;

}