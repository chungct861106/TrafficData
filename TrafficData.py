import pandas as pd 
from xml.etree import ElementTree
import requests
from bs4 import BeautifulSoup

url = "https://tisvcloud.freeway.gov.tw/"
res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')
sheets = soup.find("table", class_="table style-1").find_all("tr")

#%%

head = [cell.text.strip() for cell in sheets[0].find_all("td")]
head.pop(4)
content =[[cell.text.strip() for cell in line.find_all("td")[0:4]]+[url + line.find_all("a")[1].get("href")] for line in sheets[1:]]

sheet_df = pd.DataFrame(content, columns=head)
sheet_df.to_excel("TrafficDataSource.xlsx")


# def MergeLists(lists):
#     output = list()
#     for alist in lists:
#         output = output + alist
#     return output
# def GetTreeInfo(root):
#     return MergeLists([[cell.text] if len(cell) == 0 else GetTreeInfo(cell) for cell in root])

# def GetTreeCol(root):
#     return MergeLists([[cell.tag[cell.tag.find("}") + 1:]] if len(cell) == 0 else GetTreeCol(cell) for cell in root])

# def GetXMLSheet(url):
#     res = requests.get(url)
#     res.encoding = 'utf-8'
#     frame = list(list(ElementTree.fromstring(res.text))[-1])
#     col = GetTreeCol(frame[0])
#     data = [GetTreeInfo(child) for child in frame]
#     return pd.DataFrame(data, columns=col)
# urls = sheet_df["下載"].tolist()
# names = sheet_df["項目"].tolist() 
# excel = {"資料目錄":sheet_df}
# for i in range(len(sheet_df)):
#     print(names[i]+" Start")
#     try:
#         excel[names[i]] = GetXMLSheet(urls[i])
#         print(names[i]+" Finished")
#     except:
#         print(names[i]+" Failed")

