#Expense-Tracker!
import json,os 
File=os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.json")

tracker=[]
def load():
    """Read saved expenses from the file when the program starts."""
    if os.path.exists(File):
        try:
            with open(File, "r") as f:
                tracker.extend(json.load(f))
        except json.JSONDecodeError:
            print("Saved file was damaged. Starting with an empty tracker.")

def add(item,description,amount):
    expense={
       "item" : item,
       "description" : description,
       "amount" : amount       
       }
    tracker.append(expense)
    #print(f"Added {expense} to tracker")

def save() :   
    with open(File, "w") as file:
          json.dump(tracker,file,indent=4)
          print("Expense added to file!!")
# print(tracker)
def view():
        print("\n=========================")
        print("   Your Expense Tracker    ")
        print("\n=========================")
        with open(File , "r") as file:
            content=json.load(file)
            #print(content) 
        if len(content)==0:
              print("No expense added till now!!")
              return
    
        for i, exp in enumerate(content):
          print(f"[{i}] Item: {exp['item'].capitalize()} | Desc: {exp['description']} | Amount: ${exp['amount']}")
def totalam():
      total=0
      for i in tracker:
            total+=i["amount"]
      #print(total)
      return f"Your total expenditure {total}" #f"Your total expenditure {total}"
def delete(index):
       delitem= tracker[index]["item"]
       del tracker[index]
       return f"'{delitem.capitalize()}' successfully deleted from tracker."
def category_summary():
      summary_dict={}
      for exp in tracker:
            cat=exp["item"].lower().strip()
            amount=exp["amount"]

            if cat in summary_dict:
                  summary_dict[cat]+=amount
            else:
                summary_dict[cat]=amount
      print("\n-----Category Summary------")
      for cati,total in summary_dict.items():
            print(f".{cati.capitalize()} : ${total}")
      print("------------------------------\n")

def main():
      load()
      while True:
            print("1.Add a new Expense\n"
        "2.View all Expense\n" 
        "3.View total expenditure\n" 
        "4.Category-wise summary\n" 
        "5.Delete an expense\n" 
        "6.Exit")
            try:
                choice=int(input("Enter Your Choice: "))
            
            
                if choice==1:
                    print("Opening add expense...")
                    item=input("Enter your Item Category: ").strip()
                    desc=input("Enter your Description: ").strip()
                    amount=int(input("Enter Amount: "))
                    add(item,desc,amount)
                    save()
                    print(f"{item} added to tracker!")
                elif choice==2:
                        # print("---Your expense tracker is here---")
                            #print("----------------------------\n")
                            view()
                elif choice==3:
                            print("---Your Total Expenditure---")
                            print(totalam())
                elif choice==4:
                        print("---Category wise summary---")
                        category_summary()
                elif choice==5:
                        view()
                        target=int(input("--Enter the index (#) to delete: "))
                        delete(target)
                        save()
                        
                elif choice==6:
                    print("Thank you for using Expense Tracker!")
                    break
                else:
                            print("Invalid!")
                
            
            except ValueError:
                    print("Invalid input! Please Enter no...")

if __name__=="__main__":
      main()









