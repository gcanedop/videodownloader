import yt_dlp
import os

def criar_pasta():
    if not os.path.exists('./downloads'):
        os.makedirs('./downloads')
        print("Pasta 'downloads' criada!")

def baixar_video(url, opcoes):
    criar_pasta()

    print(f"\nBaixando de: {url}")
    print("Aguarde...\n")

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])

        print("\nDownload concluído! Arquivo salvo na pasta 'downloads'.")

    except Exception as erro:
        print(f"\nErro ao baixar: {erro}")

def opcoes_twitter():
    return {
        'outtmpl': './downloads/%(uploader)s_%(id)s.%(ext)s',
        'format': 'best',  
    }

def opcoes_instagram():
    return {
        'outtmpl': './downloads/%(uploader)s_%(id)s.%(ext)s',
        'format': 'best',
    }

def opcoes_youtube():
    print("\nEscolha a qualidade:")
    print("  [1] Melhor qualidade disponível")
    print("  [2] Qualidade média (360p)")
    print("  [3] Menor arquivo possível")
    print("  [4] Arquivo em .m4a (somente áudio)") # não toca no spotify, mas toca no app nativo de música do windows
    escolha = input("\nDigite o número da opção: ").strip()

    if escolha == '1':
        return {
            'outtmpl': './downloads/%(title)s.%(ext)s',
            'format': 'best',  # melhor formato já mesclado
        }
    elif escolha == '2':
        return {
            'outtmpl': './downloads/%(title)s.%(ext)s',
            'format': 'best[height<=360]/best',
        }
    elif escolha == '3':
        return {
            'outtmpl': './downloads/%(title)s.%(ext)s',
            'format': 'worst',
        }
    elif escolha == '4':
        return {
            'outtmpl': './downloads/%(title)s.%(ext)s',
            # baixa o melhor áudio disponível (m4a)
            'format': 'bestaudio/best',
        }
    else:
        print("Opção inválida, usando melhor qualidade.")
        return opcoes_youtube()

def escolher_plataforma():
    print("Escolha a plataforma:")
    print("  [1] Twitter")
    print("  [2] Instagram")
    print("  [3] YouTube")
    print("  [4] Sair")

    opcao = input("\nDigite o número da opção: ").strip()
    return opcao

if __name__ == "__main__":
    print("=== Downloader de Vídeos ===\n")

    while True:
        opcao = escolher_plataforma()

        if opcao == '1':
            url = input("\nCole a URL do tweet: ").strip()
            if url == "":
                print("Nenhuma URL informada. Tente novamente.")
                continue
            baixar_video(url, opcoes_twitter())

        elif opcao == '2':
            print("\n  Atenção: vídeos privados precisam de login.")
            url = input("\nCole a URL do Instagram: ").strip()
            if url == "":
                print("Nenhuma URL informada. Tente novamente.")
                continue
            baixar_video(url, opcoes_instagram())

        elif opcao == '3':
            url = input("\nCole a URL do YouTube: ").strip()
            if url == "":
                print("Nenhuma URL informada. Tente novamente.")
                continue
            baixar_video(url, opcoes_youtube())

        elif opcao == '4':
            print("\nEncerrando o programa. Até mais!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")
            continue

        print("\nDeseja baixar outro vídeo?")
        resposta = input("Digite 's' para sim ou 'n' para não: ").strip().lower()

        if resposta == 'n':
            print("\nEncerrando o programa. Até mais!")
            break
        elif resposta == 's':
            print("\n" + "=" * 40 + "\n") # separador visual
        else:
            print("\nResposta inválida. Encerrando o programa.")
            break # sai do loop por segurança