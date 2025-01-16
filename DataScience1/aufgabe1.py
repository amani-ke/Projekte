import netflix
shows = netflix.shows()

#Aufgabe1.1:
#In der ersten Teilaufgabe wird eine Funktion geschrieben, welche eine Liste als Übergabeparameter bekommt. Die Liste wird nach Rating durchgesucht und es in einer Menge mit Hilfe set() nur einmal gesammelt, sodass jedes Rating automatisch nur einmal gespeichert wird, wenn mehrmals vorhanden ist. Als Ausgabe haben wir dann Liste mit allen einzigartigen Ratings.
def ratings(liste):
    ergebniss = []      
    for rating in liste:  
        film = rating[7]  
        ergebniss.append(film)  
    return set(ergebniss)
ratings = str(ratings(shows))
print("Die RatingListe:\n", ratings)

#Aufgabe1.2:
#In diesem Teil wird eine Funktion geschrieben, welche eine Liste als Übergabeparameter annimmt. In dieser Funktion wird nach allen Schauspieler:innen in allen Filmen gesucht. Es wird mit Hilfe von set() automatisch nur einmal der Name des Schauspielers gespeichert, wenn er mehrmals auftaucht. Die Ausgabe liefert alle Namen der Schauspieler:innen in einer Liste zurück.
def schauspieler(liste):
    schauspieler_set = set()
    
    for show in shows:
        schauspieler_set.update(show[4]) 
    
    return schauspieler_set

print(f"Die Namen aller Schauspieler:innen:\n {schauspieler(shows)}")

#Aufgabe1.3:
#In diesem Aufgabeteil wird eine Funktion geschrieben, welche zwei Übergabeparameter (1. Name eines Films, 2. Name eines Schauspielers) bekommt. Mit dieser Funktion wird überprüft, ob ein bestimmter Schauspieler in einem bestimmten Film vorhanden ist. Als sinnvolle Ausgabe wird True/False zurückgeliefert, je nach dem, ob der Schauspieler vorhanden ist oder nicht.
def hat_schauspieler(show_name, schauspieler):
    for show in shows:
        if show[2] == show_name:
            cast = show[4] 
            return schauspieler in cast 
    return False 

print(f"{hat_schauspieler('Blood & Water', 'Ama Qamata')}, Diese/r Schauspieler:in spielt in dem vorgegebenen Film")

# Aufgabe 1.4
#In diesem Aufgabeteil wird eine Funktion shows_mit geschrieben, welche zwei Übergabeparameter (1. Liste der Filme, 2. Name eines Schauspielers) erhält. In dieser Funktion wird überprüft, in welchen Filmen ein bestimmter Schauspieler mitgespielt hat. Als Ausgabe wird eine Liste mit den Namen aller Filme für einen bestimmten Schauspieler zurückgeliefert.
def shows_mit(liste, schauspieler):
    ergebnis = []
    for show in shows:
        if schauspieler in show[4]:
            ergebnis.append(show[2])
    return ergebnis
    
show = shows_mit(shows, 'Khosi Ngema')   
print("Die Liste mit Namen der Filme für diese:n Schauspieler:in:\n", show)

# Aufgabe 1.5:
#Es wird eine Funktion kategorien_mit geschrieben, welche zwei Übergabeparameter (1. Liste der Filme, 2. Name eines Schauspielers) annimmt. Diese Funktion überprüft, in welchen Kategorien ein bestimmter Schauspieler mitgewirkt hat. Die Liste wird komplett durchgesucht und in einer Menge mit Hilfe von set() automatisch nur einmal gespeichert, falls eine Kategorie mehrmals auftaucht. Als Ausgabe wird eine Liste mit allen Kategorien zurückgeliefert, in denen ein bestimmter Schauspieler mitgewirkt hat.
def kategorien_mit(liste, schauspieler):
    kategorien = []
    for show in shows:
        if schauspieler in show[4]:
            kategorien.append(show[8])
    return kategorien

kategorien = kategorien_mit(shows, 'Khosi Ngema')
print("Die Liste mit allen Kategorien der Filme für diese:n Schauspieler:in:\n", kategorien)

# Aufgabe1.6
#In diesem Aufgabenteil wird eine Funktion anzahl_nach_schauspieler geschrieben, welche einen Übergabeparameter liste annimmt. Diese Funktion durchsucht die komplette Liste und speichert in einem Dictionary {} die Namen der Schauspieler:innen und wie oft jede:r Schauspieler:in in der Liste von Filmen vorkommt. Danach wird die Dictionary in eine Liste mit Tupeln umgewandelt => [(Schauspieler, Anzahl der Filme)] und als Ausgabe zurückgeliefert.
def anzahl_nach_schauspieler(liste):
    ergebniss = {} 
    for show in liste:  
        schauspieler = show[4]  
        for name in schauspieler:  
            if name in ergebniss:  
                ergebniss[name] += 1  
            else:
                ergebniss[name] = 1  

    endErgebniss = []  
    for name, anzahl in ergebniss.items():  
        endErgebniss.append((name, anzahl))  
    
    return endErgebniss  
print("Die Liste mit Tupeln [(Name, Anzahl der Filme)] für jede:n Schauspieler:in:\n")
anzahl_nach_schauspieler(shows[:4])

# Augabe1.7:
#In diesem Aufgabenteil wird eine Funktion beliebste_schauspieler mit einer Übergabeparameter liste geschrieben, welche mit Hilfe der Ergebnisse von der vorherigen Funktion anzahl_nach_schauspieler überprüft, welche:r Schauspieler:in am meisten in den Filmen vorkommt (maximale Anzahl). Dadurch wird der/die beliebteste Schauspieler:in erkannt. Als Ausgabe wird der Name des Schauspielers zurückgeliefert.
def beliebste_schauspieler(liste):
    anzahlListe = anzahl_nach_schauspieler(shows)
    maxShows = 0
    for schauspieler, anzahl in anzahlListe:
        if anzahl > maxShows:
            maxShows = anzahl
            
    bSchauspieler = ""
    for schauspieler, anzahl in anzahlListe:
        if anzahl == maxShows:
            bSchauspieler = schauspieler
    #return bSchauspieler, maxShows        # Ausgabe: ('Anupam Kher', 43) 
    return bSchauspieler
beliebsteSchauspieler = beliebste_schauspieler(shows)
print("Der beliebteste Schauspieler ist", beliebsteSchauspieler)
