#!/usr/bin/env python3
"""setup a basic Flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config:
    """config for app"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/',)
def index():
    """index route"""
    return render_template('7-index.html')


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages."""
    args = request.args.get('locale')
    if args is not None:
        if args == 'en':
            return 'en'
        elif args == 'fr':
            return 'fr'
    elif g.user:
        if g.user.get('locale') == 'en' or g.user.get('locale') == 'fr':
            return g.user.get('locale')
    elif request.headers.get('locale'):
        local = request.headers.get('locale')
        if local == 'en' or local == 'fr':
            return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_locale():
    """validate that it is a valid time zone"""
    timez = request.args.get('timezone')
    if timez:
        try:
            pytz.timezone(timez)
            return timez
        except pytz.exceptions.UnknownTimeZoneError:
            return babel.default_timezone
    elif g.user:
        try:
            return pytz.timezone(g.user)
        except pytz.exceptions.UnknownTimeZoneError:
            return babel.default_timezone
    return babel.default_timezone


def get_user():
    """user login"""
    id_loggin = request.args.get('login_as')
    if id_loggin is None:
        return None
    else:
        return users.get(int(id_loggin))


@app.before_request
def before_request():
    """excuted before_request"""
    user_loged = get_user()
    g.user = user_loged


if __name__ == "__main__":
    app.run(debug=True)
