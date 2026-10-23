// Question 1
// let temp = [28, 32, 25, 40, 18, 35]
// let count = 0
// for (let i = 0; i < temp.length; i++) {
//     if (temp[i] > 30) {
//         count++
//     }
// }
// console.log("Days hotter than 30°C:", count);


// Question 2
// let num = 4729
// let total = 0
// for (let i = num; i > 0; i = Math.floor(i / 10)) {
//     total += i % 10
// }
// console.log("Sum of digits:", total);


// Question 3
// for (let i = 1; i <= 100; i++) {
//     if (i % 3 == 0 && i % 5 == 0 && i % 7 != 0) {
//         console.log(i);
//     }
// }


// Question 4
// let string = "JavaScript"
// let newString = ""
// for (let i = 0; i < string.length; i++) {
//     let char = string[i]
//     if (!char.toLowerCase().includes("a") && !char.toLowerCase().includes("e") && !char.toLowerCase().includes("i") && !char.toLowerCase().includes("o") && !char.toLowerCase().includes("u")) {
//         newString += char
//     }
// }
// console.log(newString);


// Question 5
// let arr = [1, 2, 3, 4, 234, 2342, 2, 18]
// let largestNumber = arr[0]
// for (let i = 1; i < arr.length; i++) {
//     if (arr[i] > largestNumber) {
//         largestNumber = arr[i]
//     }
// }
// console.log(largestNumber);


// Question 6
// let number = 28
// let total = 0
// for (let i = 1; i < number; i++) {
//     if (number % i == 0) {
//         total += i
//     }
// }
// if (total == number) {
//     console.log("Yes,", number, "is a perfect number.");
// } else {
//     console.log("No,", number, "is not a perfect number.");
// }


// Question 7
// let bag = ""
// for (let i = 0; i <= 7; i++) {
//     bag += 2 ** i + " "
// }
// console.log(bag);


// Question 8
// let val1 = 0
// let val2 = 1
// let bag = "0 1 "
// for (let i = 3; i <= 20; i++) {
//     val3 = val1 + val2
//     bag += val3 + " "
//     val1 = val2
//     val2 = val3
// }
// console.log(bag);


// Question 9
// let scores = [45, 78, 90, 32, 56, 88]
// let total = 0
// let count = 0
// for (let i = 0; i < scores.length; i++) {
//     total += scores[i]
// }
// let avg = total / scores.length
// console.log("Average:", avg);
// for (let i = 0; i < scores.length; i++) {
//     if (avg < scores[i]) {
//         count++
//     }
// }
// console.log("Count:", count);


// Question 10
// let num = 13
// let numCopy = num
// let binary = ""
// for (let i=0; true; i++){
//     binary = numCopy%2 + binary
//     numCopy = Math.floor(numCopy/2)
//     if (numCopy == 0){
//         break
//     }
// }
// console.log(binary);
