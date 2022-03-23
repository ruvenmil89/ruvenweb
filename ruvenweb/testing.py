import requests

"""
This function calculate the universal number base on country and phone number
:param country of sim
:parm phoneNumber
:retrun the universalnumber
"""
def getPhoneNumbers(country, phoneNumber):

    # Get the data from the url with the country variable
    getdata = requests.get('https://jsonmock.hackerrank.com/api/countries?name={}'.format(country))
    # Check if the page exists
    if getdata.status_code == 200:
        data = getdata.json()
        # In case the array is empty retrun -1
        if len(data.get('data')) == 0:
            return -1
        # Fetch the callingCodes array
        data = data.get('data')[0].get('callingCodes')
        maxvalue = data[0]
        # Searching the max value from CallingCodes array
        for i in data:
            if int(i) > int(maxvalue):
                maxvalue = i

        returnValue = "+" + i + " " + str(phoneNumber)
        return returnValue
    return -1


print(getPhoneNumbers("Puerto Rico", 564593986))