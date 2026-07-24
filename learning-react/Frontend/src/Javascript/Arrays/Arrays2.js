const t = [1, -1, 3]

const t2 = t.concat(5)  // creates new array. This is to ensure the original array remain unchanged

console.log(t)  // [1, -1, 3] is printed
console.log(t2) // [1, -1, 3, 5] is printed