#!/usr/bin/env python3
import os
import sys
import subprocess
import string
from datetime import datetime

def print_message(color, message):
    """ Prints a formatted message to the console """
    if   color == "green":  print("\033[1;32m[+] \033[0;37m" + datetime.now().strftime("%H:%M:%S") + " - " + message)
    elif color == "blue":   print("\033[1;34m[i] \033[0;37m" + datetime.now().strftime("%H:%M:%S") + " - " + message)
    elif color == "yellow": print("\033[0;33m[<] \033[0;37m" + datetime.now().strftime("%H:%M:%S") + " - " + message, end="")
    elif color == "red":    print("\033[1;31m[-] \033[0;37m" + datetime.now().strftime("%H:%M:%S") + " - " + message)
    elif color == "error":  print("\033[1;31m[!] \033[0;37m" + datetime.now().strftime("%H:%M:%S") + " - " + message)
    else:                   print("\033[0;41mInvalid Format\033[0;37m " + datetime.now().strftime("%H:%M:%S") + " " + message)

def elevate_privileges():
    """ Gets sudo privileges and returns the current date """
    status = os.system("sudo date; echo")
    return status

def take_ownership(directory):
    #username = os.path.expanduser("~").split('/')[3]
    username = "parallels"
    cmdstring = "sudo chown " + username + ":" + username + " " + directory
    os.system(cmdstring)

def update_packages():
    """ Do a general update of the system packages """
    cmdseries = ['sudo apt update',
                 'sudo apt full-upgrade -y',
                 'sudo apt autoremove -y']
    for cmdstring in cmdseries:
        os.system(cmdstring)

def install_package(package, apt_cache):
    """ Installs a package using apt """
    if not apt_cache[package].is_installed:
        print_message("green", "Installing " + package)
        cmdstring = "sudo apt install -y " + package
        os.system(cmdstring)

def remove_package(package, apt_cache):
    """ Removes a package using apt """
    if apt_cache[package].is_installed:
        print_message("red", "Removing " + package)
        cmdstring = "sudo apt remove -y " + package
        os.system(cmdstring)

def pip_package_install(pip_packages, installed_pip_packages):
    """ Install python pip package """
    for package in pip_packages:
        if not package in installed_pip_packages:
            print_message("green", "Installing pip package " + package)
            cmdstring = "python3 -m pip install --upgrade " + package
            os.system(cmdstring)

def update_pip_packages():
    """ Update pip packages """
    cmdstring = "pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U 2>/dev/null; break"
    os.system(cmdstring)

def gem_package_install(gem_packages, installed_gem_packages):
    """ Install Ruby gem package """
    for package in gem_packages:
        if not package in installed_gem_packages:
            print_message("green", "Installing gem package " + package)
            cmdstring = "sudo gem install " + package
            os.system(cmdstring)

def update_gems():
    """ Update gem packages """
    cmdstring = "gem outdated >/dev/null; gem update"
    os.system(cmdstring)

def install_golang_module(module, golang_install_directory):
    """ Install the specified Golang module """
    modulename = module.split("/")[-1].lower()
    if not os.path.exists(golang_install_directory + "/" + modulename):
        print_message("green", "Installing go module " + modulename)
        cmdseries = ["go install " + module + "@latest",
                     "sudo ln -s " + golang_install_directory + "/" + modulename + "/bin/" +
                     modulename + " /usr/local/bin/" + modulename]
        os.environ["GOPATH"] = golang_install_directory + "/" + modulename
        for cmdstring in cmdseries:
            os.system(cmdstring)

def update_go_packages(golang_modules_to_install, golang_install_directory):
    ''' Rebuild all Go modules '''
    print_message("green", "Rebuilding Go modules")
    for modulename in golang_modules_to_install:
        module = modulename.split("/")[-1].lower()
        os.environ["GOPATH"] = golang_install_directory + "/" + module
        cmdstring = "go install " + modulename + "@latest"
        os.system(cmdstring)

def create_directory(directory):
    """ Checks if the specified directory exists, and creates it if not """
    if not os.path.exists(directory):
        print_message("green", "Creating directory: " + directory)
        cmdstring = "mkdir " + directory
        os.system(cmdstring)

def remove_directory(directory):
    """ Checks if the specified directory exists, and deletes it if it does """
    directory = os.getenv("HOME") + '/' + directory
    if os.path.exists(directory):
        print_message("red", "Removing directory: " + directory)
        cmdstring = "rmdir " + directory
        os.system(cmdstring)

#def sync_git_repo(gitrepo, repo_collection_dir):
#    """ Sync the specified git repository """
#    repo_name = gitrepo.split("/")[-1].lower()
#    if os.path.exists(repo_collection_dir + '/' + repo_name):
#        print_message("yellow", "Syncing " + repo_name + ": ")
#        sys.stdout.flush()
#        cmdstring = "git -C " + repo_collection_dir + '/' + repo_name + " pull"
#        os.system(cmdstring)
#    else:
#        print_message("green", "Cloning " + repo_name)
#        cmdstring = "git clone " + gitrepo + ' ' + repo_collection_dir + '/' + repo_name
#        os.system(cmdstring)


import zipfile
import tarfile

def sync_git_repo(gitrepo, repo_collection_dir):
    """ Sync the specified git repository, download individual releases and extract ZIP and .tar.gz files """
    repo_name = gitrepo.split("/")[-1].lower()
    
    # Check if it's a release URL
    if "releases/download" in gitrepo:
        git_name = gitrepo.split("/")[4]  # Extract the git name from the URL
        release_name = gitrepo.split("/")[-1]
        release_folder = os.path.join(repo_collection_dir, git_name)  # Create a folder named after the git name
        
        # Create the folder if it doesn't exist
        if not os.path.exists(release_folder):
            os.makedirs(release_folder)
        
        # Check if the release already exists
        full_release_path = os.path.join(release_folder, release_name)
        if os.path.exists(full_release_path):
            print_message("blue", f"Release {release_name} already exists in {release_folder}. Skipping.")
            return
        
        print_message("green", f"Downloading release {release_name} into {release_folder}")
        cmdstring = f"wget {gitrepo} -O {full_release_path}"
        os.system(cmdstring)
        
        # Extract ZIP files
        if release_name.endswith('.zip'):
            try:
                print_message("green", f"Extracting ZIP file {release_name}")
                with zipfile.ZipFile(full_release_path, 'r') as zip_ref:
                    zip_ref.extractall(release_folder)
            except zipfile.BadZipFile:
                print_message("error", f"{release_name} is not a valid ZIP file.")
        
        # Extract .tar.gz files
        elif release_name.endswith('.tar.gz'):
            try:
                print_message("green", f"Extracting .tar.gz file {release_name}")
                with tarfile.open(full_release_path, 'r:gz') as tar_ref:
                    tar_ref.extractall(path=release_folder)
            except tarfile.ReadError:
                print_message("error", f"{release_name} is not a valid .tar.gz file.")
        return
    
    # Otherwise, it's a git repo
    if os.path.exists(repo_collection_dir + '/' + repo_name):
        print_message("yellow", "Syncing " + repo_name + ": ")
        sys.stdout.flush()
        cmdstring = "git -C " + repo_collection_dir + '/' + repo_name + " pull"
        os.system(cmdstring)
    else:
        print_message("green", "Cloning " + repo_name)
        cmdstring = "git clone " + gitrepo + ' ' + repo_collection_dir + '/' + repo_name
        os.system(cmdstring)


def run_scripts():
    """ Run each .sh or .py file in the scripts directory """
    script_directory = os.path.dirname(os.path.realpath(__file__)) + '/scripts'

    if os.path.exists(script_directory):
        scripts = sorted(os.listdir(script_directory))
        for script in scripts:
            if '.sh' or '.py' in script:
                cmdstring = script_directory + '/' + script
                os.system(cmdstring)
    else:
        print_message("error", "'scripts' directory is missing")
