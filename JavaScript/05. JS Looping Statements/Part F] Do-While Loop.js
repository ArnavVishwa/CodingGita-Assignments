// Question 1
// let i = 10
// do{
//     console.log(i);
//     i--
// }while (i>=1)


// Question 2
// let i = 1
// do{
//     if (i%2==0){
//         console.log(i);
//     }
//     i++
// }while (i<=20)


// Question 3
// let n = 5
// let total = 0
// let i = 1
// do{
//     total+=i
//     i++
// }while (i<=n)
// console.log(total);


// Question 4
// let n = 234
// let product = 1
// do{
//     product*=n%10
//     n = Math.floor(n/10)
// }while (n!=0)
// console.log(product);


// Question 5
// let n = 58372
// do{
//     n = Math.floor(n/10)
// }while (n>9)
// console.log(n);


// Question 6
// let base = 3
// let exponent = 4
// let result = 1
// let i = 1
// do{
//     result *= base
//     i++
// }while (i<=exponent)
// console.log(result);


// Question 7
// let n = 100
// let i = 1
// do{
//     if (i%4==0 && i%8!=0){
//         console.log(i);
//     }
//     i++
// }while (i<=n)


// Question 8
// let num = 1221
// let numCopy = num
// let numRev = 0
// do{
//     numRev = numRev*10 + num%10
//     num = Math.floor(num/10)
// }while (num!=0)
// if (numRev == numCopy){
//     console.log("Palindrome number");
// }else{
//     console.log("Not a palindrome number");
// }


// Question 9
// let n1 = 48
// let n2 = 18
// let gcd = n2
// if (n1 > n2){
//     gcd = n1
// }
// do{
//     if (n1%gcd==0 && n2%gcd==0){
//         break
//     }
//     gcd--
// }while (true)
// console.log(gcd);


// Question 10
// let n = 13
// let binary = ""
// if (n==0){
//     binary = 0
// }
// do{
//     binary = n%2 + binary
//     n = Math.floor(n/2)
// }while (n!=0)
// console.log(binary);
