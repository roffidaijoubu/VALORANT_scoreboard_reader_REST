from flask import Flask, request, jsonify, send_file
import os
import cv2
import numpy as np
from scoreboard_reader import functions as srf
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image_file = request.files['image']
    output_format = request.form.get('output_format', 'json')

    # Save the uploaded image
    image_path = 'uploaded_image.png'
    image_file.save(image_path)

    # Process the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image_colored = cv2.imread(image_path)
    image, image_colored = srf.find_tables(image, image_colored)
    cell_images_rows, headshots_images_rows = srf.extract_cell_images_from_table(image, image_colored)
    agents = srf.identify_agents(headshots_images_rows)
    output = srf.read_table_rows(cell_images_rows)

    if output_format == 'csv':
        srf.write_csv(output, agents, ",")
        return send_file('output/scoreboard.csv', as_attachment=True)
    else:
        srf.write_json(output, agents)
        return send_file('output/scoreboard.json', as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists('output'):
        os.makedirs('output')
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
