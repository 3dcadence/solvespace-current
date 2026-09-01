find_package(Python3 COMPONENTS Interpreter Development.Module REQUIRED)

if(WIN32)
    set(PYLIB_SUFFIX .pyd)
else()
    set(PYLIB_SUFFIX .so)
endif()

add_definitions(-DSLVS_STATIC_LIB)

set_property(SOURCE ../slvs.i PROPERTY CPLUSPLUS ON)
set_property(SOURCE ../slvs.i PROPERTY SWIG_MODULE_NAME slvs)
include_directories(../ ${CMAKE_SOURCE_DIR}/include)

swig_add_library(slvspy LANGUAGE python SOURCES ../slvs.i)

set_target_properties(slvspy PROPERTIES
    OUTPUT_NAME "_slvs"
    PREFIX ""
    SUFFIX "${PYLIB_SUFFIX}")

target_link_libraries(slvspy PRIVATE slvs-interface Python3::Module)

install(TARGETS slvspy LIBRARY DESTINATION py_slvs RUNTIME DESTINATION py_slvs)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/slvs.py DESTINATION py_slvs)
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/__init__.py DESTINATION py_slvs)
