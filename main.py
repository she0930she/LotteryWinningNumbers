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

reference_number= []
original = []
for n in range(39):
    original.append(0)
print(original)

for n in range(39):
    reference_number.append(n)
print("[reference_number]")
print(reference_number)

for n in get_lottery():
    a = int(n)
    #original[a ] = original[a ]
    # original = original[a-1]+1
    print(a)

print("[lottery_result]")
print(original)




