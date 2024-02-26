Here are some topics I find noticable to highlight about this Superpy assignment. I have tried to make this application as flexible and user-friendly as possible. These are some examples of how I have tried to achieve this:

Running 'python3 main.py init' for the first time creates three files:
1. bought.csv to start storing the data of bought products
2. sold.csv to start storing the data of sold products and to be able to calculate revenue and profit
3. day.csv, in which the date of today is stored. This file gets refreshed every time you start up the application again, so the operator always works with todays date as the starting point for reports, calculations, etcetera

When using the graphs to see results, it automatically adds the date of saving to the file name. This way the operator doesn't need to worry about ordering saved graphics afterwards. In this case it is saved in the pdf format, but it can easily be exported as .png or other formats. 

Inside the code I have tried to make this more 'user' friendly by using the csv.DictReader and csv.DictWriter functions instead of the csv.writer and csv.reader for example. This helps to address tables in the csv docs more easily and makes it more obvious to the readers of the code what is going on.