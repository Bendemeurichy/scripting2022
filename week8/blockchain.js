// https://dodona.ugent.be/nl/courses/1151/series/12994/activities/1522818885

class Pearson {
  constructor (tabel = [...Array(256).keys()], combineer = function (h, v) { return (h + v) % 256 }) {
    if (tabel.length !== 256) {
      throw { name: 'AssertionError', message: 'ongeldige tabel' }
    }
    this.tabel = tabel
    this.combineer = combineer
  }

  hash (text) {
    let h = 0
    for (const el of text) {
      h = this.combineer(h, el.charCodeAt(0))
      h = this.tabel[h]
    }
    return h
  }
}

class Blok {
  constructor (hashfunction = new Pearson(), datum = 'Genesis Block', vorige_hash = 0, index = 0, vorige) {
    if (typeof hashfunction.hash === 'function') {
      this.hashf = hashfunction
    } else {
      this.hashf = new Pearson()
    }
    this._hash = this.hashf.hash(index + datum + vorige_hash)
    this._index = index
    this._datum = datum
    this._vorige_hash = vorige_hash
    this.vorige = vorige
  }

  toevoegen (dag) {
    return new Blok(this.hashf, dag, this.hash, this.index + 1, this)
  }

  is_geldig () {
    if (this.hash === this.hashf.hash(this.index + this.datum + this.vorige_hash) && this.index === 0) {
      return true
    } else if (this.hash === this.hashf.hash(this.index + this.datum + this.vorige_hash)) {
      return this.vorige.is_geldig()
    }
    return false
  }

  get index () {
    return this._index
  }

  set index (value) {
    throw { name: 'AssertionError', message: "can't set attribute" }
  }

  get datum () {
    return this._datum
  }

  set datum (value) {
    this._datum = value
  }

  get vorige_hash () {
    return this._vorige_hash
  }

  set vorige_hash (value) {
    throw { name: 'AssertionError', message: "can't set attribute" }
  }

  get hash () {
    return this._hash
  }

  set hash (value) {
    this._hash = value
  }
}
