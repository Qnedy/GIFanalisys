
with open("teste2.gif", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    data_hex = data.hex()
    print(data_hex)

    print(data_hex[:12])
    formatoHex = data_hex[:12]

    eGif = ""

    if formatoHex == "474946383961":
        print("é uma imagem no formato GIF")
        eGif = "SIM"
    else:
        print("não é uma imagem no formato GIF")
        eGif = "NÃO"

    largura = data_hex[12:16]
    print(largura[:2])
    print(largura[2:4])

    maisSig = largura[:2]
    menosSig = largura[2:4]
    hexOk = menosSig + maisSig

    print(hexOk)

    larguraOk = int(hexOk,16)
    print(larguraOk)

    altura = data_hex[16:20]
    print(altura[:2])
    print(altura[2:4])

    maisSig2 = altura[:2]
    menosSig2 = altura[2:4]
    hexOk2 = menosSig2 + maisSig2

    alturaOk = int(hexOk2,16)
    print(alturaOk)

    #saida = "IMAGEM GIF:", eGif, "\nLARGURA: ", larguraOk, "\n", "ALTURA: ", alturaOk

    print("IMAGEM GIF:", eGif, "\nLARGURA: ", larguraOk, "px", "\nALTURA: ", alturaOk, "px")


    
    

                    
