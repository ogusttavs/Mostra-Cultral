menu = 0
listaRm = []
listaNome = []
listaSerie = []
sair = 0
menu1 = 0
contarHistorias = []
aLinguaDeSinais = []
oMundoDaImaginacao = []
emojis = []
while menu != 3:
    menu = int(input("*****MENU DE OPÇÕES*****\n1-Cadastrar alunos\n2-Fazer inscrições\n3-Sair\n-->"))
    print("************************")
    if menu == 1:
        while menu1 == 0:
            rm = 1
            while rm != 0:
                rm = int(input("Qual o RM do aluno ?\n-->"))
                if rm == 0:
                    break
                elif rm not in listaRm:
                    listaRm.append(rm)
                else:
                    print("Rm ja cadastrado")
                    continue

                nome = input("Qual o nome do aluno ?\n-->")
                listaNome.append(nome)
                while sair != 1:
                    serie = input("Qual a serie do aluno?\n-->")
                    if  serie == '2 ano' or serie == '3 ano' or serie == '4 ano' or serie == '5 ano':
                        listaSerie.append(serie)
                        sair = 1
                    else:
                        print("Serie invalida")
                print("Cadastro efetuado")
                sair = 0
                menu1 = 1
        if menu1 != 0:
            print("Menu indisponivel")




    elif menu == 2:
        rm = int(input("Qual o RM do aluno ?\n-->"))
        if rm in listaRm:
           append = listaRm.index(rm)
           if listaSerie[append] == '2 ano':
               print("******* Oficinas Disponiveis 2º ano *******")
               print("Segunda matutino - Criar e contar histórias")
               print("Quarta matutino - A língua de sinais")
               print("Quarta Vespetino - O mundo da imaginação")
               print("Sexta Vespetino - Criando e recriando com emojis")
               escolha = int(input("Deseja fazer incrição em alguma oficina?\n1-Sim\n2-Não\n-->"))
               if escolha == 2:
                   continue

               elif escolha == 1:
                   quantidadeDeInscriçao = 3
                   print("Você pode participar de 3 oficinas ")

                   while quantidadeDeInscriçao != 0:
                       print("Digite o numero da que deseja:")
                       print("1-Segunda matutino - Criar e contar histórias")
                       print("2-Quarta matutino - A língua de sinais")
                       print("3-Quarta Vespetino - O mundo da imaginação")
                       print("4-Sexta Vespetino - Criando e recriando com emojis")
                       escolha2 = int(input("-->"))
                       if escolha2 == 1:
                           if rm not in contarHistorias:
                               contarHistorias.append(rm)
                               quantidadeDeInscriçao = quantidadeDeInscriçao - 1
                               print("Cadastrado com sucesso!!")
                               print("Você tem mais",quantidadeDeInscriçao,"inscrições disponiveis")
                               if quantidadeDeInscriçao - 1 > 0 :
                                   print("Desenha se inscrever em mais algm curso?")
                                   print("Digite\n1-Sim\n2-Não")
                                   escolha3 = int(input("-->"))

                                   if escolha3 == 2:
                                       continue
                           else:print("*****Você ja ta cadastrado nesse curso*****")
                       elif escolha2 == 2:
                           if rm not in aLinguaDeSinais:
                               aLinguaDeSinais.append(rm)
                               quantidadeDeInscriçao = quantidadeDeInscriçao - 1
                               print("Cadastrado com sucesso!!")
                               print("Você tem mais", quantidadeDeInscriçao, "inscrições disponiveis")
                               if quantidadeDeInscriçao - 1 > 0:
                                   print("Desenha se inscrever em mais algm curso?")
                                   print("Digite\n1-Sim\n2-Não")
                                   escolha3 = int(input("-->"))
                           else:print("*****Você ja ta cadastrado nesse curso*****")


                       elif escolha2 == 3:
                           if rm not in oMundoDaImaginacao:
                               oMundoDaImaginacao.append(rm)
                               quantidadeDeInscriçao = quantidadeDeInscriçao - 1
                               print("Cadastrado com sucesso!!")
                               print("Você tem mais", quantidadeDeInscriçao, "inscrições disponiveis")
                               if quantidadeDeInscriçao - 1 > 0:
                                   print("Desenha se inscrever em mais algm curso?")
                                   print("Digite\n1-Sim\n2-Não")
                                   escolha3 = int(input("-->"))
                           else: print("*****Você ja ta cadastrado nesse curso*****")

                       elif escolha2 == 4:
                           if rm not in emojis:
                               emojis.append(rm)
                               quantidadeDeInscriçao = quantidadeDeInscriçao - 1
                               print("Cadastrado com sucesso!!")
                               print("Você tem mais", quantidadeDeInscriçao, "inscrições disponiveis")
                               if quantidadeDeInscriçao - 1 > 0:
                                   print("Desenha se inscrever em mais algm curso?")
                                   print("Digite\n1-Sim\n2-Não")
                                   escolha3 = int(input("-->"))


                           else: print("*****Você ja ta cadastrado nesse curso*****")








           elif listaSerie[append] == '3 ano':
               print("******* Oficinas Disponiveis 3º ano *******")
               print("Segunda matutino - Criar e contar histórias")
               print("Terça Matutino - Teatro: Luz, Câmera e Ação")
               print("Quarta matutino - A língua de sinais")
               print("Terça Vespetino - O corpo fala")
               escolha = int(input("Deseja fazer incrição em alguma oficina?\n1-Sim\n2-Não\n-->"))
               if escolha == 2:
                   continue

               elif escolha == 1:
                   quantidadeDeInscriçao = 3
                   print("Você pode participar de 3 oficinas ")

                   while quantidadeDeInscriçao != 0:
                       print("Digite o numero da que deseja:")
                       print("1- Segunda matutino - Criar e contar histórias")
                       print("2- Terça Matutino - Teatro: Luz, Câmera e Ação")
                       print("3- Quarta matutino - A língua de sinais")
                       print("4- Terça Vespetino - O corpo fala")
                       escolha2 = int(input("-->"))
                       if escolha2 == 1:
                           if rm not in contarHistorias:
                               contarHistorias.append(rm)
                               quantidadeDeInscriçao = quantidadeDeInscriçao - 1
                               print("Cadastrado com sucesso!!")
                               print("Você tem mais", quantidadeDeInscriçao, "inscrições disponiveis")
                               if quantidadeDeInscriçao - 1 > 0:
                                   print("Desenha se inscrever em mais algm curso?")
                                   print("Digite\n1-Sim\n2-Não")
                                   escolha3 = int(input("-->"))

                                   if escolha3 == 2:
                                       continue
                           else:
                               print("*****Você ja ta cadastrado nesse curso*****")
                       elif escolha2 == 2:
                           if rm not in aLinguaDeSinais:
                               aLinguaDeSinais.append(rm)
                               quantidadeDeInscriçao = quantidadeDeInscriçao - 1
                               print("Cadastrado com sucesso!!")
                               print("Você tem mais", quantidadeDeInscriçao, "inscrições disponiveis")
                               if quantidadeDeInscriçao - 1 > 0:
                                   print("Desenha se inscrever em mais algm curso?")
                                   print("Digite\n1-Sim\n2-Não")
                                   escolha3 = int(input("-->"))
                           else:
                               print("*****Você ja ta cadastrado nesse curso*****")


                       elif escolha2 == 3:
                           if rm not in oMundoDaImaginacao:
                               oMundoDaImaginacao.append(rm)
                               quantidadeDeInscriçao = quantidadeDeInscriçao - 1
                               print("Cadastrado com sucesso!!")
                               print("Você tem mais", quantidadeDeInscriçao, "inscrições disponiveis")
                               if quantidadeDeInscriçao - 1 > 0:
                                   print("Desenha se inscrever em mais algm curso?")
                                   print("Digite\n1-Sim\n2-Não")
                                   escolha3 = int(input("-->"))
                           else:
                               print("*****Você ja ta cadastrado nesse curso*****")

                       elif escolha2 == 4:
                           if rm not in emojis:
                               emojis.append(rm)
                               quantidadeDeInscriçao = quantidadeDeInscriçao - 1
                               print("Cadastrado com sucesso!!")
                               print("Você tem mais", quantidadeDeInscriçao, "inscrições disponiveis")
                               if quantidadeDeInscriçao - 1 > 0:
                                   print("Desenha se inscrever em mais algm curso?")
                                   print("Digite\n1-Sim\n2-Não")
                                   escolha3 = int(input("-->"))


                           else:
                               print("*****Você ja ta cadastrado nesse curso*****")

           elif listaSerie[append] == '4 ano':
               print("******* Oficinas Disponiveis 4º ano *******")
               print("Terça Matutino - Teatro: Luz, Câmera e Ação")
               print("Quarta Matutino - A língua de sinais")
               print("Quinta Matutino - Expressão Artística")
               print("Segunda Vespertino - Leitura dramática")

           elif listaSerie[append] == '5 ano':
               print("******* Oficinas Disponiveis 5º ano *******")
               print("Quarta matutino - A língua de sinais")
               print("Quinta Matutino - Expressão Artística")
               print("Sexta Matutino - Soletrando")

        else:print("Aluno não cadastrado. Favor procurar a coordenação do Fundamental I")