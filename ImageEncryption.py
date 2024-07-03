from PIL import Image
import random
import os

def generate_key(image_size, seed):
    random.seed(seed)
    key = list(range(image_size))
    random.shuffle(key)
    return key

def encrypt_image(image_path, seed):
    try:
        image = Image.open(image_path)
        pixels = list(image.getdata())
        width, height = image.size

        key = generate_key(len(pixels), seed)
        encrypted_pixels = [pixels[i] for i in key]

        encrypted_image = Image.new(image.mode, image.size)
        encrypted_image.putdata(encrypted_pixels)
        
        encrypted_filename = os.path.splitext(os.path.basename(image_path))[0] + "_encrypted.png"
        encrypted_image.save(encrypted_filename)
        print(f"Image encrypted and saved as {encrypted_filename}")
    except Exception as e:
        print(f"Error encrypting image: {e}")

def decrypt_image(image_path, seed):
    try:
        image = Image.open(image_path)
        encrypted_pixels = list(image.getdata())
        width, height = image.size

        key = generate_key(len(encrypted_pixels), seed)
        decrypted_pixels = [None] * len(encrypted_pixels)

        for i, k in enumerate(key):
            decrypted_pixels[k] = encrypted_pixels[i]

        decrypted_image = Image.new(image.mode, image.size)
        decrypted_image.putdata(decrypted_pixels)
        
        decrypted_filename = os.path.splitext(os.path.basename(image_path))[0] + "_decrypted.png"
        decrypted_image.save(decrypted_filename)
        print(f"Image decrypted and saved as {decrypted_filename}")
    except Exception as e:
        print(f"Error decrypting image: {e}")

def main():
    print("Secret Agent Image Encryption Tool")
    print("-------------------------------")
    while True:
        print("\nMenu:")
        print("1. Encrypt an image")
        print("2. Decrypt an encrypted image")
        print("3. Exit")
        choice = input("Enter your mission (1/2/3): ").strip()

        if choice == '1':
            image_path = input("Enter the image file path: ").strip()
            seed = int(input("Enter the secret seed value for encryption: ").strip())
            encrypt_image(image_path, seed)
        
        elif choice == '2':
            image_path = input("Enter the encrypted image file path: ").strip()
            seed = int(input("Enter the secret seed value for decryption: ").strip())
            decrypt_image(image_path, seed)
        
        elif choice == '3':
            print("\nExiting the Secret Agent Image Encryption Tool. Mission accomplished!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
