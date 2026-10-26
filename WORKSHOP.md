# Phlex India workshop sandbox

This repository is a practice space for the DUNE Phlex workshop at IISc Bengaluru
(October 26–30, 2026). You can't break anything here. Fork it, push to it, open pull
requests and review each other's work.

**This is not the official repository.** The example code lives in `phlex-examples/`, a git
submodule that points at the
[`phlex-v0.4` branch of Framework-R-D/phlex-examples](https://github.com/Framework-R-D/phlex-examples/tree/phlex-v0.4)
(commit `c55bbfc`). It is unchanged and read-only for you: commits there can't be pushed, and a
pull request that moves the submodule fails the contribution check. This repository adds:

- `CMakeLists.txt`, which builds the C++ add example from `phlex-examples/`, plus `contributions/`
  (it is the official `CMakeLists.txt` with the source paths changed, and without the unfold and
  GausHitFinder parts)
- `cmake-warmup/`, a small CMake practice project
- `README.md`, `WORKSHOP.md` (this file) and `contributions/`, where each participant adds their own work
- `.github/pull_request_template.md` and a small contribution check that runs on pull requests

Please don't open pull requests from here to Framework-R-D. The `CMakeLists.txt` is a modified copy
of the official one; its copyright and license are in `NOTICE` and `LICENSE` (Apache-2.0).

## The rules

1. Only change files inside **your own** folder, `contributions/<your-github-username>/`.
2. Never push to `main`. Every change goes through a pull request.
3. Every pull request needs **one approving review** from another participant before an
   instructor merges it.
4. Don't commit build products (`build/`, `CMakeCache.txt`, `*.so`, `*.root`) or personal notes.

See [`contributions/README.md`](contributions/README.md) for the step-by-step guide and the
review checklist.
