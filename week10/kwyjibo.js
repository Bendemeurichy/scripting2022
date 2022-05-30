// https://dodona.ugent.be/nl/courses/1151/series/12996/activities/900625397
class Scrabble {
  constructor (n) {
    if (n > 26 || n < 1) {
      throw { name: 'AssertionError', message: 'ongeldig spelbord' }
    }
    this.bord = []
    for (let i = 0; i < n; i++) {
      this.bord.push(new Array(n))
    }
  }

  toString () {
    let lstring = ''
    for (let i = 0; i < this.bord[0].length; i++) {
      let strr = ''
      for (const el of this.bord) {
        strr += el[i] === undefined ? '-' : el[i]
      }
      strr += '\n'
      lstring += strr
    }
    return lstring.replace(/\n$/, '')
  }

  aanleggen (coord, letters) {
    const oldboard = this.bord.map(el => [...el])

    const rijNr = coord.replace(/\D/g, '') - 1
    const kolomNr = (coord.replace(/\d/g, '')).charCodeAt(0) - 'A'.charCodeAt(0)
    let res = ''
    if (isNaN(coord[0])) {
      if (rijNr + letters.length > this.bord[0].length) {
        throw { name: 'AssertionError', message: 'woord kan niet aangelegd worden' }
      }
      for (let i = rijNr; i < rijNr + letters.length; i++) {
        if (this.bord[kolomNr][i] === undefined) {
          this.bord[kolomNr][i] = letters[i - rijNr]
          res += letters[i - rijNr]
        } else if (this.bord[kolomNr][i].toUpperCase() === letters[i - rijNr]) {
          res += `(${this.bord[kolomNr][i]})`
        } else {
          this.bord = oldboard
          throw { name: 'AssertionError', message: 'woord kan niet aangelegd worden' }
        }
      }
    } else {
      if (kolomNr + letters.length > this.bord[0].length) {
        throw { name: 'AssertionError', message: 'woord kan niet aangelegd worden' }
      }
      for (let i = kolomNr; i < kolomNr + letters.length; i++) {
        if (this.bord[i][rijNr] === undefined) {
          this.bord[i][rijNr] = letters[i - kolomNr]
          res += letters[i - kolomNr]
        } else if (this.bord[i][rijNr].toUpperCase() === letters[i - kolomNr]) {
          res += `(${this.bord[i][rijNr]})`
        } else {
          this.bord = oldboard
          throw { name: 'AssertionError', message: 'woord kan niet aangelegd worden' }
        }
      }
    }
    return res.replaceAll(')(', '')
  }
}
