from testmathaddon import *

    ## het linken van de formules en de cijfers
formulas = {
    1: ['rechthoek', rechthoek, 'C:\\Images\\rechthoek.png'],
    2: ['cirkel', cirkel, 'C:\\Images\\cirkel.png'],
    3: ['driehoek', driehoek, 'C:\\Images\\driehoek.png'],
    4: ['rechthoekige driehoek', rechthoekige_driehoek, 'C:\\Images\\rechthoekige_driehoek.png'],
    5: ['vlieger', vlieger, 'C:\\Images\\vlieger2.png'],
    6: ['kubus', kubus, 'C:\\Images\\kubus.jpg'],
    7: ['cilinder', cilinder, 'C:\\Images\\cilinder.jpeg'],
    8: ['piramide', pyramide, 'C:\\Images\\piramide.jpg'],
    9: ['parallelogram', parallelogram, 'C:\\Images\\parallelogram.png'],
    10: ['trapezium', trapezium, 'C:\\Images\\trapezium.png'],
    11: ['driehoekige prisma', driehoekige_prisma, 'C:\\Images\\driehoekige_prisma.png'],
    12: ['kegel', kegel, 'C:\\Images\\kegel.png'],
    13: ['bol', bol, 'C:\\Images\\bol.png'],
    14: ['ellips', ellips, 'C:\\Images\\ellips.png']
}

    ## benodigde variabelen voor de formules
figures = {
    1: { 1: ["lengte", "breedte"],
         2: ["lengte", "breedte"]},
    2: { 1: ["diameter (d)"],
         2: ["diameter (d)"]},
    3: { 1: ["basis lengte", "hoogte"]},
    4: { 1: ["lengte van a", "lengte van b"], 
         2: ["lengte van a/b", "lengte van c"]},
    5: { 1: ["lengte van AC", "lengte van lengte BD"]},
    6: { 1: ["lengte van één van de zijden"]},
    7: { 1: ["diameter", "hoogte"]},
    8: { 1: ["hoogte", "breedte"]},
    9: { 1: ["hoogte", "lengte van zijde A"]},
    10: { 1: ["lengte van zijde AB", "lengte van zijde CD", "hoogte (h)"],
          2: ["lengte van zijde AB", "lengte van zijde CD",
              "lengte van zijde BC", "lengte van zijde DA"]},
    11: { 1: ["lengte (AD)", "hoogte (F tot basis DE)", "basis (DE)"],
          2: ["lengte (AD)", "hoogte (F tot basis DE)", "basis (DE)"]},
    12: { 1: ["hoogte", "radius"],
          2: ["hoogte", "radius"]},
    13: { 1: ["straal"],
          2: ["straal"]},
    14: { 1: ["lengte van AO", "lengte van BO"]}
}

    ## mogelijke opties voor berekeningen
opties = {
    1:  ["oppervlakte", "omtrek"],
    2:  ["oppervlakte", "omtrek"],
    3:  ["oppervlakte"],
    4:  ["a / b berekenen", "c berekenen"],
    5:  ["oppervlakte"],
    6:  ["inhoud"],
    7:  ["inhoud"],
    8:  ["inhoud"],
    9:  ["oppervlakte"],
    10: ["oppervlakte", "omtrek"],
    11: ["oppervlakte", "inhoud"],
    12: ["oppervlakte", "inhoud"],
    13: ["oppervlakte", "inhoud"],
    14: ["oppervlakte"]

}