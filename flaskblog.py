from flask import Flask,render_template
app=Flask(__name__)

post=[
    {'author':'niraj',
    'date_posted':'anshu',
    'title':'title1',
    'content':'this is content1'
    },

    {'author':'singh',
    'date_posted':'20 20 20',
    'title':'title2',
    'content':'this is content2'
    },

    ]

@app.route("/")
def hello():
    return render_template('index.html',posts=post)

@app.route("/about")
def about():
    return render_template('about.html',title='about')


if __name__=='__main__':
    app.run(debug=True)
