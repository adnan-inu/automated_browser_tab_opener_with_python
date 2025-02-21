# Import the webbrowser module to handle opening web pages
import webbrowser as wb

# Create a function to automate opening multiple browser tabs
def auto_worksetup():
    # Get the path of the Chrome executable from its installation directory
    # Ensure the path uses "/" instead of "\" and ends with ".exe %s"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    
    # Note: If using Firefox, you would modify the path as follows (for example):
    # firefox_path = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
    
    # Predefine a list of URLs to be opened automatically
    # You can add or remove URLs as needed to fit your workflow
    urls = (
        "gmail.com",              
        "x.com",
        "cnbc.com",
        "thebftonline.com",        
        "cointelegraph.com",      
        "coinmarketcap.com",      
        "ghanaweb.com",
        "Udemy.com",
        "youtube.com"            
    )
    
    # Loop through each URL in the list and open it in Chrome
    for url in urls:
        # Use the webbrowser module to open each URL in a new browser tab
        wb.get(chrome_path).open(url)

# Call the function to execute the browser automation
auto_worksetup()

