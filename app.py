import os
import json
from flask import Flask, render_template, abort

app = Flask(__name__)


def lataa_opiskelijat():
    students_dir = "students"
    opiskelijat = []

    if not os.path.isdir(students_dir):
        return opiskelijat

    for filename in os.listdir(students_dir):
        if not filename.endswith(".json"):
            continue

        path = os.path.join(students_dir, filename)

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not all(k in data for k in ("nimi", "reitti", "tervehdys")):
                print(f"Ohitetaan {filename}: puuttuvia kenttiä")
                continue

            reitti = str(data["reitti"]).strip()
            if not reitti.startswith("/"):
                reitti = "/" + reitti

            opiskelijat.append({
                "nimi": str(data["nimi"]).strip(),
                "reitti": reitti,
                "tervehdys": str(data["tervehdys"]).strip(),
            })

        except Exception as e:
            print(f"Virhe tiedostossa {filename}: {e}")

    opiskelijat.sort(key=lambda x: x["nimi"].lower())
    return opiskelijat


@app.route("/")
def etusivu():
    opiskelijat = lataa_opiskelijat()
    return render_template("etusivu.html", opiskelijat=opiskelijat)


@app.route("/<slug>")
def opiskelijasivu(slug):
    opiskelijat = lataa_opiskelijat()
    haettu_reitti = f"/{slug}"

    for opiskelija in opiskelijat:
        if opiskelija["reitti"] == haettu_reitti:
            return render_template(
                "opiskelija.html",
                nimi=opiskelija["nimi"],
                tervehdys=opiskelija["tervehdys"]
            )

    abort(404)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
