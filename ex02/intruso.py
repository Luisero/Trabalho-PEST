from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5

def mm2p(milimetros):
    return milimetros / 0.352777

cnv = canvas.Canvas("Concessionária_pdf.pdf", pagesize=A5)
cnv.drawString(mm2p(150),mm2p(340), "Olá")
cnv.save()