import os
import subprocess
import sys

PIP_PRE_INSTALL = os.environ.get('PIP_PRE_INSTALL', None)

if PIP_PRE_INSTALL:
    PIP_PRE_INSTALL = PIP_PRE_INSTALL.split(',')
    subprocess.check_call(['pip', 'install'] + PIP_PRE_INSTALL)

sys.exit(subprocess.check_call(
    ["jupyter", "notebook", "--notebook-dir", "/workdir"] + sys.argv[1:],
))
