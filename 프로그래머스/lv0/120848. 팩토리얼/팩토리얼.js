function solution(n) {
    var answer = 0;
    let count=1;
    let result=1;
    while(true){
        result=1;
        for(let i =1;i<=count;i++){
            result*=i;
        }
        if(result>n){
            return count-1;
        }
        count++;
    }
}