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
#define EXECUTE_ALL         0
#define EXECUTE_ERIC        1
#define EXECUTE_ALEX        2
#define EXECUTE_VINCENT     3
#define EXECUTE_DECLAN      4
#define EXECUTE_ERIC_P      5
#define EXECUTE_ALEX_P      6
#define EXECUTE_VINCENT_P   7
#define EXECUTE_DECLAN_P    8
#define EXECUTE_ERIC_S      9
#define EXECUTE_ALEX_S      10
#define EXECUTE_VINCENT_S   11
#define EXECUTE_DECLAN_S    12
int iteration_count;

//AlexLib execution
void execute_alex_lib(short posix){
    if(posix == 1){ DBG_WRAP_DRIVER(POSIX_message_queue_execute(iteration_count));}
    else{ DBG_WRAP_DRIVER(SYS_V_message_queue_execute(iteration_count));}
}

//EricLib execution
void execute_eric_lib(short posix){
    if(posix == 1){ DBG_WRAP_DRIVER(POSIX_semaphore_execute(iteration_count));}
    else{ DBG_WRAP_DRIVER(SYS_V_semaphore_execute(iteration_count));}
}

//VincentLib execution
void execute_vincent_lib(short posix){
    if(posix == 1){ DBG_WRAP_DRIVER(POSIX_shared_memory_execute(iteration_count));}
    else{ DBG_WRAP_DRIVER(SYS_V_shared_memory_execute(iteration_count));}
}


//DeclanLib execution
void execute_declan_lib(short posix){
    DBG_WRAP_DRIVER(execute_declan());
}
int execution_order = 0;


int run_IPCS(){
    LOG("Entered 'run_IPCS'\n");
    
    switch(execution_order){
        case EXECUTE_DECLAN:{
            execute_declan_lib(1);
            execute_declan_lib(0);
            break;
        }
        case EXECUTE_ALEX:{
            execute_alex_lib(1);
            execute_alex_lib(0);
            break;
        }
        case EXECUTE_VINCENT:{
            execute_vincent_lib(1);
            execute_vincent_lib(0);
            break;
        }
        case EXECUTE_ERIC:{
            execute_eric_lib(1);
            execute_eric_lib(0);
            break;
        }
        case EXECUTE_ALEX_S:{
            execute_alex_lib(0);
            break;
        }
        case EXECUTE_VINCENT_S:{
            execute_vincent_lib(0);
            break;
        }
        case EXECUTE_ERIC_S:{
            execute_eric_lib(0);
            break;
        }
        case EXECUTE_ALEX_P:{
            execute_alex_lib(1);
            break;
        }
        case EXECUTE_VINCENT_P:{
            execute_vincent_lib(1);
            break;
        }
        case EXECUTE_ERIC_P:{
            execute_eric_lib(1);
            break;
        }
        default:{
            execute_alex_lib(1);
            execute_alex_lib(0);
            execute_eric_lib(1);
            execute_eric_lib(0);
            execute_vincent_lib(1);
            execute_vincent_lib(0);
            break;
        }
    }

    UNLOAD_LOG("Finished IPC Drivers");
    return 0;
}

int sup(){
    DEBUG("Worked\n");
    return 0;
}

#define STACK_SIZE 65536
void* mem;
int driver(int argc, char* argv[]){
    LOG("Starting");
    execution_order = atoi(argv[1]);
    int run_namespace = atoi(argv[2]);
    iteration_count = atoi(argv[3]);
    LOG("Iteration count = %d", iteration_count);
    LOG("run_namespace ? %d", run_namespace );
    if(!run_namespace) return run_IPCS();
    LOG("Running namespace");
    mem = malloc(STACK_SIZE);
    if(!mem)LOG("Error allocating stack\n");
    
    pid_t child_clone_pid = clone(run_IPCS, mem + STACK_SIZE, CLONE_NEWIPC, (void*)0);
    if(child_clone_pid == -1){
         ERROR("Error code %d=%s\n", errno, strerror(errno));
         exit(1);
     }

    
    LOG("Clone id %d\n", child_clone_pid);
    
    waitpid(child_clone_pid, NULL, 0);
    return 0;

}


int main(int argc, char* argv[]){

    INIT_LOG("Starting main driver\n");
    driver(argc, argv);


    return 0;

}
