
from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)
#print(__name__)



@app.route('/')
def myhome():
    return render_template('index.html')

@app.route('/<string:which_page>')
def myhome2(which_page=None):
    return render_template(which_page)


@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()

        with open("database.txt", "a") as myfile:
            email = data['email']
            subject = data['subject']
            message = data['message']

            myfile.write(f'\n{email}, {subject}, {message}')

        return redirect('./thankyou.html')
    else:
        return 'Something went wrong'



    #return 'form submitted heyyyy'


# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')







