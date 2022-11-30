import numpy as np
import pandas as pd
import math
import array as arr
from scipy.spatial import distance

import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split

import PySimpleGUI as sg

data = pd.read_csv('db.csv')

array_1 = []
array_2 = []
array_3 = []
array_4 = []
array_5 = []
array_6 = []
array_7 = []
array_8 = []
array_9 = []
array_10 = []
array_11 = []
array_12 = []
array_13 = []
array_14 = []
array_15 = []
array_16 = []
array_17 = []
array_18 = []

for i in data.Andrea_Diaz:
        array_1.append(i)

for i in data.Angela_Campuzano:
        array_2.append(i)

for i in data.Catherine_Trujillo:
        array_3.append(i)

for i in data.Daniela_Valencia:
        array_4.append(i)

for i in data.Diana_Balanta:
        array_5.append(i)

for i in data.Diego_Montero:
        array_6.append(i)

for i in data.Laura_Fajardo:
        array_7.append(i)

for i in data.Laura_Mosquera:
        array_8.append(i)

for i in data.Laura_Orozco:
        array_9.append(i)

for i in data.Laura_Reyes:
        array_10.append(i)

for i in data.Laura_Tangarife:
        array_11.append(i)

for i in data.Maria_Polanco:
        array_12.append(i)

for i in data.Mateo_Martinez:
        array_13.append(i)

for i in data.Santiago_Gutierrez:
        array_14.append(i)

for i in data.Sara_Calderon:
        array_15.append(i)

for i in data.Sara_Castillo:
        array_16.append(i)

for i in data.Valentina_Grisales:
        array_17.append(i)

for i in data.Valentina_Mueses:
        array_18.append(i)

X = [array_1, array_2, array_3, array_4, array_5, array_6, array_7, array_8, array_9,
         array_10, array_11, array_12, array_13, array_14, array_15, array_16, array_17, array_18]

names = ["Andrea Díaz", "Ángela Campuzano", "Catherine Trujillo", "Daniela Valencia", "Diana Balanta",  "Diego Montero", "Laura Fajardo", "Laura Mosquera", "Laura Orozco", "Laura Reyes", "Laura Tangarife", "Maria José Polanco", "Mateo Martínez", "Santiago Gutiérrez", "Sara Calderón", "Sara Castillo", "Valentina Grisales", "Valientina Mueses"]


# Valor arbitrario, raíz cuadrada del número total de usuarios
arbitrary_value = math.sqrt(18)
print("Valor Arbitrario:", arbitrary_value)
nbrs = NearestNeighbors(n_neighbors=10, algorithm='ball_tree').fit(X)
distances, indices = nbrs.kneighbors(X)
print("Distancias dentro del vecindario")
i = 0
for item in distances:
    print("Distancias de los usuarios con respecto al usuario ", i, "\n", item)
    i += 1
f = 0
for item in indices:
    print("Índices de los usuarios con respecto al usuario ", f,
          " (Ordenados del más cercano al más lejano)", "\n", item)
    f += 1

monitor1 = ''
monitor2 = ''
monitor3 = ''
nameChosen = ''
nameChosen1 = ''
nameChosen2 = ''
nameChosen3 = ''

def findClosest(nameChosen):
    f = 0
    for name in names:
        if names[f] in nameChosen and f != 18:
            print("Índices de los usuarios con respecto al usuario", " (Ordenados del más cercano al más lejano)", "\n", indices[f])
            return indices[f][0]
        if nameChosen == 'own':
             return indices[18][0]   
        else:
            f += 1
    

layout1 = [
        [sg.Text('Encontremos un grupo para ti')],

        [sg.Text('Evalúate a ti mism@, califica del 1 al 10 cada cualidad en tu persona, luego definiremos un grupo para ti')],
        [sg.Text('Amabilidad'), sg.InputText(key="-AMAB-")],
        [sg.Text('Respeto'), sg.InputText(key="-RESP-")],
        [sg.Text('Disposición'), sg.InputText(key="-DISP-")],
        [sg.Text('Eficiencia'), sg.InputText(key="-EFIC-")],
        [sg.Button('Definir grupo más compatible', key="-DEFINE-")],
        [sg.Text('Monitor 1: '), sg.Text('', key="-MONITOR1a-")],
        [sg.Text('Monitor 2: '), sg.Text('', key="-MONITOR2a-")],
        [sg.Text('Monitor 3: '), sg.Text('', key="-MONITOR3a-")],
]

layout2 = [
        [sg.Text('Selecciona el Monitor')],
        [sg.Listbox(values= names, key="-LIST-", enable_events=True)],
        [sg.Button('Definir los monitores más compatibles')],
        [sg.Text('Monitor 1: '), sg.Text(monitor1, key="-MONITOR1-")],
        [sg.Text('Monitor 2: '), sg.Text(monitor2, key="-MONITOR2-")],
        [sg.Text('Monitor 3: '), sg.Text(monitor3, key="-MONITOR3-")],
]

layout3 = [
        [sg.Text('Selecciona los monitores')],
        [sg.Listbox(values= names, key="-LIST2-", enable_events=True), sg.Text('Haz click en el nombre cuándo encuentres el que desees analizar')],
        [sg.Listbox(values= names, key="-LIST3-", enable_events=True), sg.Text('Haz click en el nombre cuándo encuentres el que desees analizar')],
        [sg.Listbox(values= names, key="-LIST4-", enable_events=True), sg.Text('Haz click en el nombre cuándo encuentres el que desees analizar')],
        [sg.Button('Medir Compatibilidad',  key="-COMPAT-")],
        [sg.Text('Porcentaje de compatibilidad'), sg.Text('', key="-PERCENT-"), sg.Text('%')],
]

layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(layout3, visible=False, key='-COL3-')],
          [sg.Button('Siguiente Pantalla'), sg.Button('Inicio'), sg.Button('Grupos'), sg.Button('Listas'), sg.Button('Exit')]]

window = sg.Window("Sistema de Recomendación de Monitorías de Biblioteca", layout)

layout = 1

while True:
    event, values = window.read()
    print(event, values)
    if event == 'Siguiente Pantalla':
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout + 1 if layout < 3 else 1
        window[f'-COL{layout}-'].update(visible=True)
    if event == 'Inicio':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 1
        window[f'-COL{layout}-'].update(visible=True)
    if event == 'Grupos':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 2
        window[f'-COL{layout}-'].update(visible=True)
    if event == 'Listas':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 3
        window[f'-COL{layout}-'].update(visible=True)
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    if event == '-LIST-' and len(values['-LIST-']):
        sg.Popup('Selected ', values['-LIST-'])
        nameChosen = values['-LIST-']
    if event == '-LIST2-' and len(values['-LIST2-']):
        sg.Popup('Selected ', values['-LIST2-'])
        nameChosen1 = values['-LIST2-']
    if event == '-LIST3-' and len(values['-LIST3-']):
        sg.Popup('Selected ', values['-LIST3-'])
        nameChosen2 = values['-LIST3-']
    if event == '-LIST4-' and len(values['-LIST4-']):
        sg.Popup('Selected ', values['-LIST4-'])
        nameChosen3 = values['-LIST4-']    
    if event == '-DEFINE-':
        amab = float(values['-AMAB-'])
        resp = float(values['-RESP-'])
        disp = float(values['-DISP-'])
        efic = float(values['-EFIC-'])

        array_19 = [amab, resp, disp, efic, 10]
        X.append(array_19)
        nbrs = NearestNeighbors(n_neighbors=10, algorithm='ball_tree').fit(X)
        distances, indices = nbrs.kneighbors(X)
        
        user = findClosest('own')
        window['-MONITOR1a-'].update(names[indices[user][1]])
        window['-MONITOR2a-'].update(names[indices[user][2]])
        window['-MONITOR3a-'].update(names[indices[user][3]])   
   
    if event == '-COMPAT-': 
        user1 = findClosest(nameChosen1)
        user2 = findClosest(nameChosen2)
        user3 = findClosest(nameChosen3)

        perc1 = (X[user1][0] + X[user1][1] + X[user1][2] + X[user1][3] + X[user1][4])/5
        perc2 = (X[user2][0] + X[user2][1] + X[user2][2] + X[user2][3] + X[user2][4])/5
        perc3 = (X[user3][0] + X[user3][1] + X[user3][2] + X[user3][3] + X[user3][4])/5

        percentage1 = perc1 - perc2
        percentage2 = perc2 - perc3
        percentage3 = perc3 - perc1

        finalPercentage = 100 - ((abs(percentage1) + abs(percentage2) + abs(percentage3))*100)

        window['-PERCENT-'].update(str(round(finalPercentage, 2)))

    try:
        if event == 'Definir los monitores más compatibles':
            monitor1 = findClosest(nameChosen)
            window['-MONITOR1-'].update(names[indices[monitor1][1]])
            window['-MONITOR2-'].update(names[indices[monitor1][2]])
            window['-MONITOR3-'].update(names[indices[monitor1][3]])
    except:
        print('Out of Scope')


window.close()