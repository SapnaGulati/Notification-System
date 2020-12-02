from plyer import notification
import requests
from bs4 import BeautifulSoup

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C://Users//ADMIN//PythonProjects//CoranaVirusNotification//icon.ico",
        timeout = 10
    )


def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    # notifyMe("Dream Girl", "Let's stop the spread of this virus together")
    myHtmlData = getData("https://www.mohfw.gov.in/")
    soup = BeautifulSoup(myHtmlData, 'html.parser').encode("utf-8")
    # print(soup.preetify())
    # myDataStr = ""
    for tr in soup.find_all('tbody')[1].find_all('tr'):
        myDataStr += tr.get_text()
    # myDataStr = myDataStr[1:]
    # itemList = myDataStr.split("\n\n")

    # for item in itemList[0:21]:
    #     print(item.split('\n'))
    # for table in soup.find_all('table'):
        # print(table.get_text())