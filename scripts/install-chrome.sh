#!/bin/bash
set -Eeuo pipefail
trap "echo -e \"\033[1;31m[!] \e[0m Script error occured.\"" ERR

GREEN="\033[1;32m"
ENDCOLOR="\e[0m"

# === Exit without proceeding if run in WSL ===
if [ -f /mnt/c/Windows/System32/wsl.exe ]; then
    exit 0
fi

# Check if Chrome is installed
if [ $(sudo dpkg-query -W -f='${Status}' google-chrome-stable 2>/dev/null | grep -c "ok installed") -eq 0 ]
then
    echo -ne $GREEN"[+] "$ENDCOLOR; echo "Installing Google Chrome"
    sudo apt install -y libappindicator3-1
    cd ~
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_arm64.deb
    sudo dpkg -i google-chrome-stable_current_arm64.deb
    rm -rf google-chrome-stable_current_arm64.deb
fi

# Updates are handled by the APT repository chrome installs.
