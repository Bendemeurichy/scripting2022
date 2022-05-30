// https://dodona.ugent.be/nl/courses/1151/series/12996/activities/2146630264
class Personage {
  constructor (naam, ...kenmerken) {
    if (arguments.length < 2) {
      throw { name: 'AssertionError', message: 'geen kenmerken' }
    }
    this.naam = naam
    this.kenmerk = []
    for (const el of kenmerken) {
      this.kenmerk.push(el)
    }
  }

  toString () {
    return `new Personage("${this.naam}",${this.kenmerk.map(el => ` "${el}"`)})`
  }

  kenmerken () {
    if (this.kenmerk.length === 1) {
      return `${this.naam} heeft als kenmerken: ${this.kenmerk[0]}`
    }
    return `${this.naam} heeft als kenmerken:${this.kenmerk.slice(0, -1).map(el => ` ${el}`)} en ${this.kenmerk.slice(-1)}`
  }

  voldoet (beschrijving) {
    const has = []
    const hasnt = [];
    (Object.entries(beschrijving)).forEach(([key, value]) => value ? has.push(key) : hasnt.push(key))

    return has.every(el => this.kenmerk.indexOf(el) !== -1) && hasnt.every(el => this.kenmerk.indexOf(el) === -1)
  }
}

function product (A, n) {
  const a = []
  for (let i = 0; i < n; i++) {
    a.push(A)
  }
  const cartesian = (...a) => a.reduce((a, b) => a.flatMap(d => b.map(e => [...d, e])), [[]]) // https://yeahexp.com/cartesian-product-of-multiple-arrays/
  return cartesian(...a)
}

class Spelbord {
  constructor (naam, ...personages) {
    this.personen = []
    for (const el of personages) {
      this.personen.push(el)
    }
    if (!this.personen.some(el => el.naam === naam)) {
      throw { name: 'AssertionError', message: 'onbekende identiteit' }
    }
    this.tegenstander = naam
  }

  toString () {
    return `new Spelbord("${this.tegenstander}",${this.personen.map(el => ` ${el.toString()}`)})`
  }

  kenmerken () {
    return [...(new Set(this.personen.map(el => el.kenmerk).flat()))].sort()
  }

  vraag (beschrijving) {
    let teg
    for (const el of this.personen) {
      if (this.tegenstander === el.naam) {
        teg = el
      }
    }
    return teg.voldoet(beschrijving)
  }

  neerklappen (beschrijving) {
    for (let i = this.personen.length - 1; i >= 0; i--) {
      if (this.personen[i].voldoet(beschrijving) !== this.vraag(beschrijving)) {
        this.personen.splice(i, 1)
      }
    }
    return this
  }

  isOntmaskerd () {
    return this.personen.length === 1
  }

  potentieel (beschrijving) {
    let sum = 0
    for (const el of this.personen) {
      el.voldoet(beschrijving) ? sum += 1 : sum += 0
    }
    return sum
  }

  besteBeschrijving (kenmerken) {
    let res = {}
    for (const el of product([null, true, false], kenmerken.length)) {
      const beschrijving = {}
      for (let i = 0; i < el.length; i++) {
        const kenmerk = kenmerken[i]
        if (el[i] !== null) {
          beschrijving[kenmerk] = el[i]
        }
      }
      if (Math.abs(this.potentieel(res) - this.personen.length / 2) > Math.abs(this.potentieel(beschrijving) - this.personen.length / 2)) {
        res = beschrijving
      }
    }
    return res
  }
}
