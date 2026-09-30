// Part I: Variables (let, var, const)

// Part a

// Question 1
// const name = "Arnav";
// let age = 18;
// let city = "Ujjain";

// Question 2
// let score = 50;
// score = 80;
// console.log(score);

// Question 3
// const PI = 3.14;
// console.log(PI);

// Question 4
// var num1;
// let num2;
// console.log(num1);
// console.log(num2);
// num1 = 1;
// num2 = 2;
// console.log(num1);
// console.log(num2);


// Part b

// Question 5
// const studentName = "A";
// let marks=89;
// const schoolName = "B";
// marks = 99;
// console.log(studentName);
// console.log(marks);
// console.log(schoolName);

// Question 6
// if (true) {
//     var a = 1; // Can be accessed outside the block
//     let b = 2; // Can not be accessed outside the block
//     const c = 3; // Can not be accessed outside the block
// }
// console.log(a);
// console.log(b);
// console.log(c);

// Question 7
// var user = "A";
// var user = "B"; // Allows re-declaration
// let user = "A";
// let user = "B"; // Doesn't allow re-declaration

// Question 8
// var a = 1; // Allows re-assignment
// let b = 2; // Allows re-assignment
// const c = 3; // Doesn't allow re-assignment
// a = 11;
// b = 12;
// c = 13;


// Part c

// Question 9
// var x = 10;

// if (true) {
//     var x = 20;
//     let y = 30;
//     const z = 40;
// }

// console.log(x); // Output: 20
// console.log(y); // Output: Error
// console.log(z); // Output: Error

// let and const are block-scoped therefore they can't be accessed outside their block


// Question 10
// const name = "Arnav";

// var age = 20;
// var age = 25;

// if (true) {
//     var city = "Delhi";
//     var country = "India";
// }

// console.log(country);

// let score = 50;
// score = 80;