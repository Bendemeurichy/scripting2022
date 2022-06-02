//https://dodona.ugent.be/nl/courses/453/series/4863/activities/13082320/#

class Machine{
    constructor() {
        this.bellen={}
        this.knoppen={}
    }

    nieuweBel(label,beans){
        if(label in this.bellen){
            throw {name:"AssertionError",message:"bel bestaat reeds"};
        }
        this.bellen[label]=beans;
        return this;
    }

    nieuweKnop(label,source,dest){
        if(label in this.knoppen){
            throw {name:"AssertionError",message:"knop bestaat reeds"};
        }
        for(let el of source){
            if(!(el in this.bellen)){
                    throw {name:"AssertionError",message:"onbekende bel"};
                }
        }
        for(let el of dest){
            if(!(el in this.bellen)){
                    throw {name:"AssertionError",message:"onbekende bel"};
                }
        }
        this.knoppen[label]={"source":source,"dest":dest};
        return this;
    }

    druk(label){

        let knoppen=[...label]
        for(let el of knoppen){
            let copy= {...this.bellen}
            if(! (el in this.knoppen)){
                throw {name:"AssertionError",message:"onbekende knop"};
            }
            let addbeans=true;
            for(let s of this.knoppen[el]["source"]){
                if(!(s in this.bellen)){
                    throw {name:"AssertionError",message:"onbekende bel"};
                }
                if(this.bellen[s]>0){
                    this.bellen[s]-=1;
                } else{
                    this.bellen=copy
                    addbeans=false;
                    break;
                }

            }
            for(let d of this.knoppen[el]["dest"]){
                if(!(d in this.bellen)){
                    throw {name:"AssertionError",message:"onbekende bel"};
                }
                this.bellen[d]+=addbeans?1:0;
            }
        }
        return this
    }

    toString(){
        return Object.entries(this.bellen).map(([key, value]) =>`${key}: ${value}`).join("\n")
    }
}
