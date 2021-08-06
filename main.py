#I used Google Colab developing the logic here
#copy and paste code below will run the whole program
! pip install pyquery
# import PyQuery(class)  from pyquery modle
from pyquery import PyQuery


# get lottery results
def get_lottery():
    url = "https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx"
    html = PyQuery(url)
    tableLarge = html(".td_w.font_black14b_center")
    a = tableLarge.text().split()
    return a

print(get_lottery())

arr=[]
for i in range(39):
    arr.append(0)
total=0
for number in get_lottery():
    number= int(number)
    arr[number]+=1
    total+=1
print(arr)

order=[]
for i in range(39):
    order.append(i)
print(order)
combine= reversed(sorted(zip(arr, order))) #first: appear how many times, #second: the number itself

for group in combine:
    print(group)



