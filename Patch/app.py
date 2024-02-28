from flask import Flask, render_template, send_from_directory, request, escape, redirect
import re

app = Flask(__name__)



page_header = """
<!doctype html>
<html>
  <head>
    <!-- Internal game scripts/styles, mostly boring stuff -->
    <script src="/static/game-frame.js"></script>
    <link rel="stylesheet" href="/static/game-frame-styles.css" />
  </head>
  <body id="level1">
    <img src="/static/level1.png">
    <div>
"""

page_footer = """
    </div>
  </body>
</html>
"""

main_page_markup = """
<form action="/" method="GET">
  <input id="query" name="query" value="Enter query here..."
    onfocus="this.value=''">
  <input id="button" type="submit" value="Search">
</form>
"""


@app.route('/')
def main_page():
    response = app.make_response(page_header + main_page_markup + page_footer)
    # response.headers['X-XSS-Protection'] = '0'

    query = request.args.get('query', '')
    if query:
        # Filter special characters in user input to prevent XSS attacks
        query = escape(query)

        message = f"Sorry, no results were found for <b>{query}</b>."
        message += f" <a href='?'>Try again</a>."
        response = app.make_response(page_header + message + page_footer)
        # response.headers['X-XSS-Protection'] = '0'

    return response


@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)

@app.route('/level2/frame')
def level2():
    return render_template('xss2.html')

@app.route('/level3/frame')
def level3():
    return render_template('xss3.html')


@app.route('/level4/frame')
def level4():
    timer = request.args.get('timer', 0)
    try:
        timer = int(timer)
    except ValueError:
        timer = 3
    if not timer:
        return render_template('index.html')
    return render_template('timer.html', timer=escape(timer))

    # headers = {"X-XSS-Protection": "0"}
    # if not request.args.get('timer'):
    # return render_template('index.html'), 200, headers
    #     return render_template('index.html')
    # else:
    #     timer = request.args.get('timer', 0)
    #
    # return render_template('timer.html', timer=timer), 200, headers

@app.route('/level5/frame/')
def level5():
    # headers = {"X-XSS-Protection": "0"}
    return redirect('welcome')

@app.route('/level5/frame/signup')
def signup():
    next = request.args.get('next')

    js = r'<script|alert\(|eval\(|confirm\(|prompt\(|javascript:|<\/script'

    if(re.search(js, request.url, re.IGNORECASE) and re.search(js, next, re.IGNORECASE)):
        return redirect('welcome')
    else:
        return render_template('signup.html', next=next)
    # if "signup" in path and nextUrl and is_valid_url(nextUrl):
    # headers = {"X-XSS-Protection": "0"}
    # return render_template('signup.html', next=nextUrl)

@app.route('/level5/frame/confirm')
def confirm():
    # headers = {"X-XSS-Protection": "0"}
    return render_template('confirm.html', next=request.args.get('next', 'welcome'))

@app.route('/level5/frame/welcome')
def welcome():
    # headers = {"X-XSS-Protection": "0"}
    return render_template('welcome.html')


# @app.route('/level6/frame')
# def level6():
    # gadget_fragment = request.args.get('gadget', '/static/gadget.js')
    # url_with_hash = url_for('level6', _anchor=gadget_fragment)
    # return render_template('xss6.html')
    # print(url_with_hash)
    # return render_template('xss6.html', url_with_hash=url_with_hash)
# def level6():
#     # headers = {"X-XSS-Protection": "0"}
#     print('1111',request.url)
#     gadget = request.args.get('gadget', '/static/gadget.js')
#     print('2222',request.args.get('gadget'))
#     # url_with_hash = url_for('level6', _anchor=gadget)
#     # return render_template('xss6.html', url_with_hash=gadget)
#     return render_template('xss6.html', script_url=gadget)

@app.route('/last/frame')
def last():
    # gadget_fragment = request.url + request.args.get('gadget','/static/gadget.js')

    # cleaned_fragment = clean_url_fragment(gadget_fragment)
    # if not cleaned_fragment:
    #     return "Invalid URL fragment", 400
    return render_template('xss6.html')


@app.route('/process_hash')
def process_hash():
    # get hash
    hash_value = request.args.get('hash', '')

    if is_valid_hash(hash_value):
        return hash_value
    else:
        return False

def is_valid_hash(hash_value):
    reg = r'^((?!http[s]?://|data:).)*$'

    if hash_value.startswith('//'):
        hash_value = request.scheme + '://' + hash_value
    hash_value = escape(hash_value)
    if re.match(reg, hash_value):
        print('match',hash_value)
        return True
    else:
        return False


if __name__ == '__main__':
    app.run()
