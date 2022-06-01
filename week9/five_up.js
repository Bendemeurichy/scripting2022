// https://dodona.ugent.be/nl/courses/1151/series/12995/activities/1278671139

class Stapel {
  constructor (kaartjes) {
    if (kaartjes.length > 52 || new Set(kaartjes).size !== kaartjes.length) {
      throw { name: 'AssertionError', message: 'ongeldige kaarten' }
    }
    const re = /^(10|[2-9JQKA])[CDHS]$/i
    for (const el of kaartjes) {
      if (!re.test(el)) {
        throw { name: 'AssertionError', message: 'ongeldige kaarten' }
      }
      if (/[jqka][cdhs]/i.test(el)) {
        if (/[jqka][CDHS]/.test(el) || /[JQKA][cdhs]/.test(el)) {
          throw { name: 'AssertionError', message: 'ongeldige kaarten' }
        }
      }
    }
    this.kaarten = kaartjes
  }

  toString () {
    return this.kaarten.map(function (el) {
      if (el[el.length - 1].toUpperCase() !== el[el.length - 1]) {
        return '**'
      }
      return el
    }).join(' ')
  }

  selectie_omdraaien (indexen) {
    if (indexen === undefined) {
      indexen = [...Array(this.kaarten.length).keys()]
      indexen = indexen.map(el => el + 1)
    }
    for (const el of indexen) {
      if (this.kaarten[el - 1] === this.kaarten[el - 1].toUpperCase()) {
        this.kaarten[el - 1] = this.kaarten[el - 1].toLowerCase()
      } else {
        this.kaarten[el - 1] = this.kaarten[el - 1].toUpperCase()
      }
    }
    return this
  }

  bovenste_omdraaien (size) {
    const bovenste = new Stapel(this.kaarten.splice(0, size))
    this.kaarten = bovenste.selectie_omdraaien().kaarten.reverse().concat(this.kaarten)
    return this
  }

  couperen (size) {
    const bovenste = this.kaarten.splice(0, size)
    this.kaarten = this.kaarten.concat(bovenste)
    return this
  }
}
