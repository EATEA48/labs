cmake_minimum_required(VERSION 3.15)
project(InsertSort C)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c99 -fopenmp")

add_executable(InsertSort main.c)