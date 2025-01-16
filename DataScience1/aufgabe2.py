import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Daten einlesen
data_url = 'https://data.hsbo.de/imdb/'
filme = pd.read_csv(data_url + 'filme.csv')
bewertung = pd.read_csv(data_url + 'bewertungen.csv')
schauspieler = pd.read_csv(data_url + 'schauspieler.csv')
produzent = pd.read_csv(data_url + 'produzent.csv', dtype={'name': str})

# Aufgaben 2.1
# In dieser Aufgabe sollen csv-Dateien mit Hilfe von pandas abgelesen werden und 
# Fragen zu den Daten beantworten, wie zum Beispiel Anzahl der Schauspieler usw.

anzahl_filme = len(filme)
anzahl_schauspieler = len(schauspieler)
print("Anzahl der Filme:", anzahl_filme)
print("Anzahl der Schauspieler:", anzahl_schauspieler)

# 2.1.2 Wieviele Bewertungen hat ein Film im Schnitt? Wieviele maximal?
bewertungen_durchschnitt = bewertung['bewertung'].mean()
bewertungen_maximal = bewertung['bewertung'].max()

print("\nDurchschnittliche Bewertung beträgt:", bewertungen_durchschnitt)
print("Maximale Bewertung beträgt:", bewertungen_maximal)

# 2.1.3 Was sind die am besten bewerteten Filme:
beste_filme = bewertung[bewertung['bewertung'] == bewertung['bewertung'].max()]
print("\nDie besten bewerteten Filme sind:\n", beste_filme)

# 2.1.4 Bei wie vielen Filmen war George Clooney als Produzent tätig:
filme_george_clooney = produzent[produzent['name'] == "George Clooney"]
anzahl_george_clooney_filme = len(filme_george_clooney)
print("\nAnzahl der Filme, bei denen George Clooney Produzent war:", anzahl_george_clooney_filme)

# Aufgabe 2.2
# In dieser Aufgabe wird die Daten in der filme.csv Datei gelesen und mit Hilfe von matplotlib.pyplot als Balkendiagramm erstellt. 
# Das Balkendiagramm "Anzahl der erschienenen Filme pro Jahr" hat die y-Achse (Anzahl der Filme) und die x-Achse (Jahr). Damit werden die Anzahl der 
# veröffentlichten Filme für jedes Jahr angezeigt. Es wird ausgegeben, für welchen Zeitraum die Daten erschienene Filme enthalten.

filme_pro_jahr = filme.groupby('Jahr').size()
min_jahr = int(filme['Jahr'].min())
max_jahr = int(filme['Jahr'].max())

# Balkendiagramm erstellen:
filme_pro_jahr.plot(kind='bar', color='skyblue', figsize=(20, 10))
plt.title('Anzahl der erschienenen Filme pro Jahr')
plt.xlabel('Jahr')
plt.ylabel('Anzahl der Filme')
plt.xticks(rotation=0)
plt.show()

# Ausgabe des Zeitraums:
print("\nZeitraum der veröffentlichten Filme: [", min_jahr, "bis", max_jahr, "]")

# Aufgabe 2.3
# Es gab immer mal wieder externe Auswirkungen auf die Filmindustrie. 
# Sicherlich zum einen Corona, zum anderen aber auch der Streik der Drehbuchautoren in Hollywood. 
# Recherchieren Sie einen der beiden Zeiträume und schauen Sie ob vorher/während/nachher deutlich mehr/weniger Filme veröffentlicht wurden.

filme_jahr = filme.groupby('Jahr').size()
vor_corona = filme_jahr[filme_jahr.index < 2020].sum()
waehrend_corona = filme_jahr[(filme_jahr.index >= 2020) & (filme_jahr.index <= 2021)].sum()
nach_corona = filme_jahr[filme_jahr.index > 2021].sum()

print("\nAnzahl der Filme vor Corona:", vor_corona)
print("Anzahl der Filme während Corona:", waehrend_corona)
print("Anzahl der Filme nach Corona:", nach_corona)

labels = ['Vor Corona', 'Während Corona', 'Nach Corona']
values = [vor_corona, waehrend_corona, nach_corona]
plt.bar(labels, values, color=['blue', 'green', 'orange'])
plt.xlabel('Zeitraum')
plt.ylabel('Anzahl der Filme')
plt.title('Anzahl der Filme vor, während und nach Corona')
plt.show()

# Aufgabe 2.4
# In dieser Aufgabe werden die Dateien (filme, produzent und bewertung) gelesen. Danach werden die Tabellen miteinander verbunden und 
# mit Hilfe von merge auf die benötigten Daten zugegriffen, um die durchschnittlichen Bewertungen von Produzenten, 
# die mindestens 5 Filme produziert haben, zu berechnen und diese Informationen auszugeben.

produzent_filme = produzent.merge(filme, left_on='movie_id', right_on='ID', how='inner')
produzent_bewertungen = produzent_filme.merge(bewertung, left_on='ID', right_on='movie_id', how='inner')
anzahl_produzenten_filme = produzent_bewertungen.groupby('name').size()
min_produzenten = anzahl_produzenten_filme[anzahl_produzenten_filme >= 5].index
daten = produzent_bewertungen[produzent_bewertungen['name'].isin(min_produzenten)]
durchschnitt_bewertung = daten.groupby('name')['bewertung'].mean().round(2)
print("\nDurchschnittliche Bewertung für Produzenten mit mindestens 5 Filmen:\n")
print(durchschnitt_bewertung.head(10))

# Aufgabe 2.5
# In der Aufgabe werden die Daten nach dem Verbinden der Tabellen gefiltert, sodass nur Filme mit einer Bewertung von mindestens 6 
# und mehr als 5 Schauspielern berücksichtigt werden. Danach wird ein Film ausgewählt (z. B. der erste Film mit index = 0), 
# und das Durchschnittsalter der Schauspieler zum Zeitpunkt der Veröffentlichung des Films berechnet. Dazu werden das Geburtsjahr 
# der Schauspieler und das Jahr der Filmveröffentlichung verwendet. Die Lösung umfasst das Filtern, Verknüpfen und 
# Berechnen der gegebenen Daten. Als Ausgabe werden der Name des Films sowie das Durchschnittsalter der Schauspieler zum Zeitpunkt der Filmveröffentlichung zurückgegeben.

Film_Bewertung = filme.merge(bewertung, left_on='ID', right_on='movie_id')
mindest_Bewertung = Film_Bewertung[Film_Bewertung['bewertung'] >= 6.0]
film_schauspieler = mindest_Bewertung.merge(schauspieler, left_on='ID', right_on='FilmID')
schauspieler_anzahl = film_schauspieler.groupby('ID').size()
mfilm = film_schauspieler[film_schauspieler['ID'].isin(schauspieler_anzahl[schauspieler_anzahl > 5].index)]
film_id = mfilm['ID'].unique()[0]
film = filme[filme['ID'] == film_id]
film_name = film['Titel'].values[0]
film_jahr = int(film['Jahr'].values[0])
schauspieler_im_film = mfilm[mfilm['ID'] == film_id].copy()
schauspieler_im_film['Geburtsjahr'] = pd.to_numeric(schauspieler_im_film['Geburtsjahr'], errors='coerce')
schauspieler_im_film = schauspieler_im_film.dropna(subset=['Geburtsjahr'])
schauspieler_im_film['alter_zum_zeitpunkt'] = film_jahr - schauspieler_im_film['Geburtsjahr']
durchschnittsalter = schauspieler_im_film['alter_zum_zeitpunkt'].mean()
print("\nAusgewählter Film: " + film_name + " (" + str(film_jahr) + ")")
print("Durchschnittsalter der Schauspieler: " + str(round(durchschnittsalter)) + " Jahre")

# Aufgabe 2.6
# In der Aufgabe werden die Daten nach dem Filtern der Schauspieler-Tabelle so bearbeitet, dass nur die Filme berücksichtigt werden,
# in denen George Clooney mitgewirkt hat. Zuerst werden die Daten gefiltert, um alle Filme von George Clooney zu finden, indem der
# Name des Schauspielers mit "George Clooney" verglichen wird. Anschließend wird die Anzahl der einzigartigen Filme gezählt, in denen George Clooney auftritt.
# Danach werden die Daten der gefilterten Filme mit der Filmtabelle verknüpft, um die Informationen zum Jahr der Veröffentlichung 
# zu erhalten. Es wird dann die Anzahl der Filme pro Jahr berechnet, in denen George Clooney mitgespielt hat.

schauspieler_name = "George Clooney"
clooney_filme = schauspieler[schauspieler['Name'] == schauspieler_name]
film_anzahl = clooney_filme['FilmID'].nunique()
clooney_filme = clooney_filme.merge(filme, left_on='FilmID', right_on='ID', how='inner')
filme_jahr = clooney_filme.groupby('Jahr').size()
print("\nGeorge Clooney hat insgesamt in", film_anzahl, "Filmen mitgespielt.")
print("\nFilme pro Jahr:")
print(filme_jahr.to_string())
