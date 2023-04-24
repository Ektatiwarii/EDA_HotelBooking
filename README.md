# EDA_HotelBooking

The project contains the real world data record of hotel bookings of a city and a resort hotel containing details like bookings, cancellations, guest details etc. from 2015 to 2017.
We have preformed all the steps from Data extraction to Data visualization in this EDA project. Using various libraries provided by python, we have performed the analysis and have drawn useful insights for the business.
In this project we are going to analyze Hotel Booking Data in order to find out valuable insights and give suggestions to increase revenue of hotels.
We can follow these steps in any Exploratory Data Analysis Project.

Programming Language : Python

Libraries used : Pandas, Numpy, Matplotlib, Seaborn


Our Goal:
The main purpose of this study is to perform EDA on the given dataset and draw useful conclusions about the trends in hotel bookings and how factors that control hotel bookings influence each other.

Dataset:
We are given a hotel bookings dataset. This dataset contains booking information for a city hotel and a resort hotel. It contains the following features.

- hotel: Name of hotel ( City or Resort)
- is_canceled: Whether the booking is canceled or not (0 for no canceled and 1 for canceled)
- lead_time: time (in days) between booking transaction and actual arrival.
- arrival_date_year: Year of arrival
- arrival_date_month: month of arrival
- arrival_date_week_number: week number of arrival date.
- arrival_date_day_of_month: Day of month of arrival date
- stays_in_weekend_nights: No. of weekend nights spent in a hotel
- stays_in_week_nights: No. of weeknights spent in a hotel
- adults: No. of adults in single booking record.
- children: No. of children in single booking record.
- babies: No. of babies in single booking record. 
- meal: Type of meal chosen 
- country: Country of origin of customers (as mentioned by them)
- market_segment: What segment via booking was made and for what purpose.
- distribution_channel: Via which medium booking was made.
- is_repeated_guest: Whether the customer has made any booking before(0 for No and 1 for Yes)
- previous_cancellations: No. of previous canceled bookings.
- previous_bookings_not_canceled: No. of previous non-canceled bookings.
- reserved_room_type: Room type reserved by a customer.
- assigned_room_type: Room type assigned to the customer.
- booking_changes: No. of booking changes done by customers
- deposit_type: Type of deposit at the time of making a booking (No deposit/ Refundable/ No refund)
- agent: Id of agent for booking
- company: Id of the company making a booking
- days_in_waiting_list: No. of days on waiting list.
- customer_type: Type of customer(Transient, Group, etc.)
- adr: Average Daily rate.
- required_car_parking_spaces: No. of car parking asked in booking
- total_of_special_requests: total no. of special request.
- reservation_status: Whether a customer has checked out or canceled,or not showed 
- reservation_status_date: Date of making reservation status.


Important Steps:
Data Cleaning and Feature Engineering
1. Handling null values
2. All duplicate rows were dropped.
3. Converting columns to appropriate data types
4. Changed data type of children, company, agent to int type.

Renaming the columns:
The adr column was renamed for better understanding to average_daily_rate

Removing outliers:
One outlier was found in the average_daily_rate column. Dropping them.

Creating new columns:
Creating new column Total_members by adding adults+children+babies.


Exploratory Data Analysis
Performed EDA and tried answering the following questions:

  Which hotel has more no of bookings and What is the  percentage of bookings in each hotel ?
  Hotel Wise Bookings based on Month and year also What is the trend of bookings within a month ?
  Which meal type is the  most preffered meal of customers ?
  Country Wise - Number of Bookings ?
  Which room type is in most demand and which room type generates the  highest average daily rate?
  How long do people stay at the hotels?
  What is preferred stay length in each hotel based on weekday nights and weekend nights ?
  Which Booking is preffered with the deposite type?
  What is the Average daily rate month wise also which are the most busy months??
  Which channel is mostly used for the booking of hotels? 
  Chances that its customer will return for another stay?
  Which types of customers mostly make bookings?
 How many customers are most likely to require a parking space?
 
 
 Insights:
 
 1% bookings are for City hotel and 39% bookings are for Resort hotel, therefore City Hotel is busier than Resort hotel. 
 July- August are the most busier and profitable months for both of hotels.  
 Most popular meal type is BB(Bed and Breakfast).
 Most of the guests came from european countries, with highest number of guests from Portugal.
 Most demanded room type is A, but better average daily rate generating rooms H, G and C. Hotels should increase the no. of room types A and H to maximise revenue.
 Most common stay length is less than 4 days and generally people prefer City hotel for short stay, but for long stays, Resort Hotel is preferred.
 Guests use different channels for making bookings out of which most preferred way is TA/TO. 
 Overall average daily rate of City hotel is slightly higher than Resort hotel and no. of bookings of City hotel is also higher than Resort hotel. Hence, City hotel is makes more revenue.
 Cancelation rate is higher in city hotel. With lead time more than 100 there is more possibility of cancellation.
  Both hotels have very small percentage that customer will repeat.
 Arrivals in hotels increases at weekends and also the average daily rate tends to go up as month ends. 
