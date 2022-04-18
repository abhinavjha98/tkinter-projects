from fpdf import FPDF
import sqlite3
data = []
conn = sqlite3.connect("test1.db")
c = conn.cursor() 
# data = [
#     ("First name", "Last name", "Age", "City"),
#     ("Jules", "Smith", "34", "San Juan"),
#     ("Mary", "Ramos", "45", "Orlando"),
#     ("Carlson", "Banks", "19", "Los Angeles"),
# ]
data.append(("DishName", "Dish Description"))
c.execute("SELECT *,oid FROM dish")
records = c.fetchall()
print(records)
for i in records:
    data.append((i[0],i[1]))
pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=10)
line_height = pdf.font_size * 2.5
print(pdf.epw)
col_width = pdf.epw / 3

lh_list = [] #list with proper line_height for each row
use_default_height = 0 #flag

#create lh_list of line_heights which size is equal to num rows of data
for row in data:
    for datum in row:
        word_list = datum.split()
        number_of_words = len(word_list) #how many words
        if number_of_words>2: #names and cities formed by 2 words like Los Angeles are ok)
            use_default_height = 1
            new_line_height = pdf.font_size * (number_of_words/2) #new height change according to data 
    if not use_default_height:
        lh_list.append(line_height)
    else:
        lh_list.append(new_line_height)
        use_default_height = 0

#create your fpdf table ..passing also max_line_height!
for j,row in enumerate(data):
    for datum in row:
        line_height = lh_list[j] #choose right height for current row
        pdf.multi_cell(col_width, line_height, datum, border=1,align='L',ln=3, 
        max_line_height=pdf.font_size)
    pdf.ln(line_height)

pdf.output('table_with_cells.pdf')