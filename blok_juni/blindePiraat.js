// https://dodona.ugent.be/nl/courses/264/series/2691/activities/1672890574/#

function hoofdletters (str) {
  return str.toUpperCase()
}

function verwijderWitruimte (str) {
  return str.replaceAll(/\s/g, '')
}

class Tekst {
  constructor (tekst) {
    this.tekst = tekst
  }

  fragmenten (k, ...filters) {
    let verdeling = this.tekst
    for (const el of filters) {
      verdeling = el(verdeling)
    }
    const res = []
    for (let i = 0; i < verdeling.length - k + 1; i++) {
      res.push(verdeling.slice(i, i + k))
    }
    return res
  }
}

class Multiset {
  constructor (elements) {
    if (!Array.isArray(elements)) {
      this.freqMap = elements
    } else {
      this.freqMap = {}
      for (const el of elements) {
        if (el in this.freqMap) {
          this.freqMap[el]++
        } else {
          this.freqMap[el] = 1
        }
      }
    }
  }

  toObject () {
    return this.freqMap
  }

  kardinaliteit () {
    if (Object.entries(this.freqMap).length === 0) {
      return 0
    }
    return Object.values(this.freqMap).reduce((a, b) => a + b)
  }

  doorsnede (mset) {
    const zset = {}
    for (const el in mset.freqMap) {
      if (el in this.freqMap) {
        zset[el] = Math.min(this.freqMap[el], mset.freqMap[el])
      }
    }
    return new Multiset(zset)
  }

  unie (mset) {
    const zset = { ...this.freqMap }
    for (const el in mset.freqMap) {
      if (el in zset) {
        if (mset.freqMap[el] > zset[el]) {
          zset[el] = mset.freqMap[el]
        }
      } else {
        zset[el] = mset.freqMap[el]
      }
    }
    return new Multiset(zset)
  }
}

function jaccard (mset1, mset2) {
  return mset1.doorsnede(mset2).kardinaliteit() / mset1.unie(mset2).kardinaliteit()
}

function dice (mset1, mset2) {
  return (2 * mset1.doorsnede(mset2).kardinaliteit()) / (mset1.kardinaliteit() + mset2.kardinaliteit())
}

function similariteit (maat, text1, text2, k) {
  let ctext1 = new Tekst(text1)
  ctext1 = new Multiset(ctext1.fragmenten(k, verwijderWitruimte, hoofdletters))
  let ctext2 = new Tekst(text2)
  ctext2 = new Multiset(ctext2.fragmenten(k, verwijderWitruimte, hoofdletters))
  return maat(ctext1, ctext2)
}
