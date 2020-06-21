cmake_minimum_required(VERSION 3.15)
project(Kramer C)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c99 -fopenmp")

add_executable(Kramer main.c)