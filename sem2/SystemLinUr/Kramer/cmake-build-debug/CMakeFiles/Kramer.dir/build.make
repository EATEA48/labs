# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.15

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

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = C:\Users\Andrey\AppData\Local\JetBrains\Toolbox\apps\CLion\ch-0\193.5662.56\bin\cmake\win\bin\cmake.exe

# The command to remove a file.
RM = C:\Users\Andrey\AppData\Local\JetBrains\Toolbox\apps\CLion\ch-0\193.5662.56\bin\cmake\win\bin\cmake.exe -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\Andrey\CLionProjects\Kramer

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\Andrey\CLionProjects\Kramer\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/Kramer.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Kramer.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Kramer.dir/flags.make

CMakeFiles/Kramer.dir/main.c.obj: CMakeFiles/Kramer.dir/flags.make
CMakeFiles/Kramer.dir/main.c.obj: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\Andrey\CLionProjects\Kramer\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/Kramer.dir/main.c.obj"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\Kramer.dir\main.c.obj   -c C:\Users\Andrey\CLionProjects\Kramer\main.c

CMakeFiles/Kramer.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/Kramer.dir/main.c.i"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E C:\Users\Andrey\CLionProjects\Kramer\main.c > CMakeFiles\Kramer.dir\main.c.i

CMakeFiles/Kramer.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/Kramer.dir/main.c.s"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S C:\Users\Andrey\CLionProjects\Kramer\main.c -o CMakeFiles\Kramer.dir\main.c.s

# Object files for target Kramer
Kramer_OBJECTS = \
"CMakeFiles/Kramer.dir/main.c.obj"

# External object files for target Kramer
Kramer_EXTERNAL_OBJECTS =

Kramer.exe: CMakeFiles/Kramer.dir/main.c.obj
Kramer.exe: CMakeFiles/Kramer.dir/build.make
Kramer.exe: CMakeFiles/Kramer.dir/linklibs.rsp
Kramer.exe: CMakeFiles/Kramer.dir/objects1.rsp
Kramer.exe: CMakeFiles/Kramer.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\Andrey\CLionProjects\Kramer\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable Kramer.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\Kramer.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Kramer.dir/build: Kramer.exe

.PHONY : CMakeFiles/Kramer.dir/build

CMakeFiles/Kramer.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\Kramer.dir\cmake_clean.cmake
.PHONY : CMakeFiles/Kramer.dir/clean

CMakeFiles/Kramer.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\Andrey\CLionProjects\Kramer C:\Users\Andrey\CLionProjects\Kramer C:\Users\Andrey\CLionProjects\Kramer\cmake-build-debug C:\Users\Andrey\CLionProjects\Kramer\cmake-build-debug C:\Users\Andrey\CLionProjects\Kramer\cmake-build-debug\CMakeFiles\Kramer.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Kramer.dir/depend
