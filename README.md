# Phlex India workshop sandbox

> [!NOTE]
> **This is a workshop practice repository, not the official one.** It was made for the DUNE
> Phlex workshop at IISc Bengaluru (October 2026). The example code is the official
> [Framework-R-D/phlex-examples](https://github.com/Framework-R-D/phlex-examples), included as a
> git submodule in `phlex-examples/` at the `phlex-v0.4` branch (commit `c55bbfc`). You can read
> and build it, but you can't push to it. See [WORKSHOP.md](WORKSHOP.md) for the rules for
> pushing here.

## What's here

| File | What it is |
|---|---|
| `cmake-warmup/` | A tiny C++ project to practise CMake on, before Phlex |
| `phlex-examples/` | The official examples (a submodule, read-only). Today we build the files below from it |
| `my_add.cpp`, `my_geometry.cpp` | "Experiment code": ordinary C++ that knows nothing about Phlex (SHARED libraries) |
| `numbers_source.cpp`, `geometry_source.cpp` | **Providers**: bring data into the job |
| `add_and_verify.cpp` | A **transform** (adds two numbers) and an **observer** (checks the answer) |
| `subtract.py` | A transform written in Python |
| `test-cpp-workflow.jsonnet`, `test-py-workflow.jsonnet` | Job configurations |
| `contributions/` | Where workshop participants add their own work |

## Get the code

Clone with `--recurse-submodules`, or `phlex-examples/` will be empty:

```bash
git clone --recurse-submodules https://github.com/<you>/dune-tech-phlex-sandbox.git
```

If you already cloned without it, run `git submodule update --init` inside the repository.

## Build

From the directory that contains this repository (the build directory sits next to it):

```bash
mkdir build-sandbox
cd build-sandbox
cmake ../dune-tech-phlex-sandbox
cmake --build . -j 4
```

## Run

From the build directory:

```bash
export PHLEX_PLUGIN_PATH=${PWD}:${PHLEX_PLUGIN_PATH}
phlex -c ../dune-tech-phlex-sandbox/phlex-examples/test-cpp-workflow.jsonnet --stage examples
```

The end of the output should show:

```console
Processed layers:

  job
   │
   └ spill: 10
```

For the Python algorithm:

```bash
export PYTHONPATH=$(realpath ../dune-tech-phlex-sandbox/phlex-examples):${PYTHONPATH}
phlex -c ../dune-tech-phlex-sandbox/phlex-examples/test-py-workflow.jsonnet --stage examples
```

`--stage` names the processing pass. Current Phlex releases require it.

## Where to go next

Everything else in `phlex-examples/` is worth reading: an unfold example and the GausHitFinder
migration from LArSoft in four designs with tests. The official repository also has a branch for
each Phlex release (`phlex-v0.3`, `phlex-v0.4`, …).

To work on it for real after the workshop, clone the official repository on the branch that matches
your `phlex --version`:

```bash
git clone -b phlex-v0.4 https://github.com/Framework-R-D/phlex-examples.git
```
