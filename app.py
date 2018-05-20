from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/book/add/', methods=['GET', 'POST'])
def book_add():
    if request.method == 'POST':
        bookName = request.form.get('bookName')
        authorName = request.form.get('authorName')
        with open('user.csv', 'a', encoding='utf-8') as f:
            f.write(bookName + ',' + authorName)
        return redirect(url_for('book_list'))
    else:
        return render_template('book_add.html')

@app.route('/book/list/')
def book_list():
    f = open('user.csv', 'r', encoding='utf-8')
    a = f.readlines()
    book_list = []
    for item in a:
        info_list = item.split(',')
        book_list.append({'bookName':info_list[0], 'authorName':info_list[1]})
    f.close()
    return render_template('book_list.html', booklist=book_list)

@app.route('/book/edit/')
def book_edit():
    return request.args.get('bookName')

if __name__ == '__main__':
    app.run(debug=True)
