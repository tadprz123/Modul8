from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/mypage/mojastrona_o_mnie')
def me():
    return render_template('mojastrona_o_mnie.html')

@app.route('/mypage/mojastrona_kontakt', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f'Name: {name}, Email: {email}, Message: {message}')
    return render_template('mojastrona_kontakt.html')

if __name__ == '__main__':
    app.run(debug=True)