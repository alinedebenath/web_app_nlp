from flask import Flask, request
from processing import keywordizer
app = Flask(__name__)

app.config["DEBUG"] = True
@app.route("/", methods=["GET", "POST"])

def adder_page():
    errors = ""
    if request.method == "POST":
        text1 = ''
        try:
            text1 = str(request.form["text1"])
        except:
            errors += "Ceci n'est pas un texte.</p>\n".format(request.form["text1"])
        if text1 is not None:
            result = keywordizer(text1)
            return '''
                <html>
                    <link rel="stylesheet" media="screen" href="static/bootstrap.min.css">
                    <link rel="stylesheet" href="static/bootstrap-theme.min.css">
                     <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <body>
                        <div class="container">
                        <p>Voici les mots-clés : </p>
                        <div class="alert alert-info">
                        <br><center>{result}</center></p>
                        </div>
                        <p><center><a href="/">Cliquez ici pour recommencer</a></center></p>
                    </div>
                    </body>
                </html>
            '''.format(result=result)

    return '''
        <html>
            <link rel="stylesheet" media="screen" href="static/bootstrap.min.css">
            <link rel="stylesheet" href="static/bootstrap-theme.min.css">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <body>
                <div class="container">
                <h2><center>Extracteur de mots-clés</center></h2>
                {errors}
                <form method="post" action="." role="form">
                <div class="form-group">
                    <textarea class="form-control" rows="6" input name="text1" placeholder="Entrez votre texte" required></textarea></div>
                    <button type="submit" class="btn btn-success">Trouver les mots-clés</button>
                </form>
                </div>
            </body>
        </html>
    '''.format(errors=errors)