Casper Toolflow Development Libraries
=====================================

The [CASPER](http://casper.berkeley.edu) open-source astronomy 
instrumentation group is moving away from the Matlab/Simulink 
hardware design environment and towards a cheaper, friendly, 
and more stable Python/Verilog based approach. 

Installation
============

Python >=2.7 and the [MyHDL >= 0.7](http://www.myhdl.org) package 
are required for simulation and for running the test-benches. If 
you have setuptools installed you can simply run the following 
within the packages root directory:

```bash
$ python setup.py install
```

and it should process the dependencies for you (unless you plan 
to use co-simulation or run unit tests, if that's the case see the 
Co-simulation section below).

Co-simulation
=============

If you plan to use MyHDL co-simulation you will need Icarus Verilog 
and the MyHDL VPI file. This requires the MyHDL source code to build. 
For convenience please use the build_vpi.py script to download and 
build this file automatically (you will need Icarus installed):

```bash
$ python scripts/build_vpi.py # generates myhdl.vpi
$ export MYHDL=/path/to/hdl_devel/myhdl.py
```

Note: the co-simulating test-benches currently require the presence 
of the MYHDL environment variable to locate the VPI file so please 
add the last line above to your shell's init script.

Testing
=======

The unit tests run on both the Python/MyHDL models and the Verilog 
primitives via co-simulation, so if you'd like to run them you will 
need to set up the co-simulation environment (see above). Once you've 
done that you can run all tests using:

```bash
$ python setup.py test # add -q to make this quieter
```

If you've explicitely installed 'nose' before (e.g. by using easy_install) 
you should be able to run 'nosetests' from anywhere in the package to 
recursively run unit tests.

Developers
==========

If you'd like to develop primitives or any other block please fork 
the main repository to your local Github, checkout a working copy, 
and use the 'develop' command provided by setuptools:

```bash
$ python setup.py develop
```

This points Python to your local copy for use when importing the 
package and removes the need to constantly 'install' upon making 
local changes.