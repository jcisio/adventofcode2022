#!/bin/sh
# This script was only tested in Mac OS X. It uses BSD tools, not GNU.
mkdir day$1
cd day$1
day=$(echo $1 | sed 's/^0//')
base_url="https://adventofcode.com/2022/day/${day}"
cookies="cookie: session=$AOC2022SID"
curl $base_url -s -H $cookies | pandoc -f html -t plain | sed -n '/^--- Day/,$p' > tmp

# Include only a link to the puzzle text
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/puzzle_texts/
echo '"""' > d$1.py
echo 'Advent Of Code' >> d$1.py
cat tmp| sed -n 1p >> d$1.py
echo $base_url >> d$1.py
echo '"""' >> d$1.py
git add d$1.py

# Try to guess the example input.
cat tmp | sed -n '/^    /,$p' | sed -n '1,/^$/p' | sed 's/    //' > d$1.in
git add d$1.in

# Write real input in a test file, do not commit it.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
curl $base_url"/input" -s -H $cookies > d$1.test

git commit -m "Day $1"
cat ../template.py >> d$1.py
rm tmp
