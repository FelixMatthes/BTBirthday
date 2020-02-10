import os
from main.routes import main
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', titel='home')


@app.route('/about')
def about():
    return render_template('about.html', title='about')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


app.register_blueprint(main)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
