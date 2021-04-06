from datetime import date

users_db = {
  "users": [
    {
      "name": "Oma",
      "age": 24,
      "gender": "female",
      "rentals": 0,
      "date joined": date.today().strftime("%B %d, %Y")
    },
    {
      "name": "Tunde",
      "age": 33,
      "gender": "male",
      "rentals": 0,
      "date joined": date.today().strftime("%B %d, %Y")
    }
  ]
}