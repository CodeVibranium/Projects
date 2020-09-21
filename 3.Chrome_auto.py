import webbrowser as wb
urL='https://www.google.com'
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
wb.register('chrome', None,wb.BackgroundBrowser(chrome_path))
#wb.get('chrome').open_new_tab(urL)
def web_auto():
    Chrome_path=rf"C:\Program Files (x86)\Google\Chrome\Application"
    URLS=dict(
        Youtube="https://www.youtube.com/",
        Google="https://www.google.com/",
        Geeks_for_geeks="https://www.geeksforgeeks.org/",
        W3schools='https://www.w3schools.com/python/default.asp'
    )
    for title,url in URLS.items():
        print("Opening : ",title)
        wb.get("chrome").open(url)
web_auto()
    