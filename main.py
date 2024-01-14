import flet as ft
from presets import paleta_de_cor as pallet
from presets import btns
from functions import calcular


def main(page: ft.Page):
    page.window_width, page. window_height = 250, 380
    page.window_always_on_top, page.window_resizable = True, False
    page.bgcolor = pallet["cinza_escuro"]
    page.title = "Calculadora Flet"

    def select(e):
        valor_atual = entrada_usuario.value
        valor = e.control.content.value

        if valor.isdigit():
            valor_atual += valor
        elif valor == "AC":
            resultado.value = "0"
        else:
            if valor_atual and valor_atual[-1] in ("/", "*", "-", "+", "."):
                valor_atual = valor_atual[:-1]

            valor_atual += valor

            if valor[-1] in ("=", "%", "±"):
                print(valor_atual, valor[-1])
                valor = calcular(operador=valor, entrada=valor_atual[:-1])
                resultado.value = valor

        entrada_usuario.value = valor_atual if valor != "AC" and valor_atual[-1] not in ("=", "%", "±") else ""
        entrada_usuario.update()
        resultado.update()

    resultado = ft.Text(value="0", color=pallet["branco"], size=28)
    display_resultado = ft.Row(width=250, controls=[resultado],
                               height="content",
                               alignment="end")

    entrada_usuario = ft.Text(value="",
                              color=pallet["verde"])
    display_entrada = ft.Row(width=250,
                     height=20,
                     controls=[entrada_usuario],
                     alignment="end")
    botoes = [
        ft.Container(
            content=ft.Text(value=bts["operador"], color=bts["cor_fonte"]),
            bgcolor=bts["cor_fundo"],
            width=46,
            height=bts["height"],
            border_radius=25,
            alignment=ft.alignment.center,
            on_click=select,
            ink=True
            ) for bts in btns
    ]
    teclado = ft.Column(height=250, wrap=True, controls=botoes, alignment="start")

    page.add(display_resultado, display_entrada, teclado)


ft.app(target=main, assets_dir="assets")
