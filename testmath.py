## hier is gebruik gemaakt van 2 addons, namelijk:

## testmathaddon.py is een programma waar alle formules in verwerkt worden. 
## Deze wordt aangeslagen rond //lijn 60

## testmathlibraries.py is waar informatie wordt opgeslagen zoals welke variablen nodig zijn, 
## welke formules te gebruiken en linkt de nummers en figuren aan elkaar 
## ['example'] betekent een library in testmathlibraries

from testmathaddon import *
from testmathlibraries import *
from PIL import Image

cont = True
while cont:
    ## geef de nummers en de bijbehoorende figuren en vraag voor input
    print("\ndit zijn de figuren die je kunt uitrekenen")
    for figuren in formulas:
        print(f'{figuren} : {str(formulas[figuren][0])}')
    question_input = input("\nwelk figuur wil je iets voor uitrekenen ('q om te stoppen') ")

    ## check of user wil stoppen ('q'). Zo ja? Eindig whileloop
    if question_input == 'q' or question_input == 'Q':
        print('Jammer! Volgende keer beter!')
        cont = False
        break

    ## user heeft een nummer gekozen
    else:
        ## zet alle variabelen van vorige run op 0 en zet variable om naar float
        variables = [0,0,0,0,0]
        i = 0
        question_input = float(question_input)

        ## wat wil user berekenen van input(question_input)
        ## voor alle mogelijkheden in [opties], print vraag
        print(f"\nwat wil je berekenen van de {formulas[question_input][0]}? vul de nummer in\n")
        for optie in opties[question_input]:
            d = i
            i = i+1
            print(f"{i} : {opties[question_input][d]}")
        spec_input = float(input(""))

        ## vragen om bevestiging van opties
        confirm_input = spec_input - 1
        print(formulas[question_input][0])
        print(f"wil je de {opties[confirm_input]} van {formulas[question_input][0]} berekenen?")

        ## reset i voor toekomstig gebruik
        ## laat image zien. link staat in [formulas] op plaats 3
        i = 0
        im = Image.open(formulas[question_input][2])
        im.show()
        print('\n')

        ## voor elke benodigde variabele, print de vraag (benodigde variabelen staan in [figures])
        ## scheid d en i zodat je locatie kan veranderen zonder problemen te veroorzaken met [figures]
        for var in figures[question_input][spec_input]:
            d = i 
            if var == "hoogte (h)":
                i = 4
            variables[i] = float(input(f'wat is de {figures[question_input][spec_input][d]} : '))
            i = i + 1

        ## gebruik formule van testmathlibraries.py en rond antwoord af
        answer = formulas[question_input][1](spec_input, variables[0], variables[1], variables[2], variables[3], variables[4])
        answer = round(answer, 2)


        ## einde
        print(f"\nhet antwoord is {str(answer)}\n")
        print("///////////////////////////////////////////////////////////////////////////////////\n")







