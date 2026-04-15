# Opetusdemo — Flask-webserveri

Yksinkertainen webserveri jossa jokainen opiskelija lisää oman sivunsa.

## Käynnistys Dockerilla

```bash
docker build -t opetusdemo .
docker run -p 5000:5000 opetusdemo
```

Avaa selaimessa: http://localhost:5000

## Tehtäväsi

Lisää oma sivusi tekemällä muutokset `app.py`-tiedostoon:

### 1. Lisää itsesi OPISKELIJAT-listaan

```python
OPISKELIJAT = [
    {"nimi": "Esimerkki (opettaja)", "reitti": "/esimerkki", "tervehdys": "Hei!"},
    {"nimi": "Matti M", "reitti": "/matti", "tervehdys": "Moikka maailma!"},  # ← lisää tämä
]
```

### 2. Lisää oma reitti

```python
@app.route("/matti")
def matti():
    return render_template("opiskelija.html", nimi="Matti M", tervehdys="Moikka maailma!")
```

### 3. Tee commit ja pull request

```bash
git checkout -b oma-nimi/lisaa-oma-sivu
git add app.py
git commit -m "Lisää Matti M:n sivu"
git push origin oma-nimi/lisaa-oma-sivu
```

Avaa sen jälkeen Pull Request GitHubissa.
