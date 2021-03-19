set(CMAKE_CC_COMPILER gcc)

add_library(
    LNLib SHARED
    
    src/messagequeue/message_queue_driver.c
    src/messagequeue/message_queue_driver.h
    src/messagequeue/message_queue.c
    src/messagequeue/message_queue.h

    src/semaphore/semaphore_driver.c
    src/semaphore/semaphore_driver.h
    src/semaphore/Psemaphore.c
    src/semaphore/Psemaphore.h


    src/shmem/client.h
    src/shmem/client.c
    src/shmem/server.h
    src/shmem/server.c
    src/shmem/shared_mem_driver.h
    src/shmem/shared_mem_driver.c

    src/debug_utils.h

)

target_include_directories(LNLib PUBLIC "${ABS_ROOT}/LNLib/src")
message(${ABS_ROOT}/LNLib/src)