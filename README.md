# Phlex starter: a trimmed copy of phlex-examples

> [!NOTE]
> **This is a workshop practice copy, not the official repository.** It was made for the DUNE
> Phlex workshop at IISc Bengaluru (October 2026) from the `phlex-v0.4` branch of
> [Framework-R-D/phlex-examples](https://github.com/Framework-R-D/phlex-examples), commit
> `c55bbfc`, and cut down to the smallest set of files that builds and runs. For real work, use
> the official repository. See [WORKSHOP.md](WORKSHOP.md) for what changed and the rules for
> pushing here.

## What's here

| File | What it is |
|---|---|
| `cmake-warmup/` | A tiny C++ project to practise CMake on, before Phlex |
| `my_add.cpp`, `my_geometry.cpp` | "Experiment code": ordinary C++ that knows nothing about Phlex (SHARED libraries) |
| `numbers_source.cpp`, `geometry_source.cpp` | **Providers**: bring data into the job |
| `add_and_verify.cpp` | A **transform** (adds two numbers) and an **observer** (checks the answer) |
| `subtract.py` | A transform written in Python |
| `test-cpp-workflow.jsonnet`, `test-py-workflow.jsonnet` | Job configurations |
| `contributions/` | Where workshop participants add their own work |

## Build

From the directory that contains this repository (the build directory sits next to it):

```bash
mkdir build-sandbox
cd build-sandbox
cmake ../phlex-india-sandbox
cmake --build . -j 4
```

## Run

From the build directory:

```bash
export PHLEX_PLUGIN_PATH=${PWD}:${PHLEX_PLUGIN_PATH}
phlex -c ../phlex-india-sandbox/test-cpp-workflow.jsonnet --stage examples
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
export PYTHONPATH=$(realpath ../phlex-india-sandbox):${PYTHONPATH}
phlex -c ../phlex-india-sandbox/test-py-workflow.jsonnet --stage examples
```

`--stage` names the processing pass. Current Phlex releases require it.

## Where to go next

The [official phlex-examples](https://github.com/Framework-R-D/phlex-examples) has much more:
an unfold example, the GausHitFinder migration from LArSoft in four designs with tests, and
branches that match each Phlex release (`phlex-v0.3`, `phlex-v0.4`, …). Clone the branch that
matches your `phlex --version`:

```bash
git clone -b phlex-v0.4 https://github.com/Framework-R-D/phlex-examples.git
```
