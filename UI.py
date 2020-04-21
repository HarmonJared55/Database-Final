from tkinter import *
import pyodbc

class UI:
    def _init_():
            
        #set up dbconnection
        server = 'IN-CSCI-MSSQL.ADS.IU.EDU\SQLSERV2017DEV2' 
        database = 'Group4' 
        username = '10har10' 
        password = 'Daprar7-CSCI44300' 
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()

        #create and define the window
        window = Tk()
        window.geometry('1000x700')
        window.title("Group 4 Database final")
        lbl = Label(window,text="Hello, this is the UI for Group4's datatbase final project. Please use the following commands to query to your hearts content")
        lbl.grid(column=0,row=0)

        #standalone query
        
        
        #output
        lbl_output = Label(window, text="Output")
        lbl_output.grid(column=0,row=20)
        
        #command funtions

        #full custom querey
        def std_query():
            lbl_output.configure(text="")
            text = queryinput.get()
            cursor.execute(text)
            rows = cursor.fetchall()
            str_output = lbl_output.cget("text") + "\n"
            
            for row in rows:
               str_output += str(row) + " " + "\n"
               
            lbl_output.configure(text=str_output)

        #std_insert
        def std_insert():
            lbl_output.configure(text="")
            text = insertion_input.get()
            cursor.execute(text)
            lbl_output.configure(text="Insertion complete")
            cnxn.commit()
        

            
        #find researchers
        def find_res():
            lbl_output.configure(text="")
            text ="exec ResearcherDiscoveries @RID = " + res_proc_input.get() + ";"
            cursor.execute(text)
            rows = cursor.fetchall()
            str_output = lbl_output.cget("text") + "\n"
            for row in rows:
               str_output += str(row) + " " + "\n"
            lbl_output.configure(text=str_output)

        #get system Bodies
        def get_bodies():
            lbl_output.configure(text="")
            text = "exec GetSystemBodies @BID = '" + sys_proc_input.get() + "';"
            cursor.execute(text)
            rows = cursor.fetchall()
            str_output = lbl_output.cget("text") + "\n"
            for row in rows:
               str_output += str(row) + " " + "\n"
            lbl_output.configure(text=str_output)

        #get tel id
        def get_tel():
            lbl_output.configure(text="")
            text = "exec TelescopeDiscoveries @Tid = " + tel_proc_input.get() + ";"
            cursor.execute(text)
            rows = cursor.fetchall()
            str_output = lbl_output.cget("text") + "\n"
            for row in rows:
               str_output += str(row) + " " + "\n"
            lbl_output.configure(text=str_output)

        #get body info
        def get_body_info():
            lbl_output.configure(text="")
            text = "exec GetBodyInfo @BID = " + binfo_proc_input.get() + ";"
            cursor.execute(text)
            rows = cursor.fetchall()
            str_output = lbl_output.cget("text") + "\n"
            for row in rows:
               str_output += str(row) + " " + "\n"
            lbl_output.configure(text=str_output)

        #ui-----------------------------------------------------------------------------------------
        
        lbl2 = Label(window,text="Stored Procdeures")

        #query
        std_query_lbl = Label(window,text="Use this line to enter custom query")
        std_query_lbl.grid(column=0, row=2)
        btn_std_query = Button(window,text="Query Database",command=std_query)
        btn_std_query.grid(column=1,row=3)
        queryinput = Entry(window,width=100)
        queryinput.grid(column=0,row=3)
        
        #insertion
        insertion_lbl = Label(window,text="Use this line to insert into database with sql insertion statement")
        insertion_lbl.grid(column=0, row=4)
        insertion_input = Entry(window,width=100)
        insertion_input.grid(column=0,row=5)
        btn_insertion_input = Button(window,text="insert into database",command=std_insert)
        btn_insertion_input.grid(column=1,row=5)

        #proceduers
        #----------------------------------------------------------------------------------------------------------------------------------------------
        #find researchers
        res_proc_lbl = Label(window,text="Lookup researcher discoveries by researcher id")
        res_proc_lbl.grid(column=0,row=7)
        res_proc_input = Entry(window,width=100)
        res_proc_input.grid(column=0,row=8)
        btn_res_proc = Button(window,text="Lookup discoveries",command=find_res)
        btn_res_proc.grid(column=1,row=8)

        #find system bodies
        sys_proc_lbl = Label(window,text="Lookup systems: Enter system name ie. Jupiter,Saturn,Neptune,ect")
        sys_proc_lbl.grid(column=0,row=9)
        sys_proc_input = Entry(window,width=100)
        sys_proc_input.grid(column=0,row=10)
        btn_sys_proc = Button(window,text="Lookup systems",command=get_bodies)
        btn_sys_proc.grid(column=1,row=10)

        #find telescope discoveries
        tel_proc_lbl = Label(window,text="Lookup telescope disoveries: input the telescope id")
        tel_proc_lbl.grid(column=0,row=11)
        tel_proc_input = Entry(window,width=100)
        tel_proc_input.grid(column=0,row=12)
        btn_tel_proc = Button(window,text="Lookup telescope",command=get_tel)
        btn_tel_proc.grid(column=1,row=12)
        
        #find telescope discoveries
        binfo_proc_lbl = Label(window,text="Get info about a specfic body")
        binfo_proc_lbl.grid(column=0,row=13)
        binfo_proc_input = Entry(window,width=100)
        binfo_proc_input.grid(column=0,row=14)
        btn_binfo_proc = Button(window,text="Lookup Body",command=get_body_info)
        btn_binfo_proc.grid(column=1,row=14)

        window.mainloop()   
    
#main script        
myvar = UI._init_()
