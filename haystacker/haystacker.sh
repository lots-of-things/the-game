#!/bin/bash
for i in {1..865}
do
    awk -v a="$i" '!(NR==a)' books.txt > haystack.txt
    git add haystack.txt
    git commit -m "books to research"
done
cp books.txt haystack.txt
git add haystack.txt
git commit -m "books to research"