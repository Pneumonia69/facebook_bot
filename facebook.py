from selenium import webdriver 
import time
import getpass

final_comments = []
with open('comment.txt') as comment:
    comments = comment.readline()
    striped_comment = comments.replace(' ',"")
    for comment in striped_comment:
        final_comments.append(comment)
        
def auto_comment(striped_comment):
    your_email = input("iplaypokemongo6969696969@gmail.com")
    your_password = getpass.getpass("Aryan20069420")
    browser = webdriver.Chrome()
    browser.get("https://mbasic.facebook.com")
    

    email = browser.find_element_by_css_selector("input[name='email']")
    email.send_keys(str(your_email))
    time.sleep(1)

    password = browser.find_element_by_css_selector("input[name='pass']")
    password.send_keys(str(your_password))
    button = browser.find_element_by_css_selector("input[type='submit']")
    button.click()
    time.sleep(2)

    browser.get("https://www.facebook.com/kowshik.banarjee/posts/pfbid0UMWJZkm4jz9T1BxbsUKHUDpoHVNP6w3kv9pJVva79Eaok1eyneJDS5qkDsjKQCN9l?notif_id=1662561783714533&notif_t=comment_mention&ref=notif")

    for sc in striped_comment:
        cb = browser.find_element_by_css_selector("textarea[name='comment_text']")
        cb.send_keys(sc)

        button = browser.find_element_by_css_selector("input[type='submit']")
        button.click()

        time.sleep(2)
        print(f'{sc} comment is done !!')

if __name__ == "__main__":
    auto_comment(striped_comment)

