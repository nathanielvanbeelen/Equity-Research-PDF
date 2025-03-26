from fpdf import FPDF 
from summary_stats import sean

Ticker = input('Ticker')

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.set_font('Arial', '', 12)
Sean = summary_stats.sean(Ticker)
pdf.cell(80,150,text = Sean, border = 1) #Seans function returning text
Mathew = matthew()
image = Mathew


if os.path.exists(image):
    pdf.image(image, x=10, y=30, w=100)
    pdf.ln(110)  # Leave space after the image
    pdf.cell(0, 10, 'Image added successfully', 0, 1)
else:
    pdf.cell(0, 10, 'Image example (image file not found)', 0, 1)
    pdf.cell(0, 10, 'Replace "example.jpg" with your image path', 0, 1)


tirth = Tirth.stock_analysis(Ticker)
pdf.cell(0, 10, tirth, 0, 1)












