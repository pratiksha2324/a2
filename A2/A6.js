function convertToUpperCase() {
    const inputString = document.getElementById('inputString').value.trim();
    const resultDiv = document.getElementById('result');

    if (inputString.length === 0) {
        resultDiv.innerHTML = '<p style="color: red;">The input field cannot be empty.</p>';
        return;
    }

    const firstLetter = inputString.charAt(0).toUpperCase();
    const restOfString = inputString.slice(1);

    const resultString = firstLetter + restOfString;

    resultDiv.innerHTML = `<p>Converted String: ${resultString}</p>`;
}
