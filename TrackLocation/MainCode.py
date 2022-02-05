# pip install phonenumbers
import phonenumbers
from phonenumbers import geocoder

# Note:give number with country code 
number = input("Enter Your Number : ")

# Shows country Name
ch_num = phonenumbers.parse(number, "CH")
print("Location : "+geocoder.description_for_number(ch_num, "en"))

# Show Service Provider Name
from phonenumbers import carrier
service_num = phonenumbers.parse(number, "RO")
print("Name Of The Service Provider : "+carrier.name_for_number(service_num, "en"))
