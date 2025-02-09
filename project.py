import time
import pandas as pd
import numpy as np
# user input to filter through different cities
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please choose from the following cities to filter from: \n"
                     "Chicago, New York City, or Washington: ").casefold()
        if city in ("chicago", "new york city", "washington"):
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please choose the month of your choice from the following: \n"
                      "January, February, March, April, May, June, July, August, September, October, November, December "
                      "Or All: ").casefold()
        if month in (
                "january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
                "november",
                "december", "all"):
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please choose the day of your choice from the following: \n"
                    "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All: ").casefold()
        if day in ("monday", 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            break


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df["hour"] = df["Start Time"].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

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

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print("The most common month: {}".format(common_month))


    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print("The most common day is {}".format(common_day))


    # TO DO: display the most common start hour
    common_hour = df["hour"].mode()[0]
    print("The most common hour is: {}".format(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):


    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df["Start Station"].value_counts().head(1)
    print("Most common start station: {}".format(common_start))


    # TO DO: display most commonly used end station
    common_end = df["End Station"].value_counts().head(1)
    print("Most common end station: {}".format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + " " + df['End Station']
    print("Most common start and end stations: {}".format(df["trip"].value_counts().head(1)))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("The total travel time: {}".format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The mean travel time: {}".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("count of user types: {}".format(user_types))




    # TO DO: Display counts of gender
    try:
        user_gender = df["Gender"].value_counts()
        print("gender count: {} ".format(user_gender))
    except:
        print("Chosen city contain no data regaring gender count")


        # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earlist_year = df["Birth Year"].min()
        print("The earlist birth year: {}".format(earlist_year))

    except:
        print("Chosen city contains no data regaring earliest year")

    try:
        recent_year = df["Birth Year"].max()
        print("The most recent year: {}".format(recent_year))

    except:
        print("Chosen city contains no data regarding most recent year")

    try:
        common_year = df["Birth Year"].mode()[0]
        print("The most common year: {}".format(common_year))

    except:
        print("Chosen city contains no data regarding most common year")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? ").casefold()
    start_loc = 0
    while view_data == "yes":
        sliced_df = df.iloc[start_loc:start_loc + 5]
        print(sliced_df)
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display != "yes":
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        # asks user if they want to restars the filtering again
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
