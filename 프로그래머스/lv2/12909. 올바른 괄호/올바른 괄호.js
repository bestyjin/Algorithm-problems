function solution(s){
    s = s.split('');
    let stack =[];
    while (s.length > 0) {
        let pop = s.pop();
        if (pop === ')') {
            stack.push(')');
        } else if (pop === '(') {
            if (stack.length > 0){
                stack.pop();
            } else {
                return false;
            }
        } 
    }
    if (stack.length>0){
        return false;
    } else {
        return true;    
    }
}