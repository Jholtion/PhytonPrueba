pal = input("Digite a palabra: ")
pal2= pal[::-1]
if(pal == pal2):
    print("Es un palindromo")
else:
    print("No es un palindromo")
bool = True

for i in range(len(pal) // 2):  
    if pal[i] != pal[len(pal) - i - 1]: 
        es_palindromo = False
        break
     
if bool:
    print("Es un palindromo")
else:
    print("No es un palindromo")