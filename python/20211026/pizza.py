def make_Pizza(size,*topping):
    print(f'\nmaking {size} pizza')
    for top in topping:
        print(f'-{top}')

make_Pizza(16,'zxc','xcv','cvb','xcvbn')