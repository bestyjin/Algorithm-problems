function solution(money) {
    var answer = [];
    const coffee = parseInt(money/5500);
    answer = [coffee,money-coffee*5500]
    return answer;
}