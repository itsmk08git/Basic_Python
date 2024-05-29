import statistics

stock = {
    'info' : [600,630,620],
    'ril' : [1430, 1490, 1567],
    'mtl' : [234,180,160]
}

def add():
    s_input = input("Enter Stock:")
    price = input("Enter the Price:")
    price = float(price)
    if s_input in (x.lower() for x in stock):
        stock[s_input].append(price)
    else:
        stock[s_input]=[price]
    print_all()

def print_all():
    for x, y in stock.items():
        avg = statistics.mean(y)
        print(f"{x}==> {y} ==> avg: {avg}")

def main():
    u_input=input("Enter the Operation you want to perform(print or add):")
    user_input=u_input.lower()

    if user_input == 'print' :
        print_all()
    elif user_input == 'add' :
        add()

if __name__ == '__main__':
    main()
