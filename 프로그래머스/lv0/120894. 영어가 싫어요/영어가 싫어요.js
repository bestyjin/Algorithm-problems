function solution(numbers) {
    var answer = '';
    const num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    let string=''
    for(let i=0; i<numbers.length; i++){
        string+=numbers[i];
        if(num.includes(string)){
            answer+=Number(num.indexOf(string));
            string='';
        }
    }
    return parseInt(answer);
}