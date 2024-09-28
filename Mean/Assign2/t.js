// script.js

let myArray = [1, 2, 3, 4, 5];
let myObjectArray = [{ name: 'John', age: 25 }, { name: 'Jane', age: 30 }];

// a. Check if An Array Contains a Specified Value
function containsValue(arr, value) {
    return arr.includes(value);
}

// b. Insert Item in an Array
function insertItem(arr, index, item) {
    arr.splice(index, 0, item);
    return arr;
}

// c. Append an Object to an Array
function appendObject(arr, obj) {
    arr.push(obj);
    return arr;
}

// d. Check if An Object is An Array
function isArray(obj) {
    return Array.isArray(obj);
}

// e. Empty an Array
function emptyArray(arr) {
    arr.length = 0;
    return arr;
}

// f. Add Element to Start of an Array
function addElementToStart(arr, element) {
    arr.unshift(element);
    return arr;
}

// g. Remove Duplicates From Array
function removeDuplicates(arr) {
    return [...new Set(arr)];
}

// h. Merge Two Arrays and Remove Duplicate Items
function mergeAndRemoveDuplicates(arr1, arr2) {
    return [...new Set([...arr1, ...arr2])];
}

// i. Sort Array of Objects by Property Values
function sortArrayByProperty(arr, property) {
    return arr.sort((a, b) => (a[property] > b[property] ? 1 : -1));
}

// Function to execute selected operation
function executeOperation() {
    const operation = document.getElementById("operation").value;
    let result;

    switch (operation) {
        case '1': // Check if an Array Contains a Specified Value
            const value = prompt("Enter value to check:");
            result = containsValue(myArray, Number(value));
            break;
        case '2': // Insert Item in an Array
            const index = prompt("Enter index to insert:");
            const item = prompt("Enter item to insert:");
            result = insertItem(myArray, Number(index), Number(item));
            break;
        case '3': // Append an Object to an Array
            const obj = prompt("Enter object in format {key: value} to append:");
            result = appendObject(myArray, JSON.parse(obj));
            break;
        case '4': // Check if An Object is An Array
            const input = prompt("Enter value to check if it's an array:");
            result = isArray(JSON.parse(input));
            break;
        case '5': // Empty an Array
            result = emptyArray(myArray);
            break;
        case '6': // Add Element to Start of an Array
            const element = prompt("Enter element to add at start:");
            result = addElementToStart(myArray, Number(element));
            break;
        case '7': // Remove Duplicates From Array
            result = removeDuplicates(myArray);
            break;
        case '8': // Merge Two Arrays and Remove Duplicate Items
            const arr1 = JSON.parse(prompt("Enter first array (format: [1,2,3]):"));
            const arr2 = JSON.parse(prompt("Enter second array (format: [4,5,6]):"));
            result = mergeAndRemoveDuplicates(arr1, arr2);
            break;
        case '9': // Sort Array of Objects by Property Values
            const property = prompt("Enter property name to sort by (e.g., 'age'):");
            result = JSON.stringify(sortArrayByProperty(myObjectArray, property));
            break;
        default:
            alert("Invalid choice! Please choose a valid option.");
            return;
    }

    // Display the result
    document.getElementById("result").textContent = `Result: ${result}`;
}
