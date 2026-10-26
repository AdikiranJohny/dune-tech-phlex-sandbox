# The plugin is named after this folder (your GitHub username), so it can't clash with
# anyone else's. A username like "a-b" gives the plugin name "multiply_a_b".
get_filename_component(me "${CMAKE_CURRENT_SOURCE_DIR}" NAME)
string(MAKE_C_IDENTIFIER "${me}" me)
set(plugin multiply_${me})

add_library(${plugin} MODULE multiply_and_verify.cpp)
target_link_libraries(${plugin} PRIVATE phlex::module)
# Keep assert() active, as the examples do
target_compile_options(${plugin} PRIVATE -UNDEBUG)
# Put the .so in the top of the build directory, which is already on PHLEX_PLUGIN_PATH
set_target_properties(${plugin} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}")

message(STATUS "contributions/${me}: plugin ${plugin}")
