#! /bin/bash

set -e

pip-compile --emit-index-url --header --emit-trusted-host -qo .misc/requirements/dev.txt .misc/requirements/base.in .misc/requirements/dev.in .misc/requirements/test.in
pip-compile --emit-index-url --header --emit-trusted-host -qo .misc/requirements/test.txt .misc/requirements/base.in .misc/requirements/dev.in .misc/requirements/test.in
pip-compile --emit-index-url --header --emit-trusted-host -qo .misc/requirements/base.txt .misc/requirements/base.in
