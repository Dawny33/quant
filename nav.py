import requests

def getdata():
    """

    :return:
    """
    url = 'https://www.amfiindia.com/spages/NAVAll.txt'

    response = requests.get(url=url)

    navs = response.text

    return navs

def getnav():
    """

    :return:
    """
    navs = getdata()
    list_navs = navs.split('\n')
    #print(len(list_navs))

getnav()