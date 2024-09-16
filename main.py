#les insatalation a faire
#pip install youtube
#pip install yt_dlp

import yt_dlp as youtube_dl
import tkinter as tk
from tkinter import filedialog
import hashlib



# Fonction pour choisir un dossier de sauvegarde
def choisir_dossier():
    root = tk.Tk()
    root.withdraw()

    # Cacher la fenêtre principale

    dossier = filedialog.askdirectory()
    return dossier

# URL de la vidéo YouTube
url = input("Entrez le lien de la vidéo YouTube : ")

# Choisir le dossier de sauvegarde
dossier_sauvegarde = choisir_dossier()

# Options de téléchargement
ydl_opts = {
    'format': 'best',
    'outtmpl': f'{dossier_sauvegarde}/%(title)s.%(ext)s',
}


# Télécharger la vidéo
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Téléchargement terminé avec succès !")

# Signature invisible (hash unique)
signature_string = "Script développé par [OtisDav]"
signature_hash = hashlib.md5(signature_string.encode('utf-8')).hexdigest()
print(f"Signature hash: {signature_hash}")


