import requests

def getdata():
    """

    :return:
    """
    url = 'https://www.amfiindia.com/spages/NAVAll.txt'

    response = requests.get(url=url)

    navs = response.text

    return navs

def getnav(fund_name):
    """

    :return:
    """
    navs = getdata()
    list_navs = navs.split('\n')

    list_funds = []
    for nav in list_navs:
        if fund_name in nav:
            # If multiple funds with the same string [Div/Growth variants]
            list_funds.append(nav)

    for fund in list_funds:
        print("Fund Name: {0}; Nav: {1}".format(fund.split(';')[3], fund.split(';')[4]))


fund = 'Parag Parikh Liquid Fund'
print(getnav(fund))