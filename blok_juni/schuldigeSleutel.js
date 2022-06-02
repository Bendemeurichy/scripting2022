// https://dodona.ugent.be/nl/courses/27/series/417/activities/539443625/#

class Codeersleutel {
  constructor (sleutel, woordjes) {
    this.sleutel = sleutel.split('')
    this.rooster = []
    this.afbeelding = {}
    for (let i = 0; i < sleutel.length; i++) {
      this.rooster.push([])
    }
    let r = 0
    let c = 0
    let num = ''
    for (let k = 0; k < woordjes.length; k++) {
      const el = woordjes[k]
      if (c === sleutel.length) {
        c = 0
        r++
      }
      if (isNaN(el)) {
        this.rooster[r].push(el)
        this.afbeelding[el] = this.sleutel[r] + this.sleutel[c]
        c++
      } else {
        if (isNaN(woordjes[k + 1])) {
          num += el
          for (let i = 0; i < parseInt(num); i++) {
            if (c === sleutel.length) {
              c = 0
              r++
            }
            c++
            this.rooster[r].push('-')
          }
          num = ''
        } else {
          num += el
        }
      }
    }
    for (let arr = 1; arr < this.rooster.length; arr++) {
      const len = this.rooster[arr].length
      if (len !== this.rooster[0].length) {
        for (let i = 0; i < this.rooster[0].length - len; i++) {
          this.rooster[arr].push('-')
        }
      }
    }
  }

  codeer (bericht) {
    let res = ''
    for (const el of bericht.toUpperCase().replaceAll(/[^A-Z]/g, '')) {
      if (el in this.afbeelding) {
        res += this.afbeelding[el]
      } else {
        throw { name: 'AssertionError', message: 'ongeldig bericht' }
      }
    }
    return res
  }

  decodeer (bericht) {
    let res = ''
    for (let i = 0; i < bericht.length; i += 2) {
      const el = bericht.slice(i, i + 2)
      let found = false
      for (const key in this.afbeelding) {
        if (this.afbeelding[key] === el) {
          res += key
          found = true
        }
      }
      if (!found) {
        throw { name: 'AssertionError', message: 'ongeldig bericht' }
      }
    }
    return res
  }
}
