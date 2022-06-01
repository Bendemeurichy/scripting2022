//https://dodona.ugent.be/nl/courses/121/series/1499/activities/758056500/#
const tekentMap={"DR":"┗","LU":"┗","DD":"|","UU":"|","DL":"┛","RU":"┛","LD":"┏","UR":"┏","RD":"┓","UL":"┓","RR":"━","LL":"━",};
const richtingen={"U":[-1,0],"R":[0,1],"D":[1,0],"L":[0,-1]};

class FlowFree{
    constructor(rij,kolom,volgorde) {
        this.veld=[]
        for(let i=0;i<rij;i++) {
            this.veld.push(new Array(kolom).fill("."))
        }

        if(volgorde.length%2!==0 || volgorde.some(a=>! this.ispositie(a))|| hasdoubles(volgorde)){
            throw {name:"AssertionError",message:"ongeldige configuratie"}
        }
        let letter="A"
        for(let i=0;i<volgorde.length-1;i+=2){
            this.veld[volgorde[i][0]][volgorde[i][1]]=letter;
            this.veld[volgorde[i+1][0]][volgorde[i+1][1]]=letter
            letter=String.fromCharCode(letter.charCodeAt(0)+1)
        }
    }

    toString(){
        return (this.veld.map(el=>el.join(""))).join("\n");
    }

    ispositie(pos){
        if(pos.length===2){
            if(pos[0]>=0 && pos[1]>=0 && pos[0]<this.veld.length && pos[1]<this.veld[0].length ){
                return true
            }
        }
        return false;
    }

    pijpleiding(start,volgorde){
        let pos=start
        let res=[[start[0],start[1]]]
        if((!this.ispositie(start))||volgorde.length===0|| (! volgorde.toUpperCase().split().every(a=>a.match(/[DULR]/)))){
            throw{name:"AssertionError",message:"ongeldige pijpleiding"}
        }
        for(let i=0;i<volgorde.length-1;i++){
            let el=volgorde.toUpperCase()[i]
            pos=[pos[0]+richtingen[el][0],pos[1]+richtingen[el][1]]
            if(res.some(el=>el[0]===pos[0] && el[1]===pos[1])||! this.ispositie(pos) ||this.veld[pos[0]][pos[1]]!=="."){
                throw{name:"AssertionError",message:"ongeldige pijpleiding"}
            }
            res.push([pos[0],pos[1]])
        }
        if(this.veld[pos[0]+richtingen[volgorde[volgorde.length-1].toUpperCase()][0]][pos[1]+richtingen[volgorde[volgorde.length-1].toUpperCase()][1]]!==this.veld[start[0]][start[1]]){
            throw{name:"AssertionError",message:"ongeldige pijpleiding"}
        }
        res.push([pos[0]+richtingen[volgorde[volgorde.length-1].toUpperCase()][0],pos[1]+richtingen[volgorde[volgorde.length-1].toUpperCase()][1]])
        return res
    }

    verbinden(start,volgorde){
        let pos=[start[0]+richtingen[volgorde.toUpperCase()[0]][0],start[1]+richtingen[volgorde.toUpperCase()[0]][1]]
        const copy=[...this.veld.map(el=>[...el])]

        if(volgorde.length===0){
            throw{name:"AssertionError",message:"ongeldige pijpleiding"}
        }
        let prevrichting=volgorde.toUpperCase()[0]
        for(let i=1;i<volgorde.length;i++){
            let el=volgorde.toUpperCase()[i]
            this.veld[pos[0]][pos[1]]=tekentMap[prevrichting+el]
            pos=[pos[0]+richtingen[el][0],pos[1]+richtingen[el][1]]
            if(!(this.veld[pos[0]][pos[1]]==="." || this.veld[pos[0]][pos[1]]===this.veld[start[0]][start[1]])){
               this.veld=copy
                throw{name:"AssertionError",message:"ongeldige pijpleiding"}
           }
            prevrichting=el
        }
        return this
    }

    isgevuld(){
        return this.veld.every(el=>el.every((a)=>a!=="."));
    }
}

function hasdoubles(arr){
    for(let el of arr){
        let cop=[...arr];
        cop.splice(cop.indexOf(el),1);
        for(let i of cop){
            if(i[0]===el[0] && i[1]===el[1]){
                return true
            }
        }
    }
    return false
}

