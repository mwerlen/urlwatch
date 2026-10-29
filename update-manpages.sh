#!/bin/sh
# Update man pages from source
# 2022-03-15 Thomas Perl

VERSION=$(python3 setup.py --version)

set -e

make -C docs clean man
cp -rpv docs/build/man/man? share/man/

for filename in share/man/man?/*.?; do
    # Portable in-place edit (GNU and BSD sed disagree on sed -i).
    tmp=$(mktemp)
    sed -e 's/.TH "\(URLWATCH[^"]*\)" "\([0-9]*\)" "\([^"]*\)" "" "\([^"]*\)"/.TH "\1" "\2" "\3" "urlwatch '"$VERSION"'" "urlwatch '"$VERSION"' Documentation"/g' \
        "$filename" > "$tmp"
    mv "$tmp" "$filename"
    diff -u "docs/build/${filename#share/}" "$filename" || true
done
