set(CMAKE_C_COMPILER /usr/bin/gcc)
set(CMAKE_C_FLAGS -pthread)

add_library(
    AlexLib SHARED
    
    src/POSIX_message_queue/POSIX_message_queue_driver.c
    src/POSIX_message_queue/POSIX_message_queue_driver.h
    src/POSIX_message_queue/POSIX_message_queue.c
    src/POSIX_message_queue/POSIX_message_queue.h
    src/POSIX_message_queue/POSIX_msgq_metrics.c
    src/POSIX_message_queue/POSIX_msgq_metrics.h

    src/sysv_messagequeue/SYSV_message_queue_driver.c
    src/sysv_messagequeue/SYSV_message_queue_driver.h
    src/sysv_messagequeue/SYSV_message_queue.c
    src/sysv_messagequeue/SYSV_message_queue.h
    src/sysv_messagequeue/SYSV_msgq_metrics.c
    src/sysv_messagequeue/SYSV_msgq_metrics.h


    ../debug_utils.h
    ../debug_utils.c

)
target_compile_options(AlexLib PRIVATE -pthread)
target_link_libraries(AlexLib PRIVATE rt)
target_link_libraries(AlexLib PRIVATE m)
target_include_directories(AlexLib PUBLIC "${ABS_ROOT}UserCode/Alex/src")
target_include_directories(AlexLib PUBLIC "${ABS_ROOT}UserCode/")
message(${ABS_ROOT}AlexLib/src)