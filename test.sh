#!/bin/bash
set -e # exit with nonzero exit code if anything fails

# create the tests folder
mkdir tests
cd tests
git init
git clone https://github.com/BrythonServer/ggame.git
git clone https://${GH_REPO}
cd ..

python tests/test.py ${TESTMODULE}
