from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

#router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

#router routes for caesar cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods = ['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar_cipher = CaesarCipher()
    encrypted_text = caesar_cipher.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods = ['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar_cipher = CaesarCipher()
    decrypted_text = caesar_cipher.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

#router routes for playfair cipher
@app.route('/playfair')
def playfair_page():
    return render_template('playfair.html')

@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    plain_text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair_cipher = PlayFairCipher(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text)
    return f"Encrypted Text: {encrypted_text}"

@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    cipher_text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair_cipher = PlayFairCipher(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text)
    return f"Decrypted Text: {decrypted_text}"


#router routes for railfence cipher
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    num_rails = int(request.form['inputKeyPlain'])
    rail_fence_cipher = RailFenceCipher(num_rails) 
    encrypted_text = rail_fence_cipher.rail_fence_encrypt(text, num_rails)
    return f"Text: {text}<br/>Key: {num_rails}<br/>Encrypted Text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    num_rails = int(request.form['inputKeyCipher'])
    rail_fence_cipher = RailFenceCipher(num_rails)
    decrypted_text = rail_fence_cipher.rail_fence_decrypt(text, num_rails)
    return f"Text: {text}<br/>Key: {num_rails}<br/>Decrypted Text: {decrypted_text}"


#router routes for transposition cipher
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/transposition/encrypt", methods=['POST'])
def encrypt_transposition():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    transposition_cipher = TranspositionCipher()
    encrypted_text = transposition_cipher.encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/transposition/decrypt", methods=['POST'])
def decrypt_transposition():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    transposition_cipher = TranspositionCipher()
    decrypted_text = transposition_cipher.decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

#router routes for vigenere cipher
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere_cipher = VigenereCipher()
    encrypted_text = vigenere_cipher.vigenere_encrypt(text, key) 
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    cipher = VigenereCipher()
    decrypted_text = cipher.vigenere_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)