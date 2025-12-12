// First install: npm install prompt-sync
const prompt = require('prompt-sync')();

function checkEvenOdd(number) {
    return number % 2 === 0 ? "EVEN" : "ODD";
}

// Get input from user
const input = prompt('Enter a number: ');
const number = parseFloat(input);

if (isNaN(number)) {
    console.log('Please enter a valid number!');
} else {
    const result = checkEvenOdd(number);
    console.log(`${number} is ${result}`);
}