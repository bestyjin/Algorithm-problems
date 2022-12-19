function solution(A, B) {
    let string = '';
    let count = 0;
    let newA = A;
    while(count < newA.length){
        if(A === B){
            return 0;
        }
        string = '';
        string += newA[newA.length-1]
        for(let i = 0; i<newA.length-1; i++){
            string += newA[i];
        }
        count += 1;
        if(string === B){
            return count;
        }
        newA = string;
    }
    return -1;
}

