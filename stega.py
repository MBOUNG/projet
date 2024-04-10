from PIL import Image

def encoder(image_path, message, output_path):
    # Charger l'image de couverture
    image = Image.open(image_path)
    pixels = list(image.getdata())

    # Convertir le message en binaire
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Vérifier si la taille du message est inférieure ou égale à la capacité de l'image
    if len(binary_message) > len(pixels):
        raise ValueError("Message trop long pour l'image sélectionnée.")

    # Cacher le message dans les pixels de l'image
    for i in range(len(binary_message)):
        pixels[i] = tuple(pixels[i][:3] + (int(binary_message[i]),) + pixels[i][4:])

    # Créer une nouvelle image avec le message caché
    encoded_image = Image.new("RGB", image.size)
    encoded_image.putdata(pixels)
    encoded_image.save(output_path)

def decoder(image_path):
    # Charger l'image avec le message caché
    encoded_image = Image.open(image_path)
    pixels = list(encoded_image.getdata())

    # Extraire le message binaire caché
    binary_message = ''.join(str(pixel[-1]) for pixel in pixels)

    # Convertir le message binaire en texte
    decoded_message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))

    return decoded_message

# Exemple d'utilisation
message_to_hide = "Hello, this is a hidden message!"
cover_image_path = "chemin/vers/votre/image.jpg"
output_image_path = "chemin/vers/votre/image_cachee.png"

# Cacher le message dans l'image
encoder(cover_image_path, message_to_hide, output_image_path)

# Décoder le message à partir de l'image cachée
decoded_message = decoder(output_image_path)
print("Message caché récupéré :", decoded_message)
