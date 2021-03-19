cmake_minimum_required(VERSION 3.16.3)
project(LinuxNamespace VERSION 1.0.1)

set(ABS_ROOT "${CMAKE_SOURCE_DIR}/")

add_subdirectory(LNLib)
add_subdirectory(LNDriver)