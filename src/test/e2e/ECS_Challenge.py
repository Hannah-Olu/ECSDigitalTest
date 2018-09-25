import selenium
from selenium import webdriver


driver = webdriver
browser = driver.Firefox()
url = ("http://localhost:3000")

browser.get(url)

button = browser.find_element_by_tag_name('button')
button.click()


def extractRowsFromPage(browser, tag):
    rows = browser.find_elements_by_tag_name(tag)

    tablearrays = []

    for row in rows:
        columns = row.text.split(" ")
        tablearrays.append(columns)

    return tablearrays


def checkIndex(listOfRows):
    result = []
    found = False

    for row in listOfRows:
        for index, column in enumerate(row):
            lsum = sum(row[:index])
            rsum = sum(row[index+1:])
            if lsum == rsum:
                found = True
                result.append(index)
                continue

        if found == False:
            result.append(None)

    return result


def sum(listOfValues):
    sum = 0
    for item in listOfValues:
        sum += int(item)

    return sum


def submitResult(browser, result, name):
    inputs = browser.find_elements_by_tag_name('input')
    inputs[0].send_keys(" ".join(map(str, result)))
    inputs[3].send_keys(name)
    browser.find_element_by_id("submitbtn").click()


def run():
    rows = extractRowsFromPage(browser, 'tr')
    resultList = checkIndex(rows)
    print(resultList)
    submitResult(browser, resultList, "Hannah")

run()


browser.quit()

