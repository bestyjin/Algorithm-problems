function solution(array, n) {
    let diff=0;
    let target = 0;
    let min = 100;
    array=array.sort((a,b)=>a-b);
    for(let i=0; i<array.length;i++){
        diff = n-array[i]<0?-(n-array[i]):n-array[i];
        if(min>diff){
            min=diff;
            target = array[i];
        }
    }
    return target;
}