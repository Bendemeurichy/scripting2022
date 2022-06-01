// https://dodona.ugent.be/nl/courses/1151/series/12993/activities/1091605158

// https://www.codegrepper.com/code-examples/javascript/how+to+know+if+two+objects+contain+same+values+javascript

function draaien (pa, pb, pc) {
  const isEqual = (...objects) => objects.every(obj => JSON.stringify(obj) === JSON.stringify(objects[0]))

  if (isEqual(pa, pb) || isEqual(pa, pc) || isEqual(pb, pc)) {
    throw { name: 'AssertionError', message: 'drie punten moeten verschillend zijn' }
  }
  const val = ((pb.x - pa.x) * (pc.y - pa.y)) - ((pb.y - pa.y) * (pc.x - pa.x))
  return val === 0 ? 0 : val / Math.abs(val)
}

function volgende (begin, punten, wijzerzin) {
  for (const el of punten) {
    if (el.x === begin.x && el.y === begin.y) {
      punten.splice(punten.indexOf(el), 1)
    }
  }
  const cond = wijzerzin ? 1 : -1
  let kand = punten[0]

  for (let i = 1; i < punten.length; i++) {
    if (draaien(begin, kand, punten[i]) === cond) {
      kand = punten[i]
    } else if (draaien(begin, kand, punten[i]) === 0) {
      if (afstand(begin, kand) < afstand(begin, punten[i])) {
        kand = punten[i]
      }
    }
  }
  return kand
}

function afstand (pa, pb) {
  return Math.sqrt((pa.x - pb.x) ** 2 + (pa.y - pb.y) ** 2)
}

function contour (vorm, wijzerzin) {
  let begin = vorm[0]
  for (let i = 1; i < vorm.length; i++) {
    if (vorm[i].x < begin.x) {
      begin = vorm[i]
    } else if (vorm[i].x === begin.x) {
      if (vorm[i].y < begin.y) {
        begin = vorm[i]
      }
    }
  }
  let punten = []
  const res = []
  res.push(begin)
  let cycle = false
  while (!cycle) {
    punten = vorm.slice()
    const next = volgende(begin, punten, wijzerzin)
    if (next.x === res[0].x && next.y === res[0].y) {
      cycle = true
    } else {
      res.push(next)
      begin = next
    }
  }
  return res
}
