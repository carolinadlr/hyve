"""from index.html import Atom, render_template, request



app = Atom(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    Winter = request.form['Winter']
    Spring = request.form['Spring']
    Summer = request.form['Summer']
    Autumn = request.form['Autumn']
    return render_template('pass.html', Winter, Spring, Summer, Autumn)

"""

def main():
    print("testrun")


if __name__ == '__main__':
    main()
