let nbReponses = Number(localStorage.getItem("nbReponses")) || 0;
let nbConnexions = Number(localStorage.getItem("nbConnexions")) || 0;
let nbSeries = Number(localStorage.getItem("nbSeries")) || 0;
let nbExos = Number(localStorage.getItem("nbExos")) || 0;

// Nouvelle connexion
nbConnexions++;
localStorage.setItem("nbConnexions", nbConnexions);

// sauvegarde séries et exos (sécurité)
localStorage.setItem("nbSeries", nbSeries);
localStorage.setItem("nbExos", nbExos);

function actualiserStats(){

    document.getElementById("nbReponses").textContent = nbReponses;
    document.getElementById("nbConnexions").textContent = nbConnexions;
    document.getElementById("nbSeries").textContent = nbSeries;
    document.getElementById("nbExos").textContent = nbExos;

    calculerNiveau();
}

actualiserStats();

const banque = [

{

titre:"Exercice 1 - Théorème de Pythagore",

image:"images/pythagore.svg",

enonce:`
Dans un triangle rectangle ABC en A,
AB = 6 cm
AC = 8 cm.

Calculer BC.
`,

correction:`
BC² = 6² + 8²

BC² = 36 + 64 =100

BC =10 cm.
`

},

{

titre:"Exercice 2 - Pourcentage",

image:null,

enonce:`
Un article coûte 80 €.

Il bénéficie d'une réduction de 15%.

Calculer le prix final.
`,

correction:`
15 % de 80 =12 €

80-12=68 €

Prix final =68 €.
`

},

{

titre:"Exercice 3 - Fonctions",

image:null,

enonce:`
On considère la fonction

f(x)=3x−2

Calculer :

f(4)

f(-1)
`,

correction:`
f(4)=10

f(-1)=-5
`

},

{

titre:"Exercice 4 - Thalès",

image:"images/thales.svg",

enonce:`
Sur une figure, on sait que :

AB = 4 cm

AC = 6 cm

AE = 10 cm

Les droites (BC) et (DE) sont parallèles.

Calculer AD.
`,

correction:`
Thalès :

AB/AD = AC/AE

4/AD =6/10

AD=(4×10)/6

AD≈6,67 cm.
`

},

{

titre:"Exercice 5 - Statistiques",

image:null,

enonce:`
Voici les notes :

8 ; 10 ; 12 ; 12 ; 15 ; 18.

Calculer :

- la moyenne
- la médiane.
`,

correction:`
Moyenne :

(8+10+12+12+15+18)/6

=75/6

=12,5

Médiane=12
`

},

{

titre:"Exercice 6 - Probabilités",

image:null,

enonce:`
Une urne contient :

3 boules rouges

5 boules bleues

2 boules vertes.

On tire une boule au hasard.

Calculer la probabilité d'obtenir une boule verte.
`,

correction:`
Nombre total :

10

P(verte)=2/10=1/5=0,2
`

}

,

{
titre:"Exercice 7 - Racines carrées",

image:null,

enonce:`
Calculer :

√49

√121

5√9
`,

correction:`
√49 = 7

√121 = 11

5√9 = 15
`

},

{
titre:"Exercice 8 - Calcul littéral",

image:null,

enonce:`
Développer puis réduire :

A = 3(x+5)-2x
`,

correction:`
A = 3x+15-2x

A = x+15
`

},

{
titre:"Exercice 9 - Aire d'un disque",

image:null,

enonce:`
Un disque possède un rayon de 5 cm.

Calculer son aire.

Donner une valeur approchée au dixième.
`,

correction:`
A = π×5²

A = 25π

≈78,5 cm²
`

},

{
titre:"Exercice 10 - Volume",

image:null,

enonce:`
Un cube possède une arête de 6 cm.

Calculer son volume.
`,

correction:`
V = 6³

V = 216 cm³
`

},

{
titre:"Exercice 11 - Vitesse",

image:null,

enonce:`
Une voiture parcourt 180 km en 2 h.

Calculer sa vitesse moyenne.
`,

correction:`
v = d / t

v = 180 / 2

v = 90 km/h
`

},

{
titre:"Exercice 12 - Équation",

image:null,

enonce:`
Résoudre :

5x + 7 = 27
`,

correction:`
5x = 20

x = 4
`

},

{
titre:"Exercice 13 - Fraction",

image:null,

enonce:`
Calculer :

2/3 + 1/6
`,

correction:`
2/3 = 4/6

4/6 + 1/6 = 5/6
`

},

{
titre:"Exercice 14 - Puissances",

image:null,

enonce:`
Calculer :

2³ × 2⁴
`,

correction:`
2³ × 2⁴ = 2⁷

=128
`

},

{
titre:"Exercice 15 - Proportionnalité",

image:null,

enonce:`
5 kg de pommes coûtent 12 €.

Quel est le prix de 8 kg ?
`,

correction:`
12 ÷ 5 = 2,4 €/kg

2,4 × 8 = 19,2 €

Réponse : 19,20 €
`

},

{
titre:"Exercice 16 - Moyenne",

image:null,

enonce:`
Les notes sont :

14 ; 13 ; 17 ; 16.

Calculer la moyenne.
`,

correction:`
(14+13+17+16)/4

60/4

=15
`

},

{
titre:"Exercice 17 - Probabilité",

image:null,

enonce:`
On lance un dé équilibré.

Quelle est la probabilité d'obtenir un nombre supérieur à 4 ?
`,

correction:`
Nombres favorables :

5 et 6

P = 2/6 = 1/3
`

},

{
titre:"Exercice 18 - Théorème de Pythagore",

image:null,

enonce:`
Dans un triangle rectangle,

AB = 5 cm

BC = 13 cm.

Calculer AC.
`,

correction:`
BC² = AB² + AC²

169 = 25 + AC²

AC² = 144

AC = 12 cm
`
}

,

{
titre:"Exercice 19 - Pourcentage",

image:null,

enonce:`
Un pantalon coûte 120 €.

Il bénéficie d'une réduction de 25 %.

Calculer son nouveau prix.
`,

correction:`
25 % de 120 = 30 €

120 - 30 = 90 €

Le nouveau prix est de 90 €.
`

},

{
titre:"Exercice 20 - Équation",

image:null,

enonce:`
Résoudre :

7x - 5 = 30
`,

correction:`
7x = 35

x = 5
`

},

{
titre:"Exercice 21 - Calcul littéral",

image:null,

enonce:`
Réduire :

4x + 3 - 2x + 8
`,

correction:`
4x - 2x = 2x

3 + 8 = 11

Résultat :

2x + 11
`

},

{
titre:"Exercice 22 - Aire d'un triangle",

image:null,

enonce:`
Un triangle possède :

base = 12 cm

hauteur = 5 cm

Calculer son aire.
`,

correction:`
A = (12 × 5) / 2

A = 30 cm²
`

},

{
titre:"Exercice 23 - Cercle",

image:null,

enonce:`
Calculer le périmètre d'un cercle de rayon 7 cm.

Donner une valeur approchée au dixième.
`,

correction:`
P = 2πr

P = 14π

≈ 44,0 cm
`

},

{
titre:"Exercice 24 - Volume d'un pavé droit",

image:null,

enonce:`
Un pavé droit mesure :

8 cm

5 cm

3 cm

Calculer son volume.
`,

correction:`
V = 8 × 5 × 3

V = 120 cm³
`

},

{
titre:"Exercice 25 - Fonction",

image:null,

enonce:`
On considère :

g(x)=2x+7

Calculer :

g(5)

g(-2)
`,

correction:`
g(5)=17

g(-2)=3
`

},

{
titre:"Exercice 26 - Fraction",

image:null,

enonce:`
Calculer :

3/4 - 1/8
`,

correction:`
3/4 = 6/8

6/8 - 1/8 = 5/8
`

},

{
titre:"Exercice 27 - Puissances",

image:null,

enonce:`
Calculer :

10³ × 10²
`,

correction:`
10³ × 10² = 10⁵

=100000
`

},

{
titre:"Exercice 28 - Statistiques",

image:null,

enonce:`
Calculer l'étendue de la série :

5 ; 8 ; 11 ; 15 ; 19.
`,

correction:`
Étendue = maximum - minimum

19 - 5 = 14
`

},

{
titre:"Exercice 29 - Probabilité",

image:null,

enonce:`
Une urne contient :

4 boules rouges

6 boules noires.

Calculer la probabilité de tirer une boule rouge.
`,

correction:`
Nombre total = 10

P(rouge)=4/10=2/5=0,4
`

},

{
titre:"Exercice 30 - Théorème de Pythagore",

image:null,

enonce:`
Dans un triangle rectangle,

AB = 9 cm

AC = 12 cm.

Calculer BC.
`,

correction:`
BC² = 9² + 12²

BC² = 81 + 144

BC² = 225

BC = 15 cm
`
}

,

{
titre:"Exercice 31 - Calcul littéral",

image:null,

enonce:`
Développer :

A = 5(x-3)
`,

correction:`
A = 5x - 15
`

},

{
titre:"Exercice 32 - Équation",

image:null,

enonce:`
Résoudre :

4x + 9 = 29
`,

correction:`
4x = 20

x = 5
`

},

{
titre:"Exercice 33 - Fraction",

image:null,

enonce:`
Calculer :

5/6 + 1/3
`,

correction:`
1/3 = 2/6

5/6 + 2/6 = 7/6
`

},

{
titre:"Exercice 34 - Pourcentage",

image:null,

enonce:`
Une télévision coûte 600 €.

Son prix augmente de 8 %.

Quel est son nouveau prix ?
`,

correction:`
8 % de 600 = 48 €

600 + 48 = 648 €
`

},

{
titre:"Exercice 35 - Fonction",

image:null,

enonce:`
On considère :

h(x)=5-x

Calculer :

h(2)

h(-3)
`,

correction:`
h(2)=3

h(-3)=8
`

},

{
titre:"Exercice 36 - Aire",

image:null,

enonce:`
Un rectangle mesure :

15 cm de longueur

8 cm de largeur.

Calculer son aire.
`,

correction:`
15 × 8 = 120 cm²
`

},

{
titre:"Exercice 37 - Volume d'un cylindre",

image:null,

enonce:`
Un cylindre possède :

rayon = 3 cm

hauteur = 10 cm

Exprimer son volume en fonction de π.
`,

correction:`
V = πr²h

V = π × 3² × 10

V = 90π cm³
`

},

{
titre:"Exercice 38 - Vitesse",

image:null,

enonce:`
Un cycliste parcourt 54 km en 3 heures.

Calculer sa vitesse moyenne.
`,

correction:`
54 ÷ 3 = 18 km/h
`

},

{
titre:"Exercice 39 - Probabilité",

image:null,

enonce:`
On lance une pièce équilibrée.

Quelle est la probabilité d'obtenir Face ?
`,

correction:`
Deux issues possibles.

P(Face)=1/2
`

},

{
titre:"Exercice 40 - Statistiques",

image:null,

enonce:`
Calculer la médiane de la série :

4 ; 7 ; 9 ; 12 ; 15.
`,

correction:`
La série est déjà rangée.

La médiane est 9.
`

},

{
titre:"Exercice 41 - Théorème de Pythagore",

image:null,

enonce:`
Dans un triangle rectangle,

AB = 8 cm

BC = 17 cm

Calculer AC.
`,

correction:`
BC² = AB² + AC²

289 = 64 + AC²

AC² = 225

AC = 15 cm
`

},

{
titre:"Exercice 42 - Puissances",

image:null,

enonce:`
Calculer :

3² × 3³
`,

correction:`
3² × 3³ = 3⁵

=243
`
}

,

{
titre:"Exercice 43 - Trigonométrie",

image:null,

enonce:`
Dans un triangle rectangle,

un angle mesure 30°.

Le côté adjacent mesure 8 cm.

Exprimer le calcul permettant de trouver l'hypoténuse.
`,

correction:`
cos(30°)=8/h

h=8/cos(30°)

h≈9,2 cm
`

},

{
titre:"Exercice 44 - Équation",

image:null,

enonce:`
Résoudre :

9x-18=45
`,

correction:`
9x=63

x=7
`

},

{
titre:"Exercice 45 - Pourcentage",

image:null,

enonce:`
Un ordinateur coûte 750 €.

Il bénéficie d'une réduction de 12 %.

Calculer son nouveau prix.
`,

correction:`
12 % de 750 = 90 €

750-90=660 €

Le nouveau prix est 660 €.
`

},

{
titre:"Exercice 46 - Fonction",

image:null,

enonce:`
On considère :

f(x)=x²+1

Calculer :

f(2)

f(5)
`,

correction:`
f(2)=5

f(5)=26
`

},

{
titre:"Exercice 47 - Statistiques",

image:null,

enonce:`
Voici la série :

12 ; 15 ; 13 ; 18 ; 10.

Calculer la moyenne.
`,

correction:`
(12+15+13+18+10)/5

68/5

=13,6
`

},

{
titre:"Exercice 48 - Fraction",

image:null,

enonce:`
Calculer :

7/8-3/8
`,

correction:`
7/8-3/8=4/8

=1/2
`

},

{
titre:"Exercice 49 - Théorème de Pythagore",

image:null,

enonce:`
Dans un triangle rectangle,

AB=7 cm

AC=24 cm.

Calculer BC.
`,

correction:`
BC²=7²+24²

BC²=49+576

BC²=625

BC=25 cm
`

},

{
titre:"Exercice 50 - Probabilités",

image:null,

enonce:`
Une roue est partagée en 8 secteurs identiques.

3 secteurs sont rouges.

Calculer la probabilité d'obtenir un secteur rouge.
`,

correction:`
P(rouge)=3/8

=0,375
`

}
];


function melanger(tab){
    nbSeries++;
    return [...tab].sort(()=>Math.random()-0.5);
}

function afficher(){

    const zone = document.getElementById("questions");
    zone.innerHTML = "";

    const liste = melanger(banque).slice(0,3);

    liste.forEach((q, i)=>{

        const idUnique = q.titre; // identifiant stable

        const div = document.createElement("div");
        div.className = "question";

        div.innerHTML = `
            <h2>${q.titre}</h2>

            <p>${q.enonce.replace(/\n/g,"<br>")}</p>

            ${q.image ? `<img src="${q.image}">` : ""}

            <button onclick="voirCorrection('${idUnique}', ${i})">
                Voir la correction
            </button>

            <div class="correction" id="c${i}" data-id="${idUnique}">
                ${q.correction.replace(/\n/g,"<br>")}
            </div>
        `;

        zone.appendChild(div);
    });

    // compteur de séries
    nbExos += 3;
    localStorage.setItem("nbExos", nbExos);
    actualiserStats();
}

afficher();

document.getElementById("reload").onclick = afficher;


// VERSION ROBUSTE DU COMPTEUR DE CORRECTION
function voirCorrection(idUnique, i){

    const correction = document.getElementById("c"+i);

    if(correction.style.display === "block"){
        return;
    }

    correction.style.display = "block";

    // éviter double comptage
    let dejaVu = JSON.parse(localStorage.getItem("correctionsVues")) || {};

    if(!dejaVu[idUnique]){

        dejaVu[idUnique] = true;

        nbReponses++;
        localStorage.setItem("nbReponses", nbReponses);

        localStorage.setItem("correctionsVues", JSON.stringify(dejaVu));

        actualiserStats();
    }
}

function calculerNiveau(){

    let n = nbReponses;

    let niveau = "Débutant";

    if(n >= 10) niveau = "Novice";
    if(n >= 25) niveau = "Intermédiaire";
    if(n >= 50) niveau = "Bon niveau";
    if(n >= 100) niveau = "Très bon niveau";
    if(n >= 200) niveau = "Expert";
    if(n >= 400) niveau = "Préparation Brevet ++";

    document.getElementById("niveau").textContent = niveau;
}