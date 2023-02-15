function solution(numbers) {
    const num = [0,1,2,3,4,5,6,7,8,9];
    let sum = num.reduce((a,b)=>a+b,0);
    let numbersSum = numbers.reduce((a,b)=>a+b,0);
    
    return sum - numbersSum;
}