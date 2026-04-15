from flask import Flask, render_template

app = Flask(__name__)

# ------------------------------------------------------------
# OPISKELIJATEHTÄVÄ:
# Lisää oma reitti tähän listaan!
# Muoto: {"nimi": "Matti M", "reitti": "/matti", "tervehdys": "Moikka!"}
# ------------------------------------------------------------
OPISKELIJAT = [
    {"nimi": "Esimerkki (opettaja)", "reitti": "/esimerkki", "tervehdys": "Hei! Tämä on esimerkkisivu."},
]


@app.route("/")
def etusivu():
    return render_template("etusivu.html", opiskelijat=OPISKELIJAT)


@app.route("/esimerkki")
def esimerkki():
    return render_template("opiskelija.html", nimi="Esimerkki (opettaja)", tervehdys="Hei! Tämä on esimerkkisivu.")


# ------------------------------------------------------------
# Opiskelijat lisäävät oman reitin tähän, esim:
#
# @app.route("/matti")
# def matti():
#     return render_template("opiskelija.html", nimi="Matti M", tervehdys="Moikka!")
# ------------------------------------------------------------


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
