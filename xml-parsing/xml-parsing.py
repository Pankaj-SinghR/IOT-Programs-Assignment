import xml.etree.ElementTree as ET
import requests

url = 'https://timesofindia.indiatimes.com/rssfeeds/66949542.cms'
response = requests.get(url)
string_xml = response.content
myroot = ET.fromstring(string_xml)

channel = myroot.find('channel')
items_list = channel.findall('item')


print("****** All the TECH news from TIMES OF INDIA ******")
for values in items_list:
    title = values.find('title').text
    link = values.find('link').text
    pubdate = values.find('pubDate').text
    print(f"""
    ::::: News Title ::::
{title}
    ::::: Publish Date ::::
{pubdate}
    ::::: link ::::
{link} """)
