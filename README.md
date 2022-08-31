# Commutilator API

Base URL: [https://commutilator-api.herokuapp.com/](https://commutilator-api.herokuapp.com/)

| Method | URL                      | Description                                                                     | Request Data                                                                                                                              |
| ------ | ------------------------ | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| POST   | `<BASE_URL>/commute/`    | Create commute object                                                           | `{ "start_location": "test location", "end_location": "test location", "days_per_week_commuting":"distance":15, "avg_gas_commute": 3.76}` |
| POST   | `<BASE_URL>/vehicle/`    | Create vehicle object by providing mpg (model, year, and make are optional; mpg is not optional) | `{ "mpg": 23, "year": "1994", "model": "Acura", "make": "test make" }`                                                                    |
| POST   | `<BASE_URL>/calc/`       | Create calculation object by providing vehicle id and commute id                         | `{ "commute": "2", "vehicle": "4" }`                                                                                                        |
| GET    | `<BASE_URL>/result/<id>` | View a specific result object by id                                                | pass result object id in url, ex: `<BASE_URL>/result/4`                                                                                     |
| GET    | `<BASE_URL>/detail/` | View a list of all own calculations                                              |                                                                                      |
| GET    | `<BASE_URL>/detail/<id>` | View a specific calculation object by id                                            | pass calculation object id in url, ex: `<BASE_URL>/detail/6`                                                                                 |


## Authentication

### Create User

> /api/auth/users/
> 

Method: POST

Data json:

```python
{ 
  "username": "<username>", 
  "password": "<password>" 
}
```

Response: User json object

### Login

> /api/auth/token/login/
> 

Method: POST

Data json:

```python
{ 
  "username": "<username>", 
  "password": "<password>" 
}
```

Response: Example Authentication Token

```python
{
  "auth_token": "a65751fc4fa58a41cce703fb4deee8a9fe367618"
}
```

### Logout

> /api/auth/token/logout/
> 

Method: POST

Data: Authentication Token (See Example Auth Token in Login Section)

Response: No Data

## Create Objects

### Commute

> /commute/
> 

Method: POST

Data json: 

```python
{
  "start_location": "6529 Battle Bridge Rd., Raleigh, NC 27610",
  "end_location": "2655 Meridian Pkwy, Durham, NC 27713",
  "distance": "29.90",
  "days_per_week_commuting": 5,
  "start_avg_gas": 3.52,
  "end_avg_gas": 3.79
}
```

### Vehicle

> /vehicle/
> 

Method: POST

Data json: 

```python
{
  "make": "Ford",
  "model": "Edge",
  "year": 2011,
  "mpg": 23
}
```

### Calculation

> /calc/
> 

Method: POST

Data json: 

```python
{
  "commute": "2",
  "vehicle": "4"
}
```

## Return Objects

### Result Detail

> /result/:id
> 

Note: Id is the id of the result

Method: GET

Response: Single result object

### Calculation List

> /detail/
> 

Method: GET

Response: Array of all calculations

### Calculation Detail

> /detail/:id
> 

Note: Id is the id of the calculation

Method: GET, PUT, PATCH, DELETE

Response: Single calculation object
