function solution(x) {
    let xList = String(x).split('');
    let sum = 0;
    for (let i = 0; i < xList.length; i+=1){
        sum+=Number(xList[i]);
    }
    return (x%sum === 0) ? true : false;
}