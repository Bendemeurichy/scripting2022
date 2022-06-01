// https://dodona.ugent.be/nl/courses/1151/series/12993/activities/289356595

function codeersleutel (sleutel) {
  const res = {}
  sleutel = sleutel.replace(/\s+/g, '')
  for (let i = 0; i < sleutel.length; i++) {
    if (sleutel[i].toUpperCase() in res) {
      res[sleutel[i].toUpperCase()].push(i + 1)
    } else {
      res[sleutel[i].toUpperCase()] = [i + 1]
    }
  }
  return res
}

function codeer (code, sleutel) {
  sleutel = codeersleutel(sleutel)
  const res = []
  for (const el of code) {
    const number = sleutel[el.toUpperCase()].shift()
    sleutel[el.toUpperCase()].push(number)
    res.push(number)
  }
  return res
}
