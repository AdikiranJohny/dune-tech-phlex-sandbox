# Phlex India workshop sandbox

This repository is a practice space for the DUNE Phlex workshop at IISc Bengaluru
(October 26–30, 2026). You can't break anything here. Fork it, push to it, open pull
requests and review each other's work.

**This is a modified, trimmed copy, not the official repository.** It started from the
[`phlex-v0.4` branch of Framework-R-D/phlex-examples](https://github.com/Framework-R-D/phlex-examples/tree/phlex-v0.4)
(commit `c55bbfc`). Changes:

- kept only the C++ and Python add/subtract examples and the files they need
- left out the unfold example, `migration/` (GausHitFinder), `openspec/`, `scripts/` and the
  linting configuration
- rewrote `README.md` for the workshop
- added `cmake-warmup/`, a small CMake practice project
- added `WORKSHOP.md` (this file) and `contributions/`, where each participant adds their own work
- added `.github/pull_request_template.md` and a small contribution check that runs on pull requests
- added one line at the end of `CMakeLists.txt` that builds the `contributions/` directory

Please don't open pull requests from here to Framework-R-D. The original copyright and license
are in `NOTICE` and `LICENSE` (Apache-2.0). When you're ready for the full set of examples, go to
the [official repository](https://github.com/Framework-R-D/phlex-examples).

## The rules

1. Only change files inside **your own** folder, `contributions/<your-github-username>/`.
2. Never push to `main`. Every change goes through a pull request.
3. Every pull request needs **one approving review** from another participant before an
   instructor merges it.
4. Don't commit build products (`build/`, `CMakeCache.txt`, `*.so`, `*.root`) or personal notes.

See [`contributions/README.md`](contributions/README.md) for the step-by-step guide and the
review checklist.
