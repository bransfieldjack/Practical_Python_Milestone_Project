import os 
import json
import random
import copy
from flask import Flask, render_template


app = Flask(__name__)


riddles = [
    {
        "question":"What goes up when the rain comes down? ",
        "answer":"umbrella",
    },   
    {
        "question":"I have a head and a tail but no body. What am I?",
        "answer":"coin"
    },
    {
        "question":"They are Dark, and always on the run. without the sun, would be none.",
        "answer":"shadows"
    },
    {
        "question":"What lives as long as it eats but dies when it drinks?",
        "answer":"fire"
    },
    {
        "question":"What travels around the world but stays in one corner?",
        "answer":"stamp"
    },
    {
        "question":"What has hands but cannot clap?",
        "answer":"clock"
    },
    {
        "question":"What has an eye but cannot see?",
        "answer":"needle"
    },
    {
        "question":"What kind of tree can you carry in your hand?",
        "answer":"palm"
    }
]

@app.route('/')
def quiz():
    return render_template('index.html', riddle_data = random.choice(riddles))
    
    
@app.route('/')
def main():
    return render_template('main.js')
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), 
            debug=True)
            
            