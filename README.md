# HBTN_Assessment_Test
To run the project:
  `python manage.py runserver`

Then open:
  `http://127.0.0.1:8000/`
  
Configured endpoints:
  *  `users/all/`
  Lists all users basic info

  * `'users/new/'`
  Used with a POST request to create a new user

  * `'users/<user_id>/'`
  Gets the info of a particular user with the given ID

  * `'orders/<order_id>/'`
  Gets the info of a particular order with the given ID

  * `'orders/new/'`
  Used with a POST request to create a new order

  * `'orders/<arg>/'`
  `arg` is a string that can be:
    - Multiple order_id: Separated by comma -> '1,2,7,9'
    - Dates: Two dates to get order_id of the orders between those dates YYYY-MM-DD-YYYY-MM-DD -> '2020-04-07-2021-04-07'

  * `'orders/user/<user_id>/'`
  Lists the orders of a particular user given their ID