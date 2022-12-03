#!/bin/sh
cp -r day01 day$1
cd day$1
mv d01.py d$1.py
mv d01.in d$1.in
day=$(echo $1 | sed 's/^0//')
curl "https://adventofcode.com/2022/day/${day}/input" -s -H "cookie: session=$AOC2022SID" > d$1.in
echo > problem.md
git add d$1.in problem.md
git commit -am "Day $1"
