from datetime import date

users_db = {
  "users": [
    {
      "id": 1,
      "name": "Oma",
      "email": "oma@yahoo.com",
      "password": "jgoeoajg",
      "date joined": date.today().strftime("%B %d, %Y"),
      "rentals": 0
    },
    {
      "id": 2,
      "name": "Tunde",
      "email": "tunde@yahoo.com",
      "password": "8598464g",
      "date joined": date.today().strftime("%B %d, %Y"),
      "rentals": 0
    }
  ]
}