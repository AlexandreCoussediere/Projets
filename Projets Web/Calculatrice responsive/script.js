function appendToDisplay(value) {
    document.getElementById('display').value += value;
}

function clearDisplay() {
    document.getElementById('display').value = '';
}

function deleteLastCharacter() {
    const display = document.getElementById('display');
    display.value = display.value.slice(0, -1);
}

function calculateResult() {
    const display = document.getElementById('display');
    try {
        // Remplacer 'x²' par une opération de puissance
        display.value = display.value.replace(/x²/g, '**2');
        // Remplacer '1/x' par l'opération de réciproque
        display.value = display.value.replace(/1\/([^ ]+)/g, '1/$1');
        // Remplacer '√x' par l'opération de racine carrée
        display.value = display.value.replace(/Math.sqrt\(([^)]+)\)/g, 'Math.sqrt($1)');
        
        // Évaluer l'expression
        display.value = eval(display.value);
    } catch (error) {
        display.value = 'Erreur';
        setTimeout(() => {
            clearDisplay();
        }, 2000); // Efface l'affichage après 2 secondes
    }
}

// Fonction pour gérer l'inversion positif/négatif
function toggleSign() {
    const display = document.getElementById('display');
    if (display.value) {
        // Si le premier caractère est un '-' on l'enlève, sinon on l'ajoute
        display.value = display.value.charAt(0) === '-' ? display.value.slice(1) : '-' + display.value;
    }
}

// Fonction pour ajouter un point décimal
function appendDecimalPoint() {
    const display = document.getElementById('display');
    // Vérifie qu'il n'y a pas déjà un point dans l'affichage
    if (!display.value.includes('.')) { 
        display.value += '.';
    }
}
function calculateInverse() {
    const display = document.getElementById('display');
    const currentValue = parseFloat(display.value);
    if (!isNaN(currentValue) && currentValue !== 0) {
        display.value = (1 / currentValue).toString();
    } else {
        display.value = 'Erreur'; // Affiche une erreur si le nombre est zéro ou non valide
        setTimeout(() => {
            clearDisplay();
        }, 2000); // Efface l'affichage après 2 secondes
    }
}
function calculateSquare() {
    const display = document.getElementById('display');
    const currentValue = parseFloat(display.value);
    if (!isNaN(currentValue)) {
        display.value = (currentValue ** 2).toString(); // Calcul du carré
    } else {
        display.value = 'Erreur'; // Affiche une erreur si la valeur n'est pas valide
        setTimeout(() => {
            clearDisplay();
        }, 2000); // Efface l'affichage après 2 secondes
    }
}
function calculateSquareRoot() {
    const display = document.getElementById('display');
    const currentValue = parseFloat(display.value);
    if (!isNaN(currentValue) && currentValue >= 0) {
        display.value = Math.sqrt(currentValue).toString(); // Calcul de la racine carrée
    } else {
        display.value = 'Erreur'; // Affiche une erreur si la valeur est négative ou non valide
        setTimeout(() => {
            clearDisplay();
        }, 2000); // Efface l'affichage après 2 secondes
    }
}