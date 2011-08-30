import sys, os
cwd          = os.getcwd()
modules      = cwd + "/modules/" 
activate_env = cwd + "/env/bin/activate_this.py"

sys.path.append(modules)
execfile(activate_env, dict(__file__ = activate_env))

from mu import app as application
