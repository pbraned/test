from flask import Flask, render_template, request
from imagehash import phash
import os

app = Flask(__name__)

# Function to compute Hamming distance between two hashes
def hamming_distance(hash1, hash2):
    return bin(int(hash1, 16) ^ int(hash2, 16)).count('1')

# Function to compare uploaded image hash with stored hashes
def compare_hashes(uploaded_hash, threshold=10):
    similar_hashes = []
    with open('stored_hashes.txt', 'r') as file:
        for line in file:
            stored_hash = line.strip()
            distance = hamming_distance(uploaded_hash, stored_hash)
            if distance <= threshold:
                similar_hashes.append((stored_hash, distance))
    return similar_hashes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    threshold = int(request.form['threshold'])
    if uploaded_file.filename != '':
        # Save uploaded image
        uploaded_image_path = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(uploaded_image_path)
        # Generate perceptual hash for uploaded image
        uploaded_hash = str(phash(uploaded_image_path))
        # Compare with stored hashes
        similar_hashes = compare_hashes(uploaded_hash, threshold)
        return render_template('results.html', similar_hashes=similar_hashes)
    else:
        return render_template('index.html', error='Please upload an image file.')

if __name__ == '__main__':
    app.run(debug=True)
