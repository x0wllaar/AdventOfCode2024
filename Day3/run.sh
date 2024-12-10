#!/bin/bash
set -euo pipefail

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "$SCRIPT_DIR"

echo -n "Day 3 Part 1: "
cat input | grep -oP 'mul\([0-9]{1,3},[0-9]{1,3}\)' | python exec.py 

echo -n "Day 3 Part 2: "
cat input | grep -oP "mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)" | python exec.py 
