set(CMAKE_C_COMPILER /usr/bin/gcc)
set(CMAKE_C_FLAGS -pthread)

add_library(
    DeclanLib SHARED

    src/DLib_Driver.h
    src/DLib_Driver.c

    ../debug_utils.h

)
target_compile_options(DeclanLib PRIVATE -pthread)
target_link_libraries(DeclanLib PRIVATE rt)
target_link_libraries(DeclanLib PRIVATE m)
target_include_directories(DeclanLib PUBLIC "${ABS_ROOT}UserCode/Declan/src")
target_include_directories(DeclanLib PUBLIC "${ABS_ROOT}UserCode/")
message(${ABS_ROOT}DeclanLib/src)