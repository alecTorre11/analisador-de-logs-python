from  pathlib import Path
caminho_arquivo = Path (  "C:Users\alecsam.torres\Documents\programação\Python\projeto\analisador-de-logs-python\logs")




tentativas= 0
with open( caminho_arquivo, "r")  as log:
    for linhas in log:
        if "Failed password" in linhas:

           tentativas+= 1

    
           
           print(linhas)

print(f"A quantidade de tentativas de login mal sucedidas foram = {tentativas}")


