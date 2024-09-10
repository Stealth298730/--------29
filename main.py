from flask import Flask, render_template

import random


app = Flask(__name__)


max_score = 100

@app.get("/")
def index():
    return render_template("index.html")


@app.get("/menu/")
def menu():
    pizzas = [
        {"name": "Маргарита", "ingredients": "томатний соус, моцарела, базилік", "price": 15}  ,
    {"name": "Пепероні", "ingredients": "томатний соус, моцарела, пепероні", "price": 18}    ,
    {"name": "Чотири сири", "ingredients": "моцарела, горгонзола, пармезан", "price": 22},
    {"name": "Гавайська", "ingredients": "томатний соус, моцарела, ананас", "price": 20},
    {"name": "Вегетаріанська", "ingredients": "томатний соус, гриби, перець", "price": 19}
    ]
    discounts = [random.randint(0,100) for _ in range(5)]
    context = {
        "pizzas" :pizzas ,
        "price": random.randint(15, 50),
        "discount":discounts
    }
    return render_template("menu.html", **context)


@app.get("/contacts/")
def contacts():
    context = {
        "first_number": random.randint(101, 999),
        "second_number": random.randint(1001, 9999)
    }
    return render_template("contacts.html", **context)




if __name__ == "__main__":
    app.run()