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

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Flask Development Server Help')
    parser.add_argument("-d", "--debug", action="store_true", dest="debug",
                        help="debug in IDE (PyCharm)", default=False)
    parser.add_argument("-p", "--port", dest="port",
                        help="port of server (default:%(default)s)", type=int, default=5000)

    args = parser.parse_args()
    runtime_options = {"port": args.port}
    if args.debug:
        runtime_options["debug"] = True
        runtime_options["use_debugger"] = False
        runtime_options["use_reloader"] = False

    from helper.app import load_app
    app = load_app()
    # It's worth pointing out that there's masses of indirection and complexity with the configuration here:
    # 1. load_app fetches the (a) correct module which (b) imports its dependencies and (c) configures an app.
    # 2. The app is configured based on a config.py first and then the environment can be used to override this.
    # 3. Finally we may override the config again with some command line options -- mainly for handling IDE debugging.
    app.run(**runtime_options)