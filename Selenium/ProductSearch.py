from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print ("This code searches Amazon.com")

browser = webdriver.Chrome()

# ~PARAMETERS~ #
site_url = 'https://www.amazon.com'
item_search = 'Nikon'
sort_choice = 2 # positional index of product sort type
item_choice = 1
spec_match = 'Nikon D3X'

# ~FUNCTIONS~ #
def TextSearcher(searchStr):
    searchBar = browser.find_element_by_id('twotabsearchtextbox') # select search bar
    searchBar.send_keys(searchStr) # enter search string
    searchBar.send_keys(Keys.ENTER)

def ItemSorter(sortNum):
    sortDropdown = browser.find_element_by_id('a-autoid-0-announce') # select drop down menu
    sortDropdown.click()
    sortType = browser.find_element_by_id('s-result-sort-select_%s' % sortNum) # select sort type
    sortType.click()

def ItemPicker(indexNum):
    xpathData = "//*[@data-image-index='%s']" % indexNum # create xpath to 'nth' item
    product = browser.find_element_by_xpath(xpathData) # select item
    product.click()

def StringMatcher(specStr):
    productDescr = browser.find_element_by_id('productDescription') # find & read product description
    assert specStr in productDescr.text, '"%s" not found in product description' % specStr

def main():
    browser.get(site_url)
    TextSearcher(item_search)
    ItemSorter(sort_choice)
    ItemPicker(item_choice)
    StringMatcher(spec_match)
    browser.close()

if __name__ == "__main__":
    main()




