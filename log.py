from pathlib import Path

BASE_DIR = Path (__file__).resolve().parent


arq_logs = BASE_DIR / "logs" / "auth_logs_5000.txt"




tentativas= 0




with open(arq_logs, "r")  as log:
    for linhas in log:
        if "Failed password" in linhas:

           tentativas+= 1

    
           
           print(linhas)

print(f"A quantidade de tentativas de login mal sucedidas foram = {tentativas}")