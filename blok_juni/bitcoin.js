// https://dodona.ugent.be/nl/courses/27/series/463/activities/15429256/#

function winst (val, proc) {
  const error = { name: 'AssertionError', message: 'ongeldige acties' }
  const procArr = proc.split('')
  let res = 0
  let owned = 0
  for (const i in procArr) {
    if (procArr[i] === 'K') {
      owned++
      if (owned !== 1) {
        throw error
      }
      res -= val[i]
    } else if (procArr[i] === 'V') {
      res += val[i]
      owned--
      if (owned !== 0) {
        throw error
      }
    }
  }
  if (owned !== 0) {
    throw error
  }
  return res
}

function maximaleWinst (val) {
  let res = 0
  let pacc = -val[0]
  for (let i = 1; i < val.length; i++) {
    const p = res
    res = Math.max(res, pacc + val[i])
    pacc = Math.max(pacc, p - val[i])
  }
  return res
}
