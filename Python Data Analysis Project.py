import pandas  as pd
import matplotlib.pyplot as plt
data=pd.read_csv('data.csv')


while True:

    print('\n1. show data: ')
    print('2. top student: ')
    print('3. average marks:')
    print("4. high scorers(>80): ")
    print('5. show graph:' ) 
    print('6. exit: ')


    choice=input('Enter a choice: ')


   
    
    
    if choice == '1':
        print(data)

    elif choice == '2':
        top=data.loc[data['marks'].idxmax()]
        print(top)

    elif choice == '3':
        print('average marks: ',data["marks"].mean())
        
    elif choice == '4':
        print(data[data['marks'] > 80])

    elif choice == '5':
        name=data['name']
        marks=data['marks']


        
        plt.bar(name,marks)
        plt.xlabel('student')
        plt.ylabel('marks')
        plt.title("student marks chart")
        plt.show()

    elif choice == '6':
        print(" close this app.....")
        break

    else:
        print('Enter vai-lid number')
    

        
