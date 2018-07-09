from autom8 import my_RPA
from os import mkdir
import requests

def wipe(my_bot):
    my_bot.driver.quit()

my_form ="https://www.fema.gov/media-library-data/1520627873824-0f2350ec4204bceff0f01672d86ad151/FF086033_ElevCert_FormOnly_RE_1Mar2018.pdf"

r = requests.get(my_form)
with open('standard_form.pdf', 'wb') as f:
    f.write(r.content)

#print out all of the form fields
my_bot = my_RPA(bot_name="DocumentManager", downloads_directory="DocMngr Downloads")
fields = my_bot.pdf_form_handler.get_form_fields('standard_form.pdf')

ups_url = "https://tools.usps.com/zip-code-lookup.htm?byaddress"
print(fields)
