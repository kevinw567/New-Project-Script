import sys
import os
import creds
from selenium import webdriver

# path to destination folder
path = "C:/Users/kevin/Documents/projects/"
# load selenium browser driver
browser = webdriver.Chrome()

"""
Create a new folder and a matching github repository. 

Creates a new folder on the local system, with the user given name, and uses 
selenium to create a new github repository with the same name
"""
def create():
    # get the name of the folder to create
    folderName = sys.argv[1]
    # create the new directory in the destination folder
    os.makedirs(path + folderName)
    # go to github.com in browser
    browser.get("http://github.com/login")
    # fill in log in credentials and sign in
    login_field = browser.find_element_by_name('login')
    login_field.send_keys(creds.USERNAME)
    password_field = browser.find_element_by_name('password')
    password_field.send_keys(creds.PASSWORD)
    signIn_button = browser.find_element_by_name('commit')
    signIn_button.click()
    # got to create a new repo page
    browser.get("https://github.com/new")
    # fill in new repo name and submit
    repoNameField = browser.find_element_by_name('repository[name]')
    repoNameField.send_keys(folderName)
    createButton = browser.find_element_by_css_selector('button.first-in-line')
    createButton.submit()

if __name__ == "__main__":
    create()