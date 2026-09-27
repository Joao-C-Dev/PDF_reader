from pypdf import PdfReader
import re
import os
import glob

FILE_DIR = r"C:\Users\joaoh\Downloads"
OUTPUT_FILE = 'Resultado.txt'

def get_crea(texto):
    crea = re.search(r'(PR\-[0-9]{4,}\/[D,P])', texto)[0]
    return "CREA: " + crea

def get_art(texto):
    cod_art = re.search(r'ART de Obra ou Servi\s*ço\n\d+', texto)[0]
    if cod_art:
        cod_art = cod_art.split('\n')[1]
    return "CÓDIGO N°: " + cod_art

def generate_output(output_txt, file, txt):
    output_txt += f'{file}\n'
    output_txt += f'{get_crea(txt)}\n'
    output_txt += f'{get_art(txt)}\n\n'
    return output_txt

def generate_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)

def read_pdf(file_name):
    with open(file_name, 'rb') as arquivo:
        pdf_lido = PdfReader(arquivo)
        return pdf_lido.pages[0].extract_text()

def main():
    output_txt = ''
    os.chdir(FILE_DIR)
    for file in list(glob.glob('*.pdf')):
        texto = read_pdf(file)
        output_txt = generate_output(output_txt, file, texto)

    print(output_txt)
    generate_file(OUTPUT_FILE, output_txt)

if __name__ == "__main__":
    main()

