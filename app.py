import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders import PyPDFLoader
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import threading

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='gemma2-9b-it')

def resposta_bot(mensagens, documento):
    mensagem_system = '''Você é um assistente amigável chamado Asimo.
    Você utiliza as seguintes informações para formular as suas respostas: {informacoes}'''
    mensagens_modelo = [('system', mensagem_system)]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({'informacoes': documento}).content


def carrega_site():
    url_site = input("Digite a url do site: ")
    loader = WebBaseLoader(url_site)
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento = documento + doc.page_content
    return documento


def carrega_pdf():
    documento = ''
    def selecionar_pdf():
        nonlocal documento
        root = Tk()
        root.withdraw()
        root.call('wm', 'attributes', '.', '-topmost', True)
        caminho = askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        root.destroy()

        if not caminho:
            print("Nenhum arquivo selecionado.")
            return

        loader = PyPDFLoader(caminho)
        lista_documentos = loader.load()
        for doc in lista_documentos:
            documento += doc.page_content

   
    t = threading.Thread(target=selecionar_pdf)
    t.start()
    t.join()

    return documento


def carrega_youtube():
    url_youtube = input("Digite a url do video: ")
    loader = YoutubeLoader.from_youtube_url(
        url_youtube,
        language=['pt']
    )
    lista_documentos = loader.load()

    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    return documento


print('Bem-vindo ao ChatBot da Asimo! (Digite x a qualquer momento para sair)')

texto_selecao = '''
Digite 1 se você quiser conversar com um site
Digite 2 se você quiser conversar com um PDF
Digite 3 se você quiser conversar com um vídeo de YouTube
Digite x para sair
'''

while True:
    selecao = input(texto_selecao)
    if selecao.lower() == 'x':
        print('Até logo! Obrigado por usar o AsimoBot.')
        break

    documento = ''
    if selecao == '1':
        documento = carrega_site()
    elif selecao == '2':
        documento = carrega_pdf()
    elif selecao == '3':
        documento = carrega_youtube()
    else:
        print('Digite um valor entre 1 a 3 ou "x" para sair.')
        continue

    if not documento:
        continue

    mensagens = []
    while True:
        pergunta = input('Usuário: ')
        if pergunta.lower() == 'x':
            break
        mensagens.append(('user', pergunta))
        resposta = resposta_bot(mensagens, documento)
        mensagens.append(('assistant', resposta))
        print(f"Asimo: {resposta}")
