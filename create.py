import sys
import os 
from github import Github

project_path = os.environ.get('PROJECT_PATH')
username = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')

filename = sys.argv[1]

def create_new_project():
    os.chdir(project_path)
    os.makedirs(filename)

def create_repo():
    g=Github(username, password)
    g.get_user().create_repo(filename)


if __name__ == "__main__":
    create_new_project()
    create_repo()
