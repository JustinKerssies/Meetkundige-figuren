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
    print("///////////////////////////////////////////////////////////////////////////////////\n")
    print("\ndit zijn de figuren die je kunt uitrekenen")
    for figuren in formulas:
        print(f'{figuren} : {str(formulas[figuren][0])}')

    var_cont = True
    while var_cont:
        question_input = input("\nwelk figuur wil je iets voor uitrekenen ('q om te stoppen') ")
        if question_input == 'q' or question_input == 'Q':
            print('Jammer! Volgende keer beter!')
            cont = False
            break
        else:
            try:
                question_input = float(question_input)
                var_cont = confirmation_test(0, question_input, formulas)
            except ValueError:
                print("please enter either a number or 'q'")

    ## user heeft een nummer gekozen
    else:
        ## zet alle variabelen van vorige run op 0
        variables = [0,0,0,0,0]
        i = 0

        ## wat wil user berekenen van input(question_input)
        ## voor alle mogelijkheden in [opties], print vraag
        print(f"\nwat wil je berekenen van de {formulas[question_input][0]}? vul de nummer in\n")
        for optie in opties[question_input]:
            d = i
            i = i+1
            print(f"{i} : {opties[question_input][d]}")
        
        var_cont = True
        while var_cont:
            try: 
                spec_input = float(input("\n"))
                var_cont = confirmation_test(1, spec_input, opties[question_input])
            except ValueError:
                print('enter a number')
        

        ## vragen om bevestiging van opties
        var_cont = True
        confirm_input = int(spec_input - 1)
        message = f"\nwil je de {opties[question_input][confirm_input]} van een {formulas[question_input][0]} berekenen? (y/n) : "
        while var_cont:
            confirmation = input(message)
            var_cont = confirmation_test(0, confirmation, opties['default'])
        if confirmation == 'n' or confirmation == 'N':
            continue

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
            var_cont = True
            if var == "hoogte (h)":
                i = 4
            while var_cont:
                try:
                    var_input = float(input(f'wat is de {figures[question_input][spec_input][d]} : '))
                    variables[i] = var_input
                    i = i + 1
                    var_cont = False
                except ValueError:
                    print("invalid. please enter a number\n")
                

        ## gebruik formule van testmathlibraries.py en rond antwoord af
        answer = formulas[question_input][1](spec_input, variables[0], variables[1], variables[2], variables[3], variables[4])
        answer = round(answer, 2)


        ## einde
        print(f"\nhet antwoord is {str(answer)}\n")









