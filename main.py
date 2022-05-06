from flask import Flask,render_template, request
from text_to_handwrite import text_to_handwriting
import os

app=Flask(__name__)

# image
picFolder = 'static/img'
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/', methods=['GET', 'POST'])
def home():
    paragraph_picture = os.path.join(app.config['UPLOAD_FOLDER'], 'paragraph.png')
    # buat POST request
    if request.method=='POST':
        paragraph = request.form['paragraph']
        print(paragraph)
        text_to_handwriting(paragraph, "paragraph")

    return render_template('home.html',pic=paragraph_picture)

if __name__ == '__main__':
    print("Server is running in localhost:5000")
    app.run(debug=True)