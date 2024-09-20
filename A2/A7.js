function updateFormFields() {
    const operation = document.getElementById('operation').value;
    
    // Hide all input fields
    const fields = document.querySelectorAll('.input-field');
    fields.forEach(field => field.style.display = 'none');
    
    // Show only relevant input fields
    switch (operation) {
        case 'check':
            document.getElementById('arrayField').style.display = 'block';
            document.getElementById('valueField').style.display = 'block';
            break;
        case 'insert':
            document.getElementById('arrayField').style.display = 'block';
            document.getElementById('insertField').style.display = 'block';
            break;
        case 'append':
            document.getElementById('arrayField').style.display = 'block';
            document.getElementById('appendField').style.display = 'block';
            break;
        case 'isArray':
            document.getElementById('arrayField').style.display = 'block';
            break;
        case 'empty':
            document.getElementById('arrayField').style.display = 'block';
            break;
        case 'addStart':
            document.getElementById('arrayField').style.display = 'block';
            document.getElementById('addStartField').style.display = 'block';
            break;
        case 'removeDuplicates':
            document.getElementById('arrayField').style.display = 'block';
            break;
        case 'merge':
            document.getElementById('arrayField').style.display = 'block';
            document.getElementById('mergeField').style.display = 'block';
            break;
        case 'sort':
            document.getElementById('arrayField').style.display = 'block';
            document.getElementById('sortField').style.display = 'block';
            break;
        default:
            break;
    }
}

function performArrayOperations() {
    const operation = document.getElementById('operation').value;
    const arrayInput = document.getElementById('arrayInput').value.split(',').map(item => item.trim());
    const valueToCheck = document.getElementById('valueToCheck').value.trim();
    const itemToInsert = document.getElementById('itemToInsert').value.trim();
    const objectToAppend = document.getElementById('objectToAppend').value.trim();
    const elementToAdd = document.getElementById('elementToAdd').value.trim();
    const arrayToMerge = document.getElementById('arrayToMerge').value.split(',').map(item => item.trim());
    const propertyToSortBy = document.getElementById('propertyToSortBy').value.trim();

    let result = '';

    switch (operation) {
        case 'check':
            const containsValue = arrayInput.includes(valueToCheck) ? 'Yes' : 'No';
            result = `<p><strong>Array Contains Value "${valueToCheck}":</strong> ${containsValue}</p>`;
            break;

        case 'insert':
            arrayInput.push(itemToInsert);
            result = `<p><strong>Array After Insertion:</strong> ${arrayInput.join(', ')}</p>`;
            break;

        case 'append':
            let arrayWithObject = arrayInput;
            try {
                const objectToAppendParsed = JSON.parse(objectToAppend);
                if (typeof objectToAppendParsed === 'object' && !Array.isArray(objectToAppendParsed)) {
                    arrayWithObject = [...arrayInput, objectToAppendParsed];
                } else {
                    result = '<p><strong>Error:</strong> JSON should be an object.</p>';
                    document.getElementById('result').innerHTML = result;
                    return;
                }
            } catch (e) {
                result = '<p><strong>Error:</strong> Invalid JSON format for object.</p>';
                document.getElementById('result').innerHTML = result;
                return;
            }
            result = `<p><strong>Array After Appending Object:</strong> ${JSON.stringify(arrayWithObject)}</p>`;
            break;

        case 'isArray':
            const isArray = Array.isArray(arrayInput);
            result = `<p><strong>Is Input Array an Array:</strong> ${isArray}</p>`;
            break;

        case 'empty':
            const emptyArray = [];
            result = `<p><strong>Empty Array:</strong> ${JSON.stringify(emptyArray)}</p>`;
            break;

        case 'addStart':
            const arrayWithElementAdded = [elementToAdd, ...arrayInput];
            result = `<p><strong>Array After Adding Element to Start:</strong> ${arrayWithElementAdded.join(', ')}</p>`;
            break;

        case 'removeDuplicates':
            const removeDuplicates = [...new Set(arrayInput)];
            result = `<p><strong>Array After Removing Duplicates:</strong> ${removeDuplicates.join(', ')}</p>`;
            break;

        case 'merge':
            const mergedArray = [...new Set([...arrayInput, ...arrayToMerge])];
            result = `<p><strong>Merged Array with No Duplicates:</strong> ${mergedArray.join(', ')}</p>`;
            break;

        case 'sort':
            try {
                // Parse arrayInput as JSON objects
                const arrayOfObjects = arrayInput.map(item => {
                    try {
                        return JSON.parse(item);
                    } catch (e) {
                        return null; // If parsing fails, return null
                    }
                }).filter(item => item && typeof item === 'object' && item[propertyToSortBy] !== undefined);
                
                // Sort the array based on the given property
                const sortedArray = arrayOfObjects.sort((a, b) => {
                    if (a[propertyToSortBy] < b[propertyToSortBy]) return -1;
                    if (a[propertyToSortBy] > b[propertyToSortBy]) return 1;
                    return 0;
                });
                
                result = `<p><strong>Sorted Array of Objects by Property "${propertyToSortBy}":</strong> ${JSON.stringify(sortedArray)}</p>`;
            } catch (e) {
                result = '<p><strong>Error:</strong> Invalid JSON format for sorting.</p>';
            }
            break;

        default:
            result = '<p><strong>Please select a valid operation.</strong></p>';
            break;
    }

    document.getElementById('result').innerHTML = result;
}
