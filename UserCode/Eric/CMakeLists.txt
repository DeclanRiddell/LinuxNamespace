set(CMAKE_C_COMPILER /usr/bin/gcc)
set(CMAKE_C_FLAGS -pthread)

add_library(
    EricLib SHARED
    
    src/semaphore/semaphore_driver.c
    src/semaphore/semaphore_driver.h
    src/semaphore/Psemaphore.c
    src/semaphore/Psemaphore.h


    ../debug_utils.h

)
target_compile_options(EricLib PRIVATE -pthread)
target_link_libraries(EricLib PRIVATE rt)
target_link_libraries(EricLib PRIVATE m)
target_include_directories(EricLib PUBLIC "${ABS_ROOT}UserCode/Eric/src")
target_include_directories(EricLib PUBLIC "${ABS_ROOT}UserCode/")
message(${ABS_ROOT}EricLib/src)