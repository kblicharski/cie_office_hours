#!/bin/bash
MAX_LINE_LENGTH=100
EXCLUDED=.git,*.pyc,**migrations**

autopep8 -ir -j 0 -p 1000 -a --exclude ${EXCLUDED} --max-line-length ${MAX_LINE_LENGTH} .
isort -rc --atomic .
flake8 && pytest