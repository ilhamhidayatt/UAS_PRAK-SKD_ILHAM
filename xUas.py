#mengimport library
import os
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

#nilai key
def getKey(keysize):
    key = os.urandom(keysize)
    return key


def getIV(blocksize):#ukuran blok
    iv = os.urandom(blocksize)
    return iv


def encrypt_image(filename, key, iv):#berfungsi untuk enkripsi gambar
    BLOCKSIZE = 16 #panjang bloknya 16
    encrypted_filename = "encrypted_" + filename #inisialisasi file gambar ketika berhasil di enkripsi


    with open(filename, "rb") as file1:# berfungsi untuk membuka file
        data = file1.read()#berfungsi untuk membaca file
        #untuk enkripsi gambar Aes
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(data, BLOCKSIZE))

        with open(encrypted_filename, "wb") as file2:#berfungsi untuk membuka file
            file2.write(ciphertext)#berfungsi untuk menuliskan chipertext
    return encrypted_filename

#Deskripsi gambar
def decrypt_image(filename, key, iv):
    BLOCKSIZE = 16
    decrypted_filename = "decrypted_" + filename

    with open(filename, "rb") as file1:
        data = file1.read()

        cipher2 = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher2.decrypt(data), BLOCKSIZE)

        with open(decrypted_filename, "wb") as file2:
            file2.write(decrypted_data)

    return decrypted_filename


KEYSIZE = 16 #key yang digunakan
BLOCKSIZE = 16 #panjang blok
filename = "gbr1.JPG"# gambar yang akan dienkripsi

key = getKey(KEYSIZE)
iv = getIV(BLOCKSIZE)

encrypted_filename = encrypt_image(filename, key, iv)
decrypted_filename = decrypt_image(encrypted_filename, key, iv)
