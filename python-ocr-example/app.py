import os
from flask import Flask, render_template, request
from ocr_core import ocr_core

UPLOAD_FOLDER = '/static/uploads/'

# Allowed extensions for the image file.
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# Make app.
app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Upload a photo file.
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # Check if the post request has the file part.
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected.')
        file = request.files['file']
        
        # If the user does not select a file, tell them they did not do so.
        if file.filename == '':
            return render_template('upload.html', msg='No file selected.')

        if file and allowed_file(file.filename):
            file.save(os.path.join(os.getcwd() + UPLOAD_FOLDER, file.filename))

            # Get the text for the image.
            extracted_text = ocr_core(file)

            # Display the text.
            return render_template('upload.html',
                msg='The image was successfully processed.',
                extracted_text=extracted_text,
                img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

# Run application in debug mode.
if __name__ == '__main__':
    app.run(debug=True)