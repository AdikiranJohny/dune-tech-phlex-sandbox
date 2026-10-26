# CMake warm-up

One library (`greet`) and one program (`hello`) that uses it. Build it next to the repository,
never inside it:

```bash
mkdir -p ~/phlex-work/build-warmup
cd ~/phlex-work/build-warmup
cmake ../phlex-india-sandbox/cmake-warmup   # configure
cmake --build .                             # build
./hello
```

This project is separate from the Phlex examples: the top-level `CMakeLists.txt` doesn't build it.
Edits you make here are for practice. Undo them with `git restore cmake-warmup` before you commit.
