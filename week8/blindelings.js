// https://dodona.ugent.be/nl/courses/1151/series/12994/activities/1458295391
class Stapel {
  constructor (stapel) {
    this.stapel = stapel.slice()
  }

  toArray () {
    return this.stapel
  }

  toString () {
    const res = []
    for (const el of this.stapel) {
      if (el.charAt(el.length - 1).toUpperCase() === el.charAt(el.length - 1)) {
        res.push(el)
      } else {
        res.push('**')
      }
    }
    return res.join(' ')
  }

  beeldzijdeBoven () {
    let res = 0
    for (const el of this.stapel) {
      if (el.charAt(el.length - 1).toUpperCase() === el.charAt(el.length - 1)) {
        res++
      }
    }
    return res
  }

  splitsen (n = this.beeldzijdeBoven()) {
    const s1 = []
    const s2 = []
    for (let c = 0; c < this.stapel.length; c++) {
      if (c < n) {
        s1.push(this.stapel[c])
      } else {
        s2.push(this.stapel[c])
      }
    }
    return [new Stapel(s1), new Stapel(s2)]
  }

  omdraaien (n = undefined) {
    if (typeof n === 'undefined') {
      const res = []
      for (const el of this.stapel) {
        res.push(this.draaiKaart(el))
      }
      this.stapel = res
    } else if (typeof n === 'number') {
      this.stapel[n] = this.draaiKaart(this.stapel[n])
    } else {
      for (const el of n) {
        this.stapel[el] = this.draaiKaart(this.stapel[el])
      }
    }
    return this
  }

  evenveelNaarBovenAls (s) {
    return this.beeldzijdeBoven() === s.beeldzijdeBoven()
  }

  draaiKaart (el) {
    return el.charAt(el.length - 1).toUpperCase() === el.charAt(el.length - 1) ? el.toLowerCase() : el.toUpperCase()
  }
}
