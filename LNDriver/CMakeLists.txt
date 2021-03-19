set(CMAKE_CC_COMPILER gcc)
add_executable(LNDriver src/main.c)
target_link_libraries(LNDriver PRIVATE LNLib)