# Python Binding of SOLVESPACE Constraint Solver

`py_slvs` is a Python binding of the 2D/3D geometry constraint solver from a
[forked version](https://github.com/realthunder/solvespace) of
[SOLVESPACE](http://solvespace.com/). 

The fork is based on SOLVESPACE v2.3, with some memory optimization
on Linux build. The Python binding is done using [SWIG](http://www.swig.org/)
and modeled straight from SOLVESPACE's solver library 
(see [here](https://github.com/realthunder/solvespace/blob/python/exposed/DOC.txt)
and [here](https://github.com/realthunder/solvespace/blob/python/include/slvs.h)),
and is thus considered fairly low level.

The binding is currently used to implement the primiary solver for
FreeCAD [assembly3](https://github.com/realthunder/FreeCAD_assembly3) workbench

## Building the wheels

The wheels are built for CPython 3.13 from this `packaging` folder. The SWIG
build watches `src/swig/slvs.i` and not `slvs_swig.hpp`, so touch `slvs.i`
before every build or the wheel keeps the previous Python API.

- **Windows**: in a vcvars64 shell, with cmake, swig and ninja installed as
  Python packages, run `py -3.13 setup.py bdist_wheel -G Ninja` here.
- **Linux**: `build_linux.sh` builds inside the manylinux container from a
  clean copy of the repository and repairs the wheel with auditwheel:

      docker run --rm -v <repository>:/host -v <output folder>:/out \
          quay.io/pypa/manylinux_2_28_x86_64 bash /host/packaging/build_linux.sh

  From Git Bash, set `MSYS_NO_PATHCONV=1` first, or the paths are rewritten.
- **macOS** (Apple silicon and Intel): the `wheels` workflow in
  `.github/workflows/wheels.yml`, both on an Apple machine.

