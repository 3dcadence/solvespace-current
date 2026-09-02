from skbuild import setup

import io
import os

this_directory = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

if __name__ == '__main__':
    setup(
        name='py_slvs',
        version='1.0.6',
        packages=['py_slvs'],
        license='Gnu General Public License 3.0',
        author='Zheng, Lei',
        author_email='realthunder.dev@gmail.com',
        cmake_args=[
            '-DENABLE_GUI:BOOL=OFF',
            '-DENABLE_CLI:BOOL=OFF',
            '-DENABLE_TESTS:BOOL=OFF',
            '-DBUILD_PYTHON:BOOL=ON',
            '-DFORCE_VENDORED_Eigen3:BOOL=ON',
            '-DCMAKE_POLICY_VERSION_MINIMUM:STRING=3.5',
        ],
        cmake_source_dir='..',
        url='https://github.com/realthunder/slvs_py',
        description='Python binding of SOLVESPACE geometry constraint solver',
        long_description=long_description,
        long_description_content_type='text/markdown'
    )
