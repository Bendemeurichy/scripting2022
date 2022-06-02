//https://dodona.ugent.be/nl/courses/62/series/799/activities/2003641614/#

class Cijfer{
    constructor(code) {
        if(! code.toUpperCase().match(/^[A-Z]*$/)){
            throw {name:"AssertionError",message:"help"}
        }
        this.codewoord=code;
        this.kolommen=[];
        for(let el of [...new Set(code.toUpperCase().split(''))].join('')){
            this.kolommen.push([...new Set(code.toUpperCase().split(''))].sort().indexOf(el));
        }
    }

    codeer(bericht){
        let cop=[]
        for(let i=0;i<this.kolommen.length;i++){
            cop.push([])
        }
        let len=bericht.length
        if(len%this.kolommen.length!==0) {
            for (let k = 0; k < (cop.length - len % cop.length); k++) {
                bericht += "?"
            }
        }
        for(let i=0;i<bericht.length+1;i++){
            cop[this.kolommen[i%this.kolommen.length]].push(bericht[i])
        }
        return cop.map(el=>el.join("")).join("")
    }

    decodeer(bericht){
        if(bericht.length%this.kolommen.length!==0){
            throw {name:"AssertionError",message:"ongeldig bericht"};
        }
        let res=""
        let cop=[]
        for(let i=0;i<this.kolommen.length;i++){
            cop.push([])
        }
        let c=0
        for(let i=0;i<bericht.length;i+=(bericht.length/this.kolommen.length)){
            cop[c].push(...bericht.slice(i,(i+bericht.length/this.kolommen.length)).split(""));
            c++;
        }
        for(let k=0;k<bericht.length;k++){
            res+=cop[this.kolommen[k%this.kolommen.length]].shift()
        }
        return res
    }
}

