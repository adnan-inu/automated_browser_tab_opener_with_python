# Import the webbrowser module to handle opening web pages
import webbrowser as wb

# Create a function to automate opening multiple browser tabs
def auto_worksetup():
    # Get the path of the Chrome executable from its installation directory
    # Ensure the path uses "/" instead of "\" and ends with ".exe %s"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    
    # Note: If using Firefox, you would modify the path as follows (for example):
    # firefox_path = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
    while True:   
        #request for URL to be entered manaually by user
        url = input("ENTER WEBSITE (eg: google.com): \n")
    
        # Exit the loop if the user hit ENTER without a word
        if url == '':
            print("Exiting the program.")
            break

        #Use the webbrowser module to open the in a new browser tab
        wb.get(chrome_path).open(url)

# Call the function to execute the browser automation
auto_worksetup()