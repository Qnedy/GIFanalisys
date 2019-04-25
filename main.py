
with open("teste2.gif", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    data_hex = data.hex()
   

   
    formatoHex = data_hex[:12]

    eGif = ""

    if formatoHex == "474946383961":
       
        eGif = "SIM"
    else:
       
        eGif = "NÃO"

    largura = data_hex[12:16]
  

    maisSig = largura[:2]
    menosSig = largura[2:4]
    hexOk = menosSig + maisSig

    

    larguraOk = int(hexOk,16)
   

    altura = data_hex[16:20]
    
    maisSig2 = altura[:2]
    menosSig2 = altura[2:4]
    hexOk2 = menosSig2 + maisSig2

    alturaOk = int(hexOk2,16)
   

    

    print("IMAGEM GIF:", eGif, "\nLARGURA: ", larguraOk, "px", "\nALTURA: ", alturaOk, "px")


    
    

                    
