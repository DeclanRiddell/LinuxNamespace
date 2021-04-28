set(CMAKE_C_COMPILER /usr/bin/gcc)
set(CMAKE_C_FLAGS -pthread)

add_library(
    VincentLib SHARED
    
    src/sysv_shmem/client.h
    src/sysv_shmem/client.c
    src/sysv_shmem/server.h
    src/sysv_shmem/server.c
    src/sysv_shmem/shared_mem_driver.h
    src/sysv_shmem/shared_mem_driver.c

    src/posix_shmem/posix_client.h
    src/posix_shmem/posix_client.c
    src/posix_shmem/posix_server.h
    src/posix_shmem/posix_server.c
    src/posix_shmem/posix_shmem_driver.h
    src/posix_shmem/posix_shmem_driver.c


    ../debug_utils.h

)
target_compile_options(VincentLib PRIVATE -pthread)
target_link_libraries(VincentLib PRIVATE rt)
target_link_libraries(VincentLib PRIVATE m)
target_link_libraries(VincentLib PRIVATE mysqlclient)
target_include_directories(VincentLib PUBLIC "${ABS_ROOT}UserCode/Vincent/src")
target_include_directories(VincentLib PUBLIC "${ABS_ROOT}UserCode/")
message(${ABS_ROOT}VincentLib/src)
