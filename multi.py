import time
import threading

def fazer_requisicao_web():
    print("Fazendo requisição web...")
    time.sleep(3)
    print("Requisição web concluída")

thread_1 = threading.Thread(target=fazer_requisicao_web)
thread_1.start()