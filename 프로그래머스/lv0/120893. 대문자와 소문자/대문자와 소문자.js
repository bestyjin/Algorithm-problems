function solution(my_string) {
    my_string=my_string.split('');
    my_string=my_string.map((s)=>{
        if(s===s.toLowerCase()){
            s=s.toUpperCase();
        } else {
            s=s.toLowerCase();
        }
        return s;
    })
    return my_string.join('');
}