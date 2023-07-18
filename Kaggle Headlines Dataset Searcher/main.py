"""Program uses Pandas to read the original .csv, 
	create a dataframe of the headlines and dates pulled from the original .csv
	and finally saves the dataframe as a single .csv or separate .csv files."""
import pandas as pd

#https://www.kaggle.com/datasets/jordankrishnayah/45m-headlines-from-2007-2022-10-largest-sites
# Load data from .csv file containing headlines, date, publication, and URL
data = pd.read_csv("headlines.csv")

dates = data["Date"].tolist()
publication = data["Publication"].tolist()
headlines = data["Headline"].tolist()


def get_keywords():
    """Asks the user for an input to search for. Can search for multiple inputs.
    Saves the input(s) to a list. If multiple inputs are given, asks the user
    if they'd like a separate .csv file for each input or if they should be 
    saved to the same file."""

    keywords = []

    keyword = input("What keyword would you like to search for?\n")
    keywords.append(keyword)

    while True:
        keyword = input(
            "Would you like to add another related keyword to your search? Y/N\n"
        )
        if keyword.lower() == "y":
            keyword = input("What keyword would you like to search for?\n")
            keywords.append(keyword)
            continue
        elif keyword.lower() == "n":
            break
        else:
            print("Please enter either Y or N.")

    if len(keywords) > 1:
        while True:
            save_type = input(
                "Would you like to save the data in a single file (1) or separate files (2)?\n"
            )
            if save_type == "1":
                save_single_csv(keywords)
            elif save_type == "2":
                save_multi_csv(keywords)
            else:
                print("Please enter either 1 (single file) or 2 (separate files)")
    else:
        save_single_csv(keywords)


def save_single_csv(keywords):
    """Scans through headlines for any that match a keyword in the list
    	and appends titles with it as well as title_dates with the date
        of the headline. Converts the two lists to a Pandas dataframe
        and saves it to a single .csv file."""

    titles = []
    title_dates = []

    for k in keywords:
        for i, headline in enumerate(headlines):
            if k.lower() in str(headline).lower() and headline not in titles:
                titles.append(headline)
                title_dates.append(dates[i])
                print(headline)

    headline_data = pd.DataFrame({"Date": title_dates, "Headline": titles, "Publication": publication})
    headline_data.to_csv("CSVs/" + "-".join(keywords) + ".csv")
    print("Finished with " + "-".join(keywords) + ".csv")
    search_again()


def save_multi_csv(keywords):
    """Scans through headlines for any that match the current keyword the 
        for loop is on and appends titles with it as well as title_dates 
        with the date of the headline. Converts the two lists to a Pandas 
        dataframe and saves it to a .csv file before iterating through 
        the rest of the keywords."""

    for k in keywords:
        titles = []
        title_dates = []

        for i, headline in enumerate(headlines):
            if k.lower() in str(headline).lower() and headline not in titles:
                titles.append(headline)
                title_dates.append(dates[i])
                print(headline)

        headline_data = pd.DataFrame({"Date": title_dates, "Headline": titles, "Publication": publication})
        headline_data.to_csv("CSVs/" + k + ".csv")
        print("Finished with " + k + ".csv")
    search_again()


def search_again():
    """Asks the user if they would like to search for more headlines after executing a search."""
    while True:
        search = input("Would you like to search again? Y/N\n")

        if search.lower() == "y":
            get_keywords()
        elif search.lower() == "n":
            break
        else:
            print("Please enter either Y or N.")
            continue


if __name__ == "__main__":
    get_keywords()
