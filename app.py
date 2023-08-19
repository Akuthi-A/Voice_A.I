from flask import Flask, render_template,request, url_for, redirect,send_from_directory, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('app.html')

@app.route('/submitted_field',methods=["GET","POST"])
def submitted_field():
    if request.method == "POST":
        file_name = request.form.get('file_name')
        if file_name is None:
            return render_template('app.html', err='no file')
    return render_template('app.html',err=file_name)
if __name__ == '__main__':
    app.run(debug=True)
