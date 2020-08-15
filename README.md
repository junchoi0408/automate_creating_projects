# Automate_Creating_Projects

Automate Creating Projects automates the process of creating a project.
The process includes: 
* Creating a folder 
* Creating a repository
* git init, add, commit, remote add, push

## USAGE
***
Typing the following code in cmd will create a folder and repository on Github.
```bash
create '<foldername>'
```

## SETUP / REQUIREMENTS
***
required imports - os, sys, github

After creating .create_command.sh, type 
```bash
cd
code .bashrc
``` 
then in the following file, add 
```bash
source ~/{the path to .create_command.sh}/.create_command.sh
```
to run the function created in the file

## FAQ
***
1. What is $PROJECT_PATH?

The $PROJECT_PATH is the path I added in Envrionment Variable so that I can navigate and create repos in my project folder.


2. What are EMAIL and PASSWORD in create.py?

These are also stored in the Envrionment Varibles to make sure I don't share my Github account information.

3. Are there other ways to store and retrieve sensitive information?

.ENV file also works.

## CONTACT
***
Email: junchoi0408@gmail.com

