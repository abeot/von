#!/bin/bash

set -e

readarray -t SPELL_FILES_ARRAY < <(git ls-files)
codespell "${SPELL_FILES_ARRAY[@]}"

pyright .
pyflakes .

readarray -t PY_FILES_ARRAY < <(git ls-files '*.py')
yapf -d "${PY_FILES_ARRAY[@]}"