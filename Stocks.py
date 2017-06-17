import urllib.request #library for network calls
import re              #Regular expressions library  
#https://www.google.com/finance?q=
url="https://www.google.com/finance?q="
Category=input("Enter the category of stock Product")
url=url+Category         #Concatenated URL
data=urllib.request.urlopen(url).read() #Gets response in form of bits and bytes even though its readable it isn't parseable
data=data.decode("utf-8")   #decoding in UTF-* helps parsing
#print(data)
m=re.search('meta itemprop="price"',data)
start=m.start()
end=start+50
requiredString=data[start:end]
m=re.search('content="',requiredString) #To get the required result
start=m.end()
rdata=requiredString[start:]
m=re.search("/",rdata)
start=0
end=m.end()-3
finalResult=rdata[0:end]
print("The value of "+Category+" "+finalResult)
