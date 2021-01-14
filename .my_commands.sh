#!/bin/bash

# a bash command that will take a folder name as input, call a Python script and initialize
# a local git repository.
function create() {
    cd
    python create.py $1
    cd C:/Users/kevin/Documents/projects/$1
    git init
    touch README.md
    git remote add origin https://github.com/kevinw567/$1.git
    
    git add .
    git commit -m "Initial Commit"
    git push origin master
    code .
}