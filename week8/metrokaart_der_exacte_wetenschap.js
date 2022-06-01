// https://dodona.ugent.be/nl/courses/1151/series/12994/activities/122335742

class Station {
  constructor (naam, jaar, omschrijving) {
    this.naam = naam
    this.jaar = jaar
    this.omschrijving = omschrijving
    this.lijnen = {}
  }

  toString () {
    return `${this.naam} (${this.jaar}, ${this.omschrijving})`
  }

  verbind (lijn, s2) {
    if (lijn in this.lijnen) {
      throw { name: 'AssertionError', message: `station is reeds verbonden op lijn ${lijn}` }
    }
    this.lijnen[lijn] = s2
  }

  metrolijnen () {
    return Object.keys(this.lijnen).sort()
  }

  volgende (lijn) {
    return this.lijnen[lijn]
  }
}

class Metrokaart {
  stations = []
  laatste = {}
  beginstation (lijn) {
    const stationsL = []
    for (const station of this.stations) {
      if (lijn in station.lijnen) {
        stationsL.push(station)
      }
    }
    const res = [...stationsL]
    for (const el of stationsL) {
      if (el.volgende(lijn) in res) {
        res.splice(res.indexOf(el.volgende(lijn), 1))
      }
    }
    if (res[0] === undefined) {
      return this.eindstation(lijn)
    }
    return res[0]
  }

  eindstation (lijn) {
    return this.laatste[lijn]
  }

  uitbreiden (lijn, station) {
    for (const naam of this.stations) {
      if (station.naam === naam.naam) {
        station = naam
      }
    }
    if (lijn in this.laatste) {
      this.laatste[lijn].verbind(lijn, station)
    }
    this.laatste[lijn] = station
    this.stations.push(station)
  }

  metrolijn (lijn) {
    const res = [this.beginstation(lijn).naam]
    if (this.beginstation(lijn) !== this.eindstation(lijn)) {
      let el = this.beginstation(lijn)
      while (lijn in el.volgende(lijn).lijnen) {
        res.push(el.volgende(lijn).naam)
        el = el.volgende(lijn)
      }
      res.push(this.eindstation(lijn).naam)
    }
    return res
  }
}
