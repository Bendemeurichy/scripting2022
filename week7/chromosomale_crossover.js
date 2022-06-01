// https://dodona.ugent.be/nl/courses/1151/series/12993/activities/1522220852

function crossoverpunten (chr1, chr2) {
  return parseChr(chr1, chr2)[1]
}

function maximaleSom (chr1, chr2) {
  return parseChr(chr1, chr2)[0]
}

function parseChr (chr1, chr2) {
  let elc1 = 0
  let elc2 = 0
  let maxSom = 0
  let crossovers = 0

  let prevcrossover1 = 0
  let prevcrossover2 = 0

  while (elc1 < chr1.length && elc2 < chr2.length) {
    if (chr1[elc1] === chr2[elc2]) {
      crossovers++
      const deelsom1 = elc1 === prevcrossover1 ? 0 : chr1.slice(prevcrossover1, elc1).reduce((a, b) => a + b)
      const deelsom2 = elc2 === prevcrossover2 ? 0 : chr2.slice(prevcrossover2, elc2).reduce((a, b) => a + b)
      maxSom += deelsom1 >= deelsom2 ? deelsom1 : deelsom2

      prevcrossover1 = elc1++
      prevcrossover2 = elc2++
    } else if (chr1[elc1] < chr2[elc2]) {
      elc1++
    } else {
      elc2++
    }
  }
  const deelsom1 = chr1.slice(prevcrossover1).reduce((a, b) => a + b)
  const deelsom2 = chr2.slice(prevcrossover2).reduce((a, b) => a + b)
  maxSom += deelsom1 >= deelsom2 ? deelsom1 : deelsom2
  return [maxSom, crossovers]
}
