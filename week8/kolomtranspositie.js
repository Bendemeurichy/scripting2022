// https://dodona.ugent.be/nl/courses/1151/series/12994/activities/2003641614
const assert=require("assert");
class Cijfer{
    constructor(key) {
        this.key = [...new Set(key)].join('');
        let sorted = this.key.slice().split("").sort();
        let dic = {};
        sorted.forEach(el => dic[el] = sorted.indexOf(el));
        this.kolommen = [];
        for(let el of this.key) {
            this.kolommen.push(dic[el]);
        }
    }


    codeer(str){
        let list = str.match(new RegExp('.{1,' + this.kolommen.length + '}', 'g'));
        list[list.length-1] = list[list.length-1] + ('?'.repeat(this.kolommen.length - list[list.length-1].length))
        let bericht = "";
        for(let i = 0 ; i < list[0].length; i += 1){
            for(let j = 0 ; j < list.length; j += 1) {
                bericht = bericht.concat(list[j][this.kolommen.indexOf(i)]);
            }
        }
        return bericht;
    }

    decodeer(str) {
        let lengte1 = str.match(new RegExp('.{1,' + this.kolommen.length + '}', 'g')).length;
        let lijst = str.match(new RegExp('.{1,' + lengte1 + '}', 'g'));
        let lengte = lijst.length;
        let begin;
        let bericht = "";
        for (let i = 0; i < lengte1; i += 1) {
            for(let j = 0 ; j < lengte; j += 1){
                begin = this.kolommen[j];
                assert(lijst[begin] !== undefined, "ongeldig bericht");
                bericht = bericht.concat(lijst[begin][i]);
            }
        }
        assert(!bericht.includes(undefined), "ongeldig bericht");
        return bericht;
    }
}

