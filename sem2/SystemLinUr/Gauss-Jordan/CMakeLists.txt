cmake_minimum_required(VERSION 3.15)
project(Gauss_Jordan C)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c99 -fopenmp")

add_executable(Gauss_Jordan main.c)