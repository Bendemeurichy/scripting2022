// https://dodona.ugent.be/nl/courses/1151/series/12995/activities/1885621115
const assert = require('assert')

class Amazones {
  richtingmap =
    {
      N: [-1, 0],
      NO: [-1, 1],
      O: [0, 1],
      ZO: [1, 1],
      Z: [1, 0],
      ZW: [1, -1],
      W: [0, -1],
      NW: [-1, -1]
    }

  constructor () {
    this.amazones = { '3-0': 'A', '6-0': 'a', '0-3': 'B', '9-3': 'b', '0-6': 'C', '9-6': 'c', '3-9': 'D', '6-9': 'd' }
    this.pijlen = []
  }

  toString () {
    const bord = Array(10).fill('__________')
    for (const pos of Object.keys(this.amazones)) {
      const arrPos = [parseInt(pos.slice(0)), parseInt(pos.slice(-1))]
      bord[arrPos[0]] = bord[arrPos[0]].substring(0, arrPos[1]) + this.amazones[pos] + bord[arrPos[0]].substring(arrPos[1] + 1)
    }
    for (const arrow of this.pijlen) {
      bord[arrow[0]] = bord[arrow[0]].substring(0, arrow[1]) + '*' + bord[arrow[0]].substring(arrow[1] + 1)
    }
    return bord.join('\n')
  }

  positie (amazone) {
    const pos = Object.keys(this.amazones).find(key => this.amazones[key] === amazone)
    return [parseInt(pos.slice(0)), parseInt(pos.slice(-1))]
  }

  getKeyByValue (object, value) {
    return Object.keys(object).find(key => object[key] === value)
  }

  includesArray (data, arr) {
    return data.some(e => Array.isArray(e) && e.every((o, i) => Object.is(arr[i], o)))
  }

  mogelijkeRichtingen (letter) {
    const richtingen = []
    for (const key of Object.keys(this.richtingmap)) {
      const newpos = this.positie(letter).map((num, idx) => num + this.richtingmap[key][idx])
      const keystring = this.createKeysting(newpos)
      if (this.checkrond(newpos) && !(this.includesArray(this.pijlen, newpos)) && this.checkotheramazones(newpos)) {
        richtingen.push(key)
      }
    }
    return richtingen
  }

  checkotheramazones (pos) {
    /* let keystring = `${pos[0]}-${pos[1]}`
         if(keystring in this.amazones && !this.amazones[keystring] === letter){
             return false
         }
         return true; */
    return this.amazones[pos[0] + '-' + pos[1]] === undefined
  }

  checkrond (pos) {
    let i = 0
    while (i < 2 && pos[i] < 10 && pos[i] >= 0) {
      i += 1
    }
    return i === 2
  }

  createKeysting (pos) {
    return pos[0] + '-' + pos[1]
  }

  verzetAmazone (letter, richting, n) {
    const newKey = this.posbepaler(letter, richting, n)
    const oldKey = this.getKeyByValue(this.amazones, letter)
    delete Object.assign(this.amazones, { [newKey]: this.amazones[oldKey] })[oldKey]
    return this
  }

  schietPijl (letter, richting, n) {
    let key = this.posbepaler(letter, richting, n).split('-')
    key = [parseInt(key[0]), parseInt(key[1])]
    this.pijlen.push(key)
    return this
  }

  posbepaler (letter, richting, n) {
    const newpos = this.positie(letter).map((num, idx) => num + ((this.richtingmap[richting][idx]) * n))
    const keystring = this.createKeysting(newpos)
    assert(this.checkrond(newpos) && this.checkotheramazones(newpos) && !(this.includesArray(this.pijlen, newpos)), 'ongeldige zet')
    return keystring
  }

  winnaar () {
    let wit = true
    let zwart = true
    for (const key of Object.keys(this.amazones)) {
      if (this.amazones[key] === this.amazones[key].toLowerCase()) {
        if (this.mogelijkeRichtingen(this.amazones[key]).length !== 0) {
          wit = false
        }
      } else {
        if (this.mogelijkeRichtingen(this.amazones[key]).length !== 0) {
          zwart = false
        }
      }
    }
    if (wit) {
      return 2
    } else if (zwart) {
      return 1
    }
    return 0
  }
}
