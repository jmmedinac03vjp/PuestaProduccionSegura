# main.py
def main():
    comando = input("Introduce un comando de Python: ")
    eval(comando)  # ⚠️ Uso peligroso de eval()

if __name__ == "__main__":
    main()
