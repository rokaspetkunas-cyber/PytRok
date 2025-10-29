from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

LESSONS = [
    {
        "title": "Pradedančiųjų pianino kursas",
        "description": "Išmok groti paprastas melodijas ir akordus, lavink ritmą bei skaityk natas.",
        "duration": "8 savaitės",
        "age_group": "Vaikai ir suaugusieji nuo 8 metų",
    },
    {
        "title": "Džiazo improvizacijos dirbtuvės",
        "description": "Atrask improvizacijos pagrindus, mokykis klausytis ir reaguoti į ansamblio narius.",
        "duration": "6 savaitės",
        "age_group": "Pažengę mokiniai",
    },
    {
        "title": "Vokalo meistriškumo pamokos",
        "description": "Kvėpavimo technikos, intonavimas ir scenos judėjimas. Individualūs ir grupiniai užsiėmimai.",
        "duration": "12 savaičių",
        "age_group": "Suaugusieji",
    },
]

TEACHERS = [
    {
        "name": "Eglė Petrauskienė",
        "instrument": "Fortepijonas",
        "bio": "Klasikinės muzikos atlikėja, turinti 10 metų pedagoginę patirtį ir mėgstanti derinti klasiką su šiuolaikiniais kūriniais.",
    },
    {
        "name": "Tomas Žilinskas",
        "instrument": "Saksofonas",
        "bio": "Džiazo saksofonininkas, koncertuojantis su įvairiais projektais Baltijos šalyse, moko improvizacijos ir sceninės drąsos.",
    },
    {
        "name": "Austėja Rimkutė",
        "instrument": "Vokalas",
        "bio": "Dainavimo coach'ė, dirbanti su pop ir soul atlikėjais, padedanti atrasti individualų balso skambesį.",
    },
]

@app.route("/")
def index():
    return render_template(
        "index.html",
        lessons=LESSONS,
        teachers=TEACHERS,
        current_year=datetime.now().year,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
