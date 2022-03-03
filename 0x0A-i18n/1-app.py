

#!/usr/bin/env python3
"""setup a basic Flask app"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:

    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = Config.LANGUAGES[0]
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
babel = Babel(app)


@app.route('/',)
def index():
    """index route"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
