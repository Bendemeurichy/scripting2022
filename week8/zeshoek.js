// https://dodona.ugent.be/nl/courses/1151/series/12994/activities/202010242
// https://dodona.ugent.be/nl/courses/1151/series/12994/activities/202010242
class Zeshoek {
  constructor (q, r) {
    this._q = q
    this._r = r
    Object.freeze
  };

  toString () {
    return `Zeshoek(${this._q}, ${this._r})`
  }

  afstand (zeshoek) {
    return (1 / 2) * (Math.abs(this._q - zeshoek._q) + Math.abs(this._r - zeshoek._r) + Math.abs(this._q + this._r - zeshoek._q - zeshoek._r))
  }

  buur (richting) {
    switch (richting) {
      case 'NW':
        return new Zeshoek(this._q, this._r - 1)
        break
      case 'NO':
        return new Zeshoek(this._q + 1, this._r - 1)
        break
      case 'O':
        return new Zeshoek(this._q + 1, this._r)
        break
      case 'ZO':
        return new Zeshoek(this._q, this._r + 1)
        break
      case 'ZW':
        return new Zeshoek(this._q - 1, this._r + 1)
        break
      case 'W':
        return new Zeshoek(this._q - 1, this._r)
        break
      default:
        throw { name: 'AssertionError', message: 'ongeldige richting' }
    }
  }

  pad (richtingpad) {
    try {
      const rpad = richtingpad.replace(/([OW])/g, '$1,').slice(0, -1).split(',')
      let res = this
      rpad.forEach(el => res = res.buur(el))
      return res
    } catch (e) {
      throw { name: 'AssertionError', message: 'ongeldig pad' }
    }
  }

  buren () {
    return ['NW', 'NO', 'O', 'ZO', 'ZW', 'W'].map(el => this.buur(el))
  }
}

// console.log(new Zeshoek(2,5).pad("OWNOZO"));
