#  Downloader de Vídeos

Baixe vídeos do Twitter, Instagram e YouTube direto pelo terminal.

---

##  Aviso Legal

Este projeto é apenas para fins educacionais.
O download de conteúdo protegido por direitos autorais pode violar os Termos de Uso das plataformas.
Use com responsabilidade.

---

##  Requisitos

- Python 3.x
- yt-dlp

---

##  Como usar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Execute
```bash
python main.py
```

---

##  Plataformas suportadas

| Plataforma | Formato | Observação |
|---|---|---|
| Twitter | MP4 | Vídeos públicos |
| Instagram | MP4 | Apenas vídeos públicos |
| YouTube | MP4 / M4A / WEBM | Vídeo ou somente áudio |

---

##  Opções do YouTube

| Opção | Descrição |
|---|---|
| Melhor qualidade | Melhor formato disponível já mesclado |
| Qualidade média | Vídeo em até 360p |
| Menor arquivo | Menor qualidade disponível |
| Somente áudio | Áudio em M4A ou WEBM (sem FFmpeg) |



---

##  Onde ficam os arquivos

Os vídeos são salvos automaticamente na pasta `downloads/` criada na mesma pasta do script.

---

##  Tecnologias utilizadas

- [Python](https://python.org)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
