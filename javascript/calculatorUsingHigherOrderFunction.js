 function add(num1, num2) {
     return num1 + num2;
 }

 function substract(num1, num2) {
     return num1 - num2;
 }

 function divide(num1, num2) {
     return num1 / num2;
 }

 function multiply(num1, num2) {
     return num1 * num2;
 }

 function operator(num1, num2, operator) {
     return operator(num1, num2);
 }

 console.log(operator(5, 6, add));
