#permite percorrer pastas e arquivos
import os

#módulo do PyMuPDF, usado para ler conteúdo de PDFs
import fitz  # PyMuPDF

#função para ler o pfd
def extrair_texto_pdf(caminho):
    doc = fitz.open(caminho)
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()
    return texto.strip()

#função principal (usa os.walk a pasta dados/ e seus arquivos)
def extrair_todos_dados(diretorio="dados"):
    conteudo_total = ""

    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            caminho = os.path.join(raiz, arquivo)

            #se for pdf, chama função para pdf
            if arquivo.lower().endswith(".pdf"):
                conteudo_total += f"\n\n[PDF: {arquivo}]\n"
                conteudo_total += extrair_texto_pdf(caminho)

            #se for txt, abre e lê diretamente
            elif arquivo.lower().endswith(".txt"):
                with open(caminho, "r", encoding="utf-8") as f:
                    conteudo_total += f"\n\n[Texto: {arquivo}]\n"
                    conteudo_total += f.read()

    #esse texto vai para main.py
    return conteudo_total.strip()