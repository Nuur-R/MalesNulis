from flask import Flask,render_template, request
from text_to_handwrite import text_to_handwriting


app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # buat POST request
    if request.method=='POST':
        paragraph = request.form['paragraph']
        print(paragraph)
        text_to_handwriting(paragraph, "paragraph")

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)