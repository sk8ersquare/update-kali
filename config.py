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
                                'https://github.com/Tib3rius/AutoRecon',
                                'https://github.com/Tib3rius/SemiAutoRecon',
                                'https://github.com/CMEPW/keepass-dump-masterkey',
                                'https://github.com/Orange-Cyberdefense/KeePwn',
                                'https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.5/LaZagne.exe',
                                'https://github.com/r3motecontrol/Ghostpack-CompiledBinaries/',
                                'https://github.com/n00py/LAPSDumper',
                                'https://github.com/Hackndo/lsassy',
                                'https://github.com/S3cur3Th1sSh1t/PowerSharpPack',
                                'https://github.com/PowerShellMafia/PowerSploit',
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
                                'https://github.com/CoolHandSquid/TireFire.git',
                                'https://github.com/antonioCoco/ConPtyShell',
                                'https://github.com/wirzka/incursore',
                                'https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/linpeas.sh',
                                'https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/linpeas_darwin_amd64',
                                'https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/linpeas_darwin_arm64',
                                'https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/linpeas_fat.sh',
                                'https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/linpeas_linux_386',
                                'https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/linpeas_linux_amd64',
                                'https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/linpeas_linux_arm',
                                'https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/linpeas_linux_arm64',
                                'https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/winPEAS.bat',
                                'https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/winPEASany.exe',
                                'https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/winPEASany_ofs.exe',
                                'https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/winPEASx64.exe',
                                'https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/winPEASx64_ofs.exe',
                                'https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/winPEASx86.exe',
                                'https://github.com/carlospolop/PEASS-ng/releases/download/20230917-ec588706/winPEASx86_ofs.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/addcomputer_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/addcomputer_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/atexec_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/atexec_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/dcomexec_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/dcomexec_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/dpapi_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/dpapi_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/esentutl_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/esentutl_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/exchanger_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/exchanger_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/findDelegation_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/findDelegation_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/GetADUsers_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/GetADUsers_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/getArch_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/getArch_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/GetNPUsers_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/GetNPUsers_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/getPac_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/getPac_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/getST_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/getST_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/getTGT_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/getTGT_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/GetUserSPNs_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/GetUserSPNs_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/goldenPac_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/goldenPac_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/impacket_linux_binaries.tar.gz',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/impacket_musl_binaries.tar.gz',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/impacket_windows_binaries.zip',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/karmaSMB_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/karmaSMB_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/kintercept_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/kintercept_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/lookupsid_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/lookupsid_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/mimikatz_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/mimikatz_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/mqtt_check_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/mqtt_check_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/mssqlclient_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/mssqlclient_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/mssqlinstance_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/mssqlinstance_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/netview_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/netview_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/nmapAnswerMachine_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/nmapAnswerMachine_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/ntfs-read_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/ntfs-read_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/ntlmrelayx_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/ntlmrelayx_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/ping6_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/ping6_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/ping_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/ping_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/psexec_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/psexec_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/raiseChild_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/raiseChild_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/rdp_check_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/rdp_check_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/registry-read_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/registry-read_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/reg_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/reg_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/rpcdump_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/rpcdump_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/rpcmap_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/rpcmap_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/sambaPipe_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/sambaPipe_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/samrdump_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/samrdump_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/secretsdump_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/secretsdump_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/services_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/services_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/smbclient_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/smbclient_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/smbexec_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/smbexec_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/smbrelayx_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/smbrelayx_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/smbserver_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/smbserver_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/sniffer_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/sniffer_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/sniff_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/sniff_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/split_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/split_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/ticketConverter_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/ticketConverter_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/ticketer_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/ticketer_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/version.txt',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/wmiexec_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/wmiexec_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/wmipersist_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/wmipersist_windows.exe',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/wmiquery_linux_x86_64',
                                'https://github.com/ropnop/impacket_static_binaries/releases/download/0.9.22.dev-binaries/wmiquery_windows.exe',
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
