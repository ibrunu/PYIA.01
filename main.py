def main():
    frutas_lista = ["Morango", "Cereja", "Amora", "Jabuticaba", "Pitanga", "Mirtilo"]
    
    frutas_tupla = tuple(frutas_lista)
    
    print("Conteúdo da tupla de frutas:")
    for fruta in frutas_tupla:
        print(fruta)

if __name__ == "__main__":
    main()
