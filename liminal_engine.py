from operator import truediv
from sqlite3 import paramstyle
from tkinter import CURRENT
import requests
import json
from bs4 import BeautifulSoup

def beautify_json(json_parse):
    print(json.dumps(json_parse, indent=4, sort_keys=True))

assig_url = "https://api.fib.upc.edu/v2/quadrimestres/2021Q2/assignatures/?format=json"
schedule_url = "https://api.fib.upc.edu/v2/quadrimestres/2021Q2/classes/?format=json"
professor_url = "https://api.fib.upc.edu/v2/professors/?format=json"
exams_url = "https://api.fib.upc.edu/v2/quadrimestres/2021Q2/examens/?format=json"

public_params = {'client_id':'NnZ0cbOGjQPSWwDUtDCdRfNj9UuyJJcQbL0rGyB9'}

def order_schedule(s):
    changes = True

    while changes:
        changes = False
        i = 0
        while len(s) - 1 > i:
            if s[i]['inici'] > s[i + 1]['inici']:
                changes = True
                aux = s[i]
                s[i] = s[i + 1]
                s[i + 1] = aux
            i += 1
    return s

def schedule_to_matrix(s):
    current = s[0]['inici']
    matrix = []
    l_copy = ['','', '', '', '', '']
    l_copy[0] = current
    for assig in s:
        print(assig)
        if current == assig['inici']:
           l_copy[assig['dia_setmana']] = assig['codi_assig'] + ' ' + assig['tipus'] + ' ' + assig['aules']
        else:
           matrix.append(l_copy)
           current = assig['inici']
           l_copy = ['','', '', '', '', '']
           l_copy[0] = current
    
    return matrix

def get_subject_list():
    assig = requests.get(assig_url, params=public_params).json()
    return assig['results']

def get_schedule_list():
    schedule = requests.get(schedule_url, params=public_params).json()
    return schedule['results']

def filter_schedule(lang: str, code: str, type: str, schedule: json):
    list = []
    for assig in schedule:
        lang_bool = lang == 'null' or lang in assig['idioma']
        code_bool = code == assig['codi_assig']
        type_bool = type == 'null' or type == assig['tipus']

        if lang_bool and code_bool and type_bool:
            list.append(assig)

    return order_schedule(list)

# PROFESSOR

def get_professor(nom_actual, cognom_actual):
    professors = requests.get(professor_url, params=public_params).json()
    llista = []

    for professor in professors:
        bool_cognom = cognom_actual in professor['cognoms']
        bool_nom = nom_actual in professor['nom']
        if (((bool_cognom and bool_nom) or (nom_actual == 'null' and bool_cognom) or (cognom_actual == 'null' and bool_nom))) and professor['futur_url'] != "":

            r = requests.get("https://directori.upc.edu/directori/dadesPersona.jsp?id=" + professor['futur_url'].replace("https://futur.upc.edu/",""))

            soup = BeautifulSoup(r.content, 'html.parser')
            s = soup.find('span', class_='mail')
            mail = s.contents[0].strip() + '@' + s.contents[2].strip()

            llista.append(mail.lower())
    return llista


def get_exam(assignatures_actuals):
    assignatures = requests.get(exams_url, params=public_params).json()['results']
    llista = []

    for assignatura in assignatures:
        for assignatura_actual in assignatures_actuals:
            if(assignatura['assig'] == assignatura_actual):
                nom = assignatura['assig']
                tipus = assignatura['inici'][10]
                data = assignatura['inici'][0:10]
                hora = assignatura['inici'][11:19]
                llista.append([nom, tipus, data, hora])
    return llista
               

def fix_exams(exams):
    s = ""
    for exam in exams:
        s += exam[0] + ' ' + exam[1] + ' ' + exam[2] + ' ' + exam[3] + '\n'
    
    return s

