"""A madlib game that compliments its users."""

from random import choice, randint, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return '<link rel="stylesheet" href="/static/madlibs.css">Hi! This is the home page. <br><a href=\"/hello\"> Wanna say hi? </a>'


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    """Play game."""
    response = request.args.get("playgame")

    if response == 'no':
        return render_template("goodbye.html")
    return render_template("game.html")


@app.route('/madlib', methods=["POST"])
def show_madlib():
    name = request.form.get("name")
    color = request.form.get("color")
    noun = request.form.get("noun")
    adj = request.form.get("adj")
    music = (request.form.getlist("music"))
    story = randint(1, 2)

    return render_template("madlib.html",
                           name=name,
                           color=color,
                           noun=noun,
                           adj=adj,
                           music=music,
                           story=story)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
