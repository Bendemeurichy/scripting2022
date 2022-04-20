// https://dodona.ugent.be/nl/courses/1151/series/12993/activities/1441986817
const assert= require("assert");

function quipu(number){
    let numberlist;
    let res;
    numberlist = number.toString().split('');

    res = numberlist.slice(0,numberlist.length-1).map(a => a==='0' ? 'X ':a+'s ');
    res=res.join('')
    const last = numberlist[numberlist.length-1];
    if(last === '0'){
        res+='EE';
    } else if (last === '1'){
        res+='E';
    } else{
        res+=last+'L';
    }
    return res;
}

function decimaal2quipu(number) {
    let rope= number.map(a => quipu(a));
    return rope.join(' ');
}

function quipu2decimaal(knot) {
    let knotlist= knot.split(" ");
    assert(! knot.match("([1-9][0-9]+|X[^ ]| s|s[^ ]|[^1-9sLXE ])") && knotlist[knotlist.length-1].match("^(EE|E|[2-9]L)$"),"ongeldige knopen");

    let res=[];
    let getal='';
    for(let el of knotlist){
        if(el.match("[2-9]L") || el==="E" || el==="EE"){
            switch (el) {
                case "EE":
                    getal += '0';
                    break;
                case "E":
                    getal += '1';
                    break;
                default:
                    getal += el[0];
            }
            res.push(parseInt(getal));
            getal='';
            } else {
            getal+= el==='X' ? '0':el[0];
        }
    }
    return res;
}
