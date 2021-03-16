from csv import reader  # we use this package to read the ListOfZipCodes CSV file
# We use webdriver in order to open up a browser and navigate to different zillow urls and get the HTML code of those urls
from selenium import webdriver
# We use this package to parse the HTML code we get from the zillow URLs in order to get the property values
from bs4 import BeautifulSoup
# We use this to reduce frequency of our requests and to make sure the page is fully loaded before we get the HTML code.
import time

# A chrome driver allows you to automate web interactions through a chrome browser.
# Basically, it interacts with a website for you, doing only what you tell it to do.

# Professor, please check your google chrome version. I am using version 89.0432 which matches my chromedriver.exe
# If you are using a different version of chrome, please download the appropriate version here and replace with the currrent chromedriver.exe
# here is the url: http://chromedriver.chromium.org/downloads?tmpl=%2Fsystem%2Fapp%2Ftemplates%2Fprint%2F&showPrintDialog=1


def main():
    # Here, we are creating a main function so that we can call it later in any other file.
    driverpath = 'chromedriver.exe'
    # The driverpath variable is stting the file path of chromedriver to equal the variable "driverpath"
    driver = webdriver.Chrome(executable_path=driverpath)
    # This sets the variable driver equal to the webdriver object and uses the driver path to find the chromedriver program
    zipcodes = []
    # This is an empty list that we will add on to (append) zip codes later.
    with open("ListOfZipCodes.csv") as csvfile:
        # We are opening a CSV file that contains all of the zip codes in Boston and defining that file as 'csvfile'
        csvreader = reader(csvfile)
        # this will allow us to read through that said csv file
        for row in csvreader:
            # This for loop iterates through each row of the csv file and reads each row
            zipcodes.append(row[1])
            # In each row, we are taking the second element (zipcode) and adding this to our zipcodes list that we created in line 14
    property_value_dict = {}
    # Here, we are creating an empty dictionary so that we populate it later
    for zip in zipcodes:
        # This for loops iterates through each zip code in our zip code list
        z = str(zip).zfill(5)
        # Here, because all of our zipcodes are missing a 0 in front, we use 'zfill' to make sure the length of all zip codes is 5 digits and that if there are 4 digits it will add 0 in front
        url = f'http://zillow.com/homes/{z}_rb/'
        # in line 30, we are creating the zillow url based on the unique zip code in our current interaiton
        driver.get(url)
        # here, we are opening up a chrome driver browser and navigating to the predetermined URL in line 30
        time.sleep(4)
        # Here, we get the code to sleep to allow the page to load data as well as reduce the frequency of our requests
        soup = BeautifulSoup(driver.page_source, "html.parser")
        # This soup variable takes the full html code in our browser and parsing it using HTML format. See next line for further explanation
        property_value = soup.find_all("div", class_="list-card-price")
        # Using line 36, we are basically searching through the HTML to find all 'divs' with a specific class name.
        # After researching the HTML structure on Zillow, we found that the div with a class equal to 'list-card-price' contains the property values assocaited with each property within each zip code
        value_list = []
        # Now we are creating an empty list to store all property values in a specific zip code within Boston
        for value in property_value:
            # This for loop will iterate through each div in the HTML page source with a class = to 'list-card-price'
            propval = str(value).split(">")[1]
            # Here, we are getting rid of the starting div label in the found div
            propval = propval.split("<")[0]
            # and here we are getting rid of the ending div label in the found div in order to isolate just the property value
            propval = propval.replace("$", "")
            # In this line, becuase we are getting only text from the HTML page source, our code does not recognize that it is a number. So we will take away the dollar sign in order to get rid of non-numeric characters in the string
            propval = propval.replace(",", "")
            # In this line, becuase we are getting only text from the HTML page source, our code does not recognize that it is a number. So we will take away the commas in order to get rid of non-numeric characters in the string
            propval = propval.replace("+", "")
            # In this line, becuase we are getting only text from the HTML page source, our code does not recognize that it is a number. So we will take away the plus signs in order to get rid of non-numeric characters in the string
            propval = int(propval)
            # Here, we are converting the string to an integer/number
            value_list.append(propval)
            # In this line we are taking the property value and appending it to our value list in line 41
        property_value_dict[z] = value_list
        # Here, we are adding a new column to our dictionary with a key equal to the zip code and a value = to a list of all property values in the given zip code
    print(f'zip code\t average property value')
    mean_list = []
    # We want to display the information we are getting. So, here we are creating a list to calculate the final average property value for all of bsoton
    for key, val in property_value_dict.items():
        # Here we are iterating through each key,val pair in 'property value dict' (line 64)
        value_mean = sum(val) / len(val)
        # Here we are calculating the mean price of a given zip code (key)
        mean_list.append(value_mean)
        # Here we are appending the average property value in a zip code to the mean_list
        print(f'{key}\t\t${value_mean:>15,.2f}')
        # Here we are printing a line in a table where zipcode(key) is in our first column and the average property price is in our second column
    final_mean = sum(mean_list) / len(mean_list)
    # Here, we are calculating the total mean of all properties in Boston by finding the average of the mean list
    print(f'Boston\t\t${final_mean:>15,.2f}')
    # Here we are printing the final boston average property value

    driver.quit


if __name__ == "__main__":
    main()
