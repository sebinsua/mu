#!/usr/bin/env python

import sys, os

cwd = os.getcwd()

# Activate the correct Python virtualenv.
activate_env = cwd + "/env/bin/activate_this.py"
execfile(activate_env, dict(__file__=activate_env))

# Insert the modules directory into the sys.path ONLY if it DOES NOT exist
# there already.
modules = cwd + "/modules/"
if modules not in sys.path:
    sys.path.append(modules)

from helper.app import get_tests

if __name__ == "__main__":
    tests = get_tests()
    tests.run()
