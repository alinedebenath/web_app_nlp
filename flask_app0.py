from flask import Flask, request
from processing import keywordizer
app = Flask(__name__)

app.config["DEBUG"] = True
@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        textf = None
        if textf is not None:
            result = keywordizer(textf)
            return '''
                <html>
                    <body>
                        <p>The result is {result}</p>
                        <p><a href="/">Click here to try again</a>
                    </body>
                </html>
            '''.format(result=result)

    return '''
        <html>
            <body>
                {errors}
                <p>Enter your text:</p>
                <form method="post" action=".">
                    <p><input name="textf" /></p>
                    <p><input type="submit" value="Return keywords" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)