function solution(n) {
    var answer = 0;
    let count = 0;
    for(let j=4;j<=n;j++){
        count=0;
        for(let i=1;i<=j; i++){
            if(j%i===0) count+=1;
        }
        if(count>=3) answer+=1;
    }
    
    return answer;
}