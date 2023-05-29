#To calculate a user's total holiday cost


def hotel_cost(num_nights1,city_flight1):
    h_cost=num_nights1*price_guide[city_flight1][1]
    return h_cost
def plane_cost(city_flight1):
    f_cost=price_guide[city_flight1][0]
    return f_cost
def car_rental(rental_days1,city_flight1):
    c_cost=rental_days1*price_guide[city_flight1][2]
    return c_cost

#this function calls the above fuctions and returns the cost of flight,hotel,car rental and also the total cost of the holiday
def holiday_cost(num_nights1,city_flight1,rental_days1):
    h=hotel_cost(num_nights1,city_flight1)
    p=plane_cost(city_flight1)
    c=car_rental(rental_days1,city_flight1)
    T_cost = h+p+c
    return [p,h,c,T_cost]


# get user input for the city to visit; number of days to stay at hotel and number of days for car rental.
city_flight = input("Enter the city you would like to go on a holiday - 'London','Dubai': ").upper()
num_nights = int(input("Enter the number of nights you would like to stay in the hotel: "))
rental_days = int(input("Enter the number of days that you will be hiring the car: "))

#Dictionary which holds: destination;flight cost,hotel cost,car rental cost
price_guide = {
                "LONDON":[300,100,50],
                "DUBAI":[200,50,25]
}

#call the function 'holiday cost'
Total_cost=holiday_cost(num_nights,city_flight,rental_days)

print("Your choosen holiday city is: " , city_flight)
print("Flight Cost to {}: £".format(city_flight) ,Total_cost[0])
print("Hotel Stay: £" ,Total_cost[1])
print("Car Rental: £" ,Total_cost[2])
print("Total holiday cost: £" , Total_cost[3])
