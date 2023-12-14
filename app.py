from flask import Flask, render_template, request

from stories import story
app = Flask(__name__)

@app.route('/')
def madlib_form():
    prompts = story.prompts
    return render_template("home.html", prompts = prompts)

@app.route('/story')
def story_output():
    ans = request.args
    story_text = story.generate(ans)
    return render_template('story.html', story_text = story_text)