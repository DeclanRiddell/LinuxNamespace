# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/luke/LinuxNamespace

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/luke/LinuxNamespace/build

# Include any dependencies generated for this target.
include LNDriver/CMakeFiles/LNDriver.dir/depend.make

# Include the progress variables for this target.
include LNDriver/CMakeFiles/LNDriver.dir/progress.make

# Include the compile flags for this target's objects.
include LNDriver/CMakeFiles/LNDriver.dir/flags.make

LNDriver/CMakeFiles/LNDriver.dir/src/main.c.o: LNDriver/CMakeFiles/LNDriver.dir/flags.make
LNDriver/CMakeFiles/LNDriver.dir/src/main.c.o: ../LNDriver/src/main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/luke/LinuxNamespace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object LNDriver/CMakeFiles/LNDriver.dir/src/main.c.o"
	cd /home/luke/LinuxNamespace/build/LNDriver && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/LNDriver.dir/src/main.c.o   -c /home/luke/LinuxNamespace/LNDriver/src/main.c

LNDriver/CMakeFiles/LNDriver.dir/src/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/LNDriver.dir/src/main.c.i"
	cd /home/luke/LinuxNamespace/build/LNDriver && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/luke/LinuxNamespace/LNDriver/src/main.c > CMakeFiles/LNDriver.dir/src/main.c.i

LNDriver/CMakeFiles/LNDriver.dir/src/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/LNDriver.dir/src/main.c.s"
	cd /home/luke/LinuxNamespace/build/LNDriver && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/luke/LinuxNamespace/LNDriver/src/main.c -o CMakeFiles/LNDriver.dir/src/main.c.s

# Object files for target LNDriver
LNDriver_OBJECTS = \
"CMakeFiles/LNDriver.dir/src/main.c.o"

# External object files for target LNDriver
LNDriver_EXTERNAL_OBJECTS =

LNDriver/LNDriver: LNDriver/CMakeFiles/LNDriver.dir/src/main.c.o
LNDriver/LNDriver: LNDriver/CMakeFiles/LNDriver.dir/build.make
LNDriver/LNDriver: LNLib/libLNLib.so
LNDriver/LNDriver: LNDriver/CMakeFiles/LNDriver.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/luke/LinuxNamespace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable LNDriver"
	cd /home/luke/LinuxNamespace/build/LNDriver && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/LNDriver.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
LNDriver/CMakeFiles/LNDriver.dir/build: LNDriver/LNDriver

.PHONY : LNDriver/CMakeFiles/LNDriver.dir/build

LNDriver/CMakeFiles/LNDriver.dir/clean:
	cd /home/luke/LinuxNamespace/build/LNDriver && $(CMAKE_COMMAND) -P CMakeFiles/LNDriver.dir/cmake_clean.cmake
.PHONY : LNDriver/CMakeFiles/LNDriver.dir/clean

LNDriver/CMakeFiles/LNDriver.dir/depend:
	cd /home/luke/LinuxNamespace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/luke/LinuxNamespace /home/luke/LinuxNamespace/LNDriver /home/luke/LinuxNamespace/build /home/luke/LinuxNamespace/build/LNDriver /home/luke/LinuxNamespace/build/LNDriver/CMakeFiles/LNDriver.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : LNDriver/CMakeFiles/LNDriver.dir/depend

