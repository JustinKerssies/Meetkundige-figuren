import math
from math import sqrt
    ##1
def rechthoek(spec, lengte, breedte, null1, null2, null3):
    ## oppervlakte rechthoek
    if spec == 1:
        antwoord = lengte * breedte

    ## omtrek rechthoek
    elif spec == 2:
        antwoord = (2 * lengte) + (2 * breedte)
    return antwoord

    ## 2
def cirkel(spec, diameter, null1, null2, null3, null4):
    ## omtrek cirkel
    if spec == 2:
        antwoord = math.pi * diameter

    ## oppervlak cirkel
    elif spec == 1:
        antwoord = math.pi * ((0.5 * diameter)**2)
    return antwoord

    ## 3
def driehoek(spec, basis, hoogte, null1, null2, null3):
    ## oppervlakte driehoek                                                                            iets raar aan de hand<<<<<
    antwoord = (basis * hoogte) / 2
    return antwoord

    ## 4
def rechthoekige_driehoek(spec, a, b, null1, null2, null3):
    ## zijde C berekenen
    if spec == 1:
        antwoord = sqrt((a**2) + (b**2))

    ## zijde A of zijde B berekenen
    else:
        antwoord = sqrt((b**2) - (a**2) )
    return antwoord

    ## 5
def vlieger(spec, lengteA, lengteB, null1, null2, null3):
    ## oppervlakte vlieger berekenen
    antwoord = (lengteA * lengteB) / 2
    return antwoord

    ## 6
def kubus(spec, lengte, null1, null2, null3, null4):
    ##inhoud kubus berekenen
    antwoord = lengte**3
    return antwoord

    ## 7
def cilinder(spec, doorsnee, hoogte, null1, null2, null3):
    ## inhoud cilinder berekenen
    radius = 0.5 * doorsnee
    antwoord = math.pi * (radius**2) * hoogte
    return antwoord

    ## 8
def pyramide(spec, hoogte, breedte, null1, null2, null3):
    ## inhoud piramide berekenen
    antwoord = (breedte**2) * hoogte * (1/3)
    return antwoord

    ## 9
def parallelogram(spec, hoogte, lengte, null1, null2, null3):
    ## oppervlakte parallelogram berekenen
    antwoord = hoogte * lengte   
    return antwoord

    ## 10
def trapezium(spec, lengteAB, lengteCD, lengteBC=0, lengteDA=0, hoogte=0):
    ## oppervlakte trapezium berekenen
    if spec == 1:
        antwoord = (1/2) * (lengteAB + lengteCD) * hoogte

    ## omtrek trapezium berekenen
    elif spec == 2:
        antwoord = lengteAB + lengteBC + lengteCD + lengteDA
    return antwoord

    ## 11
def driehoekige_prisma(spec, lengte, hoogte, breedte, null1, null2):
    ## oppervlak driehoekige prisma berekenen
    if spec == 1:
        half_base = breedte/2
        lengteFD  = sqrt((hoogte**2) + (half_base**2))
        print(lengteFD)
        antwoord = 3*(lengte * lengteFD) + (hoogte * breedte)

    ## inhoud driehoekige prisma berekenen
    elif spec == 2:
        antwoord = (1/2) * hoogte * breedte * lengte
    return antwoord

    ## 12
def kegel(spec, hoogte, radius, null1, null2, null3):
        ## inhoud kegel berekenen
    if spec == 2:
        antwoord = (1/3) * hoogte * math.pi * (radius**2)

        ## oppervlak kegel berekenen
    elif spec == 1:
        bigR = sqrt((radius ** 2) + (hoogte ** 2))
        antwoord = (math.pi * (radius**2)) + (math.pi * radius * bigR)
    return antwoord

    ## 13
def bol(spec, radius, null1, null2, null3, null4):
    ## inhoud bol berekenen
    if spec == 2:
        antwoord = (4/3) * math.pi * (radius**3)

    ## oppervlak bol berekenen
    elif spec == 1:
        antwoord = 4 * math.pi * (radius**2)
    return antwoord

    ## 14
def ellips(spec, lengteAC, lengteBD, null1, null2, null3):
    
    antwoord = lengteAC * lengteBD * math.pi
    return antwoord

