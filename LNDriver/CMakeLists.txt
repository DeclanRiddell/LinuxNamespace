set(CMAKE_C_COMPILER /usr/bin/gcc)
add_executable(LNDriver src/main.c)
target_link_libraries(LNDriver PRIVATE LNLib)