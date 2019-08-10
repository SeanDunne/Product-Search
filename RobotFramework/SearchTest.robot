*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${SITE URL}    https://www.amazon.com
${BROWSER}     Chrome

*** Test Cases ***
Product Search
    Open Browser To Desired Page
    Input Search String    Nikon
    Submit Search
    Search Results Should Be Shown
    Sort Search Results From High To Low
    Select Second Result Item
    Description Should Contain    Nikon D3X
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Desired Page
    Open Browser    ${SITE URL}    ${BROWSER}
    Title Should Be    Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more

Input Search String
    [Arguments]    ${SEARCH STR}
    Input Text    id:twotabsearchtextbox    ${SEARCH STR}

Submit Search
    Press Keys    id:twotabsearchtextbox    RETURN

Search Results Should Be Shown
    Title Should Be    Amazon.com: Nikon

Sort Search Results From High To Low
    Click Element    id:a-autoid-0-announce
    Click Element    id:s-result-sort-select_2

Select Second Result Item
    Click Element    xpath://*[@data-image-index='2']

Description Should Contain
    [Arguments]    ${PRODUCT SPEC}
    Element Should Contain    id:productDescription    ${PRODUCT SPEC}