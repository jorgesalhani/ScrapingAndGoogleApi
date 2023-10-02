class Triage {
  constructor(name, email) {
    this.name = name
    this.email = email
  }

  run_triage() {
    let today_date_br = get_today_date_br()
  }

  get_today_date_br() {
    let today = new Date()
    let d = String(today.getDate()).padStart(2, '0');
    let m = String(today.getMonth()+1).padStart(2, '0');
    let y = today.getFullYear()

    let today_date_br = `${d}/${m}/${y}`
    return today_date_br
  }
}

function new_triage(name, email) {
  return new Triage(name, email)
}