listaPergunta = ['a) Telefonou para a vítima?', 'b) Esteve no local do crime?', 'c) Mora perto da vítima?', 'd) Devia para a vítima?', 'e) Já trabalhou com a vítima?']
Respostas = []
for i in range(len(listaPergunta)):
    print ('Responda as 5 perguntas: ')
    Respostas.append(input(listaPergunta[i] + ':\n')
    if(Resposta == 2)
        print ('Suspeito')
    elif(Resposta == 3 or Resposta == 4):
        print ('Cúmplice'):
    elif(Resposta == 5):
        print ('Assassino'):
    else:
        print ('Inocente')
