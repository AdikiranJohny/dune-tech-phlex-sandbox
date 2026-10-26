cmake_minimum_required(VERSION 3.31)
project(my_phlex_example VERSION 0.0.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)

if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
  if(CMAKE_CXX_COMPILER_VERSION VERSION_GREATER_EQUAL "14.1")
    if(CMAKE_CXX_COMPILER_VERSION VERSION_LESS "15")
      add_compile_options(-Wno-stringop-overflow)
    endif()
    if(CMAKE_CXX_COMPILER_VERSION VERSION_LESS "16")
      add_compile_options(-Wno-array-bounds)
    endif()
  endif()
endif()

find_package(Boost REQUIRED json)
find_package(TBB REQUIRED)
find_package(spdlog REQUIRED)
find_package(phlex REQUIRED)

# The example code comes from the official phlex-examples, included as a git submodule.
# It is read-only here: build it, read it, but don't change it.
set(EX "${CMAKE_CURRENT_SOURCE_DIR}/phlex-examples")
if(NOT EXISTS "${EX}/my_add.cpp")
  message(FATAL_ERROR "phlex-examples/ is empty. Run this in the repository, then configure again:\n"
                      "  git submodule update --init")
endif()

add_compile_options(-Wall -Wpedantic -Werror)

# Proxies for framework-agnostic experiment libraries
# N.B. The specified library type should be SHARED.
add_library(my_add SHARED ${EX}/my_add.cpp)
add_library(my_geometry SHARED ${EX}/my_geometry.cpp)

# Register providers for data products
add_library(numbers_source MODULE ${EX}/numbers_source.cpp)
target_link_libraries(numbers_source PRIVATE phlex::module)

add_library(geometry_source MODULE ${EX}/geometry_source.cpp)
target_link_libraries(geometry_source PRIVATE phlex::module my_geometry)

# Register experiment libraries with Phlex
add_library(add_and_verify MODULE ${EX}/add_and_verify.cpp)
target_link_libraries(add_and_verify PRIVATE phlex::module my_add my_geometry)

# Enable asserts for add_and_verify
# N.B. This should not be done for production code, but it is useful for testing and development.
target_compile_options(add_and_verify PRIVATE -UNDEBUG)

# Workshop sandbox: build participants' contributions (see WORKSHOP.md)
add_subdirectory(contributions)
