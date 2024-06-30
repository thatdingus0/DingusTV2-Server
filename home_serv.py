from flask import Flask, send_from_directory, abort
import os
import logging

app = Flask(__name__)

# Configure logging

home_directory = os.path.join(os.getcwd(), 'Home')  # Updated directory name
home_directory2 = os.path.join(os.getcwd(), 'Home2')  # Updated directory name
images_shared_directory = os.path.join(home_directory2, 'Images', 'Shared')

@app.route('/Pages/<path:filename>')  # Updated URL path
def serve_file(filename):
    try:
        logging.debug(f"Trying to serve file from Home: {filename}")
        return send_from_directory(home_directory, filename)
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        abort(404)

@app.route('/Images/Shared/<path:filename>')
def serve_image(filename):
    try:
        logging.debug(f"Trying to serve image from Images/Shared: {filename}")
        # Serve the image from the actual directory location
        return send_from_directory(images_shared_directory, filename)
    except FileNotFoundError:
        logging.error(f"Image not found: {filename}")
        abort(404)

if __name__ == '__main__':
    if not os.path.exists(home_directory):
        os.makedirs(home_directory)
    
    if not os.path.exists(images_shared_directory):
        os.makedirs(images_shared_directory)
    
    app.run(host='0.0.0.0', port=82, debug=False)  # Ensure it runs on the correct port
