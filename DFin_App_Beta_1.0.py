import tkinter
import tkinter.messagebox
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import webbrowser
from tkinter import ttk
from ttkthemes import ThemedTk
plt.style.use("seaborn-v0_8")
root = ThemedTk(theme='scidgreen')
root.title("Financial Information App")
root.geometry("400x85")
root.configure(bg="bisque")
def callback1(url):
    webbrowser.open_new_tab(url)
def stock_analysis():
    stock_window = tkinter.Toplevel()
    stock_window.title("Stock Information")
    stock_window.configure(bg="#CACAFF")
    stock_window.geometry("910x135")   
    text1 = tkinter.Label(stock_window, text = "Enter the ticker symbol (stock symbol):")
    text1.grid(row = 0, column = 0, padx = 2, pady = 2, sticky="W")
    text1.configure(bg="#CACAFF")
    text2 = tkinter.Label(stock_window, text = "Popular ticker symbols: MSFT, AAPL, AMZN, etc.")
    text2.grid(row = 1, column = 0, padx = 2, pady = 2, sticky="W")
    text2.configure(bg="#CACAFF")
    text3 = tkinter.Label(stock_window, text = "Visualization:")
    text3.grid(row = 2, column = 0, padx = 2, pady = 2, sticky="W")
    text3.configure(bg="#CACAFF")
    text4 = tkinter.Label(stock_window, text = "Export data:")
    text4.grid(row = 3, column = 0, padx = 2, pady = 2, sticky="W")
    text4.configure(bg="#CACAFF")  
    stock_entry = tkinter.Entry(stock_window, width = 8)
    stock_entry.grid(row = 0, column = 1, padx = 2, pady = 2)    
    textSeeMore = tkinter.Label(stock_window, text = "See more", font = "Arial 9 underline", cursor="hand2")
    textSeeMore.grid(row = 1, column = 1, padx = 2, pady = 2, sticky="W")
    textSeeMore.configure(bg="#CACAFF", fg="blue")
    textSeeMore.bind("<Button-1>", lambda e: callback2("https://business.unl.edu/outreach/econ-ed/nebraska-council-on-economic-education/student-programs/stock-market-game/documents/Top%202000%20Valued%20Companies%20with%20Ticker%20Symbols.pdf"))   
    def callback2(url):
        webbrowser.open_new_tab(url)    
    def company_sum():
        stock = stock_entry.get().strip()
        try:
            company_info = yf.Ticker(str(stock)).info
            company_info_list = list(company_info.items())
            if len(company_info_list) > 4:
                tkinter.messagebox.showinfo("Info", company_info_list[3][1])
            else:
                tkinter.messagebox.showwarning("Warning", "Please enter the correct symbol")
        except:
            tkinter.messagebox.showwarning("Warning", "Please enter the correct symbol with letters")    
    def visual_data_1y():
        stock = stock_entry.get().strip()
        try:
            company_info = yf.Ticker(str(stock)).info
            company_info_list = list(company_info.items())
            if len(company_info_list) > 4:                
                data_1y = yf.Ticker(str(stock)).history(period="1y")
                plt.figure()
                plt.ylabel("Price ($)")
                plt.xlabel("Timeline")
                plt.title((stock + " - 1 year closing prices").upper())
                plt.plot(data_1y["Close"])
                date_format = mpl_dates.DateFormatter("%b %Y")
                plt.gca().xaxis.set_major_formatter(date_format)
                plt.show()
            else:
                tkinter.messagebox.showwarning("Warning", "Please enter the correct symbol")
        except:
            tkinter.messagebox.showwarning("Warning", "Please enter the correct symbol with letters")            
    def get_data_1y():
        stock = stock_entry.get().strip()
        try:
            company_info = yf.Ticker(str(stock)).info
            company_info_list = list(company_info.items())
            if len(company_info_list) > 4: 
                data_1y = yf.Ticker(str(stock)).history(period="1y")
                data_1y[['Close']].to_csv("{} - 1 year closing prices.csv".format((stock).upper()))
                tkinter.messagebox.showinfo("Info", "Data is stored in \"{} 1 years closing prices.csv\" file!".format((stock).upper()))
            else:
                tkinter.messagebox.showwarning("Warning", "Please enter the correct symbol")
        except:
            tkinter.messagebox.showwarning("Warning", "Please enter the correct symbol with letters")  
    def visual_data_5y():
        stock = stock_entry.get().strip()
        try:
            company_info = yf.Ticker(str(stock)).info
            company_info_list = list(company_info.items())
            if len(company_info_list) > 4:                
                data_5y = yf.Ticker(str(stock)).history(period="5y")
                plt.figure()
                plt.ylabel("Price ($)")
                plt.xlabel("Year")
                plt.title((stock + " - 5 recent years closing prices").upper())
                plt.plot(data_5y["Close"])
                plt.show()
            else:
                tkinter.messagebox.showwarning("Warning", "Please enter the correct symbol")
        except:
            tkinter.messagebox.showwarning("Warning", "Please enter the correct symbol with letters")           
    def get_data_5y():
        stock = stock_entry.get().strip()
        try:
            company_info = yf.Ticker(str(stock)).info
            company_info_list = list(company_info.items())
            if len(company_info_list) > 4: 
                data_5y = yf.Ticker(str(stock)).history(period="5y")
                data_5y[['Close']].to_csv("{} - 5 years closing prices.csv".format((stock).upper()))
                tkinter.messagebox.showinfo("Info", "Data is stored in \"{} 5 years closing prices.csv\" file!".format((stock).upper()))
            else:
                tkinter.messagebox.showwarning("Warning", "Please enter the correct symbol")
        except:
            tkinter.messagebox.showwarning("Warning", "Please enter the correct symbol with letters")
    def visual_data_all():
        stock = stock_entry.get().strip()
        try:
            company_info = yf.Ticker(str(stock)).info
            company_info_list = list(company_info.items())
            if len(company_info_list) > 4:
                data_alltime = yf.Ticker(str(stock)).history(period="max")
                plt.figure()
                plt.ylabel("Price ($)")
                plt.xlabel("Year")
                plt.title((stock + " - all time historical prices").upper())
                plt.plot(data_alltime["Close"])
                plt.show()
            else:
                tkinter.messagebox.showwarning("Warning", "Please enter the correct symbol")
        except:
            tkinter.messagebox.showwarning("Warning", "Please enter the correct symbol with letters")       
    def get_data_all():
        stock = stock_entry.get().strip()
        try:
            company_info = yf.Ticker(str(stock)).info
            company_info_list = list(company_info.items())
            if len(company_info_list) > 4:
                data_alltime = yf.Ticker(str(stock)).history(period="max")
                data_alltime[['Close']].to_csv("{} - all time closing prices.csv".format((stock).upper()))
                tkinter.messagebox.showinfo("Info", "Data is stored in \"{} - all time closing prices.csv\" file!".format((stock).upper()))
            else:
                tkinter.messagebox.showwarning("Warning", "Please enter the correct symbol!")
        except:
            tkinter.messagebox.showwarning("Warning", "Please enter the correct symbol with letters!")
    summary_btn = ttk.Button(stock_window, text = "Summary of the company", width = 28, command = company_sum)
    summary_btn.grid(row = 0, column = 2, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
    visual_data_1y_btn = ttk.Button(stock_window, text = "Visualize 1 year closing prices", width = 28, command = visual_data_1y)
    visual_data_1y_btn.grid(row = 2, column = 2, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
    get_data_1y_btn = ttk.Button(stock_window, text = "Get 1 year closing prices", width = 28, command = get_data_1y)
    get_data_1y_btn.grid(row = 3, column = 2, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
    visual_data_5y_btn = ttk.Button(stock_window, text = "Visualize 5 years closing prices", width = 28, command = visual_data_5y)
    visual_data_5y_btn.grid(row = 2, column = 3, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
    get_data_5y_btn = ttk.Button(stock_window, text = "Get 5 years closing prices", width = 28, command = get_data_5y)
    get_data_5y_btn.grid(row = 3, column = 3, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
    visual_data_all_btn = ttk.Button(stock_window, text = "Visualize all closing prices", width = 28, command = visual_data_all)
    visual_data_all_btn.grid(row = 2, column = 4, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
    get_data_all_btn = ttk.Button(stock_window, text = "Get all hisorical closing prices", width = 28, command = get_data_all)
    get_data_all_btn.grid(row = 3, column = 4, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
def marcro_analysis():
    marcro_window = tkinter.Toplevel()
    marcro_window.title("Marcroeconomics Information")
    marcro_window.configure(bg="#90EE90")
    marcro_window.geometry("650x165")
    text5 = tkinter.Label(marcro_window, text = "Visualization:")
    text5.grid(row = 0, column = 1, padx = 2, pady = 2)
    text5.configure(bg="#90EE90")
    text6 = tkinter.Label(marcro_window, text = "Export data:")
    text6.grid(row = 0, column = 2, padx = 2, pady = 2)
    text6.configure(bg="#90EE90")
    text7 = tkinter.Label(marcro_window, text = "Consumer Price Index (CPI)")
    text7.grid(row = 1, column = 0, padx = 2, pady = 2, sticky="W")
    text7.configure(bg="#90EE90")
    text8 = tkinter.Label(marcro_window, text = "US Unemployment Rate (URATEUS)")
    text8.grid(row = 2, column = 0, padx = 2, pady = 2, sticky="W")
    text8.configure(bg="#90EE90")
    text9 = tkinter.Label(marcro_window, text = "CPI in the last 5 years")
    text9.grid(row = 3, column = 0, padx = 2, pady = 2, sticky="W")
    text9.configure(bg="#90EE90")
    text10 = tkinter.Label(marcro_window, text = "URATEUS in the last 5 years")
    text10.grid(row = 4, column = 0, padx = 2, pady = 2, sticky="W")
    text10.configure(bg="#90EE90")
    def visualize_cpius():
        df = pd.read_csv('https://www.econdb.com/api/series/CPIUS/?format=csv')
        df["Date"] = pd.to_datetime(df.Date, format='%Y-%m-%d')
        df.plot(x = "Date", y = "CPIUS")
        plt.title("US CPI - All time")
        plt.ylabel("Consumer Price Index")
        plt.xlabel("Year")
        plt.show()
    def get_cpius():
        df = pd.read_csv('https://www.econdb.com/api/series/CPIUS/?format=csv')
        df.to_csv("CPIUS.csv", index = False)
        tkinter.messagebox.showinfo("Info", "Data is stored in the \"CPIUS.csv\" file!")
    def visualize_urateus():
        df = pd.read_csv('https://www.econdb.com/api/series/URATEUS/?format=csv')
        df["Date"] = pd.to_datetime(df.Date, format='%Y-%m-%d')
        df.plot(x = "Date", y = "URATEUS")
        plt.title("US Unemployment Rate - All time")
        plt.ylabel("Unemployment Rate (%)")
        plt.xlabel("Year")
        plt.show()
    def get_urateus():
        df = pd.read_csv('https://www.econdb.com/api/series/URATEUS/?format=csv')
        df.to_csv("URATEUS.csv", index = False)
        tkinter.messagebox.showinfo("Info", "Data is stored in the \"URATEUS.csv\" file!")
    def visualize_cpius5y():
        df = pd.read_csv('https://www.econdb.com/api/series/CPIUS/?format=csv')
        df = df.tail(60)
        df["Date"] = pd.to_datetime(df.Date, format='%Y-%m-%d')
        df.plot(x = "Date", y = "CPIUS")
        plt.title("US CPI - Last 5 years")
        plt.ylabel("Consumer Price Index")
        plt.xlabel("Year")
        plt.show()  
    def get_cpius5y():
        df = pd.read_csv('https://www.econdb.com/api/series/CPIUS/?format=csv')
        df = df.tail(60)
        df.to_csv("5 years CPIUS.csv", index = False)
        tkinter.messagebox.showinfo("Info", "Data is stored in the \"5 years CPIUS.csv\" file!")
    def visualize_urateus5y():
        df = pd.read_csv('https://www.econdb.com/api/series/URATEUS/?format=csv')
        df = df.tail(60)
        df["Date"] = pd.to_datetime(df.Date, format='%Y-%m-%d')
        df.plot(x = "Date", y = "URATEUS")
        plt.title("US Unemployment Rate - Last 5 years")
        plt.ylabel("Unemployment Rate (%)")
        plt.xlabel("Year")
        plt.show()
    def get_urateus5y():
        df = pd.read_csv('https://www.econdb.com/api/series/URATEUS/?format=csv')
        df = df.tail(60)
        df.to_csv("5 years URATEUS.csv", index = False)
        tkinter.messagebox.showinfo("Info", "Data is stored in the \"5 years URATEUS.csv\" file!")
    visualize_cpius_btn = ttk.Button(marcro_window, text = "Visualize US CPI", width = 28, command = visualize_cpius)
    visualize_cpius_btn.grid(row = 1, column = 1, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
    get_cpius_btn = ttk.Button(marcro_window, text = "Get US CPI", width = 28, command = get_cpius)
    get_cpius_btn.grid(row = 1, column = 2, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
    visualize_urateus_btn = ttk.Button(marcro_window, text = "Visualize URATEUS", width = 28, command = visualize_urateus)
    visualize_urateus_btn.grid(row = 2, column = 1, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
    get_urateus_btn = ttk.Button(marcro_window, text = "Get URATEUS", width = 28, command = get_urateus)
    get_urateus_btn.grid(row = 2, column = 2, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
    visualize_cpius5y_btn = ttk.Button(marcro_window, text = "Visualize CPI last 5 years", width = 28, command = visualize_cpius5y)
    visualize_cpius5y_btn.grid(row = 3, column = 1, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
    get_cpius5y_btn = ttk.Button(marcro_window, text = "Get CPI last 5 years", width = 28, command = get_cpius5y)
    get_cpius5y_btn.grid(row = 3, column = 2, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
    visualize_urateus5y_btn = ttk.Button(marcro_window, text = "Visualize URATEUS last 5 years", width = 28, command = visualize_urateus5y)
    visualize_urateus5y_btn.grid(row = 4, column = 1, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
    get_urateus_btn = ttk.Button(marcro_window, text = "Get URATEUS last 5 years", width = 28, command = get_urateus5y)
    get_urateus_btn.grid(row = 4, column = 2, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
stock_button = ttk.Button(root, text = "Stock Information", width = 28, command = stock_analysis)
stock_button.grid(row = 0, column = 0, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
marcro_button = ttk.Button(root, text = "Marcroeconomics Information", width = 28, command = marcro_analysis)
marcro_button.grid(row = 0, column = 1, padx = 2, pady = 2, sticky="N"+"S"+"E"+"W")
textClick = tkinter.Label(root, text = "Click the link below to see my Github")
textClick.grid(row = 1, column = 0, padx = 2, pady = 2, sticky="W")
textClick.configure(bg="bisque")
textDuy = tkinter.Label(root, text = "github.com/nhnduy", font = "Arial 9 underline", cursor="hand2")
textDuy.grid(row = 2, column = 0, padx = 2, pady = 2, sticky="W")
textDuy.configure(bg="bisque", fg ="blue")
textDuy.bind("<Button-1>", lambda e: callback1("https://github.com/nhnduy"))
root.mainloop()

