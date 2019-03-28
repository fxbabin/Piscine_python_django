#!/bin/sh

pip --version
pip install -t local_lib --upgrade git+https://github.com/jaraco/path.py.git > path_py_install.log
curl --silent -L https://raw.githubusercontent.com/jaraco/path.py/master/path.py > local_lib/path.py

if grep -q "Successfully installed" path_py_install.log
then
   echo "toto"
fi