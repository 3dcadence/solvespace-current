#!/bin/bash
set -e
dnf install -y swig >/dev/null 2>&1 || yum install -y swig >/dev/null 2>&1
rm -rf /build
mkdir -p /build
cp -r /host /build/solvespace
rm -rf /build/solvespace/packaging/_skbuild /build/solvespace/packaging/dist /build/solvespace/packaging/*.egg-info
touch /build/solvespace/src/swig/slvs.i
cd /build/solvespace/packaging
PY=/opt/python/cp313-cp313/bin
$PY/pip install --quiet scikit-build setuptools wheel cmake ninja
$PY/python setup.py bdist_wheel -G Ninja
auditwheel repair dist/*.whl -w /out
