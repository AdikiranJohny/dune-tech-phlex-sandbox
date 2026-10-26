# Build every contribution folder that has its own CMakeLists.txt.
# Folders starting with "_" are templates and are skipped.
file(GLOB children LIST_DIRECTORIES true RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}" "*")
foreach(child IN LISTS children)
  if(NOT child MATCHES "^_" AND EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/${child}/CMakeLists.txt")
    add_subdirectory(${child})
  endif()
endforeach()
