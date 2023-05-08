#print("Aqui iniciarei meu código para realizar o cálculo de média dos alunos! Aguardem!!!")
nota1 = input("""Informe a nota das Atividades.
Utilize ponto (.) para valor decimal.
""")
nota2 = input("""Informe a nota da Prova.
Utilize ponto (.) para valor decimal.
""")
media = float(nota1) * 0.49 + float(nota2) * 0.51
if media >= 5:
    print(f"""Sua média final é: {media}
    Parabéns, você foi aprovado!!!""")
elif media <5:
    print(f"""Sua média final é: {media}
    Se dedique para revisar os conteúdos e realizar o Exame!!!""")
    examefeito = input("""Digite S para sim, se você já realizou o Exame
    Digite N caso ainda não tenha realizado Exame
    """)
if examefeito =="S" or examefeito =="s":
        notaexame = input("Digite sua nota obtida no Exame: ")
        mediafinal = (media + float(notaexame)) / 2
        if mediafinal >= 5:
            print(f"""Sua média com exame é: {mediafinal}
            Parabéns, você foi aprovado no Exame!!!""")
        elif mediafinal <5:
            print(f"""Sua média com exame é: {mediafinal}
            Você deverá realizar a disciplina em Dependência!""")
elif examefeito == "N" or examefeito == "n":
        print("Bons estudos, se dedique que conseguirá um ótimo resultado!")
else:
        print("Você deveria ter digitado S / N")