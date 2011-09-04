import sys, os
cwd = os.getcwd()

# Activate the correct Python virtualenv.
activate_env = cwd + "/env/bin/activate_this.py"
execfile(activate_env, dict(__file__ = activate_env))

# Insert the modules directory into the sys.path ONLY if it DOES NOT exist
# there already.
modules = cwd + "/modules/" 
if modules not in sys.path:
    sys.path.append(modules)

# The source code monitor utility automatically detects changes and triggers
# process restarts to make development seamless.
from utility import monitor
monitor.start(interval=1.0)
for directory, dirnames, filenames in os.walk(modules):
    # We will only track changes that happen to files that end in .py or .html
    for filename in filenames:
        if not ".swp" and (".py" or ".html") in filename:
            monitor.track(directory + "/" + filename)

# Load entry point of application
from helper.startup import get_app
application = get_app()
