

# add on comments
#login framework
# put try catch
#multiple classes
#ans sheet should be diffrent
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import xlu
from multiprocessing import Process
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

import os
load_dotenv()
#for holding website elements
ask_question = ""
start_writing = ""
title_txt = ""
question_txt = ""
ans_txt= ""
tags_txt = ""
post=""
#contetnt to be post on websites
title = ""
question = ""
answer=""
tag = ""
review = ""
#additional varible for diffrent websites process
value=""
general=""
lg_button=""
row_Q=2
#login element credentials
id=""
pw=""
lg=""
#user id and password holder
email =""
password=""

# Reading sheets from .env file
login_sheet = os.getenv("LOGIN_SHEET")
ans_sheet = os.getenv("ANS_SHEET")
target_sheet = os.getenv("TARGET_SHEET")
web_email = os.getenv("EMAIL_EXCEL")  #1
web_password = os.getenv("PASSWORD_EXCEL")  #2
web_url = os.getenv("URLS")  #3
web_IdField = os.getenv("ID_TEXTFIELD") #4
web_PwField = os.getenv("PW_TEXTFIELD")  #5
web_LoginButton = os.getenv("LOGIN_BUTTON") #6
web_AskQuestion = os.getenv("ASK_QUESTION")  #7
web_TitleText = os.getenv("TITLE_TEXT")  #8
web_QuestionText = os.getenv("QUESTION_TEXT")   #9
web_AnsText = os.getenv("ANS_TEXT")             #10
web_TagsText = os.getenv("TAGS_TEXT")           #11
web_Review = os.getenv("REVIEW")   #12
web_StartWriting = os.getenv("START_WRITING")#13
web_Keys= os.getenv("KEYS") #14
web_Post = os.getenv("POST") #15
web_GeneralQ = os.getenv("GENERAL_Q")#16
web_LoginButtonValue = os.getenv("LOGIN_BUTTON_VALUE")  #17
web_WithEmail = os.getenv("WITH_EMAIL")   #18
web_CreateQue = os.getenv("CREATE_QUE")   #19
web_Values = os.getenv("VALUES")          #20
web_ValueStack = os.getenv("VALUE_STACK")          #21
web_Cookie = os.getenv("COOKIE")          #22
#sheet2
web_Title = os.getenv("TITLE")   #1
web_Questions = os.getenv("QUESTION")   #2
web_Answer = os.getenv("ANSWER")   #3
web_Tags = os.getenv("TAGS")   #4
web_Menu = os.getenv("MENU")          #
web_Logout= os.getenv("LOGOUT")          #
web_Click_Logout= os.getenv("CLICK_LOGOUT")          #
web_Logout_All= os.getenv("LOGOUT_ALL")          #

#sheet3

search_web=os.getenv("SEARCH")
button_web=os.getenv("BUTTON")
qa_web=os.getenv("QA")
click_web=os.getenv("CLICK")
txt_click_web=os.getenv("TXT_CLICK")
ans_txt_web=os.getenv("ANS_TXT")
users_web=os.getenv("USERS")
searched_id_web=os.getenv("SEARCHED_ID")
click_id_web=os.getenv("CLICK_ID")
submit_web=os.getenv("SUBMIT")

class WebAutomation:
    def __init__(self, path):
        self.path = path
        # self.driver = webdriver.Chrome()
        self.driver = None
    def open_new_tab(self, url):
        self.driver.execute_script("window.open('', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get(url)
        time.sleep(3)

    def login(self, row):
        # Perform login operation
        try:
            # Read the website URL from the Excel sheet
            web = xlu.readData(self.path, login_sheet, row, web_url)

            # Open a new tab in the browser
            self.driver.execute_script("window.open('', '_blank');")
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # Navigate to the specified website
            self.driver.get(web)

            # Read the cookie element from the Excel sheet
            cookie = xlu.readData(self.path, login_sheet, row, web_Cookie)

            # Click on the specified cookie element
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
            self.driver.find_element(By.ID, id).send_keys(email)

            # Enter the user password into the password field
            self.driver.find_element(By.ID, pw).send_keys(password)

            # Pause for 2 seconds to allow data entry
            time.sleep(2)

            # Click on the login button
            self.driver.find_element(By.XPATH, lg).click()

            # Pause for 3 seconds to allow the login process to complete
            time.sleep(3)
        except Exception as e:
            print(f"Exception occurred: {e}")




    def type2_post(self, row):  # stack exchange
        try:
            # Read the 'value' from the spreadsheet
            value = xlu.readData(self.path, login_sheet, row, web_ValueStack)

            # If 'value' is 'ask', open a new tab and navigate to the specified website
            if (value == 'ask'):
                web = xlu.readData(self.path, login_sheet, row, web_url)
                self.driver.execute_script("window.open('', '_blank');")
                self.driver.switch_to.window(self.driver.window_handles[-1])
                self.driver.get(web)

            # Global variables for target website elements
            global question, tag, review, row_Q, post

            # Read target website elements from the spreadsheet
            users = xlu.readData(self.path, target_sheet, row, users_web)
            searched_id = xlu.readData(self.path, target_sheet, row, searched_id_web)
            search_box = xlu.readData(self.path, target_sheet, row, search_web)
            search_button = xlu.readData(self.path, target_sheet, row, button_web)
            click_id = xlu.readData(self.path, target_sheet, row, click_id_web)
            q_a = xlu.readData(self.path, target_sheet, row, qa_web)
            ans_txt = xlu.readData(self.path, target_sheet, row, ans_txt_web)
            answer = xlu.readData(self.path, ans_sheet, row, web_Answer)
            submit = xlu.readData(self.path, target_sheet, row, submit_web)

            menu = xlu.readData(self.path, login_sheet, row, web_Menu)
            logout = xlu.readData(self.path, login_sheet, row, web_Logout)
            click_logout = xlu.readData(self.path, login_sheet, row, web_Click_Logout)
            logout_all = xlu.readData(self.path, login_sheet, row, web_Logout_All)
            # Click on the 'users' element
            self.driver.find_element(By.XPATH, users).click()
            time.sleep(3)

            # Enter the 'searched_id' in the search box
            self.driver.find_element(By.XPATH, search_box).send_keys(searched_id)
            time.sleep(2)

            # Click the 'search_button' to initiate the search
            self.driver.find_element(By.XPATH, search_button).click()
            time.sleep(3)

            # Click on the link with the specified text ('click_id')
            self.driver.find_element(By.LINK_TEXT, click_id).click()
            time.sleep(3)

            # # Click on the 'q_a' element to navigate to the question-answer section
            # self.driver.find_element(By.ID, q_a).click()
            # time.sleep(3)

 # Click on the 'q_a' element to navigate to the question-answer section
            self.driver.find_element(By.LINK_TEXT, q_a).click()
            time.sleep(3)


            # Enter the 'answer' into the 'ans_txt' element
            self.driver.find_element(By.XPATH, ans_txt).send_keys(answer)
            time.sleep(5)

            # Click on the 'submit' button to submit the answer
            self.driver.find_element(By.ID, submit).click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, menu).click()
            time.sleep(3)
            self.driver.find_element(By.LINK_TEXT, click_logout).click()
            time.sleep(3)
            self.driver.find_element(By.ID, logout_all).click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, logout).click()
            time.sleep(5)


        except Exception as e:
            # Handle exceptions and print details
            print(f"Exception in type4_post on row {row}: {e}")


    def type4_post(self, row):
        try:
            # Read the web URL from the Excel sheet
            web = xlu.readData(self.path, login_sheet, row, web_url)

            # Initialize a new Chrome WebDriver
            self.driver = webdriver.Chrome()
            self.driver.get(web)
            self.driver.maximize_window()
            time.sleep(3)

            # Global variables initialization
            global id, pw, lg, row_Q
            question = xlu.readData(self.path, ans_sheet, row_Q, web_Questions)

            # Read email, login button, fields, and other elements from the Excel sheet
            email = xlu.readData(self.path, "Sheet3", row, web_email)
            lg_button = xlu.readData(self.path, login_sheet, row, web_LoginButtonValue)
            with_email = xlu.readData(self.path, login_sheet, row, web_WithEmail)
            search_box = xlu.readData(self.path, target_sheet, row, search_web)
            q_a = xlu.readData(self.path, target_sheet, row, qa_web)
            click = xlu.readData(self.path, target_sheet, row, click_web)
            txt_click = xlu.readData(self.path, target_sheet, row, txt_click_web)
            ans_txt = xlu.readData(self.path, target_sheet, row, ans_txt_web)
            answer = xlu.readData(self.path, ans_sheet, row, web_Answer)
            search_button = xlu.readData(self.path, target_sheet, row, button_web)
            password = xlu.readData(self.path, "Sheet3", row, web_password)
            id = xlu.readData(self.path, login_sheet, row, web_IdField)
            pw = xlu.readData(self.path, login_sheet, row, web_PwField)
            lg = xlu.readData(self.path, login_sheet, row, web_LoginButton)

            # Perform login operation
            self.driver.find_element(By.XPATH, lg_button).click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, with_email).click()
            time.sleep(3)
            self.driver.find_element(By.ID, id).send_keys(email)
            self.driver.find_element(By.ID, pw).send_keys(password)
            time.sleep(2)
            self.driver.find_element(By.XPATH, lg).click()
            time.sleep(3)

            # Search for the question
            self.driver.find_element(By.XPATH, search_box).send_keys(question)
            time.sleep(2)

            # Click on the search button
            self.driver.find_element(By.XPATH, search_button).click()
            time.sleep(3)

            # Navigate to the question-answer section
            self.driver.find_element(By.XPATH, q_a).click()
            time.sleep(5)

            # Click on a specific question
            self.driver.find_element(By.XPATH, click).click()
            time.sleep(5)

            # Click on a text element
            self.driver.find_element(By.XPATH, txt_click).click()
            time.sleep(5)

            # Enter the answer in the answer text box
            self.driver.find_element(By.XPATH, ans_txt).send_keys(answer)
            time.sleep(5)

        except Exception as e:
            print(f"Exception in type4_post on row {row}: {e}")

    def type5_post(self, row):
        try:
            # Read the web URL from the Excel sheet
            web = xlu.readData(self.path, login_sheet, row, web_url)

            # Refresh the browser, open a new window, and navigate to the web URL
            self.driver.refresh()
            self.driver.execute_script("window.open('', '_blank');")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.get(web)
            time.sleep(10)

            # Global variables initialization
            global id, pw, lg, ask_question, general, title_txt, question_txt, title, question, lg_button, row_Q, ans_txt, answer

            # Read elements from the Excel sheet
            search_box = xlu.readData(self.path, target_sheet, row, search_web)
            question = xlu.readData(self.path, ans_sheet, row_Q, web_Questions)
            q_a = xlu.readData(self.path, target_sheet, row, qa_web)
            search_button = xlu.readData(self.path, target_sheet, row, button_web)
            ans_txt = xlu.readData(self.path, target_sheet, row, ans_txt_web)
            answer = xlu.readData(self.path, ans_sheet, row, web_Answer)
            email = xlu.readData(self.path, target_sheet, row, web_email)
            password = xlu.readData(self.path, target_sheet, row, web_password)
            id = xlu.readData(self.path, target_sheet, row, web_IdField)
            pw = xlu.readData(self.path, target_sheet, row, web_PwField)

            # Enter search text in the search box
            self.driver.find_element(By.ID, search_box).send_keys("Missing a using directive or an assembly reference")
            time.sleep(3)

            # Navigate to the question-answer section
            self.driver.find_element(By.ID, q_a).click()
            time.sleep(3)

            # Click on the search button
            self.driver.find_element(By.XPATH, search_button).click()
            time.sleep(3)

            # Click on a specific question related to the search text
            self.driver.find_element(By.LINK_TEXT, "Missing a using directive or an assembly reference").click()
            time.sleep(3)

            # Enter the answer in the answer text box
            self.driver.find_element(By.XPATH, ans_txt).send_keys(answer)
            time.sleep(5)

            # Additional steps for login
            self.driver.find_element(By.XPATH, ans_txt).send_keys(answer)
            time.sleep(3)
            self.driver.find_element(By.ID, id).send_keys(email)
            time.sleep(3)
            self.driver.find_element(By.ID, pw).send_keys(password)
            time.sleep(3)


        except Exception as e:
            print(f"Exception in type4_post on row {row}: {e}")

    def close_driver(self):
        if self.driver:
            self.driver.quit()

# code with try-catch
def process_websites(start_row, end_row, path, failed_websites):
    web_automation = WebAutomation(path)
    for row in range(start_row, end_row + 1):
        print(row)
        key = xlu.readData(path, login_sheet, row, web_Keys)
        try:
            if (key == "ans_com"):
                web_automation.type4_post(row)
            elif (key == 'procode'):
                web_automation.type5_post(row)
            else:
                web_automation.login(row)
                # webites with similar login process
                if (key == 'stack'):
                    web_automation.type2_post(row)  # stack exchange

        except WebDriverException as e:
            print(f"Exception on row {row} with key value {key}: {e}")
            failed_websites.append(row)
            print("appended")

    web_automation.close_driver()

def main():
    path = "C:/Users/HP/Desktop/Final.xlsx"

    # Get the total number of rows in the Excel sheet
    rows = xlu.getRowCount(path, login_sheet)

    # Create an instance of the WebAutomation class
    web_automation = WebAutomation(path)

    # List to store row numbers of failed websites
    failed_website = []

    # Iterate through rows in the Excel sheet
    for row in range(2, rows + 1):
        print(row)

        # Read key and value from the Excel sheet
        key = xlu.readData(path, login_sheet, row, web_Keys)
        value = xlu.readData(path, login_sheet, row, web_ValueStack)

        try:
            # Check the key and perform corresponding actions
            if key == "ans_com":
                web_automation.type4_post(row)
            elif key == 'procode':
                web_automation.type5_post(row)
            else:
                # Login to the website and perform type2_post (stack exchange)
                web_automation.login(row)
                web_automation.type2_post(row)

        except WebDriverException as e:
            # Handle exceptions and append row number to the list
            print(f"Exception on row {row} with key value {key}: {e}")
            failed_website.append(row)

    # Close the WebDriver instance
    web_automation.close_driver()

    # Display information about passed and failed websites
    print("This website has passed exception")
    print(failed_website)


if __name__ == "__main__":
    main()







