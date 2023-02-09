function solution(s){
    let pCnt = 0;
    let yCnt = 0;
    
    for(const i of s){
        if(i === 'p' || i ==='P'){
            pCnt += 1;
        } else if(i === 'y' || i ==='Y'){
            yCnt += 1;
        }
    }
    
    return (pCnt === yCnt) ? true : false;
}