function compareStrings() {
    const str1 = document.getElementById('string1').value.trim();
    const str2 = document.getElementById('string2').value.trim();
    const output = document.getElementById('comparison-output');

    if (str1.length === 0 || str2.length === 0) {
        output.innerHTML = '<p style="color: red;">Both fields must be filled out.</p>';
        return;
    }

    let comparisonResult = '';

    // Compare lengths
    if (str1.length === str2.length) {
        comparisonResult += `<p>Both strings have the same length: ${str1.length} characters.</p>`;
    } else {
        comparisonResult += `<p>String 1 has ${str1.length} characters and String 2 has ${str2.length} characters.</p>`;
    }

    // Compare content
    if (str1 === str2) {
        comparisonResult += '<p>The strings are identical in content.</p>';
    } else {
        comparisonResult += '<p>The strings have different content.</p>';
    }

    output.innerHTML = comparisonResult;
}
