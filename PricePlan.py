from selenium import webdriver  # Loads Selenium Library

driver = webdriver.Chrome()
print("Welcome to Bell Device Price Plan Selection")
print("Please wait while we load the device names.....")

# Opens Bell Devices Web Page using Chrome
driver.get('https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices')

count = 0
# Loop to get the list of 12 Device names from the web page
while count < 12:
    var1 = "div_product_list_item_div_product_list_item_" + str(count)
    # Command to get the Device name along with other attributes
    var = driver.find_element_by_id(var1)
    count = count + 1
    # Command to isolate and print only Device name
    print(count,".",var.text.split("\n")[0])
# While loop with Exception handler to validate user input to be an Integer
while True:
    try:
        # Fetch User Input and validate it
        var2 = int(input('Please choose a device by typing the corresponding number, to see further details : '))
        if var2 < 1 or var2 > 12:
            raise ValueError
        break
    except ValueError:
        print('Please Type a number between 1 to 12 listed against the device of your choice')

var2 = var2 - 1
print("\nThanks for choosing , Please wait while we retreive the information.....")
var3 = 'div_product_list_item_div_product_list_item_' + str(var2)
# Clicking on the device selected by the User to fetch price plans
driver.find_element_by_id(var3).click()
# Fetch device name from the web page
print('\nDevice Name : ',driver.find_element_by_class_name('bcx-detail-header1').text.split("\n")[0])
print('Available Price Plans are... \n')
# Format the output to display price plans
print(driver.find_element_by_class_name('bcx-order-now-box-group').text.replace('.\n','.\n\n'))
# Close the web browser
driver.close()