# Commutilator API

Base URL: [https://commutilator-api.herokuapp.com/](https://commutilator-api.herokuapp.com/)

| Method | URL                      | Description                                                                     | Request Data                                                                                                                              |
| ------ | ------------------------ | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| POST   | `<BASE_URL>/commute/`    | Create commute object                                                           | `{ "start_location": "test location", "end_location": "test location", "days_per_week_commuting":"distance":15, "avg_gas_commute": 3.76}` |
| POST   | `<BASE_URL>/vehicle/`    | Create vehicle object (model, year, and make are optional. MGP is not optional) | `{ "mpg": 23, "year": "1994", "model": "Acura", "make": "test make" }`                                                                    |
| POST   | `<BASE_URL>/calc/`       | Create calculate object, need vehicle id and commute id                         | `{ "commute": 2, "vehicle": "4" }`                                                                                                        |
| GET    | `<BASE_URL>/result/<id>` | View a result calculation by id                                                 | pass calc object id in url, ex: `<BASE_URL>/result/4`                                                                                     |
