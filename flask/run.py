import os 
import json
import random
import copy
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def quiz():
    data = []
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
    return render_template('index.html', riddle_data = random.choice(data))
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), 
            debug=True)
            
            