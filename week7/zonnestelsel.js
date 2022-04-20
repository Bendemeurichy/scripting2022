// https://dodona.ugent.be/nl/courses/1151/series/12993/activities/1301922445
const assert=require("assert");

function letterwaarde(letterreeks) {
    assert(new Set(letterreeks.toUpperCase().split("")).size===letterreeks.length && ! letterreeks.match(/[^A-Za-z]/) && letterreeks.length%2===1,"ongeldige letterreeks");
    let length=letterreeks.length;
    const neg=letterreeks.slice(0,(length-1)/2).split('');
    const pos=letterreeks.slice(length/2,length).split('');
    const res={}

    for(let [i,el] of neg.entries()){
        res[el.toUpperCase()]=1+i-((length+1)/2);
    }

    for(let [i,el] of pos.entries()){
        res[el.toUpperCase()]=i;
    }
    return res;
}

function woordwaarde(woord,letterreeks){
    const waarden=letterwaarde(letterreeks);
    let res=0;

    for(let el of woord){
        assert(el.toUpperCase() in waarden,"ontbrekende letters")
        res+=waarden[el.toUpperCase()];
    }

    return res;

}

function alignering(woorden,letterreeks){
    for(let i=0;i<woorden.length;i++){
        if(woordwaarde(woorden[i],letterreeks)!==i){
            return false;
        }
    }
    return true;
}

function rangschik1(woorden,letterreeks){
    woorden.sort(((a,b)=> woordwaarde(a,letterreeks)-woordwaarde(b,letterreeks) || a.localeCompare(b)));
}

function rangschik2(woorden,letterreeks){
    rangschik1(woorden,letterreeks);
    return [...woorden];
}

