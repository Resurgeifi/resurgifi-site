from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sneakpeek')
def sneakpeek():
    return render_template('sneakpeek.html')
@app.route("/testvideo")
def test_video():
    return render_template("test_video.html")
if __name__ == '__main__':
    app.run(debug=True)
app.run(host='0.0.0.0', port=5001, debug=True)

