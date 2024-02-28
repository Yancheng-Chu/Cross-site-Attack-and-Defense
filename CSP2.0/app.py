from flask import Flask, render_template, send_from_directory, request, session

app = Flask(__name__)

# @app.after_request
# def add_csp_header(response):
#     nonce = secrets.token_hex(16)
#     csp_policy = "script-src 'self' 'nonce-{}'".format(nonce)
#     response.headers['Content-Security-Policy'] = csp_policy
#     print(response.headers['Content-Security-Policy'])
#     return response

page_header = """
<!doctype html>
<html>
  <head>
    <script src="/static/game-frame.js"></script>
    <link rel="stylesheet" href="/static/game-frame-styles.css" />
    <!-- Internal game scripts/styles, mostly boring stuff -->
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
    <script src="/static/xss1.js"></script>
<form action="" method="GET">
  <input id="query" name="query" value="Enter query here...">
  <input id="button" type="submit" value="Search">
</form>
"""

@app.route('/')
def main_page():
    response = app.make_response(page_header + main_page_markup + page_footer)

    query = request.args.get('query', '')
    if query:
        query = request.args.get('query', '[empty]')
        message = f"Sorry, no results were found for <b>{query}</b>."
        message += f" <a href='?'>Try again</a>."
        response = app.make_response(page_header + message + page_footer)

    csp_header = f"default-src 'self'; script-src 'self'"
    response.headers['Content-Security-Policy'] = csp_header
    return response


@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)


@app.route('/level2/frame')
def level2():
    return render_template('xss2.html')


@app.route('/level3/frame')
def level3():
    # header = ["X-XSS-Protection", "0"]
    return render_template('xss3.html')


@app.route('/level4/frame')

def level4():
    if not request.args.get('timer'):
        return render_template('index.html')
    else:
        timer = request.args.get('timer', 0)
        script = f"startTimer('{timer}')"
        print(script)
        import hashlib
        sha256_hash = hashlib.sha256(script.encode()).hexdigest()
        print(sha256_hash)
        return render_template('t.html', timer=timer,script=script)


@app.route('/level5/frame/')
def level5():
    path = request.path
    if "signup" in path:
        return render_template('signup.html', next=request.args.get('next'))
    elif "confirm" in path:
        return render_template('confirm.html', next=request.args.get('next', 'welcome'))
    else:
        return render_template('welcome.html')


@app.route('/level5/frame/signup')
def signup():
    return render_template('signup.html', next=request.args.get('next'))


@app.route('/level5/frame/confirm')
def confirm():
    return render_template('confirm.html', next=request.args.get('next', 'welcome'))


@app.route('/level5/frame/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/last/frame')
def level6():
    return render_template('xss6.html')


if __name__ == '__main__':
    app.run()
