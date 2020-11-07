def make_icecream(*toppings):
    print("這個冰淇淋的配料:")
    for i in toppings:
        print("-----",i)
make_icecream(["草莓"])
make_icecream(["巧克力醬","煉乳","泡芙"])