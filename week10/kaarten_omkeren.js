// https://dodona.ugent.be/nl/courses/1151/series/12996/activities/1096639573
class Kaarten{
    constructor(kaarten) {
        if(kaarten.length>52 ||new Set(kaarten.map(el=>el.toUpperCase())).size!==kaarten.length){
            throw {name:"AssertionError",message:"ongeldige kaarten"};
        }
        const re=/^(10|[2-9JQKA])[CDHS]$/i
        for(let el of kaarten){
            if(! re.test(el)){
                throw {name:"AssertionError",message:"ongeldige kaarten"};
            }
            if(/[jqka][cdhs]/i.test(el)){
                if( /[jqka][CDHS]/.test(el) || /[JQKA][cdhs]/.test(el)) {
                    throw {name: "AssertionError", message: "ongeldige kaarten"};
                }
            }
        }
        this.kaarten=kaarten;
    }

    toString(){
        return this.kaarten.map(function (el){
            if(el==="") {
                return "><";
            }else if(el[el.length-1].toUpperCase()!==el[el.length-1]){
                return "**";
            }
            return el;
        }).join(" ");
    }

    verwijder(kaart){
        if(typeof(kaart) === 'string'){
            kaart = parseInt(this.kaarten.indexOf(kaart.toUpperCase()));
        }
        if(typeof (this.kaarten[kaart]) === 'undefined'|| this.kaarten[kaart]==="" || this.kaarten[kaart]!==this.kaarten[kaart].toUpperCase()){
            throw {name:"AssertionError",message:"ongeldige kaart"}
        }
        this.kaarten[kaart]='';
        this.draaien([kaart-1,kaart+1]);
        return this;
    }

    draaien(indexen){
        for(let el of indexen){
            if (el>=0 && el<this.kaarten.length) {
                if (this.kaarten[el] === this.kaarten[el].toUpperCase()) {
                    this.kaarten[el] = this.kaarten[el].toLowerCase();
                } else {
                    this.kaarten[el] = this.kaarten[el].toUpperCase();
                }
            }
        }
        return this
    }

    isgewonnen(){
        return this.kaarten.every(el=>el==="");
    }
}
