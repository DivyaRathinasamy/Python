from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "watermelon secret"

@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 1
    else:
        session['count'] += 1

    return render_template("index.html")

@app.route('/destroy_session')
def destroy():
    popped_count  = session.pop('count')

    return redirect('/')

@app.route('/click', methods=['POST'])
def click():
    button = request.form['button']

    if button == 'add2':
        session['count'] += 1
        return redirect('/')
    elif button == 'remove':
        return redirect('/destroy_session')
    else:
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
