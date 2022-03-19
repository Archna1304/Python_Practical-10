# @author
# Name : ARCHANA VYAS
# ID : 20CE157


# Aim :
# Generate PDF file of your 3rd Semester Mark-sheet


# GitHUb repository link: https://github.com/Archna1304/Python_Practical-10.git

print(f"\nName : Archana Vyas \nID : 20CE157\n")


from re import I
from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial",size = 15)

print("\n-----------------------3rd Sem Result-----------------------\n")

L,F,M = map(str,input("Enter your name in LFM format : ").split(" "))
Name = L + " " + F + " " + M

Id = input("Enter your Id : ")

Month,Year = map(str,input("Enter Month & Year : ").split(" "))

print("\n\n              Subject Details                  \n")
print("CE224     : INTRODUCTION TO WEB DESIGNING")
print("CE244     : SOFTWARE GROUP PROJECT-1")
print("CE251     : JAVA PROGRAMMING")
print("CE252     : DIGITAL ELECTRONICS")
print("CE257     : DATA COMMUNICATION & NETWORKING")
print("HS121.02A : CREATIVITY,PROBLEM SOLVING AND INNOVATION")
print("MA253     : DISCRETE MATHEMATICS AND ALGEBRA\n")

Total_Credits = input("\nEnter Total Credits : ")

C_WEB = input("\nEnter Credit of CE224 : ")
WEB = input("Enter Grade of CE224 : ")

C_SGP = input("\nEnter Credit of CE244 : ")
SGP = input("Enter Grade of CE244 : ")

C_JAVA_T = input("\nEnter Credit of CE251-Theory : ")
JAVA_T = input("Enter Grade of CE251-Theory : ")

C_JAVA_P = input("\nEnter Credit of CE251-Practical : ")
JAVA_P = input("Enter Grade of CE251-Practical : ")

C_DE_T = input("\nEnter Credit of CE252-Theory : ")
DE_T = input("Enter Grade of CE252-Theory : ")
C_DE_P = input("\nEnter Credit of CE252-Practical : ")
DE_P = input("Enter Grade of CE252-Practical : ")

C_DCN_T = input("\nEnter Credit of CE257-Theory : ")
DCN_T = input("Enter Grade of CE257-Theory : ")
C_DCN_P = input("\nEnter Credit of CE257-Practical : ")
DCN_P = input("Enter Grade of CE257-Practical : ")

C_CPI = input("\nEnter Credit of HS121.02A : ")
CPI = input("Enter Grade of HS121.02A : ")

C_DMA = input("\nEnter Credit of MA253 : ")
DMA = input("Enter Grade of MA253 : ")

SGPA = input("\nEnter your SGPA : ")
Credits_Earned = float(C_WEB) + float(C_SGP) + float(C_JAVA_T) + float(C_JAVA_P) + float(C_DE_T) + float(C_DE_P) + float(C_DCN_T) + float(C_DCN_P) + float(C_CPI) + float(C_DMA)
print("")


pdf.cell(200, 10, txt = "", ln = 1, align = 'C')
pdf.cell(200,10,txt = f"          Name                {Name}",ln=1,align='L')
pdf.cell(200,10,txt = f"          ID                      {Id}" ,ln=1,align='L')
pdf.cell(200,10,txt = f"          Month/Year       {Month}  {Year}",ln=1,align='L')
pdf.cell(200,10,txt = f"          Semester          3",ln=1,align='L')


pdf.cell(200, 10, txt = "", ln = 1, align = 'C')
pdf.cell(200, 10, txt = "", ln = 1, align = 'C')
pdf.cell(200,10,txt ="RESULT ",ln=1,align='C')
pdf.cell(200, 10, txt = "", ln = 1, align = 'C')


pdf.cell(200,10,txt =" Course Code                 Course Type                  Credit                     Grade ",ln=1,align='C')
pdf.cell(200,10,txt =f"   CE224                          Practical                         {C_WEB}                        {WEB} ",ln=1,align='C')
pdf.cell(200,10,txt =f"   CE244                          Practical                         {C_SGP}                        {SGP} ",ln=1,align='C')
pdf.cell(200,10,txt =f"   CE25                            Theory                           {C_JAVA_T}                        {JAVA_T} ",ln=1,align='C')
pdf.cell(200,10,txt =f"   CE251                          Practical                         {C_JAVA_P}                        {JAVA_P} ",ln=1,align='C')
pdf.cell(200,10,txt =f"   CE252                           Theory                           {C_DE_T}                        {DE_T} ",ln=1,align='C')
pdf.cell(200,10,txt =f"   CE252                          Practical                         {C_DE_P}                        {DE_P} ",ln=1,align='C')
pdf.cell(200,10,txt =f"   CE257                           Theory                           {C_DCN_T}                        {DCN_T} ",ln=1,align='C')
pdf.cell(200,10,txt =f"   CE257                          Practical                         {C_DCN_P}                        {DCN_P} ",ln=1,align='C')
pdf.cell(200,10,txt =f"HS121.02 A                     Practical                         {C_CPI}                        {CPI} ",ln=1,align='C')
pdf.cell(200,10,txt =f"   MA253                           Theory                           {C_DMA}                        {DMA} ",ln=1,align='C')


pdf.cell(200, 10, txt = "", ln = 1, align = 'C')
pdf.cell(200, 10, txt = "", ln = 1, align = 'C')
pdf.cell(200,10,txt =" SEMESTER AVERAGE",ln=1,align='C')
pdf.cell(200, 10, txt = "", ln = 1, align = 'C')

pdf.cell(200,10,txt ="Total Credits                              Credits Earned                                   SGPA    ",ln=1,align='C')
pdf.cell(200,10,txt =f"  {Total_Credits}                                                {Credits_Earned}                                          {SGPA}",ln=1,align='C')


pdf.cell(200, 10, txt = "", ln = 1, align = 'C')
pdf.cell(200, 10, txt = "", ln = 1, align = 'C')
pdf.cell(200,10,txt ="SUBJECT DETAILS",ln=1,align='C')
pdf.cell(200, 10, txt = "", ln = 1, align = 'C')

pdf.cell(200,10,txt ="                  CE224          :    INTRODUCTION TO WEB DESIGNING",ln=1,align='L')
pdf.cell(200,10,txt ="                  CE244          :    SOFTWARE GROUP PROJECT-1",ln=1,align='L')
pdf.cell(200,10,txt ="                  CE251          :    JAVA PROGRAMMING",ln=1,align='L')
pdf.cell(200,10,txt ="                  CE252          :    DIGITAL ELECTRONICS",ln=1,align='L')
pdf.cell(200,10,txt ="                  CE257          :    DATA COMMUNICATION & NETWORKING",ln=1,align='L')
pdf.cell(200,10,txt ="                  HS121.02A   :   CREATIVITY,PROBLEM SOLVING AND INNOVATION",ln=1,align='L')
pdf.cell(200,10,txt ="                  MA253          :   DISCRETE MATHEMATICS AND ALGEBRA\n",ln=1,align='L')


pdf.output("20CE157_ARCHANA VYAS_Sem3_UniversityResult.pdf")