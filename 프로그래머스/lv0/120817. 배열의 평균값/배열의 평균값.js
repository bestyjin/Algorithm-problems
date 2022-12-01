function solution(numbers) {
    var answer = 0;
    let sum = 0;
    sum = numbers.reduce((p,c)=>p+c)
    answer = sum / numbers.length;
    
    return answer;
}