const getEven = require("./even");

test("should return even number array", () =>{
    
    let number = [45, 60, 3, 10, 9, 12];
    expect(getEven(number)).toBe([60, 10, 12]);

});

const getEven = require("./odd");

test("should return odd number array", () =>{
    
    let number = [45, 60, 3, 10, 9, 12];
    expect(getEven(number)).toBe([45, 3, 9]);

});

const checkPalindrome = require("./palindrome");

test("should return true for palindrome number array", () =>{
    
    let number = [45, 0, 8, 0, 45];
    expect(getEven(number)).toBe([45, 0, 8, 0, 45]);

});
