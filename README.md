# BOUTIQUE HOTEL DEVELOPMENT (STATIC) 
## Technologies USed :SQL, Python, HTML


## General description:
The objective of this Project is to build a database system for boutique hotel business. Below are the entities considered while building the system.

__Entities- __ 

1. P_CUSTOMER- Primary customer responsible for bookings, payments and events
2. DEPENDANTS- Customers who are related to the primary customer
3. ROOMS- Rooms available in the hotel
4. OFFERS- Offers that are applicable for the season
5. EVENT- Events that are organized by customers
6. PAYMENT- Payment details of the bookings
7. BOOKINGS- Reservations made by each primary customer

__Assumptions__

Assumptions based on the entities listed above-
1. A Primary customer can book only one event at a time
2. A Dependent cannot exist without a primary customer
3. A Primary customer can book many rooms
4. All rooms including the rooms used for events is identified by a unique room no- rid 
5. Reservations can be searched only through the primary customer phone number
6. Primary Customer no is key to for the entities - events, bookings, payment and dependents
7. Customer should book an event in order to register for an event
8. All the details about the customers, room bookings and events are entered by hotel staff
