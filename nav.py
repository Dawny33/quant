import requests

def getnav():
    """

    TODO: Take the name of fund and the option (dividend/growth) and give out nav
    :return:
    """
    url = 'https://www.amfiindia.com/spages/NAVAll.txt'

    response = requests.get(url=url)

    navs = response.text