# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:19:09 2026

@author: ekata
"""
#oppgave 1 
alder = int(input('Hvilket år er du født? '))
hvor_gammel = 2024 - alder

print('Du blir', hvor_gammel, 'år i løpet av 2024.')

#oppgave 2 
import math

antall_elever = int(input('Skriv inn antall elever: '))
# resultat er avrunded til nærmeste verdi 
pizzar = math.ceil(antall_elever / 4)

print('Det må handles inn', pizzar, 'pizzaer til festen.')

#oppgave 3
import numpy as np  #importerer NumPy-biblioteket
#lager en funksjon som regner om grader til radianer
def grader_til_radianer(v_grad):
    v_rad = v_grad * np.pi / 180
    return v_rad

v_grad = float(input('Skriv inn gradtallet: '))
#sender resultatet tilbake fra funksjonen
v_rad = grader_til_radianer(v_grad)
# runded svar til 2 tall 
print('Vinkelen i radianer er:', round(v_rad, 2))

#opgave 4 
#A
data = {
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Norge": ["Oslo", 0.717],
    "Tyskland": ["Berlin", 3.645],
    "Italia": ["Roma", 2.873]
}
#B
land = input("Skriv inn et land: ")

hovedstad = data[land][0]
innbyggere = data[land][1]

print(hovedstad, "er hovedstaden i", land,
      "og det er", innbyggere,
      "mill. innbyggere i", hovedstad)
#C
nytt_land = input("Skriv inn et nytt land: ")

hovedstad = input("Skriv inn hovedstaden: ")

innbyggere = float(input("Skriv inn antall innbyggere i mill.: "))

data[nytt_land] = [hovedstad, innbyggere]

print(data)

#oppgave 5 
import numpy as np

def figur(a, b):
    # Areal av halvsirkel
    A1 = np.pi * a**2 / 8

    # Areal av trekant
    A2 = a * b / 2

    # Totalt areal
    areal = A1 + A2

    # Ytre omkrets
    omkrets = np.pi * a / 2 + b + np.sqrt(a**2 + b**2)

    return areal, omkrets


a = float(input("Skriv inn a: "))
b = float(input("Skriv inn b: "))

areal, omkrets = figur(a, b)

print("Arealet er:", round(areal, 2))
print("Ytre omkrets er:", round(omkrets, 2))

#oppgave 6 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)

y = -x**2 - 5

plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Grafen til f(x) = -x² - 5")

plt.grid()
plt.show()