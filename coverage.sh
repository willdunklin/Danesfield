#!/bin/bash

this_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd $this_dir

# set coverage sources to all directories (default is to only include directories with __init__.py)
# excluding danesfield/geon_fitting/tf_ops because of python 2 usage
find ./danesfield -type d \
    -not -name __pycache__ \
    -not -path "./danesfield/geon_fitting/tf_ops*" \
    | tr '\n' ',' | \
    coverage run --source $(</dev/stdin) -m pytest ./tests

coverage html # generate htmlcov report
echo "*" > ./htmlcov/.gitignore # ignore htmlcov directory in git
coverage report
