// a. Find a Series of Even-Odd Numbers
function evenOddSeries() {
    const limit = parseInt(document.getElementById('limit').value);
    const evenNumbers = [];
    const oddNumbers = [];

    if (isNaN(limit) || limit < 0) {
        document.getElementById('even-odd-output').innerHTML = 'Please enter a valid positive number.';
        return;
    }

    for (let i = 0; i <= limit; i++) {
        if (i % 2 === 0) {
            evenNumbers.push(i);
        } else {
            oddNumbers.push(i);
        }
    }

    document.getElementById('even-odd-output').innerHTML = `<strong>Even Numbers:</strong> ${evenNumbers.join(", ")} <br> <strong>Odd Numbers:</strong> ${oddNumbers.join(", ")}`;
}

// b. Basic Mathematical Calculator
function calculate() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const operator = document.getElementById('operator').value;
    let result;

    if (isNaN(num1) || isNaN(num2)) {
        document.getElementById('calculator-output').innerHTML = 'Please enter valid numbers.';
        return;
    }

    switch (operator) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            result = num2 !== 0 ? num1 / num2 : 'Error: Division by zero';
            break;
        default:
            result = 'Invalid operator';
    }
    document.getElementById('calculator-output').innerHTML = `<strong>Result:</strong> ${result}`;
}

// c. Replace Characters in a String
function replaceCharacter() {
    const str = document.getElementById('replace-str').value;
    const charToReplace = document.getElementById('char-to-replace').value;
    const replacementChar = document.getElementById('replacement-char').value;

    if (!charToReplace || replacementChar.length !== 1) {
        document.getElementById('replace-output').innerHTML = 'Please enter a single character for replacement.';
        return;
    }

    const newString = str.split(charToReplace).join(replacementChar);
    document.getElementById('replace-output').innerHTML = `<strong>Replaced String:</strong> ${newString}`;
}

// d. Sort Words in Alphabetical Order
// d. Sort Words in Alphabetical Order
function sortWords() {
    const str = document.getElementById('sort-str').value;
    
    // Check if input is empty
    if (!str.trim()) {
        document.getElementById('sort-output').innerHTML = 'Please enter a string with words.';
        return;
    }

    // Split the string into words, trim each word, and remove empty strings
    const words = str.split(/\s+/).map(word => word.trim()).filter(word => word.length > 0);

    // Check if there are words to sort
    if (words.length === 0) {
        document.getElementById('sort-output').innerHTML = 'Please enter a string with valid words.';
        return;
    }

    // Sort words alphabetically
    const sortedWords = words.sort((a, b) => a.localeCompare(b));

    // Join sorted words into a string and display
    document.getElementById('sort-output').innerHTML = `<strong>Sorted Words:</strong> ${sortedWords.join(' ')}`;
}
