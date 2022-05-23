from models.model import *
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
db = Model()

@app.route('/')
def index():
    data = db.query()
    print(data) # ცოტახანი იყოს აქ დიბაგინგისთვის
    return render_template('index.html', data = data)

@app.route('/average')
def average():
    data = db.query()
    return render_template('average.html', data=data)

@app.route('/update')
def update():
    pk = request.args.get('pk')
    data = db.select_user_by_pk(int(pk))
    
    return render_template('update.html', data = data)
    
@app.route('/process', methods=['POST', 'GET'])
def process():
    
    # Request steps:
        # request.form['action'] ამოწმებს რას უდრის request.form['action']. ეს რექვესტი უტოლდება value-ს, რის შედეგადაც
        # ვარჩევ რომელი ღილაკიდან მოდის რექვესტი. ამიტომ ყველა ღილაკს აქვს ერთნაირი სახელი, მაგრამ value სხვა
        
    if request.form['action'] == "Add user": # Add request from index page
        first_name = request.form['first_name'].strip()
        last_name = request.form['last_name'].strip()

        db.add_user(first_name, last_name)
        return redirect(url_for('index'))
    
    elif request.form['action'] == 'Delete': # Delete request from index page
        pk = int(request.form['primary_key'])
        db.delete_user_by_pk(pk)
        return redirect(url_for('index'))
    
    elif request.form['action'] == "Edit": # Edit request from index page        
        pk = int(request.form['primary_key'])
        return redirect(url_for('update', pk = pk))
    
    elif request.form['action'] == 'Back': # Back request from update page
        return redirect(url_for('index'))
    
    elif request.form['action'] == "Save changes": # Save changes request from edit page
        primary_key = int(request.form['primary_key'])
        first_name = request.form['first_name'].strip()
        last_name = request.form['last_name'].strip()
        math = int(request.form['math'])
        history = int(request.form['history'])
        biology = int(request.form['biology'])
        sports = int(request.form['sports'])
        
        db.update_user_by_pk(primary_key, first_name, last_name,
                             math, history, biology,
                             sports)
        
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


