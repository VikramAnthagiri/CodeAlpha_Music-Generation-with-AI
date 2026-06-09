from flask import Flask, render_template
from music21 import stream, note
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate')
def generate():

    melody = stream.Stream()

    notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']

    for i in range(20):
        n = note.Note(random.choice(notes))
        n.quarterLength = 1
        melody.append(n)

    melody.write('midi', fp='generated_music/output.mid')

    return "Music Generated Successfully!"

if __name__ == '__main__':
    app.run(debug=True)