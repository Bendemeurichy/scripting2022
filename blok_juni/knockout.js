// https://dodona.ugent.be/nl/courses/121/series/1662/activities/378330409/#

function letterfrequenties (str) {
  const letters = str.toUpperCase().replace(/([^A-Z]|\s)/g, '')
  const freq = {}
  for (let i = 0; i < letters.length; i++) {
    const character = letters.charAt(i)
    if (character in freq) {
      freq[character]++
    } else {
      freq[character] = 1
    }
  }
  return freq
}

class Knockout {
  constructor () {
    this.landen = []
    this.landHoofdstad = {}
  }

  land_toevoegen (land, hoofdstad) {
    this.landen.push(land)
    this.landHoofdstad[land] = hoofdstad
  }

  hoofdstad (land) {
    if (land in this.landHoofdstad) {
      return this.landHoofdstad[land]
    }
    throw { name: 'AssertionError', message: 'onbekend land' }
  }

  reguliere_speeltijd (land1, land2) {
    let score1 = 0
    let score2 = 0
    let hoofdstad1 = this.hoofdstad(land1).toUpperCase()
    let hoofdstad2 = this.hoofdstad(land2).toUpperCase()
    for (const el of land1.toUpperCase().replaceAll(' ', '')) {
      if (hoofdstad2.includes(el)) {
        hoofdstad2 = hoofdstad2.replace(el, '')
        score1++
      }
    }
    for (const i of land2.toUpperCase().replaceAll(' ', '')) {
      if (hoofdstad1.includes(i)) {
        hoofdstad1 = hoofdstad1.replace(i, '')
        score2++
      }
    }
    return [score1, score2]
  }

  extra_speeltijd (land1, land2) {
    let score1 = 0
    let score2 = 0
    const freqmap1 = letterfrequenties(land1)
    const freqh1 = letterfrequenties(this.hoofdstad(land2))
    for (const el in freqmap1) {
      if (el in freqh1) {
        score1 += freqmap1[el] * freqh1[el]
      }
    }
    const freqmap2 = letterfrequenties(land2)
    const freqh2 = letterfrequenties(this.hoofdstad(land1))
    for (const k in freqmap2) {
      if (k in freqh2) {
        score2 += freqmap2[k] * freqh2[k]
      }
    }
    return [score1, score2]
  }

  wedstrijd (land1, land2) {
    const landen = [land1, land2]
    const normal = this.reguliere_speeltijd(land1, land2)
    if (normal[0] === normal[1]) {
      const special = this.extra_speeltijd(land1, land2)
      if (special[0] === special[1]) {
        return landen.sort()[0]
      }
      return landen[special.indexOf(Math.max(...special))]
    }
    return landen[normal.indexOf(Math.max(...normal))]
  }

  winnaar () {
    if (!((this.landen.length !== 0) && ((this.landen.length & (this.landen.length - 1)) === 0))) {
      throw { name: 'AssertionError', message: 'ongeldig aantal landen' }
    }
    let bracket = this.landen
    while (bracket.length > 1) {
      const winnaars = []
      for (let i = 0; i < bracket.length; i += 2) {
        winnaars.push(this.wedstrijd(bracket[i], bracket[i + 1]))
      }
      bracket = winnaars
    }
    return bracket[0]
  }
}
