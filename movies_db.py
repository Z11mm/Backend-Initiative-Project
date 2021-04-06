from datetime import date

movies_db = {
  "movies": [
    {
      "title": "Lord of The Rings",
      "year": 2012,
      "genre": "fantasy",
      "can_rent": True,
      "cast": "Jane Doe, Jane Doe, Jane Doe",
      "date added": date.today().strftime("%B %d, %Y")
    },
    {
      "title": "Titanic",
      "year": 1968,
      "genre": "romance",
      "can_rent": True,
      "cast": "Jane Doe, Jane Doe, Jane Doe",
      "date added": date.today().strftime("%B %d, %Y")
    }
  ]
}