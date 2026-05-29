import customtkinter as ctk
from PIL import Image
import subprocess
import os
from tkinter import messagebox

# ─── DADOS DOS JOGOS  ────────────────────────────────────
GAME_INFO = {
    "snake": {
        "descricao": (
            "🐍  CYBER-SNAKE é um clássico reimaginado em estética neon.\n\n"
            "Você controla uma cobra que cresce a cada presa capturada. "
            "Quanto maior ela fica, mais difícil é evitar colidir com o próprio corpo. "
            "Um teste puro de reflexo e estratégia espacial."
        ),
        "como_jogar": (
            "1️⃣  Use as teclas W A S D ou as setas do teclado para mover a cobra.\n\n"
            "2️⃣  Coma os pontos/frutas que aparecem na tela para crescer e ganhar pontos.\n\n"
            "3️⃣  Evite bater nas paredes ou no próprio corpo da cobra.\n\n"
            "4️⃣  A velocidade aumenta conforme você come mais itens.\n\n"
            "5️⃣  Tente bater seu recorde de pontos!"
        ),
    },
    "space": {
        "descricao": (
            "🚀  NEON INVADERS é um shooter espacial de tiro vertical.\n\n"
            "Hordas de inimigos alienígenas descem em formação e você deve destruí-las "
            "antes que cheguem ao solo. Cada onda é mais rápida e agressiva que a anterior. "
            "Sobreviva o máximo que puder!"
        ),
        "como_jogar": (
            "1️⃣  Mova sua nave com as setas ← → (ou A / D).\n\n"
            "2️⃣  Atire nos inimigos pressionando ESPAÇO.\n\n"
            "3️⃣  Destrua todos os aliens da onda para avançar ao próximo nível.\n\n"
            "4️⃣  Não deixe nenhum inimigo chegar à linha inferior da tela.\n\n"
            "5️⃣  Power-ups podem aparecer — colete-os para vantagens especiais!"
        ),
    },
    "raiva": {
        "descricao": (
            "🕹️  RAIVA 2.0 é um jogo de ação frenética onde a frustração é o combustível.\n\n"
            "Enfrente fases impossíveis, chefes raivosos e obstáculos absurdos. "
            "O jogo foi feito para testar seus limites — cada morte é uma lição. "
            "Quantas tentativas você vai precisar?"
        ),
        "como_jogar": (
            "1️⃣  Use as setas ou WASD para mover seu personagem.\n\n"
            "2️⃣  Pule com ESPAÇO e ataque com Z ou X.\n\n"
            "3️⃣  Cada fase tem um obstáculo único — observe os padrões antes de agir.\n\n"
            "4️⃣  Você tem vidas limitadas; ao perder todas, reinicia do começo.\n\n"
            "5️⃣  Respire fundo. Raiva só piora as coisas. 😄"
        ),
    },
    "pacman": {
        "descricao": (
            "👻  CYBER PACMAN é uma releitura neon do arcade mais icônico de todos os tempos.\n\n"
            "Navegue por labirintos cyberpunk, devore pontos e fuja de fantasmas inteligentes. "
            "Colete as pílulas especiais para virar o jogo e caçar os fantasmas de volta. "
            "Clássico e viciante como sempre!"
        ),
        "como_jogar": (
            "1️⃣  Mova o Pac-Man pelas setas ← → ↑ ↓ do teclado.\n\n"
            "2️⃣  Coma todos os pontos do labirinto para completar a fase.\n\n"
            "3️⃣  Evite os fantasmas coloridos — um toque e você perde uma vida.\n\n"
            "4️⃣  Coma as pílulas grandes nos cantos para ficar invencível por alguns segundos.\n\n"
            "5️⃣  Durante a invencibilidade, você pode comer os fantasmas para ganhar pontos extras!"
        ),
    },
    "wordle": {
        "descricao": (
            "⌨️  WORDLE PRO é um jogo de dedução de palavras inspirado no famoso Wordle.\n\n"
            "Você tem 6 tentativas para descobrir a palavra secreta de 5 letras. "
            "A cada palpite, as cores das letras te guiam até a resposta correta. "
            "Simples de aprender, difícil de dominar!"
        ),
        "como_jogar": (
            "1️⃣  Digite uma palavra de 5 letras e pressione ENTER para confirmar.\n\n"
            "2️⃣  🟩 Verde = letra certa no lugar certo.\n\n"
            "3️⃣  🟨 Amarelo = letra existe na palavra, mas está no lugar errado.\n\n"
            "4️⃣  ⬛ Cinza = letra não existe na palavra secreta.\n\n"
            "5️⃣  Você tem 6 tentativas. Use as dicas de cor para raciocinar a palavra!"
        ),
    },
    "game": {
        "descricao": (
            "🎲  GAME SHOW é um jogo de perguntas e respostas com temática de quiz.\n\n"
            "Teste seus conhecimentos gerais em diversas categorias. "
            "Responda corretamente para acumular pontos e avançar para perguntas mais difíceis. "
            "Será que você é um mestre do trivia?"
        ),
        "como_jogar": (
            "1️⃣  Selecione uma categoria de perguntas para começar.\n\n"
            "2️⃣  Leia a pergunta e escolha a resposta correta entre as opções apresentadas.\n\n"
            "3️⃣  Responda corretamente para ganhar pontos e avançar para a próxima pergunta.\n\n"
            "4️⃣  A cada resposta certa, as perguntas ficam mais difíceis.\n\n"
            "5️⃣  Tente alcançar a pontuação máxima e se tornar o campeão do quiz!"
        ),
    },
}
# ──────────────────────────────────────────────────────────────────────────────


class GameHubPro(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("GAME HUB - DEV EDITION")
        self.geometry("1150x750")
        ctk.set_appearance_mode("dark")

        self.sidebar_expandida = False
        self.largura_retraida = 70
        self.largura_expandida = 240
        self.poster_size = (140, 200)

        # ── Configurações persistentes ────────────────────────────────────────
        self.volume_global = 50
        self.tema_atual = "dark"
        self.tamanho_fonte = 13  # pequeno=11, médio=13, grande=15

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.poster_images = {}
        self.carregar_todos_os_posters()

        self.jogos = [
            {"id": "snake",  "file": "cobrinha.py", "nome": "CYBER-SNAKE",   "emoji": "🐍", "cor": "#00F2FF"},
            {"id": "space",  "file": "space.py",    "nome": "NEON INVADERS", "emoji": "🚀", "cor": "#1eff00"},
            {"id": "raiva",  "file": "RAIVA2.py",   "nome": "RAIVA 2.0",     "emoji": "🕹️", "cor": "#FF0055"},
            {"id": "pacman", "file": "pacman.py",   "nome": "CYBER PACMAN",  "emoji": "👻", "cor": "#ffea00"},
            {"id": "wordle", "file": "termo.py",    "nome": "WORDLE PRO",    "emoji": "⌨️", "cor": "#6aaa64"},
            {"id":"game", "file":"game.py", "nome":"GAME SHOW", "emoji":"🎲", "cor":"#ff6f91"},
        ]

        self.setup_ui()

    # ── Carregamento de posters ───────────────────────────────────────────────
    def carregar_todos_os_posters(self):
        mapeamento = {
            "snake":  "poster_snake.png",
            "space":  "poster_space.png",
            "raiva":  "poster_raiva.png",
            "pacman": "poster_pacman.png",
            "wordle": "poster_wordle.png",
            "game": "poster_game.png",
        }
        for pid, arquivo in mapeamento.items():
            caminho = os.path.join(os.path.dirname(__file__), arquivo)
            if os.path.exists(caminho):
                try:
                    img = Image.open(caminho)
                    self.poster_images[pid] = ctk.CTkImage(
                        light_image=img, dark_image=img, size=self.poster_size
                    )
                except:
                    self.poster_images[pid] = None
            else:
                self.poster_images[pid] = None

    # ── Layout principal ──────────────────────────────────────────────────────
    def setup_ui(self):
        # --- SIDEBAR ---
        self.sidebar = ctk.CTkFrame(
            self, width=self.largura_retraida, corner_radius=0, fg_color=("gray90", "#0a0a0a")
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        self.sidebar.grid_columnconfigure(0, weight=1)
        self.sidebar.grid_rowconfigure(99, weight=1)

        # ── Botão ☰ ───────────────────────────────────────────────────────────
        self.btn_menu = ctk.CTkButton(
            self.sidebar, text="☰", width=50, height=50,
            fg_color="transparent", hover_color=("gray75", "#1e1e1e"),
            font=("Arial", 24),
            text_color=("gray10", "gray90"),   # FIX: visível em ambos os temas
            command=self.toggle_sidebar,
        )
        self.btn_menu.grid(row=0, column=0, pady=(20, 30))

        # ── Botões dos jogos ──────────────────────────────────────────────────
        self.botoes_sidebar = []
        for i, jogo in enumerate(self.jogos, start=1):
            btn = ctk.CTkButton(
                self.sidebar, text=jogo["emoji"],
                width=60, height=60,
                fg_color="transparent", hover_color=("gray75", "#1e1e1e"),
                font=("Segoe UI Emoji", 26), anchor="center",
                text_color=("gray10", "gray90"),   # FIX: visível em ambos os temas
                command=lambda j=jogo: self.mostrar_resumo(j),
            )
            btn.grid(row=i, column=0, pady=5)
            self.botoes_sidebar.append(btn)

        # ── Botão de AJUDA ────────────────────────────────────────────────────
        self.btn_ajuda = ctk.CTkButton(
            self.sidebar,
            text="❓",
            width=36, height=36,
            fg_color=("#ddeeff", "#1a1a2e"),
            hover_color=("#bbddff", "#16213e"),
            border_color="#000000",
            border_width=2,
            corner_radius=18,
            font=("Segoe UI Emoji", 16),
            text_color=("gray10", "#00F2FF"),   # FIX: visível em ambos os temas
            command=self.abrir_ajuda,
        )
        self.btn_ajuda.grid(row=99, column=0, pady=(0, 4), sticky="s")

        # ── Botão de CONFIGURAÇÕES ────────────────────────────────────────────
        self.btn_config = ctk.CTkButton(
            self.sidebar,
            text="⚙️",
            width=36, height=36,
            fg_color=("#ddeeff", "#1a1a2e"),
            hover_color=("#bbddff", "#16213e"),
            border_color="#000000",
            border_width=2,
            corner_radius=18,
            font=("Segoe UI Emoji", 16),
            text_color=("gray10", "#00F2FF"),   # FIX: visível em ambos os temas
            command=self.abrir_configuracoes,
        )
        self.btn_config.grid(row=100, column=0, pady=(0, 16), sticky="s")

        # --- ÁREA PRINCIPAL ---
        self.scroll_frame = ctk.CTkScrollableFrame(
            self, fg_color=("gray90", "#141414"), label_text="BIBLIOTECA DE JOGOS"
        )
        self.scroll_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        for jogo in self.jogos:
            self.adicionar_item_catalogo(jogo)

    # ── Sidebar toggle ────────────────────────────────────────────────────────
    def toggle_sidebar(self):
        if self.sidebar_expandida:
            self.sidebar.configure(width=self.largura_retraida)
            self.btn_ajuda.configure(text="❓", anchor="center", width=36)
            self.btn_config.configure(text="⚙️", anchor="center", width=36)
            for btn, jogo in zip(self.botoes_sidebar, self.jogos):
                btn.configure(text=jogo["emoji"], anchor="center")
        else:
            self.sidebar.configure(width=self.largura_expandida)
            self.btn_ajuda.configure(text="  ❓  AJUDA", anchor="w", width=180)
            self.btn_config.configure(text="  ⚙️  CONFIGS", anchor="w", width=180)
            for btn, jogo in zip(self.botoes_sidebar, self.jogos):
                btn.configure(text=f"  {jogo['emoji']}   {jogo['nome']}", anchor="w")
        self.sidebar_expandida = not self.sidebar_expandida

    # ── Modal de CONFIGURAÇÕES ────────────────────────────────────────────────
    def abrir_configuracoes(self):
        win = ctk.CTkToplevel(self)
        win.title("Configurações")
        win.geometry("420x420")
        win.resizable(False, False)
        win.attributes("-topmost", True)
        win.grab_set()

        # Cabeçalho
        header = ctk.CTkFrame(win, fg_color="#00F2FF", corner_radius=0, height=6)
        header.pack(fill="x")

        ctk.CTkLabel(
            win, text="⚙️  CONFIGURAÇÕES",
            font=("Fixedsys", 22), text_color="#00F2FF",
        ).pack(pady=(16, 4))

        separador = ctk.CTkFrame(win, height=2, fg_color="#00F2FF")
        separador.pack(fill="x", padx=30, pady=(0, 20))

        # ── Tema Visual ───────────────────────────────────────────────────────
        ctk.CTkLabel(
            win, text="🎨  Tema Visual:",
            font=("Arial", 13, "bold"), text_color=("gray35", "#aaaaaa"),
        ).pack(anchor="w", padx=35, pady=(0, 4))

        tema_var = ctk.StringVar(value="Dark" if self.tema_atual == "dark" else "Light")

        tema_menu = ctk.CTkOptionMenu(
            win,
            values=["Dark", "Light"],
            variable=tema_var,
            fg_color=("#ddeeff", "#1a1a2e"),
            button_color=("#ddeeff", "#1a1a2e"),
            button_hover_color=("#bbddff", "#16213e"),
            dropdown_fg_color=("gray88", "#1a1a1a"),
            text_color="#00F2FF",
            font=("Arial", 13),
            command=self._preview_tema,
        )
        tema_menu.pack(fill="x", padx=35, pady=(0, 20))

        # ── Tamanho de Fonte ──────────────────────────────────────────────────
        ctk.CTkLabel(
            win, text="🔤  Tamanho da Fonte:",
            font=("Arial", 13, "bold"), text_color=("gray35", "#aaaaaa"),
        ).pack(anchor="w", padx=35, pady=(0, 4))

        fonte_var = ctk.StringVar(value={11: "Pequeno", 13: "Médio", 15: "Grande"}.get(self.tamanho_fonte, "Médio"))

        fonte_menu = ctk.CTkOptionMenu(
            win,
            values=["Pequeno", "Médio", "Grande"],
            variable=fonte_var,
            fg_color=("#ddeeff", "#1a1a2e"),
            button_color=("#ddeeff", "#1a1a2e"),
            button_hover_color=("#bbddff", "#16213e"),
            dropdown_fg_color=("gray88", "#1a1a1a"),
            text_color="#00F2FF",
            font=("Arial", 13),
        )
        fonte_menu.pack(fill="x", padx=35, pady=(0, 20))

        # ── Volume Geral ──────────────────────────────────────────────────────
        self._label_volume = ctk.CTkLabel(
            win, text=f"🔊  Volume Geral: {self.volume_global}%",
            font=("Arial", 13, "bold"), text_color=("gray35", "#aaaaaa"),
        )
        self._label_volume.pack(anchor="w", padx=35, pady=(0, 4))

        vol_slider = ctk.CTkSlider(
            win, from_=0, to=100,
            button_color="#00F2FF",
            button_hover_color="#00c8d4",
            progress_color="#00F2FF",
            fg_color=("#ddeeff", "#1a1a2e"),
            command=self._atualizar_volume_label,
        )
        vol_slider.set(self.volume_global)
        vol_slider.pack(fill="x", padx=35, pady=(0, 24))

        # ── Botões Salvar / Cancelar ──────────────────────────────────────────
        btn_frame = ctk.CTkFrame(win, fg_color="transparent")
        btn_frame.pack(fill="x", padx=35, side="bottom", pady=20)

        ctk.CTkButton(
            btn_frame, text="✕  CANCELAR",
            fg_color="transparent", hover_color=("gray75", "#1e1e1e"),
            border_color="#555", border_width=1,
            text_color=("gray50", "#555555"), font=("Arial", 12),
            height=40,
            command=lambda: [self._preview_tema(
                "Dark" if self.tema_atual == "dark" else "Light"
            ), win.destroy()],
        ).pack(side="left", expand=True, fill="x", padx=(0, 6))

        ctk.CTkButton(
            btn_frame, text="✔  SALVAR",
            fg_color="#00F2FF", hover_color="#00c8d4",
            text_color="#000000", font=("Arial", 12, "bold"),
            height=40,
            command=lambda: self._salvar_configuracoes(
                tema_var.get(), fonte_var.get(), vol_slider.get(), win
            ),
        ).pack(side="left", expand=True, fill="x", padx=(6, 0))

    def _preview_tema(self, valor):
        ctk.set_appearance_mode(valor.lower())

    def _atualizar_volume_label(self, valor):
        self._label_volume.configure(text=f"🔊  Volume Geral: {int(valor)}%")

    def _salvar_configuracoes(self, tema, fonte, volume, win):
        self.tema_atual = tema.lower()  
        ctk.set_appearance_mode(self.tema_atual)

        mapa_fonte = {"Pequeno": 11, "Médio": 13, "Grande": 15}
        self.tamanho_fonte = mapa_fonte.get(fonte, 13)

        self.volume_global = int(volume)
        win.destroy()

    # ── Modal de resumo do jogo ───────────────────────────────────────────────
    def mostrar_resumo(self, jogo):
        info = GAME_INFO.get(jogo["id"], {})

        win = ctk.CTkToplevel(self)
        win.title(f"Sobre: {jogo['nome']}")
        win.geometry("520x580")
        win.resizable(False, False)
        win.attributes("-topmost", True)
        win.grab_set()

        # ── Cabeçalho colorido ────────────────────────────────────────────────
        header = ctk.CTkFrame(win, fg_color=jogo["cor"], corner_radius=0, height=6)
        header.pack(fill="x")

        ctk.CTkLabel(
            win, text=jogo["emoji"],
            font=("Segoe UI Emoji", 64),
            fg_color="transparent",
        ).pack(pady=(20, 4))

        ctk.CTkLabel(
            win, text=jogo["nome"],
            font=("Fixedsys", 26),
            text_color=jogo["cor"],
        ).pack()

        separador = ctk.CTkFrame(win, height=2, fg_color=jogo["cor"])
        separador.pack(fill="x", padx=40, pady=12)

        # ── Descrição ─────────────────────────────────────────────────────────
        ctk.CTkLabel(
            win, text="📋  SOBRE O JOGO",
            font=("Arial", 13, "bold"),
            text_color=("gray35", "#aaaaaa"),
        ).pack(anchor="w", padx=30)

        desc_box = ctk.CTkTextbox(
            win, height=130, fg_color=("gray88", "#1a1a1a"),
            font=("Arial", self.tamanho_fonte), wrap="word",
            border_color=("gray70", "#333"), border_width=1,
        )
        desc_box.pack(fill="x", padx=30, pady=(6, 14))
        desc_box.insert("end", info.get("descricao", "Sem descrição disponível."))
        desc_box.configure(state="disabled")

        # ── Botões ────────────────────────────────────────────────────────────
        btn_frame = ctk.CTkFrame(win, fg_color="transparent")
        btn_frame.pack(fill="x", padx=30, pady=(0, 6))

        ctk.CTkButton(
            btn_frame,
            text="📖  COMO JOGAR",
            fg_color=("#ddeeff", "#1a1a2e"),
            hover_color=("#bbddff", "#16213e"),
            border_color=jogo["cor"],
            border_width=2,
            text_color=jogo["cor"],
            font=("Arial", 13, "bold"),
            height=42,
            command=lambda: self.abrir_como_jogar(jogo),
        ).pack(side="left", expand=True, fill="x", padx=(0, 6))

        ctk.CTkButton(
            btn_frame,
            text="▶  JOGAR AGORA",
            fg_color=jogo["cor"],
            hover_color=jogo["cor"],
            text_color="#000000",
            font=("Arial", 13, "bold"),
            height=42,
            command=lambda: [self.launch(jogo["file"]), win.destroy()],
        ).pack(side="left", expand=True, fill="x", padx=(6, 0))

        ctk.CTkButton(
            win, text="✕  FECHAR",
            fg_color="transparent",
            hover_color=("gray75", "#1e1e1e"),
            text_color=("gray50", "#555555"),
            font=("Arial", 11),
            height=30,
            command=win.destroy,
        ).pack(pady=(4, 10))

    # ── Modal "Como Jogar" ────────────────────────────────────────────────────
    def abrir_como_jogar(self, jogo):
        info = GAME_INFO.get(jogo["id"], {})

        win = ctk.CTkToplevel(self)
        win.title(f"Como jogar: {jogo['nome']}")
        win.geometry("480x420")
        win.resizable(False, False)
        win.attributes("-topmost", True)
        win.grab_set()

        header = ctk.CTkFrame(win, fg_color=jogo["cor"], corner_radius=0, height=6)
        header.pack(fill="x")

        ctk.CTkLabel(
            win,
            text=f"📖  COMO JOGAR  —  {jogo['nome']}",
            font=("Fixedsys", 16),
            text_color=jogo["cor"],
        ).pack(pady=(18, 8))

        separador = ctk.CTkFrame(win, height=2, fg_color=jogo["cor"])
        separador.pack(fill="x", padx=30, pady=(0, 12))

        text_box = ctk.CTkTextbox(
            win, fg_color=("gray88", "#1a1a1a"),
            font=("Arial", self.tamanho_fonte), wrap="word",
            border_color=("gray70", "#333"), border_width=1,
        )
        text_box.pack(fill="both", expand=True, padx=30, pady=(0, 10))
        text_box.insert("end", info.get("como_jogar", "Sem instruções disponíveis."))
        text_box.configure(state="disabled")

        ctk.CTkButton(
            win, text="▶  JOGAR AGORA",
            fg_color=jogo["cor"],
            text_color="#000000",
            font=("Arial", 13, "bold"),
            height=42,
            command=lambda: [self.launch(jogo["file"]), win.destroy()],
        ).pack(fill="x", padx=30, pady=(0, 6))

        ctk.CTkButton(
            win, text="✕  FECHAR",
            fg_color="transparent", hover_color=("gray75", "#1e1e1e"),
            text_color=("gray50", "#555555"), font=("Arial", 11), height=30,
            command=win.destroy,
        ).pack(pady=(0, 10))

    # ── Modal de AJUDA GERAL ──────────────────────────────────────────────────
    def abrir_ajuda(self):
        win = ctk.CTkToplevel(self)
        win.title("Ajuda — Todos os Jogos")
        win.geometry("620x680")
        win.resizable(False, False)
        win.attributes("-topmost", True)
        win.grab_set()

        # Barra superior
        header = ctk.CTkFrame(win, fg_color="#00F2FF", corner_radius=0, height=6)
        header.pack(fill="x")

        ctk.CTkLabel(
            win, text="❓  CENTRAL DE AJUDA",
            font=("Fixedsys", 22), text_color="#00F2FF",
        ).pack(pady=(16, 4))

        ctk.CTkLabel(
            win, text="Selecione um jogo para ver o guia passo a passo:",
            font=("Arial", 13), text_color=("gray40", "#888888"),
        ).pack(pady=(0, 10))

        separador = ctk.CTkFrame(win, height=2, fg_color="#00F2FF")
        separador.pack(fill="x", padx=30, pady=(0, 14))

        # Scroll com os cards de cada jogo
        scroll = ctk.CTkScrollableFrame(win, fg_color=("gray92", "#0d0d0d"))
        scroll.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        for jogo in self.jogos:
            card = ctk.CTkFrame(scroll, fg_color=("gray88", "#1a1a1a"), corner_radius=10)
            card.pack(fill="x", padx=6, pady=6)

            left = ctk.CTkFrame(card, fg_color="transparent", width=60)
            left.pack(side="left", padx=12, pady=10)
            left.pack_propagate(False)

            ctk.CTkLabel(
                left, text=jogo["emoji"],
                font=("Segoe UI Emoji", 28),
            ).pack(expand=True)

            mid = ctk.CTkFrame(card, fg_color="transparent")
            mid.pack(side="left", fill="both", expand=True, pady=10)

            ctk.CTkLabel(
                mid, text=jogo["nome"],
                font=("Fixedsys", 15),
                text_color=jogo["cor"],
            ).pack(anchor="w")

            # Preview de uma linha da descrição
            info = GAME_INFO.get(jogo["id"], {})
            primeira_linha = info.get("descricao", "").split("\n")[2].strip() if info.get("descricao") else ""
            ctk.CTkLabel(
                mid, text=primeira_linha[:60] + ("…" if len(primeira_linha) > 60 else ""),
                font=("Arial", 11), text_color=("gray45", "#777777"),
            ).pack(anchor="w")

            ctk.CTkButton(
                card,
                text="📖 COMO JOGAR",
                fg_color=("#ddeeff", "#1a1a2e"),
                hover_color=("#bbddff", "#16213e"),
                border_color=jogo["cor"],
                border_width=2,
                text_color=jogo["cor"],
                font=("Arial", 11, "bold"),
                width=140, height=38,
                command=lambda j=jogo: self.abrir_como_jogar(j),
            ).pack(side="right", padx=12, pady=10)

        ctk.CTkButton(
            win, text="✕  FECHAR",
            fg_color="transparent", hover_color=("gray75", "#1e1e1e"),
            text_color=("gray50", "#555555"), font=("Arial", 11), height=32,
            command=win.destroy,
        ).pack(pady=(0, 10))

    # ── Cards do catálogo ─────────────────────────────────────────────────────
    def adicionar_item_catalogo(self, jogo):
        card = ctk.CTkFrame(self.scroll_frame, fg_color=("gray85", "#1e1e1e"), height=230)
        card.pack(fill="x", padx=10, pady=10)
        card.grid_propagate(False)

        poster_frame = ctk.CTkFrame(card, width=150, height=210, fg_color=("gray75", "#141414"))
        poster_frame.pack(side="left", padx=15, pady=10)

        img_ref = self.poster_images.get(jogo["id"])
        if img_ref:
            ctk.CTkLabel(poster_frame, text="", image=img_ref).place(
                relx=0.5, rely=0.5, anchor="center"
            )
        else:
            ctk.CTkLabel(poster_frame, text=jogo["emoji"], font=("Arial", 50)).place(
                relx=0.5, rely=0.5, anchor="center"
            )

        info_frame = ctk.CTkFrame(card, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True, padx=10, pady=30)

        ctk.CTkLabel(
            info_frame, text=jogo["nome"],
            font=("Fixedsys", 26), text_color=jogo["cor"],
        ).pack(anchor="w")

        # Breve descrição no card principal
        info = GAME_INFO.get(jogo["id"], {})
        descricao_curta = info.get("descricao", "").split("\n\n")[1][:100] + "…" if info.get("descricao") else ""
        ctk.CTkLabel(
            info_frame, text=descricao_curta,
            font=("Arial", self.tamanho_fonte), text_color=("gray40", "#888888"),
            wraplength=400, justify="left",
        ).pack(anchor="w", pady=(4, 0))

        # Botões
        btns = ctk.CTkFrame(card, fg_color="transparent")
        btns.pack(side="right", padx=25)

        ctk.CTkButton(
            btns,
            text="ℹ️ INFO",
            fg_color="transparent",
            hover_color=("gray75", "#1e1e1e"),
            border_color=jogo["cor"],
            border_width=2,
            text_color=jogo["cor"],
            font=("Arial", 11, "bold"),
            width=100, height=38,
            command=lambda j=jogo: self.mostrar_resumo(j),
        ).pack(pady=(0, 8))

        ctk.CTkButton(
            btns,
            text="▶ JOGAR",
            fg_color=jogo["cor"],
            text_color="#000",
            font=("Arial", 12, "bold"),
            width=100, height=45,
            command=lambda f=jogo["file"]: self.launch(f),
        ).pack()

    # ── Launch ────────────────────────────────────────────────────────────────
    def launch(self, filename):
        try:
            subprocess.Popen(["python", filename, str(self.volume_global)])
        except:
            messagebox.showerror("Erro", f"Falha ao abrir {filename}")


if __name__ == "__main__":
    app = GameHubPro()
    app.mainloop()