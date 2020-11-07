def kitchen(unserved,served):
    print("廚房處理顧客所點的餐點")
    while unserved:
        current_meal=unserved.pop()
        print("菜單: ",current_meal)
        served.append(current_meal)
def show_unserved_meal(unserved):
    print("下列是尚未服務的餐點: ")
    if not unserved:
        print("沒有餐點")
    for unserved_meal in unserved:
        print(unserved_meal)
def show_served_meal(served):
    print("下列是已經服務的餐點:")
    if not served:
        print("沒有餐點")
    for served_meal in served:
        print(served_meal)

unserved=["大麥克","勁辣雞腿堡","麥克雞塊"]
served=[]

show_unserved_meal(unserved)
show_served_meal(served)

kitchen(unserved,served)
print("廚房處理完成")

show_unserved_meal(unserved)
show_served_meal(served)