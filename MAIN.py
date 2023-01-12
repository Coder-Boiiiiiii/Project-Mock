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

#Create Window
Root_Window = Tk()
Root_Window.title("Project Mock")
Root_Window.geometry('350x200')
Root_Window.resizable(False, False)
Root_Window['background'] = "#171615"

#Title
title = Label(Root_Window, text = "Project Mock", justify=CENTER, font=("Consolas", 20), fg="#FFFFFF")
title.pack(padx=50, pady=0)
title['background'] = "#171615"

#Create Text
lbl = Label(Root_Window, text = "What Should The PDF Be Called?", justify=CENTER, font=("Consolas", 10), fg="#FFFFFF")
lbl.pack(padx=50, pady=0)
lbl['background'] = "#171615"

#Create Textbox
txt = Entry(Root_Window, width=50, justify=CENTER, font=("Consolas", 10), fg = "#FFFFFF")
txt.pack(padx=50, pady=5)    
txt['background'] = "#2B2A29"

#Function Played When Button Is Clicked
def Enter_Command():
    #File Name (Final PDF Name)
    File_Name = ""
    File_Name = str(txt.get()) + ".pdf"
    if File_Name == "":
        File_Name = "MOCK"

    #To Let Program Get Textbox Values
    time.sleep(1)

    #Hide Other UI When Button Is Clicked
    btn_enter.destroy()
    txt.destroy()
    lbl.destroy()
    lbl_end4.pack()
        
    print("Deciding on questions...")
    #Choosing randomly from the questions in each folder
    Question_Numbers = []
    for x in range(0,12):
        num = random.randint(1,5)
        Question_Numbers.append(num)

    #Getting Current Directory's Path
    Current_Path = pathlib.Path(__file__).parent.resolve()
    print(" ")
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

    #Randomly Picking Questions & Adding To Target Directory
    def Copier(Question_Number, Q_Type):
        if(Q_Type == "_qp"):
            Target_Dir = str(Current_Path) + fr"\Chosen Questions"

        elif(Q_Type == "_ms"):
            Target_Dir = str(Current_Path) + fr"\Chosen Answers"

        print("============================================= Question Information =============================================")
        print("Details For Question: " + str(Question_Number))
        Target_Folder = r"{}".format(Target_Dir)
        Original_Folder = str(Current_Path) + fr"\Source\Paper 4{Q_Type}\Q{Question_Number}"
        print("Origin: " + Original_Folder)
        pattern = "*" + str(Question_Numbers[Question_Number-1]) + ".pdf"
        print("Pattern: '" + pattern + "'")
        Source_Files = os.listdir(Original_Folder)

        for file_name in Source_Files:
            if fnmatch.fnmatch(file_name, pattern) == True:
                print("File Chosen: " + str(file_name))
                Full_File_Name = os.path.join(Original_Folder, file_name)
                if os.path.isfile(Full_File_Name):
                    shutil.copy(Full_File_Name, Target_Folder)
                    print("Copying File To Target Directory...")
                    print("Copy Successful!")
                    print("================================================ End of Question ===============================================")
                    print("  ")

    #Using The Choser Function For The 12 Questions
    for x in range(1,13):
        Copier(x, "_qp")
    
    for x in range(1,13):
        Copier(x, "_ms")

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
    merger_qp.write(str(pdf_output_dir_qp / (File_Name[:-4] + "_qp.pdf")))
    merger_qp.close()

    merger_ms = PdfMerger()
    for file in PDF_files_ms:
        merger_ms.append(file)
    merger_ms.write(str(pdf_output_dir_ms / (File_Name[:-4] + "_ms.pdf")))
    merger_ms.close()

    #Notifying User That The PDF Files Were Successfully Merged & Outputted Into Output Folder
    print("Files were successfully merged & stored in the 'OUTPUT' folder")
    lbl_end4.destroy()
    lbl_end1.pack()
    lbl_end2.pack()
    lbl_end3.pack()

#Create Enter Button
btn_enter = Button(Root_Window, text="Create Mock!", justify=CENTER, width=20, command=Enter_Command, font=("Consolas", 10), fg = "#FFFFFF")
btn_enter.pack(padx=50, pady=5)
btn_enter['background'] = "#2B2A29"

#Create Labels When Program Ends
lbl_end1 = Label(Root_Window, text = "Mock Paper Successfully Created", justify=CENTER, width= 200, font=("Consolas", 10), fg = "#FFFFFF")
lbl_end1.pack(padx=50, pady=0)
lbl_end1.pack_forget()
lbl_end1['background'] = "#171615"

lbl_end2 = Label(Root_Window, text = "and", justify=CENTER, width= 200, font=("Consolas", 10), fg = "#FFFFFF")
lbl_end2.pack(padx=50, pady=0)
lbl_end2.pack_forget()
lbl_end2['background'] = "#171615"

lbl_end3 = Label(Root_Window, text = "Stored In 'OUTPUT' Folder", justify=CENTER, width= 200, font=("Consolas", 10), fg = "#FFFFFF")
lbl_end3.pack(padx=50, pady=0)
lbl_end3.pack_forget()
lbl_end3['background'] = "#171615"

lbl_end4 = Label(Root_Window, text = "Please Wait...", justify=CENTER, width= 200, font=("Consolas", 10), fg = "#FFFFFF")
lbl_end4.pack(padx=50, pady=0)
lbl_end4.pack_forget()
lbl_end4['background'] = "#171615"

#Tkinter Loop
Root_Window.mainloop()