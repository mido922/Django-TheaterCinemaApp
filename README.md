# TheaterCinemaApp

This is a cinema ticket and seat reservation app created in Django to use in my portfolio.

Features:
1. Lists each seat and its occupancy in a grid.
2. Neat UI and clean presentation.
3. Has a lot of functionality, allowing for adding, editing, and changing reservation
(Soon) Allows cancelling reservations.
(Soon) Allows resetting the list of movies, users or reservations.

Instructions:

1. Clone this git to your device
2. Type python3 manage.py runserver in the directory containing manage.py

Usage:

1. Manager or customer account is selected at account creation(inside the sign-up form), however managers cannot add movies unless their "ManagerAuthenticated" variable is set to true by an admin
2. Both Managers and Customers can reserve seats
