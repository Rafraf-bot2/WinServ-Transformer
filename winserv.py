import os

path = os.path.abspath("nssm.exe")
os.environ["PATH"] += os.pathsep + path

nameServ = "OSvmf"
pathGen = "on met ici le chemin du programme que l'on veut transformer en service"
servDisplay = "Service de generation de clés vmf"
servDesc = "vmf key generator"

os.system('nssm install '+nameServ+" "+pathGen)
os.system('nssm set '+nameServ+' DisplayName '+servDisplay)
os.system('nssm set '+nameServ+' Description '+servDesc)
os.system('nssm set '+nameServ+' Start SERVICE_AUTO_START')

os.system('nssm start '+nameServ)