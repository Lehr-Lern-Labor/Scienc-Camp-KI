from resources.code.help_functions import pruefe_eingabe
from resources.code.help_functions import pruefe_fibonacci
from resources.code.help_functions import morse, pruefe_kodiertes_wort, pruefe_dekodiertes_wort

#Datenstrukturen
# Lösung
name = "Elias"
maennlich = True
alter = 22
groesse = 1,75

# Lösung
# Ergänze unter jedem nachfolgenden Kommentar deinen Code.
x = 9

# Addiere zur Variable 'x' 6 dazu.
x = x + 6 #oder x += 6

# Multipliziere das Ergebnis mit 3. 
x = x * 3 #oder x *= 3

# Nehme das Ergebnis hoch 4 (Hochzeichen: **).
x = x ** 4 #oder x **= 4

# Teile das Ergebnis durch 91125.
x = x / 91125 #oder x /= 91125

# Subtrahiere 3 vom Ergebnis.
x = x - 3#oder x -= 3

pruefe_eingabe(x)

#Lösung
begruessung1 = 'hi'
begruessung2 = 'hallo'
begruessung3 = 'hey'

# Konkateniere alle Begrüßungen indem du die oberen String jeweils durch ein '+' verbindest
# und das Ergebnis mit der Variable 'begruessung' gleichsetzt.
begruessung = begruessung1 + begruessung2 + begruessung3

print("Konkatierter String: ", begruessung)

# Gebe den dritten und siebten Buchstaben der Variable 'begruessung' aus und überprüfe dein Ergebnis selbst. 
# Möchtest du den i-ten Buchstaben eines Strings str ausgeben lassen, schreibst du einfach str[i].
# (Beachte, dass Informatiker von 0 anfangen zu zählen!)
print(begruessung[2])
print(begruessung[6])

# Du kannst nicht nur einzelne Buchstaben eines Strings ausgeben lassen, sondern bestimmte Bereiche.
# Möchtest du von einem String str z.B. den Bereich vom fünften bis ausschließlich zum achten String ausgeben 
# lassen, machst du das durch str[5:8]. 
# Möchtest du den Bereich von Anfang bis ausschließlich dem vierten Buchstaben erhalten, 
# schreibst du str[0:4] oder str[:4]. 
# Analog schreibst du str[4:], wenn du den Bereich vom vierten bis zum letzten Buchstaben
# erhalten möchtest.

# Benutze deine vorher definierte Variable 'begruessung', um hi, hallo und hey mithilfe [] ausgeben zu lassen.
print(begruessung[0:2]) #oder print(begruessung[:2])
print(begruessung[2:7])



#Kontrollstrukturen
#Lösung
benutzer = "Jana"
passwort = True
punkteJana = 2241
punkteRamon = 2110

if benutzer == "Jana" and passwort: #alternativ passwort == True
    print(punkteJana)
elif benutzer == "Ramon" and passwort:
    print(punkteRamon)
elif not passwort: #alternativ passwort == False
    print("Falsches Passwort")
else:
    print("Nutzername unbekannt")

#Ganz alternativ: Verschachteltes if für Passwort. Gefährlich! Kann schnell unübersichtlich werden!!!

#Lösung
i = 1
sum = 0
while i <= 10: #alternativ < 11
    sum += i
    i += 1
print(sum)

#Lösung
satz = "Max wachst Wachsmasken. Was macht Max? Wachsmasken wachst Max."
countA = 0
for s in satz:
    if s == 'a':
        countA += 1
print(satz.count('a') == countA)



#Sequentielle Datentypen
#Lösung
fibonacci = [0, 1]
i = 2
while i < 15:
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    i += 1
pruefe_fibonacci(fibonacci)

#Lösung
# Die Variable 'morse' ist eine Dictionary. 
# Für jeden Großbuchstaben, Umlaut, Ziffer, Punkt, Komma und Leerzeichen 
# gibt es einen entsprechenden Eintrag in Morse-Code. 
morse = morse()

ausdruck = "KÜNSTLICHE INTELLIGENZ"
codiertes_wort = ""

# Füge deinen Code hier ein
for c in ausdruck:
    codiertes_wort += " " + morse[c]

pruefe_kodiertes_wort(codiertes_wort)

morse_code = '-. . ..- .-. --- -. .- .-.. . ... / -. . - --..'
ergebnis = ""

# Füge deinen Code hier ein
morse_list = []
while morse_code != "":
    part = morse_code.partition(" ")
    morse_list.append(part[0])
    morse_code = part[2]
for m in morse_list:
    for symbol in morse:
        if morse[symbol] == m:
            ergebnis += symbol

pruefe_dekodiertes_wort(ergebnis)
#Hinweise: string.partition("c") erstellt ein Tripel (string vor erstem c, c, rest); Dictionaries sollen nicht in beide richtungen verwendet werden



#Funktionen
#Lösung 
def fibo(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        zaehler = 2
        vorher = 1
        vorvorher = 0
        neu = vorher + vorvorher
        while zaehler < i:
            vorvorher = vorher
            vorher = neu
            neu = vorher + vorvorher
            zaehler += 1
        return neu

#alternative
def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i-1) + fib(i-2)



#Klassen
#Lösung
class Automat:

    def __init__(self, an, konto):
        self.an = an
        self.konto = konto

    def anschalten(self):
        self.an = True
    
    def ausschalten(self):
        self.an = False
    
    def muenze_einwerfen(self):
        self.konto += 1
    
    def getreank_ausgeben(self):
        if not self.an:
            return
        if self.konto > 1:
            self.konto -= 2
            print("Genießen Sie ihr Getreank!")
        else: 
            print("Zu wenig Geld!")

kaffeeAutomat = Automat(True, 1)

kaffeeAutomat.getreank_ausgeben()
kaffeeAutomat.muenze_einwerfen()
kaffeeAutomat.getreank_ausgeben()



#Sonstige Aufgaben
#Lösung
unsortierte_liste = [-2, 45, -102, 231, 89, -73, 42, 0, 99, 123, -11]
unsortierte_liste.sort()
print(unsortierte_liste)

#Lösung