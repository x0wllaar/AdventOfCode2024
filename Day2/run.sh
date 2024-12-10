#!/bin/bash
set -euo pipefail

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "$SCRIPT_DIR"

echo -n "Day 2 Part 1: "
cat input | python part1.py | wc -l

echo -n "Day 2 Part 2: "
cat input | python part2.py | wc -l