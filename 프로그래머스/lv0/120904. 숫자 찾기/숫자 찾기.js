function solution(num, k) {
    num=String(num);
    k=String(k);
    if(num.includes(k)){
        return num.indexOf(k)+1;
    }
    return -1;
}