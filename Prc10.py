from fpdf import FPDF pdf = FPDF() pdf.add_page() pdf.set_font("Arial", size = 10) f = open(r"E:\College\SEMESTER 4\Result.txt") for i in f: 
    pdf.cell(200,10,txt=i,ln=1) pdf.output("Result.pdf") 
