tentativas= 0
with open("auth_logs_5000.txt", "r")  as log:
    for linhas in log:
        if "Failed password" in linhas:

           tentativas+= 1

    
           
           print(linhas)

print(f"A quantidade de tentativas de login mal sucedidas foram = {tentativas}")


