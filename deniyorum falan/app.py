from flask import Flask, render_template, request
import random

app = Flask(__name__)

data = ["Python", "C", "C++", "C#", "Java", "JavaScript", "R", "Kotlin", "Swift", "PHP", "Pascal", "Ruby", "Objective-C", "Go", "SQL", "Typescript"]

selected_data = []    

round_count = 1

random_data = []

@app.route('/')
def index():
    global data, selected_data, round_count
    if len(data) != 0:
        if len(data)!=1:
            if len(data)!=2:
                random_data = random.sample(data,2)
                for item in random_data:
                    data.remove(item)
                return render_template('index.html', data=random_data, round=round_count)
            else:
                soniki = data.copy()
                data.clear()  
                return render_template('index.html', data=soniki, round=round_count)
        else:
            return render_template('result.html', data=data)            
    else:
        data = selected_data.copy()
        selected_data.clear()
        round_count += 1
        return index()

@app.route('/submit', methods=['POST'])
def submit():
    global data, selected_data
    selected = request.form['selected']
    selected_data.append(selected)
    return index()


#if __name__ == '__main__':
 #  app.run(debug=True)