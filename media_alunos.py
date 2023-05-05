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