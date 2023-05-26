from PIL import Image
import os

folder_path = "./public/images/products_images"

# Parcourir tous les fichiers du dossier
for filename in os.listdir(folder_path):
    # Vérifier si le fichier est une image PNG
    if filename.endswith(".png"):
        # Construire le chemin complet du fichier
        file_path = os.path.join(folder_path, filename)

        # Ouvrir l'image avec Pillow
        image = Image.open(file_path)

        # Obtenir le nouveau nom de fichier en supprimant "_01"
        new_filename = filename.replace("_01", "")
#         new_filename = filename.replace("_02", "")
#         new_filename = filename.replace("_03", "")
#         new_filename = filename.replace("_04", "")
#         new_filename = filename.replace("_05", "")

        # Construire le nouveau chemin complet du fichier
        new_file_path = os.path.join(folder_path, new_filename)

        # Renommer le fichier
        os.rename(file_path, new_file_path)

        # Fermer l'image
        image.close()