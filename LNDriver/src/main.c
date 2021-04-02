#define _GNU_SOURCE
#define __USE_GNU
#include <sysv_shmem/shared_mem_driver.h>
#include <posix_shmem/posix_shmem_driver.h>

#include <SYSV_semaphore/SYSVsemaphore_driver.h>
#include <semaphore/semaphore_driver.h>

#include <POSIX_message_queue/POSIX_message_queue_driver.h>
#include <sysv_messagequeue/SYSV_message_queue_driver.h>
#include <DLib_Driver.h>
#include <debug_utils.h>
#include <stdlib.h>

#include <sched.h>
#define EXECUTE_ALL     0
#define EXECUTE_ERIC    1
#define EXECUTE_ALEX    2
#define EXECUTE_VINCENT 3
#define EXECUTE_DECLAN  4


//AlexLib execution
void execute_alex_lib(){
    DBG_WRAP_DRIVER(POSIX_message_queue_execute());
    DBG_WRAP_DRIVER(SYS_V_message_queue_execute());
}

//EricLib execution
void execute_eric_lib(){
    DBG_WRAP_DRIVER(POSIX_semaphore_execute());
    DBG_WRAP_DRIVER(SYS_V_semaphore_execute());
}

//VincentLib execution
void execute_vincent_lib(){
    DBG_WRAP_DRIVER(POSIX_shared_memory_execute());
    DBG_WRAP_DRIVER(SYS_V_shared_memory_execute());
}


//DeclanLib execution
void execute_declan_lib(){
    DBG_WRAP_DRIVER(execute_declan());
}
int execution_order = 0;


int run_IPCS(){
    LOG("Entered 'run_IPCS'\n");
    
    switch(execution_order){
        case EXECUTE_DECLAN:{
            execute_declan_lib();
            break;
        }
        case EXECUTE_ALEX:{
            execute_alex_lib();
            break;
        }
        case EXECUTE_VINCENT:{
            execute_vincent_lib();
            break;
        }
        case EXECUTE_ERIC:{
            execute_eric_lib();
            break;
        }
        default:{
            execute_alex_lib();
            execute_eric_lib();
            execute_vincent_lib();
            break;
        }
    }
    return 0;
}

int sup(){
    DEBUG("Worked\n");
    return 0;
}

#define STACK_SIZE 65536
void* mem;
int driver(int argc, char* argv[]){
    execution_order = atoi(argv[1]);
    int run_namespace = atoi(argv[2]);
    LOG("run_namespace ? %d", run_namespace );
    if(!run_namespace) return run_IPCS();
    LOG("Running namespace");
    mem = malloc(STACK_SIZE);
    if(!mem)LOG("Error allocating stack\n");
    
    //generate a new ipc namespace
    //create child process for run_ipcs
    // send child into ipc namespace
   // 0x08000000
    //0x04000000
    int ret = clone(run_IPCS, mem + STACK_SIZE, CLONE_NEWIPC, (void*)0);
    if(ret == -1){
         ERROR("Error code %d=%s\n", errno, strerror(errno));
         exit(1);
     }

    LOG("Clone id %d\n", ret);
    return 0;

}


int main(int argc, char* argv[]){

    INIT_LOG("Starting main driver\n");
    driver(argc, argv);


    return 0;

}
