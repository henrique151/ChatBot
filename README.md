# 🤖 AsimoBot – ChatBot Inteligente com LangChain e Groq

## 📌 Sobre o projeto

O **AsimoBot** é um chatbot inteligente que interage com o usuário com base em diferentes fontes de informação como **sites**, **PDFs** e **vídeos do YouTube**, utilizando inteligência artificial com a biblioteca **LangChain** e o modelo da **Groq API**.

A aplicação tem como objetivo facilitar o acesso à informação de maneira interativa e dinâmica, resumindo, explicando e respondendo perguntas sobre conteúdos específicos fornecidos pelo usuário.

### 🔎 Como funciona:

1. **Seleção de Fonte de Informação:**
   - O usuário escolhe interagir com:
     - 🌐 Um site (digitando a URL),
     - 📄 Um arquivo PDF (selecionando via uma janela do sistema),
     - ▶️ Um vídeo do YouTube (informando a URL do vídeo).

2. **Extração de Conteúdo:**
   - O conteúdo é carregado da fonte escolhida utilizando loaders da LangChain (WebBaseLoader, PyPDFLoader e YoutubeLoader).

3. **Interação com o AsimoBot:**
   - Um assistente virtual chamado **Asimo** é iniciado e responde às perguntas feitas com base nas informações extraídas.

4. **Diálogo Contínuo:**
   - O chat mantém o histórico da conversa, permitindo interações mais naturais e contextualizadas.

---

## 🧰 Tecnologias Utilizadas

- **Python** – linguagem principal da aplicação
- **LangChain** – orquestração de LLMs e gerenciamento de conversas
- **Groq API** – modelos de linguagem de alta performance
- **Tkinter** – interface para seleção de arquivos PDF
- **dotenv** – gerenciamento de variáveis sensíveis (.env)

---

## ⚙️ Como utilizar o projeto localmente

### ✅ Pré-requisitos:

- Python 3.10+
- Conta ativa na [Groq](https://console.groq.com/)
- Chave de API da Groq
- (Para usar YouTube): conexão com a internet e o vídeo deve ter legendas disponíveis
- (Para PDFs): o sistema precisa suportar GUI (janela para seleção de arquivos)

---

### 🛠️ Passo a passo:

1. **Clone o repositório:**
```bash
git clone https://github.com/henrique151/ChatBot
```

2. **Acesse o diretório do projeto:**
```bash
cd ChatBot
```

3. **Crie o arquivo .env com sua chave da Groq:**
```bash
GROQ_API_KEY="sua-chave-da-groq"
```

4. **Instale as dependências:**
```bash
pip install langchain langchain_groq langchain_community python-dotenv tkinter
```

5.**Execute o programa:**
```bash
python app.py
```
