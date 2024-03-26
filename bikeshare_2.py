<<<<<<< HEAD
# bikeshare project
=======
# add comments
# add comments 2
# add comments 3
>>>>>>> refactoring

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    valid_cities = ['chicago', 'new york city', 'washington']
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    city = None
    month = None
    day = None

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in valid_cities:
        city = input("Please enter the name of the city to analyze (Chicago, New York City, Washington): ").lower()
        if city not in valid_cities:
            print("Invalid city name. Please choose from Chicago, New York City, or Washington.")

    # get user input for month (all, january, february, ... , june)
    while month not in valid_months:
        month = input("Please enter the name of the month to filter by, or \"all\" to apply no month filter: ").lower()
        if month not in valid_months:
            print("Invalid month. Please choose from (all, January, February, ... ,June).")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in valid_days:
        day = input("Please enter the name of the day of week to filter by, or \"all\" to apply no day filter: ").lower()
        if month not in valid_months:
            print("Invalid day. Please choose from (all, Monday, Tuesday, ... ,Sunday).")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    m_month = df['month'].value_counts().index[0]
    print(f'The most common month is: {m_month}.')

    # display the most common day of week
    m_day_of_week = df['day_of_week'].value_counts().index[0]
    print(f'The most common month is: {m_day_of_week}.')

    # display the most common start hour
    m_start_hour = df['Start Time'].dt.hour.value_counts().index[0]
    print(f'The most common month is: {m_start_hour}.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    m_start_station = df['Start Station'].value_counts().index[0]
    print(f'The most commonly used start station is: {m_start_station}.')

    # display most commonly used end station
    m_end_station = df['End Station'].value_counts().index[0]
    print(f'The most commonly used end station is: {m_end_station}.')

    # display most frequent combination of start station and end station trip
    df['start_end_combination'] = df['Start Station'] + ' To ' + df['End Station']
    mf_start_end_combination = df['start_end_combination'].value_counts().index[0]
    print(f'The most frequent combination of start station and end station trip is: {mf_start_end_combination}.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = np.sum(df['Trip Duration'])
    print(f'The total travel time is: {total_travel_time}.')

    # display mean travel time
    mean_travel_time = np.mean(df['Trip Duration'])
    print(f'The mean travel time is: {mean_travel_time}.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_dict = df['User Type'].value_counts().to_dict()

    for key, value in user_type_dict.items():
        print(f'For User Type, the count of {key} is {value}.')

    if 'Gender' in df.columns:
        # Display counts of gender
        gender_dict = df['Gender'].value_counts().to_dict()
        
        for key, value in gender_dict.items():
            print(f'For Gender, the count of {key} is {value}.')
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')


    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        earliest_year = np.min(df['Birth Year'])
        print(f'The earliest year of birth is {earliest_year}.')

        most_recent_year = np.max(df['Birth Year'])
        print(f'The most recent year of birth is {most_recent_year}.')

        most_common_year = df['Birth Year'].mode()[0]
        print(f'The most common year year of birth is {most_common_year}.')
    else:
        print('Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe')
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


def display_data(df):
    """Displays first 5 rows of data in dataframe."""
    display = input('\nDo you want to see the first 5 rows of data?\n')
    if display.lower() != 'yes':
        return None
    else:
        start_loc = 0
        print(df.iloc[start_loc: start_loc+5])
        while True:
            display = input('\nDo you want to see the next 5 rows of data?\n')
            if display.lower() != 'no':
                start_loc = start_loc + 5
                print(df.iloc[start_loc: start_loc+5])
            else:
                break


if __name__ == "__main__":
	main()
