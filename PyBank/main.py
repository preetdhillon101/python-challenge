#Challenge PyBank

#Import modules os and csv
import os 
import csv
#Set path for csv file in csv_path
csv_path = 'PyBank/Resources/budget_data.csv'

#Creating and Assigning variables

dates = []
change = []
profits = []
count = 0
initial_profit = 0
total_profit = 0
total_change_profits = 0

#Open and read CSV file
with open (csv_path, newline='') as csvfile:
    #with open('../Resources/budget_data.csv', newline=" ") as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter= ',')
        csv_header = next(csvreader)
  

    # Read each row 
        for row in csvreader:
        #Counting and adding dates
         count = count+1
         dates.append(row[0])
        
    
         profits.append(row[1])
        
         total_profit = total_profit + int(row[1])

        # Read the header row 
         final_profit = int(row[1])
         monthly_change_profits = final_profit - initial_profit


         change.append(monthly_change_profits)

         # Calculate total change over entire period of time

         total_change_profits = total_change_profits  + monthly_change_profits
         initial_profit = final_profit
         #Calculate average change in profit
         average_change_profits = (total_change_profits/count)
        

         #Greatest Increase and corresponding date
         greatest_increase = max(change)
         greatest_date = dates[change.index(greatest_increase)]
 
        #Greatest Decrease  and corresponding date
         greatest_decrease = min(change)
         lowest_date = dates[change.index(greatest_decrease)]

   
        #Print the results
        print("Financial Analysis")

        
        print("Total Months: " + str(count))
        print("Total profits: " + "$" + str(total_profit))
        print("Average Change:" + "$" + str(int(average_change_profits)))
        print("Greatest Increase in Profits: " + str(greatest_date) +  " ($" + str(greatest_increase) + ")")
        print("Greatest Decrease in Profits: " + str(lowest_date) +  " ($" + str(greatest_decrease) + ")")


#print to a text file names financial_analysis
with open('financial_analysis.txt', 'w') as text:
         

        text.write(" Financial Analysis"+ "\n")
        text.write("Total Months: " + str(count)+ "\n")
        text.write("Total profits: $" + str(total_profit)+ "\n")
        text.write("Average Change:" + "$" + str(int(average_change_profits))+ "\n")
        text.write("Greatest Increase in Profits: " + str(greatest_date) +  " ($" + str(greatest_increase) + ")"+ "\n")
        text.write("Greatest Decrease in Profits: " + str(lowest_date) +  " ($" + str(greatest_decrease) + ")"+ "\n")



    