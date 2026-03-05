import flet as ft
from funciones import prefijos 
from funciones import sufijos
from funciones import subcadenas
from funciones import kleene
from funciones import positiva


def main(page: ft.Page):
    page.title = "Práctica 1 - Operaciones sobre Lenguajes"


    #Primer seccion
    Titulo1=ft.Text("Operaciones")
    page.scroll = "auto"

    entrada_de_la_cadena=ft.TextField(label="Ingresa una cadena, por favor:")
    entrada_longitud = ft.TextField(
        label="Longitud máxima (solo para Σ* y Σ+)",
        width=400
    )

    entrada_alfabeto = ft.TextField(
    label="Ingresa un alfabeto, por favor (ej: a,b,c):",
    width=400
)

    



    def accion_prefijos(e):
        texto = entrada_de_la_cadena.value
        lista = prefijos(texto)   # Llamada a mi funcion prefijos
        resultado.value = "\n".join(lista)
    page.update()

    def accion_sufijos(e):
        texto = entrada_de_la_cadena.value
        lista=sufijos(texto)
        resultado.value = "\n".join(lista)
        page.update()

    def accion_subcadenas(e):
        texto = entrada_de_la_cadena.value
        lista=subcadenas(texto)
        resultado.value = "\n".join(lista)
        page.update()

    def accion_kleene(e):
        alfabeto = entrada_alfabeto.value.split(",") #transformar de a,b,c a [a,b,c]
        long_max = int(entrada_longitud.value)
        lista=kleene(alfabeto,long_max)
        lista_mostrar = ["ε" if x == "" else x for x in lista] #asignar los valores
        resultado.value = ",".join(lista_mostrar)
        page.update()

    def accion_positiva(e):
        alfabeto = entrada_alfabeto.value.split(",")
        long_max = int(entrada_longitud.value)
        lista = positiva(alfabeto, long_max)
        resultado.value = "\n".join(lista)
        page.update()

    def guardar_archivo(e):
        contenido = resultado.value

        with open("resultado.txt", "w", encoding="utf-8") as f:
            f.write(contenido)

        resultado.value += "\n\nArchivo guardado como resultado.txt"
        page.update()

    resultado = ft.TextField(
    label="Resultado",
    multiline=True,
    min_lines=8,
    read_only=True,
    width=600
    )

    ##BOTONES
    boton_prefijos = ft.ElevatedButton("Prefijos", on_click=accion_prefijos)
    boton_sufijos = ft.ElevatedButton("Sufijos", on_click=accion_sufijos)
    boton_subcadenas = ft.ElevatedButton("Subcadenas", on_click=accion_subcadenas)
    boton_kleene = ft.ElevatedButton("Σ*", on_click=accion_kleene)
    boton_positiva = ft.ElevatedButton("Σ+", on_click=accion_positiva)
    boton_guardar = ft.ElevatedButton("Guardar en archivo", on_click=guardar_archivo)


## ESTO YA ES PURO DISENO
    botones = ft.Row(
        controls=[
            ft.Column([boton_prefijos, boton_sufijos]),
            ft.Column([boton_subcadenas]),
            ft.Column([boton_kleene, boton_positiva]),
        ],
        spacing=30
    )

    columna_cadena = ft.Column(
    controls=[
        ft.Text("Operaciones sobre cadena"),
        entrada_de_la_cadena,
        boton_prefijos,
        boton_sufijos,
        boton_subcadenas,
    ],
    spacing=10
)

    columna_alfabeto = ft.Column(
    controls=[
        ft.Text("Operaciones sobre alfabeto"),
        entrada_alfabeto,
        entrada_longitud,
        boton_kleene,
        boton_positiva,
    ],
    spacing=10
)
    secciones = ft.Row(
    controls=[columna_cadena, columna_alfabeto],
    spacing=50,
    alignment=ft.MainAxisAlignment.SPACE_AROUND
)
    resultadoc = ft.Row(
    controls=[resultado],
    alignment=ft.MainAxisAlignment.CENTER
)

    page.add(
    secciones,
    resultadoc,
    boton_guardar
    )

ft.app(target=main)