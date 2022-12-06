function solution(rsp) {
    var answer = '';
    // 2 가위, 0 바위, 5 보
    for(let r of rsp){
        if(r==='2'){
            answer+='0';
        } else if(r==='0'){
            answer+='5';
        } else if(r==='5'){
            answer+='2';
        }
    }
    return answer;
}