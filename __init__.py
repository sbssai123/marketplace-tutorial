from flask import (Flask, render_template, request)

app = Flask(__name__, instance_relative_config=True)

@app.route("/")
def first_program():
    pass

@app.route("/hello")
def hello_world_pretty():
    pass

@app.route("/practice", methods=['GET'])
def python_fundamentals():
    return render_template("practice.html")

# TODO: Define functions that:
# 1. Calculates the sum of 5 and 6

# 2. Concatenates the words "Yes," "I" "Love" "Python"

# 3. Subtracts 5 from the number the user inputs
@app.route('/subtract_number', methods=['POST', 'GET'])
def subtract5():
    return render_template("practice.html", subtract5=subtract5)


# 4. Concatenates the word "Hello" and the Name the User Inputs

# 5. Concatenates all of the words in a list of strings

# 6. Add up all of the numbers in the list and display

# 7. Picks a random compliment in the list of strings 
# displays to the user when they click a button
compliments = ["You are doing amazing sweetie!!", "Have an amazing day!", "You are a Python Pro",
"Hello sunshine!"]

# 8. Tell the user what to wear based off of the weather

# 9. Have the user pick a color and a shape and tell them their fortune



