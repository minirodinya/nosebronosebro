#Programa de tutoriales para San Valentin

import webbrowser


print("Bienvenido a nuestro programa de tutoriales\nESPECIAL SAN VALENTIN")
print("1. Tutorial Nº1\n2. Tutorial Nº2\n3. Tutorial Nº3\n4. Tutorial Nº4\n5. Tutorial Nº5\n6. Salir")

while True:
    
    print("¡ADVERTENCIA EL TUTORIAL Nº5 NO FUNCIONA SI NO TIENES CASCOS!")

    opcion = int(input("Eliga un tutorial (1, 2, 3, 4, 5 o 6): "))
    
    if opcion == 1:
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        webbrowser.open(url)

    elif opcion == 2:
        url = "https://www.instagram.com/p/CGh4a0iASGS/"
        webbrowser.open(url)

    elif opcion == 3:
        url = "https://www.tiktok.com/@vant3lla/video/7454626358887730450?lang=es"
        webbrowser.open(url)

    elif opcion == 4:
        url = "https://x.com/gonregon4/status/913165887200485378"
        webbrowser.open(url)

    elif opcion == 5:
        url = "https://www.tiktok.com/@elizabethhrd4/video/6957911095717727493"
        webbrowser.open(url)

    elif opcion == 6:
        print("Saliendo...")
        break
    
    else:
        print("Opción no válida")