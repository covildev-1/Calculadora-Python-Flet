def calcular(operador, entrada):
    valor = eval(entrada)

    try:
        match operador:
            case "%":
                valor /= 100
            case "±":
                valor = -valor
    except:
        return "Error"

    a = str(valor).split(".")
    b = ""

    for i in a[-1]:
        if i == "0":
            break
        b += i

    valor = a[0] + ("." + b) if b != "" else a[0]

    return valor
