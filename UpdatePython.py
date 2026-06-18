import os

def titre(letitre):
    texte = ("#######################\n"
    + "\t" + letitre
    + "\n#######################")
    print(texte)

titre("update")        
os.system("sudo apt update")
titre("upgrade")
os.system("sudo apt upgrade")
titre("autoremove")
os.system("sudo apt autoremove")
titre("autoclean")
os.system("sudo apt autoclean")
titre("refresh")        
os.system("sudo snap refresh")

