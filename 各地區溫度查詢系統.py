# _*_ coding: utf-8 _*_

def disp_area():
    i=0
    for a in climate_data:
        print("{:>2}:{:<6}\t".format(i,a[0]),end="")
        i=i+1
        if not (i%5): print()
    print()

def disp_temp(data):
    print("顯示區域:",data[0])
    print("-------------------------")
    for i in range(1,13):
        print(i,"月均溫:",data[i],"度")
    print("本地區年均溫為",data[13],"度")
    print("-------------------------")
    
target_file="climate.txt"
with open("climate.txt","r",encoding="utf-8") as fp:
    raw_data=fp.readlines()

climate_data=[]
c=0
while c<len(raw_data):
    t=[]
    for i in range(16):
        t.append(raw_data[i+c].rstrip("\n"))
    climate_data.append(t)
    c=c+16

while True:
    disp_area()
    area=int(input("請輸入你要查詢平均溫度的地區:(-1結束)"))
    if area==-1: break
    disp_temp(climate_data[area])
    x=input("請按Enter返回主選單")