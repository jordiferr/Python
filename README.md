# Python

Recull d'algunes utilitats escrites en Python. Algunes només són poques línies per automatitzar alguna tasca.<br /><br />
D'altres són scripts per a facilitar algun càlcul, provar alguna llibreria o fins i tot aconseguir trobar una solució d'algun problema amb el que em vaig trobar a la carrera.

## <em>Calculadora resistències</em>

L'objectiu d'aquest programa era solucionar el fet d'haver de calcular les resistències optimes per projecte personal.

Per a que puguis veure a què m'estic referint, aquí tens una imatge.<br />
<br />
<img src="./Calculadora resistències/pictures/imatge_1.png" alt="Programa calculadoraResistencies_especifiques">
<br />
Bàsicament el que es mostra per pantalla és:

| Simbols | Explicació |
| :--- | :--- |
| R1 (Ω) | Resistència 1 en Ohms |
| conf | Configuració de R1 amb R2: Pot ser '+' que indica SÈRIE o '\|\|' que indica PARAL·LEL |
| R2 (Ω) | Resistència 2 en Ohms |
| Rt (Ω) | Resistència total en Ohms |
| Error (%) | Error respecte a la resistència que desitjes |

## <em>Networkx</em>

En aquest petit programa va consistir en fer proves tant amb les llibreries PyQt5 (part gràfica) així com amb la llibreria **networkx** (nucli del programa). La llibreria **networkx** permet treballar amb [grafs](https://ca.wikipedia.org/wiki/Teoria_de_grafs).<br />
La necessitat d'utilitzar-la va ser degut a les pràctiques a la univeristat, al algorisme de Dijkstra i a com plantejar xarxes.

## <em>Instagram ID to USERNAME</em>

El programa **instagram_ID_to_username** el vaig crear per la necessitat de saber interactuar amb pàgines web per demanar i/o aconseguir informació. En aquest cas, utilitzant una pàgina web tercera permet obtenir dades aparentment no accessibles per a l'usuari normal.<br />

Tant mateix les dades obtingudes no es poden utilitzar per a res, fent del projecte només una pràctica d'utilització de les següents llibreries:<br />

- BeautifulSoup (bs4)
- selenium
