# FFXE

## Dynamic Control Flow Graph Recovery for Embedded Firmware Binaries

This repository contains the artifacts for the paper **FFXE: Dynamic Control Flow Graph Recovery for Embedded Firmware Binaries**, which presents a novel technique for resolving indirect branches dependent on asynchronous writes (callback functions) that is based on dynamic forced execution.

Our implementation of the Forced Firmware Execution Engine can be found in the file `ffxe.py`, and a reimplementation of the original Forced Execution Engine by Xu et al. can be found in `fxe.py`. 

## Setup

The dependencies can be installed in a conda environment using the provided `environment.yml` file.

After activating the environment, the engine must be installed via pip in developer mode with `pip install -e .` from the project root directory. 

## Duplicating FFXE Experiments

FFXE can be invoked on all samples in our unit test set by invoking the command

```console
$ python tests/test-unit.py
```
This will generate basic CFGs in python pickled format for all firmware images with a `.bin` extension in the `examples/unit-tests` folder.

The results can be visualized using another script `visual_cfg.py`, which is meant for correctness checking and therefore maps the generated cfgs onto the unstripped elf firmware binary.

```console
$ python scripts/visual_cfg.py
```
This will write rough CFGs in the form of annotated disassembly to the folder `scripts/cfgs`. 

### Testing Real World Samples

FFXE can be invoked on our real-world test set by invoking the command

```console
$ python tests/test-real.py
```
This will generate basic CFGs in python pickled format for each real-world sample directory in the `examples/real-world` folder.

The resulting CFG cannot be visualized directly using the `visual_cfg.py` script due to lack of ELF files for baseline disassembly accuracy; however, we have included scripts that allow for high-level visualization of coverage and coverage comparison in the `scripts` directory.

### Testing Other Recovery Methods

Our version of FXE can be invoked with the command
```console
$ python tests/fxe-all.py
```
This has the same behavior as `test-unit.py` except that it invokes FXE instead.

Running the other recovery methods is somewhat more involved as additional dependencies must be installed for our provided scripts to work. Moreover, other dependencies must be installed in different environments to avoid package conflicts. (There is a known conflict between the version of Unicorn we use, and the version that angr uses)

The script `scripts/angr-analyze.py` will run angr's static and emulated recovery methods on all `.bin` images in the `examples/unit-tests` folder, but must be run from an environment that has angr installed.

The scripts `script/ghidra-analyze.py` requires a working installation of [Ghidrathon](https://github.com/mandiant/Ghidrathon) to work, for which we do not yet have a quick install method. We will try to upload a Dockerfile that contains a working version if time permits.

Scripts `scripts/angr-analyze-real.py` and `scripts/ghidra-analyze-real.py` can be used for analyzing the real-world set but have the same requirements as already stipulated.

## Other Scripts

Other scripts are used to tabulate results and generate images for our paper. The `tabulate-` scripts can be invoked in the same environment as FFXE. However, the `visualize-` scripts require matplotlib, which is not installed in the FFXE environment by default.
