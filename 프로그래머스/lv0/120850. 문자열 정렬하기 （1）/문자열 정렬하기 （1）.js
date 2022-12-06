function solution(my_string) {
    my_string=my_string.replace(/[^0-9]/g,'')
    my_string=my_string.split('');
    my_string = my_string.map((s)=>parseInt(s));
    return my_string.sort((a,b)=>a-b);
}