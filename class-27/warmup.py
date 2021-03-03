
def get_planet_age(age_in_seconds):
    planet_years = {
        'earth' : 31557600,
        'mercury': 31557600 * 0.2408467,
        'venus' : 31557600 * .61519726,
        'mars' : 31557600 * 1.8808158,
        'jupiter' : 31557600 * 11.862615,
        'saturn' : 31557600 * 9.447498,
        'uranus' : 31557600 * 84.016846,
        'neptune' : 31557600 * 164.79132 
    }
    for name, value in planet_years.items():
        if name == 'earth':
            print(f'On {name} you would be {age_in_seconds} seconds old or {age_in_seconds / value} in years')
        elif name != 'earth':
            print(f'On {name} you would be {value * age_in_seconds} seconds old or {age_in_seconds / value} in years')

get_planet_age(31557600 * 75)