nome = (input("Qual é o seu nome?")).strip().lower()
idade = int(input("Qual é a sua idade?"))

if idade >= 18:
    aluno = int(input("Se você é estudante de Python digite 1. Se você não é estudante de Python digite 2."))
    entradas = int(input("Se você deseja a entrada padrão digite 1. Caso contrário digite 2."))
    if (aluno == 1) and (entradas == 1):
        print("Você pode adquirir a entrada padrão e terá um desconto de 50%")
    elif (aluno == 1) and (entradas == 2 ):
        print ("Você pode adquirir a entrada VIP e terá um desconto de 50%")
    elif (aluno == 2) and (entradas == 1 ):
        print ("Você pode adquirir a entrada padrão!")
    elif (aluno == 2) and (entradas == 2):
        print ("Você pode adquirir a entrada VIP!")
else:
    falta = (idade - 18)
    print("Você ainda não pode participar do clube de festas. Faltam", falta, "anos para você poder participar")