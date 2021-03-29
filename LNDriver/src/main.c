#include <SYSV_semaphore/SYSVsemaphore_driver.h>
#include <semaphore/semaphore_driver.h>

#include <debug_utils.h>
#include <stdlib.h>
#define EXECUTE_ALL     0
#define EXECUTE_ERIC    1
#define EXECUTE_ALEX    2
#define EXECUTE_VINCENT 3


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



int main(int argc, char* argv[]){

    printf("Starting main driver\n");
    int execution_order = atoi(argv[2]);
    printf("%s, %d\n", argv[1], execution_order);
    switch(execution_order){
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
