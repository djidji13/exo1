from machine import Pin # importe dans le code la lib qui permet de gerer les Pins de sortie
import utime # importe dans le code la lib qui permet de gerer le temps

pinNumber = 2 # declaration d'une variable pinNumber à 17
led = Pin(pinNumber, mode=Pin.OUT)

pinNumber = 6 # declaration d'une variable pinNumber à 17
led1 = Pin(pinNumber, mode=Pin.OUT)

pinNumber = 10 # declaration d'une variable pinNumber à 17
led2 = Pin(pinNumber, mode=Pin.OUT)

while True:          # boucle infini
    led.toggle()
    utime.sleep(1)
    led.on()
    led.off()

    led1.toggle()
    utime.sleep(1)
    led1.on()
    led1.off()

    led2.toggle()
    utime.sleep(1)
    led2.on()
    led2.off()
De : LOUZINI Zedjiga <zedjiga.louzini@edu.devinci.fr>
Envoyé : vendredi 31 mai 2024 10:40
À : SOW-MOUVAGHA Cellou <cellou.sow-mouvagha@edu.devinci.fr>
Objet : onction lier au temps import ujson #import des fonction lier aà la convertion en Json import random from machine impor
 
import network   #import des fonction lier au wifi
import urequests  #import des fonction lier au requetes http
import utime      #import des fonction lier au temps
import ujson      #import des fonction lier aà la convertion en Json
import random
from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'Galaxy S10 5G6c46'
password = 'urfq3149'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "https://hp-api.lainocs.fr/characters/"

houses = {"Gryffindor":(30000,1000,1000),
          "Slytherin":(1000, 30000, 1000),
          "Hufflepuff":(int((227*30000)/255), 20000, 1000),
          "Ravenclaw":(int((30*30000)/255), int((144*30000)/255), 30000)}

rouge = PWM(Pin(2,mode=Pin.OUT))
rouge.freq(1_000)
vert = PWM(Pin(1,mode=Pin.OUT))
vert.freq(1_000)
bleu = PWM(Pin(0,mode=Pin.OUT))
bleu.freq(1_000)

rouge.duty_u16(0)
vert.duty_u16(0)
bleu.duty_u16(0)

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

print("GET")
r = urequests.get(url) # lance une requete sur l'url
slug = []
for item in r.json():
    slug.append(item["slug"])
r.close() # ferme la demande

try:
    rslug = random.randint(0,29)
    url = "https://hp-api.lainocs.fr/characters/"+slug[rslug]
    print("GET")
    r = urequests.get(url) # lance une requete sur l'url
    print(r.json()["name"])
    print(r.json()["house"]) # traite sa reponse en Json
    intensity = houses[r.json()["house"]]
    rouge.duty_u16(intensity[0])
    vert.duty_u16(intensity[1])
    bleu.duty_u16(intensity[2])
    r.close() # ferme la demande
    utime.sleep(1)  
except Exception as e:
    print(e)