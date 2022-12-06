function solution(age) {
    //0~9 => a~j
    var answer = '';
    const ageTable={
        0:'a',
        1:'b',
        2:'c',
        3:'d',
        4:'e',
        5:'f',
        6:'g',
        7:'h',
        8:'i',
        9:'j'
    };
    age=String(age);
    for(let i=0; i<age.length;i++){
        answer+=ageTable[age[i]]
    }
    return answer;
}