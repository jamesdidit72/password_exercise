from flask import Flask, request, abort
import password_generator.password_functions as password_functions

app = Flask(__name__)

@app.route('/')
def welcome_main():
    return 'Welcome to the Password Generator App'

# URL: 127.0.0.1:5000/strength_checker?firstname=james&lastname=barton&dobDAY=17&dobMONTH=03&dobYEAR=1999&password=james72

@app.route('/strength_checker')
def perform_strength_checker():
    first_name = request.args.get('firstname', type = str, default = "")
    last_name = request.args.get('lastname', type = str, default = "")
    dob_day = request.args.get('dobDAY', type = int, default = 0)
    dob_month = request.args.get('dobMONTH', type = int, default = 0)
    dob_year = request.args.get('dobYEAR', type = int, default = 0)
    user_pw = request.args.get('password', type = str, default = "")
    password_check = password_functions.strength_checker(first_name, last_name, dob_day, dob_month, dob_year,user_pw) # first_name, last_name, dob_day, dob_month, dob_year,
    return str(password_check)

@app.route('/pass_generate')
def perform_pass_generation():
    new_password = password_functions.pass_generate(first_name, last_name, dob_day, dob_month, dob_year)
    return new_password
# @app.route('/add/<int:num1>/<int:num2>')
# def perform_add(num1, num2):
#     num3 = calc_functions.add(num1, num2)
#     print(num3)
#     return str(num3)

# using query string
# URL: 127.0.0.1:5000/add?num1=1&num2=2
# @app.route('/add')
# def perform_add_query():
#     num1 = request.args.get('num1', type =int, default = 0)
#     num2 = request.args.get('num2', type = int, default = 0)
#
#     if num1 is None or num2 is None:
#         abort(404)
#     num3 = calc_functions.add(num1, num2)
#     print(num3)
#     return str(num3)
# @app.route('/pass_generate')
# def perform_pass_generation():
#     first_name = request.args.get('firstname', type = str, default = "")
#     last_name = request.args.get('lastname', type = str, default = "")
#     dob_day = request.args.get('dobDAY', type = int, default = "")
#     dob_month = request.args.get('dobMONTH', type = int, default = "")
#     dob_year = request.args.get('dobYEAR', type = int, default = "")
#
#     new_password = pass_generate()
#
