function solution(my_string) {
    var answer = 0;
    my_string=my_string.split(' ');
    my_string.forEach((v,i)=>{
        if (i===0){
            answer=Number(v);
        }
        if(v==='+'){
            answer+=Number(my_string[i+1]);
        } else if(v==='-'){
            answer-=Number(my_string[i+1]);
        }
    })
    return answer;
}