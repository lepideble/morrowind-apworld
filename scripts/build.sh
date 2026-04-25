#!/bin/sh

set -e

cd $(dirname $(dirname $0))

# Create build folders
mkdir --parents build output

# Remove old builds
rm --force --recursive "build/morrowind"
rm --force "output/morrowind.apworld"

# Build
cp --recursive world build/morrowind

# Create .apworld
(cd build && zip --recurse-paths "../output/morrowind.apworld" "morrowind" --exclude \*__pycache__\*)