function solution(s) {
    var answer = '';
    for(let i=0; i<s.length; i++){
        if(s.split('').filter(v=>v===s[i]).length === 1){
            answer+=s[i];
        }
    }
    answer = answer.split('').sort((a, b) => {
        if(a<b) return -1;
        else if(a>b) return 1;
        else if(a===b) return 0;
    });
    
    return answer.join('');
}