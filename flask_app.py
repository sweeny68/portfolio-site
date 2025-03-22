from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from flask import send_from_directory

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'oranmcclintock10@gmail.com'
app.config['MAIL_PASSWORD'] = 'flaj dkfb rxrb jixq '
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/personalstatement')
def personalstatement():
    return render_template('personalstatement.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        comments = request.form['comments']

        msg = Message("Contact Form Submission",
                    sender='oranmcclintock10@gmail.com', 
                    recipients=['oranmcclintock10@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\n\n{comments}"

        try:
            mail.send(msg)
            return redirect(url_for('thank_you', name=name))
        except Exception as e:
            return f"An error occurred: {e}"

    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/thank_you')
def thank_you():
    name = request.args.get('name')
    return f'Thank you, {name}! Your message has been received.'

@app.route('/robots.txt')
def static_from_root():
    # Serve robots.txt from the static folder without using os
    return send_from_directory(app.static_folder, 'robots.txt')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)