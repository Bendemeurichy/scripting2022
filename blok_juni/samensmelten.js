//https://dodona.ugent.be/nl/courses/121/series/1662/activities/718691043/#

class Rooster{
    constructor(pattern,rows, col=null) {
        let columns=col? col:rows;
        this.rooster=[];
        for(let i=0;i<pattern.length-columns+1;i+=columns){
            this.rooster.push(pattern.slice(i,i+columns).split(""));
        }
    }

    toArray(){
        return this.rooster
    }

    toString(){
        return this.rooster.map(a=>a.join("")).join("\n")
    }

    groep(row,col){
        let res=[[row,col]];
        let temp=[[row,col]];
        let num=this.rooster[row][col];

        while(temp.length!==0){
            let el=temp.pop();
            if(el[0]<this.rooster.length-1 && (this.rooster[el[0]+1][el[1]])===num && res.every(a => (a[0]!==el[0]+1 || a[1]!==el[1]))) {
                res.push([el[0] + 1, el[1]]);
                temp.push([el[0] + 1, el[1]]);
            }

            if(el[0]>0 &&(this.rooster[el[0]-1][el[1]])===num && res.every(a => (a[0]!==el[0]-1 || a[1]!==el[1]))){
                res.push([el[0]-1,el[1]]);
                temp.push([el[0]-1,el[1]]);
            }

            if(el[1]<this.rooster[0].length-1 &&(this.rooster[el[0]][el[1]+1])===num && res.every(a => (a[0]!==el[0] || a[1]!==el[1]+1))){
                res.push([el[0],el[1]+1]);
                temp.push([el[0],el[1]+1]);
            }

            if(el[1]>0 &&(this.rooster[el[0]][el[1]-1])===num && res.every(a => (a[0]!==el[0] || a[1]!==el[1]-1))){
                res.push([el[0],el[1]-1]);
                temp.push([el[0],el[1]-1]);
            }
        }
        return res.sort(function(a,b){
            if (a[0] !== b[0])
                return (a[0] - b[0]);
<<<<<<< HEAD
            return a[1] - b[1];
=======
            else
                return a[1] - b[1];
>>>>>>> master
        })
    }

    is_opgelost(){
        return this.rooster.every(el=>el.every((a)=>a===this.rooster[0][0]))
    }

    zet(row,col,turn){
        for(let el of this.groep(row,col)){
            let val=(parseInt(this.rooster[el[0]][el[1]])+(turn?1:-1));
            if(val<0){
                val=0;
            } else if (val>9){
                val=9;
            }

            this.rooster[el[0]][el[1]]=""+val;
        }
        return this;
    }
}

