//https://dodona.ugent.be/nl/courses/1151/series/12997/activities/1569264620/#

class Centrifuge{
    constructor(n,config){
        this.n=n;
        this.config=config
    }

    toString(){
        return `Centrifuge(${this.n}, [${this.config.sort(function(a, b){return a-b}).join(", ")}])`;
    }

    roteer(wijzerzin){
        let factor=1;
        if(wijzerzin){
            factor=-1;
        }

        for(let i=0;i<this.config.length;i++){
            this.config[i]=(this.config[i]+factor+this.n)%(this.n);
        }
        return this
    }

    spiegel(){
        for(let i=0;i<this.config.length;i++){
            this.config[i]=(this.n-this.config[i])%this.n;
        }
        return this;
    }

    isGelijk(d){
        let temp=[...this.config]
        if(this.n!==d.n){
            return false;
        }
        let i=0;
        let found=false;
        while(i<this.n && ! found){
            let res=true
            let j=0
            while(j<this.config.length && res){
                let a=this.config.sort(function(a, b){return a-b})[j]
                let c=d.config.sort(function(a, b){return a-b})[j]
                res=a===c
                j++
            }
            this.roteer();
            found=res
            i++
        }
        this.config=temp;
        return found;
    }

    vul(d) {
        if (this.n !== d.n) {
            throw {name: "AssertionError", message: "gaten kunnen niet gevuld worden"};
        }
        for(let el of d.config){
            if(this.config.some(a=>a===el)){
                throw {name:"AssertionError",message:"gaten kunnen niet gevuld worden"};
            }
            this.config.push(el);
        }
        return this
    }

    leeg(d) {
        let temp=[...d.config]
        if (this.n !== d.n) {
            throw {name: "AssertionError", message: "gaten kunnen niet geleegd worden"};
        }
        for(let i=temp.length-1;i>=0;i--){
            if(! this.config.some(a=>a===d.config[i])){
                throw {name:"AssertionError",message:"gaten kunnen niet geleegd worden"};
            }
            this.config.sort(function(a, b){return a-b}).splice(d.config.sort(function(a, b){return a-b})[i],1);
            d.config.sort(function(a, b){return a-b}).splice(d.config.sort(function(a, b){return a-b})[i],1);
        }
        d.config=temp
        return this
    }
}

