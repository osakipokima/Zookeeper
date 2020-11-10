# put your python code here
duration_in_days = int(input())
total_cost_of_food = int(input()) * duration_in_days
round_trip_flight_cost = int(input()) * 2
hotel_stay = int(input()) * (duration_in_days - 1)

print(total_cost_of_food + round_trip_flight_cost + hotel_stay)
