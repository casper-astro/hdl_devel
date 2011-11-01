Casper Toolflow Development Libraries
=====================================

The [CASPER](http://casper.berkeley.edu) open-source astronomy 
instrumentation group is moving away from the Matlab/Simulink 
hardware design environment and towards a cheaper, friendly, 
and more stable Python/Verilog based approach. 

Dependencies
============

Python >=2.7 and the [MyHDL >= 0.7](http://www.myhdl.org) package 
are required for simulation and for running the test-benches. 

In addition, if you are co-simulating the Verilog primitives 
you will need Icarus Verilog and the MyHDL source code to build 
the VPI file needed for co-simulation. After extracting the MyHDL 
source point the MYHDL environment variable to the root of the 
source and build the VPI file similar to below:

```bash
$ export MYHDL=/path/to/myhdl
$ cd $MYHDL/cosimulation/icarus/  
$ make
```

Of course, this assumes you have build-essentials or your system's 
equivalent package. Note: the co-simulating test-benches currently 
use the MYHDL environment variable to locate the VPI file so please 
add the first line above to your shell's init script.
