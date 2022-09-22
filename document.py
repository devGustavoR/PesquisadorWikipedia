import wikipedia
import re
from docx import Document

name = input('Digite seu nome: ')
wikipedia.set_lang('pt')
title = input('Sobre o que você quer pesquisar ?\n')

while True:
  try:
    wiki = wikipedia.page(title)
  except:
    print('Nome do projeto inválido')
    title = input('Digite outro nome de projeto: \n')

text = wiki.content
text = re.sub(r'==','',text)
text = re.sub(r'=','',text)
split = text.split('Veja também',1)
text = split[0]

print(text)

document = Document()
paragraph = document.add_heading(title,0)
paragraph.alignment = 1

paragraph = document.add_paragraph('   '+text)
paragraph = document.add_paragraph(name)
paragraph.alignment = 2
document.save(title + '.docx')
input()