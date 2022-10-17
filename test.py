import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_list = ['chicago', 'new york city' , 'washington']

month_list = ['all', 'january', 'february' , 'march', 'april','may','june']

day_list = ['all', 'monday', 'tuesday' , 'wednesday', 'thursday','friday','saturday','sunday']

df_chi = pd.read_csv('./chicago.csv')
df_nyc = pd.read_csv('./new_york_city.csv')
df_was = pd.read_csv('./washington.csv')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input ('So which of the following cities do you want to explore? Chicago, New York City or Washington?').lower()
    while city not in city_list:
        print ('That was an invalid input.\n')
        city = input ('Choose between: Chicago, New York City or Washington.').lower()
            
   # TO DO: get user input for month (all, january, february, ... , june)
    month = input ('Which month?').lower()
    while month not in month_list:
        print ('That was an invalid input.\n')
        month = input ('Choose between: all month, january, february, march, april, may or june ').lower()
                  

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input ('Which week day?').lower()
    while day not in day_list:
        print ('That was an invalid input.\n')
        day = input ('Choose between: all, monday, tuesday, wednesday, thursday, friday, saturday or sunday ').lower()

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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month.index(month) + 1

    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print ('The most common month is ' , popular_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day_name
    popular_dow = df['day'].mode()[0]
    print (df['day'])
    print ('The most common day of week is ' , popular_dow)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print ('The most common hour is ' , popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


                
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            

if __name__ == "__main__":
	main()
