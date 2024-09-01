import openpyxl
from PIL import Image, ImageDraw, ImageFont

workbook_students = openpyxl.load_workbook('planilha_alunos.xlsx')
sheet_students = workbook_students['Sheet1']

for indice, line in enumerate(sheet_students.iter_rows(min_row=2, max_row=2)):
    course = line[0].value
    name = line[1].value
    participation = line[2].value
    workload = line[3].value
    issue_date = line[4].value

    font_name = ImageFont.truetype('./Montserrat-SemiBold.otf', 30)
    default_font = ImageFont.truetype('./Montserrat-Regular.otf', 30)

    # Carregar a imagem do certificado
    image = Image.open('./certificado.jpg')
    draw = ImageDraw.Draw(image)

    # Adicionar texto à imagem
    draw.text((1056, 540), name, fill='white', font=font_name)
    draw.text((1068, 588), course, fill='white', font=default_font)
    draw.text((1190, 639), participation, fill='white', font=default_font)
    draw.text((1218, 689), str(workload), fill='white', font=default_font)

    draw.text((1055, 1055), issue_date, fill='white', font=default_font)

    image.save(f'./{indice} {name} Certificado.png')
