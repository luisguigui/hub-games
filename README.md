# 🎮 Game Hub - DEV EDITION

Uma plataforma moderna e intuitiva para gerenciar e jogar diversos jogos em um único lugar. Desenvolvida com Python e interface gráfica elegante, o Game Hub oferece uma experiência gamificada com temas neon personalizáveis.

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab.svg?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-Latest-blue.svg?style=flat-square)](https://github.com/TomSchimansky/CustomTkinter)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

---

## ✨ Características Principais

### 🎯 Plataforma Unificada
- **6 jogos diferentes** integrados em uma única aplicação
- Interface centralizada com navegação intuitiva
- Biblioteca de jogos organizada com cards informativos

### 🎨 Design Moderno
- **Tema escuro/claro** personalizável
- Paleta de cores **neon cyberpunk** para cada jogo
- Interface responsiva e fluida com CustomTkinter
- Sidebar expansível com ícones e nomes dos jogos

### ⚙️ Configurações Personalizáveis
- Alternar entre temas Dark e Light
- Ajustar tamanho da fonte (Pequeno, Médio, Grande)
- Controlar volume global dos jogos (0-100%)
- Configurações persistentes durante a sessão

### 📚 Sistema de Ajuda Integrado
- Central de ajuda centralizada
- Instruções "Como Jogar" para cada jogo
- Descrições detalhadas e modalidades interativas
- Acesso rápido às regras antes de começar

---

## 🎮 Jogos Disponíveis

| Jogo | Emoji | Descrição | Tipo |
|------|-------|-----------|------|
| **CYBER-SNAKE** 🐍 | Clássico reimaginado | Controle uma cobra que cresce | Action |
| **NEON INVADERS** 🚀 | Shooter vertical | Destrua hordas de aliens | Shoot'em Up |
| **RAIVA 2.0** 🕹️ | Ação frenética | Fases impossíveis e frustração | Arcade |
| **CYBER PACMAN** 👻 | Labirintos cyberpunk | Devore pontos e fuja de fantasmas | Puzzle |
| **WORDLE PRO** ⌨️ | Dedução de palavras | Descubra a palavra em 6 tentativas | Word Game |
| **GAME SHOW** 🎲 | Quiz interativo | Teste seus conhecimentos gerais | Quiz |

---

## 🚀 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/luisguigui/hub-games.git
cd hub-games
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Execute o Hub**
```bash
python hub.py
```

---

## 📋 Dependências

O projeto utiliza as seguintes bibliotecas Python:

- **customtkinter** - Interface gráfica moderna
- **Pillow (PIL)** - Processamento de imagens para posters dos jogos
- **tkinter** - Framework GUI padrão do Python (incluído)

> Veja `requirements.txt` para versões específicas

---

## 🎮 Como Usar

### Iniciar um Jogo
1. Abra o Game Hub
2. Clique no card do jogo desejado ou em seu ícone na sidebar
3. Escolha entre **ℹ️ INFO** para instruções ou **▶ JOGAR** para começar

### Acessar Instruções
- Clique no botão **❓ AJUDA** na sidebar para a central de ajuda
- Selecione qualquer jogo para ver as regras "Como Jogar"
- Use **📖 COMO JOGAR** em cada card para instruções rápidas

### Personalizar Experiência
- Clique em **⚙️ CONFIGS** na sidebar
- Ajuste tema, tamanho de fonte e volume
- Clique **✔ SALVAR** para aplicar mudanças

---

## 🎯 Estrutura do Projeto

```
hub-games/
├── hub.py                 # Aplicação principal - Game Hub
├── cobrinha.py           # Jogo CYBER-SNAKE
├── space.py              # Jogo NEON INVADERS
├── RAIVA2.py             # Jogo RAIVA 2.0
├── pacman.py             # Jogo CYBER PACMAN
├── termo.py              # Jogo WORDLE PRO
├── game.py               # Jogo GAME SHOW
├── poster_*.png          # Imagens dos posters dos jogos
├── requirements.txt      # Dependências do projeto
└── README.md             # Este arquivo
```

---

## 🛠️ Desenvolvimento

### Executar em Modo Desenvolvimento
```bash
python hub.py
```

### Adicionar um Novo Jogo
1. Crie seu arquivo de jogo (ex: `novo_jogo.py`)
2. Adicione a entrada em `GAME_INFO` no `hub.py`:
```python
"novo_jogo": {
    "descricao": "Descrição do seu jogo...",
    "como_jogar": "Instruções passo a passo..."
}
```
3. Adicione à lista `self.jogos`:
```python
{"id": "novo_jogo", "file": "novo_jogo.py", "nome": "NOVO JOGO", 
 "emoji": "🎮", "cor": "#FF00FF"}
```
4. Adicione um arquivo de poster (`poster_novo_jogo.png`)

---

## 🎨 Customização

### Cores dos Temas
As cores padrão para cada jogo podem ser modificadas em `hub.py`:
```python
"cor": "#00F2FF"  # Formato hexadecimal
```

### Tamanho da Janela
Altere na classe `GameHubPro.__init__()`:
```python
self.geometry("1150x750")  # Largura x Altura
```

---

## 📝 Configurações do Sistema

O Game Hub armazena as seguintes configurações durante a sessão:

| Configuração | Padrão | Opções |
|--------------|--------|--------|
| Tema | Dark | Dark, Light |
| Tamanho da Fonte | Médio | Pequeno, Médio, Grande |
| Volume Global | 50% | 0-100% |

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'customtkinter'"
```bash
pip install --upgrade customtkinter
```

### "Falha ao abrir [arquivo do jogo]"
- Certifique-se de que todos os arquivos dos jogos estão no mesmo diretório
- Verifique se os arquivos `.py` estão com nomes corretos

### Posters não aparecem
- Coloque os arquivos `poster_*.png` no diretório raiz
- Confirme que os nomes seguem o padrão: `poster_[id_jogo].png`

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 👨‍💻 Autor

**Luis Guigui**
- GitHub: [@luisguigui](https://github.com/luisguigui)

---

## 🎉 Agradecimentos

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) pela incrível biblioteca GUI
- Comunidade Python pelo suporte e inspiração

---

## 📞 Suporte

Se você tiver dúvidas ou encontrar problemas:

1. Verifique as [Issues](https://github.com/luisguigui/hub-games/issues) existentes
2. Crie uma nova Issue descrevendo seu problema
3. Inclua prints de tela se relevante

---

**Desenvolvido com ❤️ em Python**

*"A melhor plataforma de jogos começa com uma grande experiência de usuário"*
