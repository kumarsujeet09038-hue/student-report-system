import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('sales.csv')

while True:
    print("\n1. Show data")
    print("2. Total sales")
    print("3. Best product")
    print("4. Best month")
    print("5. Show product graph")
    print("6. Show month graph")
    print("7. Exit")
    choice=input('Enter choice: ')

    if choice == '1':
        print(data)
    

    elif choice == '2':
        print("Total_sales:",data["sales"].sum())

    elif choice == '3':
        best_product=data.groupby("product")['sales'].sum().idxmax()
        print("Best product: ",best_product)

    elif choice == '4':
        best_month=data.groupby('month')['sales'].sum().idxmax()
        print( "Best month: ",best_month)

    elif choice == '5':
        product=data.groupby('product')['sales'].sum()

        max_product=product.max()

        color=[]
        for i in product:
            if i == max_product:
                color.append('red')
            else:
                color.append('blue')

        product.plot(color=color,kind="bar")

        plt.title("Sales by Product (Top Highlighted)")
        plt.xlabel("product")
        plt.ylabel('sales')
        plt.show()

    elif choice == '6':
        month_sales=data.groupby('month')['sales'].sum()

        month=month_sales.max()

        color=[]

        for i in month_sales:
            if i == month:
                color.append("red")
            else:
                color.append('blue')
        
        month_sales.plot(color=color,kind="bar")

        plt.title("Best month(top highlight)")
        plt.xlabel('month')
        plt.ylabel("sales")
        plt.show()
    
    elif choice == '7':
        print("Closing APP...")
        break

    else:
        print("Inv-lid input!")