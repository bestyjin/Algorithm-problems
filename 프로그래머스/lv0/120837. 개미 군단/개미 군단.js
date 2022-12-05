function solution(hp) {
    var answer = 0;
    // 5 3 1
    while(hp){
        if(parseInt(hp/5)>0){
            answer+=parseInt(hp/5);
            hp-=parseInt(hp/5)*5;
        } else if(parseInt(hp/3)>0){
            answer+=parseInt(hp/3);
            hp-=parseInt(hp/3)*3;
        } else {
            answer+=hp;
            hp=0;
        }
        
    }
    
    
    return answer;
}