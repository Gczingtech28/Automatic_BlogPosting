from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import xlu
import os
from dotenv import load_dotenv
from selenium.common.exceptions import WebDriverException
load_dotenv()


# List to store row numbers with exceptions
failed_website = []

import os

# Declare variables for website elements
ask_question = ""
start_writing = ""
title_txt = ""
question_txt = ""
ans_txt= ""
tags_txt = ""
# Declare variables for content to be posted on websites
title = ""
question = ""
answer =""
tag = ""
review = ""
# Additional variables for different website processes
value =""
general =""
lg_button =""
row_Q =2
# Login element credentials
id =""
pw =""
lg =""
# User ID and password holder
email =""
password = ""

# Reading sheets from .env file
login_sheet = os.getenv("LOGIN_SHEET")
ans_sheet = os.getenv("ANS_SHEET")
web_email = os.getenv("EMAIL_EXCEL")  # 1
web_password = os.getenv("PASSWORD_EXCEL")  # 2
web_url = os.getenv("URLS")  # 3
web_IdField = os.getenv("ID_TEXTFIELD")  # 4
web_PwField = os.getenv("PW_TEXTFIELD")  # 5
web_LoginButton = os.getenv("LOGIN_BUTTON")  # 6
web_AskQuestion = os.getenv("ASK_QUESTION")  # 7
web_TitleText = os.getenv("TITLE_TEXT")  # 8
web_QuestionText = os.getenv("QUESTION_TEXT")  # 9
web_AnsText = os.getenv("ANS_TEXT")  # 10
web_TagsText = os.getenv("TAGS_TEXT")  # 11
web_Review = os.getenv("REVIEW")  # 12
web_StartWriting = os.getenv("START_WRITING")  # 13
web_Keys = os.getenv("KEYS")  # 14
web_Post = os.getenv("POST")  # 15
web_GeneralQ = os.getenv("GENERAL_Q")  # 16
web_LoginButtonValue = os.getenv("LOGIN_BUTTON_VALUE")  # 17
web_WithEmail = os.getenv("WITH_EMAIL")  # 18
web_CreateQue = os.getenv("CREATE_QUE")  # 19
web_Values = os.getenv("VALUES")  # 20
web_ValueStack = os.getenv("VALUE_STACK")  # 21
web_Cookie = os.getenv("COOKIE")          #22
web_Menu = os.getenv("MENU")          #
web_Logout= os.getenv("LOGOUT")          #
web_Click_Logout= os.getenv("CLICK_LOGOUT")          #
web_Logout_All= os.getenv("LOGOUT_ALL")          #

# sheet2
web_Title = os.getenv("TITLE")  # 1
web_Questions = os.getenv("QUESTION")  # 2
web_Answer = os.getenv("ANSWER")  # 3
web_Tags = os.getenv("TAGS")  # 4

#sheet4
web_user_data_dir = os.getenv("USER_DATA_DIR")
web_chrome_path= os.getenv("CHROME_PATH")
web_cross_button= os.getenv("CROSS_BUTTON")
web_click_textfield= os.getenv("CLICK_TEXTFIELD")
web_search_button= os.getenv("SEARCH_BUTTON")

class WebAutomation:
    def __init__(self, path):
        self.path = path
        # self.driver = driver

    def open_new_tab(self, url):
        # Open a new tab in the browser
        self.driver.execute_script("window.open('', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get(url)
        time.sleep(3)

    def login(self, row, driver):
        # Perform login operation
        try:
            # # Read the website URL from the Excel sheet
            # web = xlu.readData(self.path, login_sheet, row, web_url)
            #
            # # Open a new tab in the browser
            # driver.execute_script("window.open('', '_blank');")
            # driver.switch_to.window(driver.window_handles[-1])
            #
            # # Navigate to the specified website
            # driver.get(web)

            chwd = driver.window_handles
            print(chwd)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(5)

            # Access another website
            web = xlu.readData(self.path, login_sheet, row, web_url)
            driver.get(web)
            time.sleep(5)

            # Read the cookie element from the Excel sheet
            cookie = xlu.readData(self.path, login_sheet, row, web_Cookie)

            # Click on the specified cookie element
            # self.driver.find_element(By.LINK_TEXT, "Log in").click()
            # time.sleep(5)
            # self.driver.find_element(By.XPATH, cookie).click()

            # Pause for 2 seconds to allow the page to load
            time.sleep(2)

            # Initialize global variables for user credentials
            global id, pw, lg, email, password

            # Read user email from the Excel sheet
            email = xlu.readData(self.path, login_sheet, row, web_email)

            # Read user password from the Excel sheet
            password = xlu.readData(self.path, login_sheet, row, web_password)

            # Read the ID field element from the Excel sheet
            id = xlu.readData(self.path, login_sheet, row, web_IdField)

            # Read the password field element from the Excel sheet
            pw = xlu.readData(self.path, login_sheet, row, web_PwField)

            # Read the login button element from the Excel sheet
            lg = xlu.readData(self.path, login_sheet, row, web_LoginButton)

            # Enter the user email into the ID field
            driver.find_element(By.ID, id).send_keys(email)

            # Enter the user password into the password field
            driver.find_element(By.ID, pw).send_keys(password)

            # Pause for 2 seconds to allow data entry
            time.sleep(2)

            # Click on the login button
            driver.find_element(By.XPATH, lg).click()

            # Pause for 3 seconds to allow the login process to complete
            time.sleep(3)

        except Exception as e:
            print(f"Exception occurred: {e}")
            failed_website.append(row)



    def type2_post(self, row,driver):
        # Perform type2 post operation
        try:
            # Read the value from the Excel sheet
            value = xlu.readData(self.path, login_sheet, row, web_ValueStack)

            # Check if the value is 'ask'
            if value == 'ask':
                # Read the website URL from the Excel sheet
                web = xlu.readData(self.path, login_sheet, row, web_url)

                # Open a new tab in the browser
                driver.execute_script("window.open('', '_blank');")
                driver.switch_to.window(self.driver.window_handles[-1])

                # Navigate to the specified website
                driver.get(web)

            # Initialize global variables
            global ask_question, start_writing, title_txt, question_txt, tags_txt, title, question, tag, review, row_Q

            # Read elements from the Excel sheet
            ask_question = xlu.readData(self.path, login_sheet, row, web_AskQuestion)
            start_writing = xlu.readData(self.path, login_sheet, row, web_StartWriting)
            title_txt = xlu.readData(self.path, login_sheet, row, web_TitleText)
            question_txt = xlu.readData(self.path, login_sheet, row, web_QuestionText)
            tags_txt = xlu.readData(self.path, login_sheet, row, web_TagsText)
            title = xlu.readData(self.path, ans_sheet, row_Q, web_Title)
            question = xlu.readData(self.path, ans_sheet, row_Q, web_Questions)
            tag = xlu.readData(self.path, ans_sheet, row_Q, web_Tags)
            review = xlu.readData(self.path, login_sheet, row, web_Review)
            value = xlu.readData(self.path, login_sheet, row, web_Values)
            menu = xlu.readData(self.path, login_sheet, row, web_Menu)
            logout = xlu.readData(self.path, login_sheet, row, web_Logout)
            click_logout = xlu.readData(self.path, login_sheet, row, web_Click_Logout)
            logout_all = xlu.readData(self.path, login_sheet, row, web_Logout_All)
            post = xlu.readData(self.path, login_sheet, row, web_Post)

            # Click on the 'Ask a Question' element
            driver.find_element(By.XPATH, ask_question).click()
            time.sleep(10)

            # Check if the value is not 'fault'
            if value != "fault":
                # Click on the 'Start Writing' element
                driver.find_element(By.XPATH, start_writing).click()
                time.sleep(5)

            # Enter title, question, and tags
            driver.find_element(By.XPATH, title_txt).send_keys(title)
            time.sleep(3)
            driver.find_element(By.XPATH, question_txt).send_keys(question)
            time.sleep(3)
            driver.find_element(By.XPATH, tags_txt).send_keys(tag)
            time.sleep(5)

            # Click on the 'Review' element
            driver.find_element(By.XPATH, review).click()
            time.sleep(10)
            driver.find_element(By.ID, post).click()
            time.sleep(3)
            driver.find_element(By.XPATH,menu).click()
            time.sleep(3)
            driver.find_element(By.LINK_TEXT,click_logout ).click()
            time.sleep(3)
            driver.find_element(By.ID, logout_all).click()
            time.sleep(3)
            driver.find_element(By.XPATH,logout).click()
            time.sleep(5)


        except Exception as e:
            print(f"Exception occurred: {e}")
            failed_website.append(row)

    def type4_post(self, row,driver):
        # Perform type4 post operation
        try:
            chwd = driver.window_handles
            print(chwd)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(7)

            # Access another website
            web = xlu.readData(self.path, login_sheet, row, web_url)
            driver.get(web)
            time.sleep(5)


            # Define global variables           global id, pw, lg, row_Q

            # Read login credentials from the spreadsheet
            email = xlu.readData(self.path, login_sheet, row, web_email)
            lg_button = xlu.readData(self.path, login_sheet, row, web_LoginButtonValue)
            with_email = xlu.readData(self.path, login_sheet, row, web_WithEmail)
            password = xlu.readData(self.path, login_sheet, row, web_password)
            id = xlu.readData(self.path, login_sheet, row, web_IdField)
            pw = xlu.readData(self.path, login_sheet, row, web_PwField)
            lg = xlu.readData(self.path, login_sheet, row, web_LoginButton)
            post = xlu.readData(self.path, login_sheet, row, web_Post)

            print("web")

            # Click on the login button
            driver.find_element(By.XPATH, lg_button).click()
            time.sleep(3)

            print("log")

            # Click on the 'Login with Email' button
            driver.find_element(By.XPATH, with_email).click()
            time.sleep(3)

            # Enter email and password
            driver.find_element(By.ID, id).send_keys(email)
            driver.find_element(By.ID, pw).send_keys(password)
            time.sleep(2)

            # Click on the 'Login' button
            driver.find_element(By.XPATH, lg).click()
            time.sleep(3)

            # Read the 'Create Question' element from the spreadsheet
            create_Q = xlu.readData(self.path, login_sheet, row, web_CreateQue)

            # Read the 'Ask Question' element from the spreadsheet
            ask_question = xlu.readData(self.path, login_sheet, row, web_AskQuestion)

            # Read the 'Title Text' element from the spreadsheet
            title_txt = xlu.readData(self.path, login_sheet, row, web_TitleText)
            time.sleep(3)

            # Read the title from the spreadsheet
            title = xlu.readData(self.path, ans_sheet, row_Q, web_Title)
            print("prachi")

            # Wait for 10 seconds
            time.sleep(10)

            # Click on the 'Create Question' element
            driver.find_element(By.XPATH, create_Q).click()
            time.sleep(3)

            # Click on the 'Ask Question' element
            driver.find_element(By.XPATH, ask_question).click()
            time.sleep(15)

            # Enter title
            driver.find_element(By.XPATH, title_txt).send_keys(title)
            time.sleep(3)

            driver.find_element(By.XPATH, post).click()
            time.sleep(3)

            driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div/div[4]/div[3]/span/div/button/span/img").click()
            time.sleep(3)
            driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div/div[4]/div[3]/span/div/div/div/button[3]/a/span").click()
            time.sleep(3)

        except Exception as e:
            print(f"Exception occurred: {e}")
            failed_website.append(row)

    def type5_post(self, row,driver):
        # Perform type5 post operation
        try:
            chwd = driver.window_handles
            print(chwd)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(5)

            # Access another website
            web = xlu.readData(self.path, login_sheet, row, web_url)
            driver.get(web)
            time.sleep(5)
            # time.sleep(60)

            # Define global variables
            global id, pw, lg, ask_question, general, title_txt, question_txt, title, question, lg_button, row_Q, ans_txt, answer

            # Read login button value from the spreadsheet
            post = xlu.readData(self.path, login_sheet, row, web_Post)
            lg_button = xlu.readData(self.path, login_sheet, row, web_LoginButtonValue)

            # Read login credentials from the spreadsheet
            email = xlu.readData(self.path, login_sheet, row, web_email)
            password = xlu.readData(self.path, login_sheet, row, web_password)
            id = xlu.readData(self.path, login_sheet, row, web_IdField)
            pw = xlu.readData(self.path, login_sheet, row, web_PwField)
            lg = xlu.readData(self.path, login_sheet, row, web_LoginButton)

            # Click on the login button
            driver.find_element(By.LINK_TEXT, lg_button).click()
            time.sleep(3)

            # Enter email and password
            driver.find_element(By.ID, id).send_keys(email)
            driver.find_element(By.ID, pw).send_keys(password)
            time.sleep(2)

            # Click on the 'Login' button
            driver.find_element(By.CLASS_NAME, lg).click()
            time.sleep(3)

            # Read elements from the spreadsheet
            ask_question = xlu.readData(self.path, login_sheet, row, web_AskQuestion)
            title_txt = xlu.readData(self.path, login_sheet, row, web_TitleText)
            question_txt = xlu.readData(self.path, login_sheet, row, web_QuestionText)
            tags_txt = xlu.readData(self.path, login_sheet, row, web_TagsText)
            ans_txt = xlu.readData(self.path, login_sheet, row, web_AnsText)
            title = xlu.readData(self.path, ans_sheet, row_Q, web_Title)
            question = xlu.readData(self.path, ans_sheet, row_Q, web_Questions)
            answer = xlu.readData(self.path, ans_sheet, row_Q, web_Answer)
            tag = xlu.readData(self.path, ans_sheet, row_Q, web_Tags)
            time.sleep(15)

            # Click on the 'Ask Question' element
            driver.find_element(By.XPATH, ask_question).click()
            time.sleep(3)


            # Enter title
            driver.find_element(By.XPATH, title_txt).send_keys(title)
            time.sleep(3)

            # Enter question
            driver.find_element(By.XPATH, question_txt).send_keys(question)
            time.sleep(3)

            # Enter answer
            driver.find_element(By.XPATH, ans_txt).send_keys(answer)
            time.sleep(3)

            # Enter tags
            driver.find_element(By.XPATH, tags_txt).send_keys(tag)
            time.sleep(8)

            driver.find_element(By.XPATH, post).click()
            time.sleep(3)

            driver.find_element(By.ID, "ctl00_ctl00_MemberBar_MyProfile").click()
            time.sleep(5)



            driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[3]/span[4]/div/form/input[2]").click()
            time.sleep(3)

        except Exception as e:
            print(f"Exception occurred: {e}")
            failed_website.append(row)

    def close_driver(self):
        # Close the driver
        if self.driver:
            self.driver.quit()
def main():
    path = "C:\\Users\\hp\\Downloads\\WebAutomation\\WebAutomation\\Final.xlsx"

    # Get the total number of rows in the Excel sheet
    rows = xlu.getRowCount(path, login_sheet)

    user_data_dir = "C:/Users/HP/AppData/Local/Google/Chrome/User Data"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

    # Set up Chrome options and extension
    options = Options()
    options.add_argument(f"user-data-dir={user_data_dir}")
    options.add_extension('C:/Users/HP/AppData/Local/Google/Chrome/User Data/Default/Extensions/eppiocemhmnlbhjplcgkofciiegomcon/4.6.1_0.crx')

    options.binary_location = chrome_path
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)


    for row in range(2, rows + 1):
        print(row)

        # Access the extension URL
        driver.get("chrome-extension://eppiocemhmnlbhjplcgkofciiegomcon/popup/index.html#/main")
        time.sleep(5)
        # web_Vpn = os.getenv("VPN")
        # vpn_sheet = os.getenv("VPN_SHEET")
        country = xlu.readDATA(path, 'Sheet3',row, 11)
        # Create an instance of the WebAutomation class
        web_automation = WebAutomation(path)

        # Click on buttons and interact with elements
        #CLICK ON CROSS
        driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div[2]/div[4]/div/div").click()
        time.sleep(3)
        #CLICK ON TEXTFIELD
        driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div").click()
        time.sleep(3)
        print(country)
        if country is not None:
            driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div[2]/div[2]/div/div[1]/input").send_keys(country)
        else:
            print("Country is None. Skipping send_keys operation.")
        # driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div[2]/div[2]/div/div[1]/input").send_keys(country)
        time.sleep(4)

        driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div[2]/div[2]/div/div[2]/div/ul/li/p").click()
        time.sleep(4)
        # Read 'key' and 'value' from the spreadsheet
        key = xlu.readData(path, login_sheet, row, web_Keys)
        value = xlu.readData(path, login_sheet, row, web_ValueStack)

        try:
            # Check the value of 'key' and perform corresponding actions
            if key == "ans_com":
                web_automation.type4_post(row, driver)
            elif key == 'procode':
                web_automation.type5_post(row, driver )
            else:
                web_automation.login(row,driver)
                web_automation.type2_post(row, driver)  # stack exchange
        except WebDriverException as e:
            # Handle exceptions and print details
            print(f"Exception on row {row} with key value {key}: {e}")
        #        failed_website.append(row)


       # driver.quit()

if __name__ == "__main__":
    main()
