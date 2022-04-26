// https://dodona.ugent.be/nl/courses/1151/series/12994/activities/202010242
// https://dodona.ugent.be/nl/courses/1151/series/12994/activities/202010242
const assert=require("assert");

class Zeshoek{

    constructor(q,r) {
        this.q=q;
        this.r=r;
    };

    toString(){
        return `Zeshoek(${this.q}, ${this.r})`;
    }

    afstand(zeshoek){
        return (1/2)*(Math.abs(this.q-zeshoek.q)+Math.abs(this.r-zeshoek.r)+Math.abs(this.q+this.r-zeshoek.q-zeshoek.r));
    }

    buur(richting){
        switch (richting){
            case "NW":
                return new Zeshoek(this.q,this.r-1);
                break;
            case "NO":
                return new Zeshoek(this.q+1,this.r-1);
                break;
            case "O":
                return new Zeshoek(this.q+1,this.r);
                break;
            case "ZO":
                return new Zeshoek(this.q,this.r+1);
                break;
            case "ZW":
                return new Zeshoek(this.q-1,this.r+1);
                break;
            case "W":
                return new Zeshoek(this.q-1,this.r);
                break;
            default:
                throw {name:"AssertionError",message:"ongeldige richting"};
        }
    }

    pad(richtingpad){
        try {
            let rpad = richtingpad.replace(/([OW])/g, "$1,").slice(0, - 1).split(",");
            let res = this;
            rpad.forEach(el => res = res.buur(el));
            return res;
        } catch(e){
            throw {name:"AssertionError",message:"ongeldig pad"};
        }
    }

    buren(){
        return ["NW","NO","O","ZO","ZW","W"].map(el => this.buur(el));
    }
}


//console.log(new Zeshoek(2,5).pad("OWNOZO"));

