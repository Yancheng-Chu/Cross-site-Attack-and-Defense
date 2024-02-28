from flask import Flask, render_template, send_from_directory, request, session
import os
import secrets

app = Flask(__name__)
app.secret_key = os.urandom(24)

global page_header, page_footer, main_page_markup

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
    <script nonce="{{nonce}}"> 
    document.addEventListener("DOMContentLoaded", function() {
    
    var queryInput = document.getElementById('query');
        queryInput.addEventListener("focus", function(event) {
      event.target.value = ''; 
    });
    });
    </script>
<form action="" method="GET">
  <input id="query" name="query" value="Enter query here...">
  <input id="button" type="submit" value="Search">
</form>
"""

@app.route('/')
def main_page():
    global page_header, page_footer, main_page_markup
    nonce = secrets.token_hex(16)

    main_page_markup = main_page_markup.replace('{{nonce}}', nonce)

    response = app.make_response(page_header + main_page_markup + page_footer)

    query = request.args.get('query', '')
    if query:
        query = request.args.get('query', '[empty]')
        message = f"Sorry, no results were found for <b>{query}</b>."
        message += f" <a href='?'>Try again</a>."
        response = app.make_response(page_header + message + page_footer)

    csp_header = f"default-src 'self'; script-src 'self' 'nonce-{nonce}'"
    response.headers['Content-Security-Policy'] = csp_header

    return response



@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)


@app.route('/level2/frame')
def level2():
    nonce = secrets.token_hex(16)
    session['nonce'] = nonce
    return render_template('xss2.html', nonce=nonce)


@app.route('/level3/frame')
def level3():
    nonce = secrets.token_hex(16)
    session['nonce'] = nonce
    # header = ["X-XSS-Protection", "0"]
    return render_template('xss3.html', nonce=nonce)


@app.route('/level4/frame')
def level4():
    nonce = secrets.token_hex(16)
    session['nonce'] = nonce
    if not request.args.get('timer'):
        return render_template('index.html')
    else:
        timer = request.args.get('timer', 0)
        return render_template('timer.html', timer=timer, nonce=nonce)


@app.route('/level5/frame/')
def level5():
    nonce = secrets.token_hex(16)
    session['nonce'] = nonce
    path = request.path
    if "signup" in path:
        return render_template('signup.html', next=request.args.get('next'), nonce=nonce)
    elif "confirm" in path:
        return render_template('confirm.html', next=request.args.get('next', 'welcome'), nonce=nonce)
    else:
        return render_template('welcome.html')


@app.route('/level5/frame/signup')
def signup():
    nonce = secrets.token_hex(16)
    session['nonce'] = nonce
    return render_template('signup.html', next=request.args.get('next'), nonce=nonce)


@app.route('/level5/frame/confirm')
def confirm():
    nonce = secrets.token_hex(16)
    session['nonce'] = nonce
    return render_template('confirm.html', next=request.args.get('next', 'welcome'), nonce=nonce)


@app.route('/level5/frame/welcome')
def welcome():
    nonce = secrets.token_hex(16)
    session['nonce'] = nonce
    return render_template('welcome.html', nonce=nonce)


@app.route('/last/frame')
def level6():
    nonce = secrets.token_hex(16)
    session['nonce'] = nonce
    return render_template('xss6.html', nonce=nonce)


if __name__ == '__main__':
    app.run()
