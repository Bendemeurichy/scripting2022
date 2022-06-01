// https://dodona.ugent.be/nl/courses/1151/series/12997/activities/2141798882/#
class Doolhof {
  constructor (rijen, kolommen, hormuren, vertmurenn, uitgang, thes, min) {
    this.rijen = rijen
    this.kolommen = kolommen
    this.hormuren = hormuren
    this.vertmuren = vertmurenn
    this.uitgang = uitgang
    this.the = thes
    this.min = min
    this.richtingen = { L: -1, U: -kolommen, D: kolommen, R: 1 }
  }

  isGeldig (r, k, d) {
    if (!(r < this.rijen && k < this.kolommen)) {
      return false
    } else if (!d in this.richtingen) {
      return false
    } else if (d === 'U' || d === 'D') {
      if (this.vertmuren.some(el => el === ((r * this.kolommen + k) + this.richtingen[d]))) {
        return false
      }
    }
    const temp = ((r * this.kolommen + k) + this.richtingen[d])
    return !this.hormuren.some(el => el === ((r * this.kolommen + k) + this.richtingen[d]))
  }
}
const doolhof01 = new Doolhof(6, 6, [6, 13, 16, 20, 22, 26], [8, 9, 10, 13, 14, 16, 20, 25, 27, 30, 31], [0, 4], [2, 4], [0, 0])
doolhof01.isGeldig(1, 3, 'R')
