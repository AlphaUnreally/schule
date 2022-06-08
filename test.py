country_a = 60000000
country_b = 4000000
falling_perc_a = 0.5
rising_perc_b = 2.5
country_ten_perc_year = 0
country_equals_year = 0
year = 0
result_country_a_1 = 0
result_country_a_2 = 0
result_country_b_1 = 0
result_country_b_2 = 0


while (country_ten_perc_year == 0 or country_equals_year == 0) :
    
    year += 1
    
    country_a = country_a - (country_a * 0.005)

    country_b = country_b + (country_b * 0.025)

    if (country_b >= (country_a * 0.1)) and country_ten_perc_year == 0 :
        country_ten_perc_year = year
        result_country_a_1 = int(country_a)
        result_country_b_1 = int(country_b)

    if (country_b >= country_a) and country_equals_year == 0 :
        country_equals_year = year
        result_country_a_2 = int(country_a)
        result_country_b_2 = int(country_b)

print("Land B erreicht mindesten 10% Bevölkerung von Land A nach " + str(country_ten_perc_year) + " Jahren.")
print("Die Bevölkerung von Land A beträgt " + str(result_country_a_1) + " Menschen")
print("Die Bevölkerung von Land B beträgt " + str(result_country_b_1) + " Menschen")

print("\n")

print("Die Bevölkerung in Land B ist nach " + str(country_equals_year) + " Jahren mindestens so groß wie in Land A.")
print("Die Bevölkerung von Land A beträgt " + str(result_country_a_2) + " Menschen")
print("Die Bevölkerung von Land B beträgt " + str(result_country_b_2) + " Menschen")