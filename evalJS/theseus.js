// https://dodona.ugent.be/nl/courses/1151/series/12997/activities/2141798882/#
const assert = require('assert')
class Doolhof {
  constructor (r, k, hor, vert, uitgang, thes, mino) {
    this.r = r
    this.k = k
    this.hor = hor
    this.vert = vert
    this.uitgang = uitgang
    this.thes = thes
    this.mino = mino
  }

  isGeldig (r, k, d) {
    switch (d) {
      case 'U':
        if (r - 1 >= 0 && !this.hor.includes(this.k * r + k)) {
          return true
        }
        break
      case 'D':
        if (r + 1 < this.r && !this.hor.includes(this.k * (r + 1) + k)) {
          return true
        }
        break
      case 'R':
        if (k + 1 < this.k && !this.vert.includes(this.r * (k + 1) + r)) {
          return true
        }
        break
      case 'L':
        if (k - 1 >= 0 && !this.vert.includes(this.r * k + r)) {
          return true
        }
        break
      case 'P':
        return true
    }
    return false
  }

  isGewonnen () {
    return this.thes[0] === this.uitgang[0] && this.thes[1] === this.uitgang[1]
  }

  isVerloren () {
    return this.mino[0] === this.thes[0] && this.mino[1] === this.thes[1]
  }

  toString () {
    let doolhof = ''
    // startlijn maken
    let startlijn = ''
    for (let i = 0; i < this.k; i++) {
      startlijn += '+-'
    }
    startlijn += '+\n'
    doolhof += startlijn
    for (let r = 0; r < this.r; r++) {
      let horLijn = ''
      let vertLijn = '|'
      for (let k = 0; k < this.k; k++) {
        // 2x
        const horCode = this.k * (r + 1) + k
        const vertCode = this.r * k + (r)
        horLijn += this.hor.includes(horCode) ? '+-' : '+ ';
        if (this.vert.includes(vertCode)) {
          vertLijn += '| '
        } else {
          vertLijn += k === 0 ? ' ' : '  ';
        }
      }
      horLijn = this.hor.includes((r + 1) * this.k + this.k - 1) ? horLijn.substring(0, horLijn.length - 1) + '-+' : horLijn.substring(0, horLijn.length - 1) + ' +';
      doolhof += vertLijn + '|\n' + horLijn + '\n'
    }
    doolhof = this.plaatsCharInDoolhof(doolhof, this.uitgang, 'S')
    doolhof = this.plaatsCharInDoolhof(doolhof, this.thes, 'T')
    doolhof = this.plaatsCharInDoolhof(doolhof, this.mino, 'M')
    return doolhof.substring(0, doolhof.length - ((this.k + 1) * 2)) + startlijn.substring(0, startlijn.length - 1)
  }

  plaatsCharInDoolhof (doolhof, pos, char) {
    const index = (pos[0] + Number(pos[0]) + 1) * 2 * (this.k + 1) + 1 + pos[1] * 2

    return this.replaceAt(doolhof, index, char)
  }

  replaceAt (string, index, replacement) {
    return string.substring(0, index) + replacement + string.substring(index + replacement.length)
  }

  verzetTheseus (richting) {
    assert(this.isGeldig(this.thes[0], this.thes[1], richting), 'ongeldige zet')
    switch (richting) {
      case 'U':
        this.thes[0] -= 1
        break
      case 'D':
        this.thes = [this.thes[0] + 1, this.thes[1]]
        break
      case 'R':
        this.thes = [this.thes[0], this.thes[1] + 1]
        break
      case 'L':
        this.thes[1] -= 1
        break
      case 'P':
        break
    }
  }

  verzet (volgorde) {
    let res = ''
    for (const el of volgorde.split('')) {
      this.verzetTheseus(el)
      if (this.isGewonnen()) {
        return res
      }
      for (let _ = 0; _ < 2; _++) {
        if (!this.isGewonnen() && !this.isVerloren()) {
          res += this.verzetMinotaurus()
        }
      }
    }
    return res
  }

  verzetMinotaurus () {
    const dist = Math.abs(this.thes[0] - this.mino[0]) + Math.abs(this.thes[1] - this.mino[1])
    if (this.isGeldig(this.mino[0], this.mino[1], 'L')) {
      if (Math.abs(this.thes[0] - this.mino[0]) + Math.abs(this.thes[1] - (this.mino[1] - 1)) < dist) {
        this.mino[1]--
        return 'L'
      }
    }
    if (this.isGeldig(this.mino[0], this.mino[1], 'R')) {
      if (Math.abs(this.thes[0] - this.mino[0]) + Math.abs(this.thes[1] - (this.mino[1] + 1)) < dist) {
        this.mino[1]++
        return 'R'
      }
    }
    if (this.isGeldig(this.mino[0], this.mino[1], 'D')) {
      if (Math.abs(this.thes[0] - (this.mino[0] + 1)) + Math.abs(this.thes[1] - this.mino[1]) < dist) {
        this.mino[0]++
        return 'D'
      }
    }
    if (this.isGeldig(this.mino[0], this.mino[1], 'U')) {
      if (Math.abs(this.thes[0] - (this.mino[0] - 1)) + Math.abs(this.thes[1] - this.mino[1]) < dist) {
        this.mino[0]--
        return 'U'
      }
    }
    return 'P'
  }
}
