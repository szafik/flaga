from flask import Flask, render_template, request
from moje_programy.password_generator import password_generator
from moje_programy.character_wiki import character
from moje_programy.open_poem import open_poem
import random

app=Flask(__name__)

@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/xd')
def xd():
    return render_template("xd.html")

@app.route('/kubus_puchatek')
def kubus_puchatek():
	return render_template('kubus_puchatek.html')


@app.route('/password_generator', methods=["POST", "GET"])
def passwd_generator():
    lenght = 14
    password = password_generator(lenght)
    return render_template("password_generator.html", password = password)	
    

@app.route('/flaga_dla_ukrainy')
def flaga_dla_ukrainy():
    return render_template('flaga_dla_ukrainy.html')

@app.route('/brudnopis')
def brudnopis():
    super_heroes = ['Bruce Lee', 'Kubuś Puchatek', 'Mikołaj Kopernik', 'Adam Małysz', 'Don Henley']
    chosen_hero = random.choice( super_heroes)
    description = character( chosen_hero)
    poem_lines = open_poem()
    return render_template("brudnopis.html", hero=chosen_hero, description=description, poem_lines=poem_lines) 

@app.route('/ciekawe-postacie')
def ciekawe_postacie():
    intresting_characters = [
        'Glenn Frey', 
        'Jimmy Page', 
        'Don Henley', 
        'Bob Seger', 
        'Bruce Springsteen',
        'Tom Petty',
        'Tom Waits',
        'Eric Clapton',
        'Van Morrison',
        'Ray Charles',
        'Johnny Cash',
        'Bob Dylan'
        ]
    opisy_postaci = []
    
    for i in range(3):
        postac = random.choice(intresting_characters)
        #get rid of duplicates
        indeks = intresting_characters.index(postac)
        intresting_characters.pop(indeks)
        #add text
        opis_postaci = character(postac)
        # number of words
        num_of_words = len(opis_postaci.split(' '))
        # 0 - head, 1-text 2- number of words
        info = [postac, opis_postaci, num_of_words]
        # complete list
        opisy_postaci.append(info)
        # let's sort by number of words
        opisy_postaci = sorted(opisy_postaci, key=lambda info:info[2], reverse=True)
    return render_template('ciekawe-postacie.html', opisy_postaci=opisy_postaci)

if __name__=="__main__":
    app.run()

