set(CMAKE_C_COMPILER /usr/bin/gcc)
set(CMAKE_C_FLAGS -pthread)

add_library(
    LNLib SHARED
    
    src/messagequeue/message_queue.c
    src/messagequeue/message_queue.h
    src/messagequeue/message_queue_driver.c
    src/messagequeue/message_queue_driver.h

    #src/semaphore/Psemaphore.c
    #src/semaphore/Psemaphore.h
    #src/semaphore/semaphore_driver.h
    #src/semaphore/semaphore_driver.c

    src/SYSV_semaphore/SYSVsemaphore.c
    src/SYSV_semaphore/SYSVsemaphore.h
    src/SYSV_semaphore/SYSVsemaphore_driver.h
    src/SYSV_semaphore/SYSVsemaphore_driver.c


    src/shmem/client.h
    src/shmem/client.c
    src/shmem/server.h
    src/shmem/server.c
    src/shmem/shared_mem_driver.h
    src/shmem/shared_mem_driver.c

    src/debug_utils.h

)
#target_compile_definitions(LNLib PRIVATE DEBUG=1)
target_compile_options(LNLib PRIVATE -pthread)
target_link_libraries(LNLib PRIVATE m)
target_include_directories(LNLib PUBLIC "${ABS_ROOT}/LNLib/src")
message(${ABS_ROOT}/LNLib/src)