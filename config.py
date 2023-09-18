import os
import subprocess

''' This file defines what the update-kali script should do. '''

# Determine release, and whether we are on Windows Subsystem for Linux (WSL) so that we can set
# different settings for different environments. Anything common can go outside the if statements.

release = subprocess.check_output("""sh -c '. /etc/os-release; echo "$NAME"'""", shell=True,
    universal_newlines=True).strip()
are_we_on_wsl = os.path.exists("/mnt/c/Windows/System32/wsl.exe")


if 'Kali' in release:
    # These directories will be removed from your home directory
    directories_to_remove = ['Documents', 'Music', 'Pictures', 'Public', 'Templates', 'Videos']

    # These kali packages will be installed
    packages_to_install = ['most', 'ttf-mscorefonts-installer', 'gobuster', 'amass',
                           'golang', 'exif', 'hexedit', 'jq', 'curl', 'filezilla', 'net-tools',
                           'tmux', 'bash-completion', 'ieee-data', 'powercat', 'cewl', 'nbtscan', 
                           'tree', 'grc', 'passing-the-hash', 'evil-winrm', 'mimikatz', 
                           'feroxbuster', 'ffuf', 'bloodhound', 'hashdeep', 'freerdp2-dev',
                           'crackmapexec', 'creddump7', 'hping3', 'dos2unix', 'dotdotpwn', 'impacket-scripts',
                           'nishang', 'onesixtyone', 'kerberoast', 'patator', 'powersploit',
                           'powershell-empire', 'pwncat', 'python3-pip', 'python3-virtualenv', 'rdesktop',
                           'seclists', 'secure-socket-funneling-windows-binaries', 'sherlock', 'smbmap',
                           'snmpcheck', 'windows-privesc-check', 'rlwrap', 'whatweb', 'wpscan']

    # These kali packages will be removed
    packages_to_remove = []

    # These python packages will be installed globally
    pip_packages = ['pipenv', 'pylint', 'defaultcreds-cheat-sheet', 'wesng', 'certipy-ad', 'pycryptodomex', 'ldap3', 'pywerview', 'terminator', 
                    'pyperclip3', 'updog', 'pwnshelter', 'colorama', 'readchar', 'netifaces']

    # These gem packages will be installed globally
    gem_packages = []

    # These go tools will be installed globally. You will need to have the following settings in your
    # .bashrc already:
    #
    # export GOROOT=/usr/lib/go
    # export GOPATH=$HOME/go
    # export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
    
    golang_install_directory = '/opt'
    golang_modules_to_install = [
                                'github.com/lc/gau',
                                'github.com/ropnop/go-windapsearch',
                                'github.com/ropnop/kerbrute',
                                'github.com/CristinaSolana/ggtfobins'
                                ]

    # These git repositories will be synced to the 'external repo' directory
    external_tools_directory = '/opt'
    ext_repositories_to_sync =  [
                                'https://github.com/swisskyrepo/PayloadsAllTheThings',
                                'https://github.com/Hacking-Notes/VulnScan',
                                'https://github.com/p0dalirius/LDAPmonitor',
                                'https://github.com/GhostPack/Certify',
                                'https://github.com/GhostPack/SafetyKatz',
                                'https://github.com/GhostPack/Seatbelt',
                                'https://github.com/GhostPack/Rubeus',
                                'https://github.com/SnaffCon/Snaffler/releases/download/1.0.132/Snaffler.exe',
                                'https://github.com/p0dalirius/FindUncommonShares',
                                'https://github.com/ShutdownRepo/targetedKerberoast',
                                'https://github.com/shutdownrepo/pywhisker',
                                'https://github.com/topotam/PetitPotam',
                                'https://github.com/dirkjanm/PKINITtools',
                                'https://github.com/TH3xACE/SUDO_KILLER',
                                'https://github.com/cwinfosec/revshellgen',
                                'https://github.com/Tib3rius/windowsprivchecker',
                                'https://github.com/Tib3rius/creddump7',
                                'https://github.com/Tib3rius/Windows-PrivEsc-Tools',
                                'https://github.com/Tib3rius/Linux-PrivEsc-Tools',
                                'https://github.com/61106960/adPEAS',
                                'https://github.com/nicocha30/ligolo-ng/releases/download/v0.4.4/ligolo-ng_agent_0.4.4_windows_amd64.zip',
                                'https://github.com/nicocha30/ligolo-ng/releases/download/v0.4.4/ligolo-ng_agent_0.4.4_linux_amd64.tar.gz',
                                'https://github.com/cddmp/enum4linux-ng',
                                'https://github.com/Anon-Exploiter/SUID3NUM',
                                'https://github.com/The-Z-Labs/linux-exploit-suggester',
                                'https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy32',
                                'https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64',
                                'https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy32s',
                                'https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64s',
                                'https://github.com/faustinoaq/sswws/releases/download/v0.1.0/sswws.zip',
                                'https://github.com/RustScan/RustScan/archive/refs/tags/2.1.1.zip',
                                'https://github.com/Tib3rius/AutoRecon',
                                'https://github.com/Tib3rius/SemiAutoRecon',
                                'https://github.com/CMEPW/keepass-dump-masterkey',
                                'https://github.com/Orange-Cyberdefense/KeePwn',
                                'https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.5/LaZagne.exe',
                                'https://github.com/r3motecontrol/Ghostpack-CompiledBinaries/',
                                'https://github.com/n00py/LAPSDumper',
                                'https://github.com/Hackndo/lsassy',
                                'https://github.com/S3cur3Th1sSh1t/PowerSharpPack',
                                'https://github.com/PowerShellMafia/PowerSploit/blob/master/Privesc/PowerUp.ps1',
                                'https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1',
                                'https://github.com/aniqfakhrul/powerview.py',
                                'https://github.com/gtworek/Priv2Admin',
                                'https://github.com/byt3bl33d3r/pth-toolkit',
                                'https://github.com/antonioCoco/RunasCs',
                                'https://github.com/OPENCYBER-FR/RustHound',
                                'https://github.com/SpiderLabs/scavenger',
                                'https://github.com/eladshamir/Whisker',
                                'https://github.com/blankshiro/OSCP-Tools',
                                'https://github.com/Syslifters/offsec-tools',
                                'https://github.com/mikes-hacks/mxhelp',
                                'https://github.com/OlivierLaflamme/Cheatsheet-God',
                                'https://github.com/CoolHandSquid/TireFire/tree/TireFire_V4',
                                'https://github.com/antonioCoco/ConPtyShell',
                                'https://github.com/wirzka/incursore',
                                'https://github.com/ropnop/impacket_static_binaries/releases/tag/0.9.22.dev-binaries', 
                                'https://github.com/carlospolop/PEASS-ng/releases/tag/20230917-ec588706'
                                ]

    # These git repositories will be synced to the 'personal repo' directory. I use my home directory.
    personal_repo_directory = os.getenv("HOME")
    personal_repositories_to_sync = [
                                    ]

    # Next, take a look in the /scripts directory. Every script ending in .sh or .py will be run,
    # provided it's # executable. For example, the current scripts install VS Code, Google Chrome and
    # Typora. Any script that goes in this directory should be written so it can run multiple times
    # without causing problems.

if 'Ubuntu' in release and not are_we_on_wsl:
    # These directories will be removed from your home directory
    directories_to_remove = ['Documents', 'Music', 'Pictures', 'Public', 'Templates', 'Videos']

    # These Ubuntu packages will be installed
    packages_to_install = ['most', 'ttf-mscorefonts-installer', 'pydf', 'htop', 'golang', 'exif',
                           'hexedit', 'jq', 'python3-pip', 'python3-venv', 'apt-transport-https',
                           'curl', 'filezilla', 'meld', 'ncat', 'net-tools', 'tmux',
                           'bash-completion', 'ruby-full', 'nbtscan', 'tree', 'grc', 'john']

    # These Ubuntu packages will be removed
    packages_to_remove = []

    # These python packages will be installed globally
    pip_packages = ['pipenv', 'pylint', 'stegcracker', 'truffleHog']

    # These gem packages will be installed globally
    gem_packages = ['wpscan']

    # These go tools will be installed globally. You will need to have the following settings in your
    # .bashrc already:
    #
    # export GOROOT=/usr/lib/go
    # export GOPATH=$HOME/go
    # export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
    golang_modules_to_install = [
                                'github.com/lc/gau',
                                'github.com/hakluke/hakrawler',
                                'github.com/hahwul/dalfox',
                                ]

    # These git repositories will be synced to the 'external repo' directory
    external_tools_directory = '/opt'
    ext_repositories_to_sync =  [
                                ]

    # These git repositories will be synced to the 'personal repo' directory. I use my home directory.
    personal_repo_directory = os.getenv("HOME")
    personal_repositories_to_sync = [
                                    'git@github.com:rafaelh/dotfiles',
                                    'git@github.com:rafaelh/.private'
                                    ]

    # Next, take a look in the /scripts directory. Every script ending in .sh or .py will be run,
    # provided it's # executable. For example, the current scripts install VS Code, Google Chrome and
    # Typora. Any script that goes in this directory should be written so it can run multiple times
    # without causing problems.

if 'Ubuntu' in release and are_we_on_wsl:
        # These directories will be removed from your home directory
    directories_to_remove = []

    # These Ubuntu packages will be installed
    packages_to_install = ['most', 'pydf', 'golang', 'exif', 'hexedit', 'jq', 'python3-pip',
                           'python3-venv', 'curl', 'net-tools', 'tmux', 'bash-completion',
                           'ruby-full', 'nbtscan', 'tree', 'grc']

    # These Ubuntu packages will be removed
    packages_to_remove = []

    # These python packages will be installed globally
    pip_packages = ['pipenv', 'pylint']

    # These gem packages will be installed globally
    gem_packages = []

    # These go tools will be installed globally. You will need to have the following settings in your
    # .bashrc already:
    #
    # export GOROOT=/usr/lib/go
    # export GOPATH=$HOME/go
    # export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
    golang_modules_to_install = [
                                ]

    # These git repositories will be synced to the 'external repo' directory
    external_tools_directory = '/opt'
    ext_repositories_to_sync =  [
                                ]

    # These git repositories will be synced to the 'personal repo' directory. I use my home directory.
    personal_repo_directory = os.getenv("HOME")
    personal_repositories_to_sync = [
                                    'git@github.com:rafaelh/dotfiles',
                                    'git@github.com:rafaelh/.private'
                                    ]

    # Next, take a look in the /scripts directory. Every script ending in .sh or .py will be run,
    # provided it's # executable. For example, the current scripts install VS Code, Google Chrome and
    # Typora. Any script that goes in this directory should be written so it can run multiple times
    # without causing problems.
