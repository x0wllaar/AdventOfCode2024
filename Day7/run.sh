#!/bin/bash
set -euo pipefail

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "$SCRIPT_DIR"

echo -n "Day 7 Part 1: "
cat input1 | python filter.py | python sum.py

echo -n "Day 7 Part 2: "
cat input1 | python filter2.py | python sum.py