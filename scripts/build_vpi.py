"""
Use this to download and build the 'myhdl.vpi' file.
"""

import os
import urllib
import shutil
import shlex
import tarfile
import tempfile
import subprocess


MYHDL_SRC = "http://sourceforge.net/projects/myhdl/files/myhdl/0.7/myhdl-0.7.tar.gz/download"
TEMP_DIR = tempfile.mkdtemp()


tar_filename = os.path.join(TEMP_DIR, 'myhdl-0.7.tar.gz')
print "Downloading MyHDL source to a temporary directory..."
urllib.urlretrieve(MYHDL_SRC, tar_filename)
tar = tarfile.open(tar_filename, 'r:gz')


print "Extracting only the necessary files..."
tar_prefix = os.path.join('myhdl-0.7', 'cosimulation', 'icarus')
files = ['myhdl.c', 'myhdl_table.c']
for name in files:
    with open(os.path.join(TEMP_DIR, name), 'w') as file_obj:
        file_obj.write(tar.extractfile(os.path.join(tar_prefix, name)).read())


print "Compiling myhdl.vpi using Icarus Verilog..."
temp_files = tuple(os.path.join(TEMP_DIR, name) for name in files)
proc = subprocess.Popen(shlex.split('iverilog-vpi ' + ' '.join(temp_files)),
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        cwd=TEMP_DIR)
if proc.wait():
    raise RuntimeError("Could not compile myhdl.vpi. Are you sure you have Icarus installed?")


print "Copying myhdl.vpi to current directory..."
shutil.copyfile(os.path.join(TEMP_DIR, 'myhdl.vpi'), os.path.join(os.getcwd(), 'myhdl.vpi'))


print "Destroying the evidence... ",
shutil.rmtree(TEMP_DIR)
