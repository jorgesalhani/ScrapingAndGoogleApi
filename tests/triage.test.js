
const Triage = require("../src/triage.js")

describe('Triage', () => {
  const triage = new Triage('name', 'email')

  test('Today date format DD/MM/YYYY on get_today_date_br()', () => {
    expect(triage.get_today_date_br()).toBe('01/10/2023')
  })

})