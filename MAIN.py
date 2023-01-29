from tkinter import *
#Importing Built-in Libraries
import random
import os
import shutil
import fnmatch
import glob
import pathlib
from pathlib import Path
import sys
import subprocess
import time
from tkinter import *

#Getting Modules from PyPi
print("Downloading Packages From PyPi...")
try:
    from PyPDF2 import PdfMerger
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PyPDF2'])
    from PyPDF2 import PdfMerger

print("Deciding on questions...")

#Choosing randomly from the questions in each folder
Question_Numbers = []
Chapters = []
File_Name = ""
Num_of_Qs = 0

#Getting Current Directory's Path
Current_Path = pathlib.Path(__file__).parent.resolve()
print(" ")

#Making lists  of the files stored in each topic
CH_Content_1 = [name for name in os.listdir(str(Current_Path) + fr"\Source\Topic Questions\Paper 4_qp\Number") if os.path.isfile(os.path.join(str(Current_Path) + fr"\Source\Topic Questions\Paper 4_qp\Number", name))]
CH_Content_2 = [name for name in os.listdir(str(Current_Path) + fr"\Source\Topic Questions\Paper 4_qp\Algebra and Graphs") if os.path.isfile(os.path.join(str(Current_Path) + fr"\Source\Topic Questions\Paper 4_qp\Algebra and Graphs", name))]
CH_Content_3 = [name for name in os.listdir(str(Current_Path) + fr"\Source\Topic Questions\Paper 4_qp\Geometry and Coordinate Geometry") if os.path.isfile(os.path.join(str(Current_Path) + fr"\Source\Topic Questions\Paper 4_qp\Geometry and Coordinate Geometry", name))]
CH_Content_4 = [name for name in os.listdir(str(Current_Path) + fr"\Source\Topic Questions\Paper 4_qp\Mensuration") if os.path.isfile(os.path.join(str(Current_Path) + fr"\Source\Topic Questions\Paper 4_qp\Mensuration", name))]
CH_Content_5 = [name for name in os.listdir(str(Current_Path) + fr"\Source\Topic Questions\Paper 4_qp\Trignometry") if os.path.isfile(os.path.join(str(Current_Path) + fr"\Source\Topic Questions\Paper 4_qp\Trignometry", name))]
CH_Content_6 = [name for name in os.listdir(str(Current_Path) + fr"\Source\Topic Questions\Paper 4_qp\Vectors and Transformations") if os.path.isfile(os.path.join(str(Current_Path) + fr"\Source\Topic Questions\Paper 4_qp\Vectors and Transformations", name))]
CH_Content_7 = [name for name in os.listdir(str(Current_Path) + fr"\Source\Topic Questions\Paper 4_qp\Probabilities") if os.path.isfile(os.path.join(str(Current_Path) + fr"\Source\Topic Questions\Paper 4_qp\Probabilities", name))]
CH_Content_8 = [name for name in os.listdir(str(Current_Path) + fr"\Source\Topic Questions\Paper 4_qp\Statistics") if os.path.isfile(os.path.join(str(Current_Path) + fr"\Source\Topic Questions\Paper 4_qp\Statistics", name))]

#Emptying directories
print("Clearing files in Target Directories...")
Target_Dir_qp = str(Current_Path) + fr"\Chosen Questions"
files_qp = glob.glob(Target_Dir_qp + "\*")
for f in files_qp:
    if(os.path.basename(f) != "0 Front_Page.pdf"):
        os.remove(f)

Target_Dir_ms = str(Current_Path) + fr"\Chosen Answers"
files_ms = glob.glob(Target_Dir_ms + "\*")
for f in files_ms:
    if(os.path.basename(f) != "0 Front_Page.pdf"):
        os.remove(f)

print("Folder Cleared...")

#Create Window
Root_Window = Tk()
Root_Window.title("Project Mock")
Root_Window.geometry('350x200')
Root_Window.resizable(False, False)
Root_Window['background'] = "#171615"

#Title
title = Label(Root_Window, text = "Project Mock", justify=CENTER, font=("Consolas", 20), fg="#20C20E")
title.pack(padx=50, pady=0)
title['background'] = "#171615"

#Translator
def translator(Input):
    if(Input == 1):
        return True
    
    elif(Input == 0):
        return False
    
    else:
        print("not possible")

c_val = IntVar()
c1_val = IntVar()
c2_val = IntVar()
c3_val = IntVar()
c4_val = IntVar()
c5_val = IntVar()
c6_val = IntVar()
c7_val = IntVar()

c_int = c_val.get()
c1_int = c1_val.get()
c2_int = c2_val.get()
c3_int = c3_val.get()
c4_int = c4_val.get()
c5_int = c5_val.get()
c6_int = c6_val.get()
c7_int = c7_val.get()

if translator(c_int) == True:
    Chapters.append(1)
    print(Chapters)
elif translator(c1_int) == True:
    Chapters.append(2)
    print(Chapters)
elif translator(c2_int) == True:
    Chapters.append(3)
    print(Chapters)
elif translator(c3_int) == True:
    Chapters.append(4)
elif translator(c4_int) == True:
    Chapters.append(5)
    print(Chapters)
elif translator(c5_int) == True:
    Chapters.append(6)
    print(Chapters)
elif translator(c6_int) == True:
    Chapters.append(7)
    print(Chapters)
elif translator(c7_int) == True:
    Chapters.append(8)
    print(Chapters)

def c():
    if int(c_val.get()) == 1:
        Chapters.append(1)
    
    elif int(c_val.get()) == 0 and 1 in Chapters:
        Chapters.remove(1)
    print(Chapters)

def c1():
    if int(c1_val.get()) == 1:
        Chapters.append(2)
    
    elif int(c1_val.get()) == 0 and 2 in Chapters:
        Chapters.remove(2)
    print(Chapters)

def c2():
    if int(c2_val.get()) == 1:
        Chapters.append(3)
    
    elif int(c2_val.get()) == 0 and 3 in Chapters:
        Chapters.remove(3)
    print(Chapters)

def c3():
    if int(c3_val.get()) == 1:
        Chapters.append(4)
    
    elif int(c3_val.get()) == 0 and 4 in Chapters:
        Chapters.remove(4)
    print(Chapters)
        
def c4():
    if int(c4_val.get()) == 1:
        Chapters.append(5)
    
    elif int(c4_val.get()) == 0 and 5 in Chapters:
        Chapters.remove(5)
    print(Chapters)

def c5():
    if int(c5_val.get()) == 1:
        Chapters.append(6)
    
    elif int(c5_val.get()) == 0 and 6 in Chapters:
        Chapters.remove(6)
    print(Chapters)
 
def c6():
    if int(c6_val.get()) == 1:
        Chapters.append(7)
    
    elif int(c6_val.get()) == 0 and 7 in Chapters:
        Chapters.remove(7)
    
    print(Chapters)
 
def c7():
    if int(c7_val.get()) == 1:
        Chapters.append(8)
    
    elif int(c7_val.get()) == 0 and 8 in Chapters:
        Chapters.remove(8)
    
    print(Chapters)
 
lbl_start = Label(Root_Window, text = "Welcome!", justify=CENTER, font=("Consolas", 10), fg="#20C20E")
lbl_start.pack()
lbl_start['background'] = "#171615"

lbl_Intro = Label(Root_Window, text = "This is Project Mock,\n a program I made which generates\n math papers from past papers!", justify=CENTER, font=("Consolas", 10), fg="#20C20E")
lbl_Intro.pack()
lbl_Intro['background'] = "#171615"

def Slides():
    lbl_start.pack_forget()
    lbl_Intro.pack_forget()

    Slide_2_Topic.place(x = 2, y = 40)
    c.place(x = 2, y = 70)
    c1.place(x=80, y = 70)
    c2.place(x=2, y = 90)
    c3.place(x=105, y = 110)
    c4.place(x=2, y = 110)
    c5.place(x=2, y = 130)
    c6.place(x=205, y = 130)
    c7.place(x=210, y = 110)
    print("smth: " + str(c1_int))
    print(Chapters)
    
    Button_Start.place_forget()
    Button_Slide_2.place(x = 5, y = 165)

def Slide_2():
    Slide_2_Topic.place_forget()
    c.place_forget()
    c1.place_forget()
    c2.place_forget()
    c3.place_forget()
    c4.place_forget()
    c5.place_forget()
    c6.place_forget()
    c7.place_forget()

    Button_Slide_2.place_forget()

    Slide_3_Topic.place(x = 2, y = 40)
    Slide_3_Topic_Lower.place(x = 2, y = 65)
    txt_Q_Nums.place(x = 5, y = 90)
    Button_Slide_3.place(x = 5, y = 165)

def Slide_3():
    global Num_of_Qs

    Slide_3_Topic.place_forget()
    Slide_3_Topic_Lower.place_forget()
    txt_Q_Nums.place_forget()
    Button_Slide_3.place_forget()

    Slide_4_Topic.place(x = 2, y = 40)
    Button_Slide_4.place(x = 2, y = 165)
    txt_PDF_Name.place(x = 5, y = 70)
    Num_of_Qs = txt_Q_Nums.get()

def Slide_4():
    Slide_4_Topic.place_forget()
    Button_Slide_4.place_forget()
    txt_PDF_Name.place_forget()

    Complete_Notif.pack()
    lbl_End.pack()

def Create_Mock(Question_Number, Q_Type, CH_Num):
    if(Q_Type == "_qp"):
        Target_Dir = str(Current_Path) + fr"\Chosen Questions"

    elif(Q_Type == "_ms"):
        Target_Dir = str(Current_Path) + fr"\Chosen Answers"
    
    #Set chapter paths
    if CH_Num == 1:
        CH_dir = str(Current_Path) + fr"\Source\Topic Questions\Paper 4{Q_Type}\Number"
        CH_Content = CH_Content_1

    elif CH_Num == 2:
        CH_dir = str(Current_Path) + fr"\Source\Topic Questions\Paper 4{Q_Type}\Algebra and Graphs"
        CH_Content = CH_Content_2
    
    elif CH_Num == 3:
        CH_dir = str(Current_Path) + fr"\Source\Topic Questions\Paper 4{Q_Type}\Geometry and Coordinate Geometry"
        CH_Content = CH_Content_3

    elif CH_Num == 4:
        CH_dir = str(Current_Path) + fr"\Source\Topic Questions\Paper 4{Q_Type}\Mensuration"
        CH_Content = CH_Content_4

    elif CH_Num == 5:
        CH_dir = str(Current_Path) + fr"\Source\Topic Questions\Paper 4{Q_Type}\Trignometry"
        CH_Content = CH_Content_5

    elif CH_Num == 6:
        CH_dir = str(Current_Path) + fr"\Source\Topic Questions\Paper 4{Q_Type}\Vectors and Transformations"
        CH_Content = CH_Content_6

    elif CH_Num == 7:
        CH_dir = str(Current_Path) + fr"\Source\Topic Questions\Paper 4{Q_Type}\Probabilities"
        CH_Content = CH_Content_7

    elif CH_Num == 8:
        CH_dir = str(Current_Path) + fr"\Source\Topic Questions\Paper 4{Q_Type}\Statistics"
        CH_Content = CH_Content_8
    
    if Q_Type == "_qp":
        #Choosing a random file and appending it to the list we defined in the start
        Chosen_File = random.choice(CH_Content)
        Question_Numbers.append(Chosen_File)

    print(Question_Numbers)

    print("============================================= Question Information =============================================")
    print("Question Type: " + Q_Type)
    print("Details For Question: " + str(Question_Number))
    Target_Folder = r"{}".format(Target_Dir)
    print("Origin: " + CH_dir)
    pattern = "*" + str(Question_Numbers[Question_Number])
    print("Pattern: '" + pattern + "'")
    Source_Files = os.listdir(CH_dir)

    for file_name in Source_Files:
        if fnmatch.fnmatch(file_name, pattern) == True:
            print("File Chosen: " + str(file_name))
            Full_File_Name = os.path.join(CH_dir, file_name)
            if os.path.isfile(Full_File_Name):
                shutil.copy(Full_File_Name, Target_Folder)
                print("Copying File To Target Directory...")
                print("Copy Successful!")
                print("================================================ End of Question ===============================================")
                print("  ")

    if Q_Type == "_qp":
        #Removing the chosen file from the chapter content lists
        if Chosen_File in CH_Content_1: CH_Content_1.remove(Chosen_File)
        if Chosen_File in CH_Content_2: CH_Content_2.remove(Chosen_File)
        if Chosen_File in CH_Content_3: CH_Content_3.remove(Chosen_File)
        if Chosen_File in CH_Content_4: CH_Content_4.remove(Chosen_File)
        if Chosen_File in CH_Content_5: CH_Content_5.remove(Chosen_File)
        if Chosen_File in CH_Content_6: CH_Content_6.remove(Chosen_File)
        if Chosen_File in CH_Content_7: CH_Content_7.remove(Chosen_File)
        if Chosen_File in CH_Content_8: CH_Content_8.remove(Chosen_File)

def Create_Mock_BTN():
    File_Name = txt_PDF_Name.get()

    for x in range(0, int(Num_of_Qs)):
        if CH_Content_1 == [] and 1 in Chapters:
            Chapters.remove(1)
        if CH_Content_2 == [] and 2 in Chapters:
            Chapters.remove(2)
        if CH_Content_3 == [] and 3 in Chapters:
            Chapters.remove(3)
        if CH_Content_4 == [] and 4 in Chapters:
            Chapters.remove(4)
        if CH_Content_5 == [] and 5 in Chapters:
            Chapters.remove(5)
        if CH_Content_6 == [] and 6 in Chapters:
            Chapters.remove(6)
        if CH_Content_7 == [] and 7 in Chapters:
            Chapters.remove(7)
        if CH_Content_8 == [] and 8 in Chapters:
            Chapters.remove(8)
        
        if Chapters != []:
            CH = random.choice(Chapters)
            print("Chapter: " + str(CH))
            Create_Mock(x, "_qp", CH)
            Create_Mock(x, "_ms", CH)
        
        else:
            print("NO MORE QS LEFT!")
        
    #Notifying User That All Question Have Been Successfully Put Into Target Directory
    print("All questions have been created as individual PDFs and stored in: \n" + Target_Dir_qp)
    print("All answers have been created as individual PDFs and stored in: \n" + Target_Dir_ms)

    print("  ")
    print("================================================ PDF Merging ================================================")
    print("  ")

    #Identifying Directory With Individual Question PDFs(Target Directory)
    pdf_dir_qp = Path(__file__).parent / Target_Dir_qp
    pdf_dir_ms = Path(__file__).parent / Target_Dir_ms

    #Creating The Output Folder Unless It Was Already Created
    pdf_output_dir_qp = Path(__file__).parent / "OUTPUT"
    pdf_output_dir_qp.mkdir(parents = True, exist_ok = True)

    pdf_output_dir_ms = Path(__file__).parent / "OUTPUT"
    pdf_output_dir_ms.mkdir(parents = True, exist_ok = True)

    #Getting All The PDF Files In The Target Directory
    PDF_files_qp = list(pdf_dir_qp.glob("*.pdf"))
    PDF_files_ms = list(pdf_dir_ms.glob("*.pdf"))

    #Outputting PDF Files Which Are Merged
    qpcount = 0
    mscount = 0

    for PDF_qp in PDF_files_qp:
        qpcount += 1
        print("File " + str(qpcount) + ": " + str(os.path.basename(PDF_qp)))

    for PDF_ms in PDF_files_qp:
        mscount += 1
        print("File " + str(mscount) + ": " + str(os.path.basename(PDF_ms)))

    #Iterating Through The List & Appending Them To PDF Merger(From PyPDF2 Library)
    merger_qp = PdfMerger()
    for file in PDF_files_qp:
        merger_qp.append(file)
    merger_qp.write(str(pdf_output_dir_qp / (File_Name + "_qp.pdf")))
    merger_qp.close()

    merger_ms = PdfMerger()
    for file in PDF_files_ms:
        merger_ms.append(file)
    merger_ms.write(str(pdf_output_dir_ms / (File_Name + "_ms.pdf")))
    merger_ms.close()

    #Notifying User That The PDF Files Were Successfully Merged & Outputted Into Output Folder
    print("Files were successfully merged & stored in the 'OUTPUT' folder")

    #Calling Function To Show That Everything Worked Out
    Slide_4()

Button_Start = Button(Root_Window, text="Start!", justify=CENTER, width=47, command=Slides, font=("Consolas", 10), fg = "#20C20E")
Button_Start.place(x = 5, y = 165)
Button_Start['background'] = "#2B2A29"

Button_Slide_2 = Button(Root_Window, text="Next!", justify=CENTER, width=47, command=Slide_2, font=("Consolas", 10), fg = "#20C20E")
Button_Slide_2['background'] = "#2B2A29"
Button_Slide_2.place_forget()

Button_Slide_3 = Button(Root_Window, text="Next!", justify=CENTER, width=47, command=Slide_3, font=("Consolas", 10), fg = "#20C20E")
Button_Slide_3['background'] = "#2B2A29"
Button_Slide_3.place_forget()

Button_Slide_4 = Button(Root_Window, text="Create Mock!", justify=CENTER, width=47, command=Create_Mock_BTN, font=("Consolas", 10), fg = "#20C20E")
Button_Slide_4['background'] = "#2B2A29"
Button_Slide_4.place_forget()

Slide_2_Topic = Label(Root_Window, text = "Choose Chapters!", justify=LEFT, font=("Consolas", 12, "underline"), fg="#20C20E")
Slide_2_Topic['background'] = "#171615"
Slide_2_Topic.place_forget()

Slide_3_Topic = Label(Root_Window, text = "How Many Questions?", justify=LEFT, font=("Consolas", 12, "underline"), fg="#20C20E")
Slide_3_Topic['background'] = "#171615"
Slide_3_Topic.place_forget()

Slide_3_Topic_Lower = Label(Root_Window, text = "[Maximum is 14]", justify=LEFT, font=("Consolas", 10), fg="#20C20E")
Slide_3_Topic_Lower['background'] = "#171615"
Slide_3_Topic_Lower.place_forget()

Slide_4_Topic = Label(Root_Window, text = "Enter PDF Name", justify=LEFT, font=("Consolas", 12, "underline"), fg="#20C20E")
Slide_4_Topic['background'] = "#171615"
Slide_4_Topic.place_forget()

Complete_Notif = Label(Root_Window, text = "Success!", justify=CENTER, font=("Consolas", 12, "underline"), fg="#20C20E")
Complete_Notif['background'] = "#171615"
Complete_Notif.pack_forget()

lbl_End = Label(Root_Window, text = "Mock Paper Successfully Created \n and \n Stored In 'OUTPUT' Folder", justify=CENTER, font=("Consolas", 10), fg="#20C20E")
lbl_End.pack_forget()
lbl_End['background'] = "#171615"

txt_Q_Nums = Entry(Root_Window, width=40, justify=CENTER, font=("Consolas", 10), fg = "#20C20E")    
txt_Q_Nums['background'] = "#2B2A29"
txt_Q_Nums.place_forget()

txt_PDF_Name = Entry(Root_Window, width=40, justify=CENTER, font=("Consolas", 10), fg = "#20C20E")    
txt_PDF_Name['background'] = "#2B2A29"
txt_PDF_Name.place_forget()
File_Name = str(txt_PDF_Name.get())

c = Checkbutton(Root_Window, text = "Numbers", font=("Consolas", 10), variable=c_val, command = c)
c['background'] = "#171615"
c['fg'] = "#20C20E"
c["selectcolor"] = "#171615"
c.place_forget()

c1 = Checkbutton(Root_Window, text = "Algebra and Graphs", font=("Consolas", 10), variable=c1_val, command = c1)
c1['background'] = "#171615"
c1['fg'] = "#20C20E"
c1["selectcolor"] = "#171615"
c1.place_forget()

c2 = Checkbutton(Root_Window, text = "Geometry & Coordinate Geometry", font=("Consolas", 10), variable=c2_val, command = c2)
c2['background'] = "#171615"
c2['fg'] = "#20C20E"
c2["selectcolor"] = "#171615"
c2.place_forget()

c3 = Checkbutton(Root_Window, text = "Mensuration", font=("Consolas", 10), variable=c3_val, command = c3)
c3['background'] = "#171615"
c3['fg'] = "#20C20E"
c3["selectcolor"] = "#171615"
c3.place_forget()

c4 = Checkbutton(Root_Window, text = "Trignometry", font=("Consolas", 10), variable=c4_val, command = c4)
c4['background'] = "#171615"
c4['fg'] = "#20C20E"
c4["selectcolor"] = "#171615"
c4.place_forget()

c5 = Checkbutton(Root_Window, text = "Vectors & Transformations", font=("Consolas", 10), variable=c5_val, command = c5)
c5['background'] = "#171615"
c5['fg'] = "#20C20E"
c5["selectcolor"] = "#171615"
c5.place_forget()

c6 = Checkbutton(Root_Window, text = "Probabilities", font=("Consolas", 10), variable=c6_val, command = c6)
c6['background'] = "#171615"
c6['fg'] = "#20C20E"
c6["selectcolor"] = "#171615"
c6.place_forget()

c7 = Checkbutton(Root_Window, text = "Statistics", font=("Consolas", 10), variable=c7_val, command = c7)
c7['background'] = "#171615"
c7['fg'] = "#20C20E"
c7["selectcolor"] = "#171615"
c7.place_forget()

#Tkinter Loop
Root_Window.mainloop()
