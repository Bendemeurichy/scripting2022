// https://dodona.ugent.be/nl/courses/1151/series/12995/activities/1185606204

class Combinatieslot {
  constructor (comb, top = 9) {
    if (comb.length < 1 || comb.some(function (el) { return el > top })) {
      throw { name: 'AssertionError', message: 'ongeldige combinatie' }
    }
    this.schijven = new Array(comb.length).fill(0)
    this.top = top
    this.sol = comb
  }

  toString () {
    return this.schijven.join('-')
  }

  roteer (schijven, pos) {
    schijven = [].concat(schijven)
    for (const el of schijven) {
      if (el >= this.schijven.length || el < 0) {
        throw { name: 'AssertionError', message: 'ongeldige schijf' }
      }
    }
    for (let i = 0; i < pos; i++) {
      for (const el of schijven) {
        this.schijven[el] = (this.schijven[el] + 1) % (this.top + 1)
      }
    }
  }

  open () {
    for (const el in this.schijven) {
      if (this.schijven[el] !== this.sol[el]) {
        return false
      }
    }
    return true
  }
}
