#!/bin/bash

function create() {
    cd $PROJECT_PATH/automate_creating_projects
    python create.py $1
    cd $PROJECT_PATH/$1

    git init
    git remote add origin https://github.com/junchoi0408/$1.git
    touch README.md
    touch .gitignore
    git add .
    git commit -m "Initial commit"
    git push origin master
    code .
} 