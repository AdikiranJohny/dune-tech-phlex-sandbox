#!/usr/bin/env bash
# Check that a pull request follows the sandbox rules in WORKSHOP.md.
# Usage: check-contribution.sh <base-commit> <head-commit> <github-username>
set -u

base=$1
head=$2
author=$3
folder="contributions/${author}/"
failed=0

fail() { echo "::error::$1"; failed=1; }
warn() { echo "::warning::$1"; }

mapfile -t files < <(git diff --name-only "$base" "$head")
echo "Files changed in this pull request:"
printf '  %s\n' "${files[@]}"

for f in "${files[@]}"; do
  # GitHub usernames are case-insensitive, so compare in lower case
  if [[ "${f,,}" != "${folder,,}"* ]]; then
    fail "$f is outside your folder ($folder). Only change files in your own folder."
  fi
  case "$f" in
    *CMakeCache.txt | *CMakeFiles/* | *.so | *.o | *.root | build/* | */build/*)
      fail "$f looks like a build product or job output. These are made from the source, so they never go in git." ;;
    *NOTES.md | *notes.md | *notes.txt)
      warn "$f looks like personal notes. Is it meant for other people to read?" ;;
  esac
done

if ! git ls-tree -r --name-only "$head" contributions/ | grep -qix "${folder}README.md"; then
  fail "There is no ${folder}README.md. Say what your work does and how to run it."
fi

if (( failed )); then
  echo "Some checks failed. Read the messages above, fix them in your branch, and push again."
  exit 1
fi
echo "All checks passed."
