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
void execute_alex_lib(int argc, char* argv[]){
    DBG_WRAP_DRIVER(POSIX_message_queue_execute(argc, argv));
    DBG_WRAP_DRIVER(SYS_V_message_queue_execute(argc, argv));
}

//EricLib execution
void execute_eric_lib(int argc, char* argv[]){
    DBG_WRAP_DRIVER(POSIX_semaphore_execute(argc, argv));
    DBG_WRAP_DRIVER(SYS_V_semaphore_execute(argc, argv));
}

//VincentLib execution
void execute_vincent_lib(int argc, char* argv[]){
    DBG_WRAP_DRIVER(POSIX_shared_memory_execute(argc, argv));
    DBG_WRAP_DRIVER(SYS_V_shared_memory_execute(argc, argv));
}


//DeclanLib execution
void execute_declan_lib(int argc, char* argv[]){
    DBG_WRAP_DRIVER(execute_declan(argc, argv));
}


int run_IPCS(int argc, char* argv[]){
    LOG("Entered 'run_IPCS'\n");
    int execution_order = atoi(argv[2]);
    printf("%s, %d\n", argv[1], execution_order);
    
    switch(execution_order){
        case EXECUTE_DECLAN:{
            execute_declan_lib(argc, argv);
            break;
        }
        case EXECUTE_ALEX:{
            execute_alex_lib(argc, argv);
            break;
        }
        case EXECUTE_VINCENT:{
            execute_vincent_lib(argc, argv);
            break;
        }
        case EXECUTE_ERIC:{
            execute_eric_lib(argc, argv);
            break;
        }
        default:{
            execute_alex_lib(argc, argv);
            execute_eric_lib(argc, argv);
            execute_vincent_lib(argc, argv);
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
    int run_namespace = atoi(argv[3]);
    LOG("run_namespace ? %d", run_namespace );
    if(!run_namespace) return run_IPCS(argc, argv);
    LOG("Running namespace");
    mem = malloc(STACK_SIZE);
    if(!mem) printf("Error allocating stack\n");
    
    //generate a new ipc namespace
    //create child process for run_ipcs
    // send child into ipc namespace
   // 0x08000000
    //0x04000000
    int ret = clone(run_IPCS, mem + STACK_SIZE, CLONE_NEWIPC, (void*)argc, (void*)argv);
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
