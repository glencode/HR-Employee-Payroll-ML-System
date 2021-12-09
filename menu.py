
import sys
import os
import subprocess
from tkinter import *
import tkinter
from tkinter import messagebox
import PIL
from PIL import ImageTk
from PIL import Image
 

class empsal:
    def __init__(self,root):
        
        self.mainLabel=Label(root,text='WHO WE ARE? :A state corporation mandated to provide financial and business development support services to youth owned enterprises',font=('Arial',-15,'bold underline'))
        self.mainLabel.place(x=150,y=200)
        
        
        self.menubar=Menu(root)
        root.config(menu=self.menubar)
        
        self.mysql_menu=Menu(root,tearoff=0)
        self.menubar.add_cascade(label='CSV/DF File Maintenance',menu=self.mysql_menu)
        self.mysql_menu.add_command(label='Build/Display Csv File',command=self.create_csv)
        self.mysql_menu.add_command(label='Convert Csv to excel',command=self.csv_to_excel)
        self.mysql_menu.add_command(label='Display Data from Excel',command=self.excel_to_table)
        
        self.mysql_menu.add_separator()
        self.mysql_menu.add_command(label='Exit',command=root.destroy)
        
        self.reports_menu=Menu(root,tearoff=0)
        self.menubar.add_cascade(label='Reports/Data Visualization',menu=self.reports_menu)
        self.reports_menu.add_command(label='Display Updated DF',command=self.disp_updt_df)
        self.reports_menu.add_command(label='County Wise Mean Expenses,Bar Graph',command=self.County_wise_mean)
        self.reports_menu.add_command(label='Gender wise sum,mean,std. Deviation',command=self.gender_wise_calc)
        self.reports_menu.add_command(label='County Wise Total Expenses ,Bar Graph',command=self.County_wise_total)
        self.reports_menu.add_command(label='Scatter plot of experience in years(x) v/s Salary(y)',command=self.scatter_plot)
        
        
        self.predict_menu=Menu(root,tearoff=0)
        self.menubar.add_cascade(label='Prediction',menu=self.predict_menu)
        self.predict_menu.add_command(label='Predict Salary given experience',command=self.predict_salary)
        
        
    def create_csv(self):
        os.system("python.exe create_csv.py")
    def csv_to_excel(self):
        os.system("python.exe csv_to_xls.py")
    def excel_to_table(self):
        os.system("python.exe Excel_to_table.py")
    
    def disp_updt_df(self):
        os.system("python.exe disp_updt_df.py")
    def County_wise_mean(self):
        os.system("python.exe County_wise_mean.py")
        
    def County_wise_total(self):
        os.system("python.exe County_wise_total.py")
    def gender_wise_calc(self):
        os.system("python.exe gender_wise_calc.py")
    def scatter_plot(self):
        os.system("python.exe scatter_plot.py")
    def predict_salary(self):
        os.system("python.exe predictSalary.py")
        

        

root=Tk()
root.title("Youthfund Employee HR Ml System")
root.geometry("1200x800")
#root.resizable(FALSE,FALSE)
warmth1 = messagebox.showinfo("Welcome", "We believe in empowering the youth to empower the future")
my_image= ImageTk.PhotoImage(Image.open("some_img.jpg"))
glenext = Label(root, image=my_image)
glenext.place(x=0,y=0,width=1200,height=800)
obj=empsal(root)
root.mainloop()  
        
