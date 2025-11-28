const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function checkEvenOdd(number) {
    if (number % 2 === 0) {
        return "EVEN";
    } else {
        return "ODD";
    }
}

rl.question('Enter a number: ', (input) => {
    const number = parseFloat(input);
    
    if (isNaN(number)) {
        console.log('Please enter a valid number!');
    } else {
        const result = checkEvenOdd(number);
        console.log(`${number} is ${result}`);
    }
    
    rl.close();
});

