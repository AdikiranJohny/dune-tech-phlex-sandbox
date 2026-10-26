cmake_minimum_required(VERSION 3.31)
project(cmake_warmup LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)

# A shared library, built from greet.cpp
add_library(greet SHARED greet.cpp)

# A program that uses the library
add_executable(hello hello.cpp)
target_link_libraries(hello PRIVATE greet)
