// Given a roman numeral, convert it to an integer
/*
Roman Numeral
-string symbol
-int value

// Create a roman numeral object for each symbol
I - new obj (I, 1)
V - new obj (V, 5)
-> store objects in array

// Edge cases
RN written from largest to smallest (left to right)
Subsctration is used of the previous symbol is lower than the next symbol

// IV IV = 8
// preVal = first element [1,]

// see 'I'
// if (preVal < element) // if prev. value is less than the current element
total = element - prevVal
prevVal = element
// else
total += element
prevVal = element


// see 'V'
// if (preVal < element)
total = element - prevVal // 4
preVal = element

// see 'I'
// total += element // 5





*/

class RomanNumeral{
	constructor(symbol) {
	if (symbol === 'I') this.value = 1;
		else if (symbol === 'V') this.value = 5;
		else if (symbol === 'X') this.value = 10;
		else if (symbol === 'L') this.value = 50;
		else if (symbol === 'C') this.value = 100;
		else if (symbol === 'D') this.value = 500;
		else if (symbol === 'M') this.value = 1000;
	}
}

// JS arrow functions
var romanToInt = function(s) {
	// traverse through ronumeral string
	const numeralValues = [];

	for (let i = 0; i < s.length; i++) {
	let element = s[i];
	const romanNumeralObj = new RomanNumeral(element);
	numeralValues[i] = romanNumeralObj;
	}


	let total = 0;

	for (let i = 0; i < numeralValues.length; i++) {
		let currentValue = numeralValues[i].value; // 1000 100
		let nextValue = 0;

		if ((i + 1) < numeralValues.length) {
			nextValue = numeralValues[i+1].value; // 100
		}

		if (currentValue >= nextValue) {
			total += currentValue;
		} else {
			let x = nextValue - currentValue;
			total += x;
			i++;
		}
	}
	return total;
};

console.log(romanToInt('III'));
console.log(romanToInt('IV'));
console.log(romanToInt('LVIII'));
console.log(romanToInt('MCMXCIV'));
console.log('hello world'); 