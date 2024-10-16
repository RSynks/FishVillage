#------FishVillage------
#--------INDICE--------
#LINHA 31 - VARIÁVEIS DO JOGO
#LINHA 52 – LISTA DE EQUIPAMENTOS BÁSICOS DISPONÍVEIS NA LOJA
#LINHA 71 – ALGORITMO PARA DETERMINAR AS CHANCES DE PESCA
#LINHA 96 – LISTA DE DIÁLOGO COM O SENHOR DESCONHECIDO DA PRAIA
#LINHA 109 – LISTA DE DIÁLOGO COM O SENHOR DESCONHECIDO DO RIO
#LINHA 122 – LISTA DE DIÁLOGO COM A DONA DA LOJA
#LINHA 135 – LISTA ALEATÓRIA DE INTERAÇÕES DESCONTRAÍDAS COM A DONA DA LOJA
#LINHA 208 – FUNÇÃO PARA MODIFICAR O NOME DOS NPC’S APÓS APRESENTAÇÃO
#LINHA 216 – FUNÇÃO PARA MOSTRAR OS ITENS DA LOJA
#LINHA 225 – FUNÇÃO PARA MOSTRAR OS ITENS EQUIPADOS
#LINHA 230 – FUNÇÃO PARA ADICIONAR OS PEIXES PESCADOS A BOLSA
#LINHA 238 – FUNÇÃO ATUALIZA O NÍVEL DE EXPERIÊNCIA APÓS CADA TENTATIVA DE PESCA
#LINHA 243 – FUNÇÃO PARA VERIFICAR O NÍVEL DE EXPERIÊNCIA E DETERMINAR O NÍVEL DO JOGADOR
#LINHA 269 – FUNÇÃO PARA ASSOCIAR PREÇO A CADA TIPO DE PEIXE
#LINHA 282 – FUNÇÃO PARA CALCULAR O VALOR DE TODOS OS PEIXES NA BOLSA
#LINHA 288 – FUNÇÃO PARA MOSTRAR O PROGRESSO ATUALIZADO DO JOGADOR
#LINHA 306 – FUNÇÃO PARA VERIFICAR SE A BOLSA ESTÁ CHEIA OU O ESPAÇO DISPONÍVEL
#LINHA 312 – FUNÇÃO PARA GERAR UM NUMERO ALEATÓRIO ENTRE 1 E 100
#LINHA 332 – INICIO DO JOGO, APRESENTAÇÃO DO MENU PRIMÁRIO E LÓGICA DOS MENUS SECUNDÁRIOS
#LINHA 343 – LOGICA DE REPETIÇÃO E NAVEGAÇÃO ENTRE OS NÍVEIS DE MENUS DO JOGO
#LINHA 349 – LOGICA DOS RECURSOS DISPONÍVEIS NA CASA
#LINHA 453 – LOGICA DOS RECURSOS DISPONÍVEIS NA LOJA
#LINHA 695 – LOGICA DOS RECURSOS DISPONÍVEIS NO RIO
#LINHA 887 – LOGICA DOS RECURSOS DISPONÍVEIS NA PRAIA
#LINHA 1075 – APRESENTAÇÃO DOS CRÉDITOS CASO O JOGADOR RESOLVA SAIR DO JOGO

#---------inicio da declaracao de variaveis, funcoes, importacao de biblioteca, listas, matrizes e afins

aquario=[] #onde player poderá guardar os peixes pescados, limite dessa lista deverá ser 5 slots
limaqua=5 #variavel que define o limite do aquario
dinheiro=0 #quantidade de dinheiro inicial do jogador, em teste está 10k, in game iniciará com 0
bolsa=[] #bolsa para receber os itens coletados, limite dela é a variavel {limite=3}
bequi=0 #bonus de equipamentos equipados
bequip=0 #bonus de equipamento geral do personagem, é a soma do bequi+fbequi
fbequi=0 #bonus por nivel do personagem
energia=100 #quantidade de energia do personagem pra executar acoes no jogo
fadiga=10 #valor a ser subtraido da energia apos ações dentro do game, no futuro inserir perda de 10 ao sair da cidade, para retornar a cidade nao gastara energia
tedio=0 #variavel pra limitar a açao de nadar nos ambientes rio e mar
dia=1 #variavel demonstrar tempo de jogo
nivel=1 #variavel que expressa o nivel do personagem
limite=3 #limite mochila
exp=0 #variavel da experiencia do jogador, nivel está em funcao da exp
loja=[["FisherHat",1500],["FisherRobe",500],["Pro-Rod",2000],["RubberGalocha",1200],["FisherBag",1000]] #matriz contendo os itens presentes na loja e seus respectivos precos
ehead=['Nada'] #lista mostrando item equipado na cabeça
echest=['Básica'] #lista mostrando roupa equipada
etool=['Amador Rod'] #lista mostrando ferramenta equipada
eboot=['Havaianas'] #lista mostrando calçado equipado
ebag=['Estudantil'] #lista mostrando mochila equipada

equipamentos=[["Cabeça",ehead],["Vestimenta",echest],["Ferramenta",etool],["Botas",eboot],["Mochila",ebag]] #matriz que apresenta os itens equipados, dessa forma fica melhor expressao visual
c1=0 #variavel pra checar se o player já possui o chapeu da loja comprado/equipado
c2=0 #variavel para checar se o player ja possui roupa da loja comprada/equipada
c3=0 #variavel pra checar se o player ja possui a ferramenta da loja comprada/equipada
c4=0 #variavel pra checar se o player ja possui a bota da loja comprada/equipada
c5=0 #variavel rpa cehcar se o player ja possui a mochila da loja comprada/equipada

cpyi=0 #variavel pra checar qual sexo do peixe raro rio o player vai receber; carpa ying
cpya=0 #variavel pra checar qual sexo do peixe raro rio o player vai receber; carpa yang

#aqui iremos definir as chances de min e max das pescadas em variavel invés de constantes
#ideia é fazer falha = negativo, conforme bonus aumenta, isso fará com que falha tende a zero conforme progresso do player
#memsa ideia segue pra peixe pequeno, porem, nao tender a zero mas fazer com que chance seja pequena
#se bonus for 50% (nivel 10)
#falha-49,5;
#30,6~35
#10,36~45
#5;46~100

fr=[1,55] #range inicial de falha no rio
sr=[(fr[1]+1),85] #range inicial de chance smallfish river
mr=[(sr[1]+1),95] #range inicial de chance medfish river
lr=[(mr[1]+1),100] #range inicial de chance largfish river
fs=[1,80] #range inicial falha sea
ss=[(fs[1]+1),90] #range inicial de chance smallfish sea
ms=[(ss[1]+1),98] #range inicial de chance medfish sea
ls=[(ms[1]+1),100] #range inicial de chance largfish sea

#FR=falha rio mnfr=1; mxfr=55 (mnfr-bequip)~(mxfr-bequip) mn=minimo; mx=maximo
#SR=small rio ((mxfr+1)-bequip)~(mxsr85-bequip) // range min e max da falha segue para negativo conforme bonus geral aumenta
#MR=medio rio ((mxsr+1)-bequip)~(mxmr-bequip)   // range min e max small fish permanece constante e segue para negativo
#LR=large rio ((mxmr+1)-bequip)~(mxlr-bequip)   // apenas range min large fish cai, fazendo com que a chance aumente conforme bonus geral aumenta
#FS=falha mar (mnfs-bequip)~(mxfs-bequip)       // range min e max falha segue apra negativo conforme bonus geral aumenta
#SS=small mar ((mxfs+1)-bequip)~(mxss-bequip)   // range min e max small fish se desloca para esquerda tendendo ao negativo
#MS=medio mar ((mxss+1)-bequip)~(mnls-bequip)   // range min e max med fish se desloca para esquerda tendendo ao negativo
#LS=large mar ((mnls+1)-bequip)~(mxls)          // apenas range min se desloca a esquerda, aumentando a chance

#vide exemplo peixe grande
#range min começa em 98; max 100
#conforme bonus, min 95~100; 90~100; 85~100; 80~100; 72~100
#mesma lógica segue os demais:
#falha 1~55; -9~45; -19~35; -29~25; -39~15....
#como dado gera numeros positivos entre 1 a 100, neste caso (-39~15) só existe 15% de chance de falhar!

srtorufin=["-Parece ser um belo dia pra pescar, não acha?",#só por selecionar a opção dele
           "-Ah! que falta de educação minha... Me desculpe, eu me chamo Torufin, muito prazer!", #opcao qual é seu nome
           "-Hunn.... Dica?.. Vejamos... Se você é iniciante eu recomendo começar no rio, sempre achei mais fácil pegar peixes no rio", #tem alguma dica sobre pesca?
           "-Aaah... Minha esposa ama peixes do mar, todos os dias venho pescar nosso almoço...",
           "-A muito tempo atrás... Eu e minha esposa estavamos passeando por aqui e ela jura ter visto um polvo azul..",
           "-Parece loucura né? polvo azul... Queria ter a sorte de vê-lo!",
           "-dizem que a tinta dele faz bem para pele e o cozido é de dar água na boca!",
           "-se um dia você o encontrar eu posso te oferecer meu macacão profissional em troca",
           "-ele pode parecer meio velho mas por algum motivo atrai os peixes.",
           "-MEU DEUS!! realmente existe o polvo azul!! quer trocar pelo meu macacão profissional?",
           "-Fico muito agradecido!! boa sorte com a pesca, de agora em diante vou passar mais tempo com minha esposa."
           ]#vai ficar na praia

srjin=["-O som da água... do vento.. das folhas das árvores é tão relaxante! você não acha?",
       "-Muito prazer! meu nome é Jin, quase sempre venho aqui.",
       "-Uma dica?!.... Hun.. deixe me ver...",
       "-Sempre achei quase impossível conseguir pescar peixes no mar, fique por aqui que você vai se divertir mais!",
       "-Certa vez estava por aqui e avistei um casal de peixes nadando em circulos",
       "-Dizem que neste rio habitam peixes muito raros que equilibram as forças naturais",
       "-se você me trouxer um casal deles eu lhe darei minhas botas",
       "-Não se engane pela aparência, com elas você vai se sentir como uma árvore de raízes longas e",
       "-profundas, como uma âncora na terra! elas sempre compensaram minha falta de força HaHaHa!!...",
       "-Waaaaaaah! você realmente encontrou o casal de carpas raras!! quer trocar pelas minhas botas??",
       "-Muito obrigado!! vou cuidar muito bem deles. Não seria lindo se esse rio tivesse vários desses?.."
       ]#vai ficar no rio

srtajuliana=["-Olá! seja bem-vindo(a), sou Juliana a dona da loja.",
             "-Seja bem-vindo(a) o que deseja?",
             "-O FisherHat é perfeito se deseja permanecer horas pescando, ele reduz seu cansaço em 5 e aumenta em 5 suas chances de pesca.",
             "-FisherRobe é uma ótima escolha, além de estiloso ele aumenta em 5 suas chances de pesca.",
             "-Pro-Rod é perfeita se quiser se tornar um ótimo pescador, ela aumenta em 12 sua chance de pesca.",
             "-A RubberGalocha... Eu particularmente amo esse nome kkkkk ela é uma bota que mantém seus pés firmes no chão, aumenta em 10 suas chances de pesca.",
             "-FisherBag é uma mochila profissional para pescadores, dentro dela há compartimentos perfeitos para encaixar tudo que quiser!",
             "-arrisco dizer que ela caberia quase o triplo de coisas que a estudantil...",
             "-Agradeço pela preferencia! volte sempre e boa sorte na pescaria!"
             ]
#A variável "srtajuliana",trata-se de um 'npc'inserido no ambiente loja,sua função é trazer informações ao jogador,também há um diferencial,já que a mesma faz piadas a cada
#diálogo,que são sorteados a partir da lista abaixo:

piadinhasjuli=["-O que uma impressora disse para a outra?",#0
               "-Essa folha é sua ou é impressão minha?",#1
               "-Kakakkaj, pode admitir... Essa foi boa! kkkk",#2
               "-O que a esfera disse para o cubo?",#3
               "-Deixa de ser quadrado! kkkkk",#4
               "-Kakaka eu sou incrível",#5
               "-O que é, o que é..? Quanto mais se tira mais se aumenta?",#6
               "-O buraco! kkkkk",#7
               "-Kakakakak eu vou morrer de tanto rir!",#8
               "-O que são vários pontinhos amarelos na parede?",#9
               "-Fandangos alpinistas!",#10
               "-heuehheheh",#11
               "-O que é,o que é? que se alimenta de éguas?",#12
               "-O papa-léguas! pluplu bibip!-",#13
               "-Kakaka eu sou demais!",#14
               "-Antes de mais nada..."
              ]

#RubberGalocha=+10bequi // RootsBoots=20bequi; fadiga deslocamento=0; receberá após entrega do casal de carpa
#FishRobe=+5bequi
#FisherHat=+5bequi and fadiga=5; FishTafary reduz a fadiga ao pescar bigfish de 30 para 15; medfish de 20 para 10, smalfish permacenecera sempre 5
#ProRod=+12bequi
#FisherBag +4 limite
#total bequi=+32bequi

#valor de bonus do personagem = valor de bonus equip + valor de bonus nivel
#bequip=bequi+fzbequi(nivel,fbequi)

import random #importando biblioteca pra criar a funcao que gera numeros aleatorios

jnam=0 #variavel que altera abordagem npc dependendo da interação do jogador
tnam=0 #variavel que altera abordagem do npc dependendo da interação do jogador
junam=0 #variavel que altera abordagem do npc dependendo da interação do jogador
julyidk=0 #variavel que altera a abordagem do npc dependendo da interação do jogador
inforareriver=0 #variavel que libera a opcao de troca por item lendário
inforaresea=0 #variavel que libera a opcao de troca por item lendário

namejuliana="Juliana" #nome fixo a npc da loja
namejinidk="Senhor desconhecido do rio" #definindo nome do npc quando nao nos apresentamos
nametoruidk="Senhor desconhecido da praia" #definindo nome do npc quando nao nos apresentamos

#funcoes:

def fmenuplacefish(npcstatus,namenpc):#função que disponibiliza o"menu","river","and","If",de acordo com os eventos ocorridos
  if(npcstatus==0):
    return["Pescar","Nadar",namenpc]

  elif(npcstatus==1):
    return["Pescar","Nadar",namenpc]

  else:
    return["Pescar","Nadar"]

def removeritem(index,recip,vvenda):#index=opção;recip=bolsa(origem);vvenda=preço por unidade
  if(index>len(recip)):
    print("OPÇÃO INVÁLIDA!")
  else:
    index-=1
    print(f"Você recebeu {vvenda} moedas pelo{recip[index]}vendido")
    del recip[index]
    print(recip)

def transfere(index,recip,recip2):#recip1 é a lista origem e recip2 é a lista destino
  if(index>len(recip)):
    print("OPÇÃO INVÁLIDA!")
  else:
    index-=1
    recip2.append(recip[index])
    print(f"Você moveu{recip[index]}.")
    del recip[index]
    print(recip)
    print(recip2)

def namenpc(n):#Função que deve renomear o npc Jim,após a apresentação
  if(n==0):
    return "Senhor Jin"
  elif(n==1):
    return "Senhor Torufin"
  else:
    return "Juliana"

def showloja():#funcao pra printar os itens da loja
  print("---Nome--- : ---Preço---")
  for l in range(len(loja)):
    for c in range(1):
      print(l+1,"-",loja[l][c],":",loja[l][c+1])

  print(f"9 - Player Status")
  print(f"0 - Sair")

def showequip():#funcao pra printar os itens equipados
  for l in range(4):
    for c in range(1):
      print(equipamentos[l][c],":",equipamentos[l][c+1])

def increaseinv(bolsa,limite,peixe):#funcao pra adicionar o pescado a bolsa
  if len(bolsa)<limite:
    bolsa.append(peixe)
    print("Você enviou ",peixe," para sua bolsa")
  else:
    print("Sua bolsa esta cheia, o que ganhou foi perdido..")
  return bolsa

def subxp(expz,exp):#funcao adiciona xp após pescar peixes
  exp+=expz
  print(exp)
  return exp

def fzbequi(fnivel,fbequi): #funcao que verifica seu nivel e define o bonus por nivel
  if(fnivel==1): fbequi=0
  elif(fnivel==2): fbequi=2
  elif(fnivel==3): fbequi=4
  elif(fnivel==4): fbequi=6
  elif(fnivel==5): fbequi=8
  elif(fnivel==6): fbequi=10
  elif(fnivel==7): fbequi=12
  elif(fnivel==8): fbequi=14
  elif(fnivel==9): fbequi=20
  elif(fnivel==10): fbequi=50
  return fbequi

def fnivel(xp,nivel):#funcao que interpreta a xp atual e define seu nivel atual
  if(xp<=50): nivel=1
  elif(50<xp<=100): nivel=2
  elif(100<xp<=200): nivel=3
  elif(200<xp<=400): nivel=4
  elif(400<xp<=800): nivel=5
  elif(800<xp<=1600): nivel=6
  elif(1600<xp<=3200): nivel=7
  elif(3200<xp<=6000): nivel=8
  elif(6000<xp<=10000): nivel=9
  elif(10000<xp): nivel=10
  return nivel

def valorvenda(npeixe):#funcao que expressa o valor de cada peixe presente no game
  if(npeixe=="Lambari"): vdinheiro=5
  elif(npeixe=="Anchova"): vdinheiro=10
  elif(npeixe=="Tilápia"): vdinheiro=20
  elif(npeixe=="Corvina"): vdinheiro=40
  elif(npeixe=="Traira"): vdinheiro=50
  elif(npeixe=="Tubarão"): vdinheiro=100
  elif(npeixe=="Carpa Ying"): vdinheiro=200#falta implementar
  elif(npeixe=="Carpa Yang"): vdinheiro=200#falta implementar
  elif(npeixe=="Kralamor"): vdinheiro=300#falta implementar, FishTafary
  else: vdinheiro=0
  return vdinheiro #a funcao recebe string nome peixe, me devolve vdinheiro=preço do peixe

def vvtotal():#calculo da loja de todos os peixes da bag
  vtotal=0
  for l in range(len(bolsa)):
    vtotal+=valorvenda(bolsa[l])
  return vtotal

def pstatus():#funcao para mostrar o playerstatus
  print("----------")
  print("Player:",nomeplayer)
  print("Nível:",nivel)
  print("Experiencia:", exp)
  print("Bonus:+", bequip,"% chance sucesso")
  print("Dia:",dia)
  print("Moedas:",dinheiro)
  print("Energia:",energia)
  print("")
  showequip()
  print("")
  print("Bolsa:")
  print(bolsa)
  spacebag()
  print("----------")
  print("")

def spacebag(): #funcao que lê e imprime se a bolsa esta cheia, ou quantos espaços ainda tem disponivel
  if(len(bolsa)==limite):
    print("Bolsa cheia")
  elif(len(bolsa)<limite):
    print(f"Restam {limite-len(bolsa)} espaços na bolsa")

def prob():#funcao que gera numeros entre 1 a 100, simula as chances
  stnum=random.randint(1,100)
  return stnum

def displaymenu(menu,opt1,opt2):#automatizacao dos menus sem necessidade de milhoes de print
  for i,l in enumerate(menu):
    i+=1
    print(f"{i} - {l}") #os "f..." dentro do print serve pra colocar variaveis sem precisar fechar as aspas
  print(f"9 - {opt1}") #manter sempre padrão 9 como player status (com excessão da loja na parte de "vender tudo")
  print(f"0 - {opt2}") #manter sempre padrão 0 como voltar/sair...
#---------fim da declaracao de variaveis, funcoes, importacao de biblioteca, listas, matrizes e afins
#-----------------------------start do jogo-----------------------------------------------------------------------------------
print("---FishVillage---") #nome do game
nomeplayer=str(input("Insira o nome do jogador: ")) #input nome do jogador

#respostas aos dialogos com npcs
asknpcr=[f"É verdade! aqui é bem bonito.. Prazer em conhecê-lo, me chamo {nomeplayer}.","Você teria alguma dica sobre pescaria?","Conversar","Tenho uma surpresa...."] #frases resposta npc rio
asknpcs=[f"Com um pouco de sorte ficará ainda melhor!.. Prazer em conhecê-lo, me chamo {nomeplayer}.","Você teria alguma dica sobre pescaria?","Conversar","Tenho uma surpresa..."] #frases respostas npc mar

#listas contendo os menus dos locais
menucity=["Casa","Loja","Rio","Praia"] #todas opções presentes no menu "vila"
menuhouse=["Dormir","Aquário"] #todas opções presentes no menu casa
menushop=["Comprar","Vender","Informações"] #todas opcoes presentes no menu loja
menushop2=["Comprar","Vender","Informações","Dar ouvidos.."]
menujin=[asknpcr[1],asknpcr[2]] #todas opcoes presentes no menu npc rio, quando nao se apresentaram
menujin2=[asknpcr[1],asknpcr[2],asknpcr[3]]
menutorufin=[asknpcs[1],asknpcs[2]] #todas opcoes presentes no menu npc mar, quando nao se apresentaram
menutorufin2=[asknpcs[1],asknpcs[2],asknpcs[3]]
menuaquario=["Colocar peixe","Retirar peixe"]

#onde começa de fato a repetição infinita do jogo
while True:
  print("")
  print("---VILA---")
  displaymenu (menucity,"Player Status","Sair do Jogo")
  opcao = int(input("")) #fim parte star do jogo ------

  if(opcao==1):#opcoes da casa -------------------------------------------------------------------
    while True:
      print("")
      print("---CASA---")
      displaymenu(menuhouse, "Player Status","Voltar a vila")
      opcao=int(input(""))
      if (opcao==1): #se opcao "dormir" for selecionada, fara verificacao da energia, se estiver cheia o player se recusa a dormir

        if(energia>=100):
          print("~Não estou cansado, preciso fazer algo produtivo!")

        else: #se energia nao estiver cheia, o player aceita dormir
          energia=100
          tedio=0
          dia+=1
          print("~Que ótima noite de sono! Me sinto revigorado!")

      elif(opcao==2): #aqui devemos inserir a mecanica do aquario pra depositar os peixes da mochila de acordo com a selecao do jogador
        while True:
          print("")
          print("---AQUÁRIO---")
          print(f"{limite-len(bolsa)} espaços na bolsa")
          print(bolsa)
          print(f"{limaqua-len (aquario)} espaços no aquário")
          print (aquario)
          displaymenu (menuaquario,"Player status","Voltar")
          opcao=int(input(""))
          print("")
          if (opcao==1): #inicio do codigo de depositar peixes no aquario

            while True:
              print(f"{limite-len(bolsa)} espaços na bolsa")
              print(bolsa)
              print(f"{limaqua-len(aquario)} espaços no aquário")
              print(aquario)
              if(len(aquario)<limaqua and len(bolsa)>0):

                for l in range(len(bolsa)):
                  print(f"{l+1} - Colocar {bolsa[l]}")
                print("0 - Sair")
                opcao=int(input(""))

                if(opcao==0):
                  break

                else:
                  transfere(opcao,bolsa,aquario)

              elif(len(bolsa)<1):
                print("Você não possui peixes para colocar no aquário.")
                break

              else:
                print("AQUÁRIO CHEIO!")
                break #fim da funcao deposito no aquario

          elif (opcao==2): #inicio codigo para retirar peixes do aquario
            while True:
              print(f"{limite-len(bolsa)} espaços na bolsa:")
              print(bolsa)
              print(f"{limaqua-len(aquario)} espaços no aquario:")
              print(aquario)

              if(len(bolsa)<limite and len(aquario)>0):
                for l in range(len(aquario)):
                  print(f"{l+1} - Retirar {aquario[l]}")
                print("0 - Sair")
                print(bolsa)
                opcao=int(input(""))

                if(opcao==0):
                  break

                else:
                  transfere(opcao,aquario,bolsa)

              elif(len(aquario)<1):
                print("Você não possui peixes no aquário para retirar.")
                break

              else:
                print("BOLSA CHEIA!") #fim da funcao retirar peixe do aquario
                break

          elif(opcao==9):
            pstatus()

          elif(opcao==0):
            break

          else:
            print("OPÇÂO INVÁLIDA!")

      elif(opcao==9): #opcao 9 para mostrar player status
        pstatus()

      elif(opcao==0): #opcao 0 para retornar a cidade
        break

      else: #verificacao de erro ao inserir opcao, se input diferente das opcoes oferecidas retorna menu e espera novo input
        print("OPÇÃO INVÁLIDA!")

  #LOJA!!

  elif(opcao==2):#opcoes da loja
    while True:
      print("")
      print("---LOJA---")
      if(julyidk==0):
        print(srtajuliana[0])
        print("")
        julyidk=1
        displaymenu(menushop,"Player Status","Voltar a vila")
        opcao=int(input(""))

      else:
        print(srtajuliana[1])
        print(piadinhasjuli[15])
        stnum=prob()
        if(0<stnum<=20):
          print(piadinhasjuli[0])
          print("")

        elif(20<stnum<=40):
          print(piadinhasjuli[3])
          print("")

        elif(40<stnum<=60):
          print(piadinhasjuli[6])
          print("")

        elif(60<stnum<=80):
          print(piadinhasjuli[9])
          print("")

        else:
          print(piadinhasjuli[12])
          print("")

        displaymenu(menushop2,"Player status","Voltar a vila")
        opcao=int(input(""))

      if(opcao==1): #se selecionado opcao comprar
        while True:
          showloja() #funcao que mostra os itens que a loja oferece
          opcao=int(input(""))
          if(opcao==1): #comprando o chapeu da loja
            if(dinheiro>=loja[0][1] and c1==0):#se dinheiro for maior que o preço do item e vc nao tiver o item, entao permite a compra
              dinheiro-=loja[0][1] #subtrai o dinheiro do jogador pelo preço do item
              ehead.insert(0,loja[0][0]) #insere o item comprado na lista de equipamentos da cabeça
              ehead.pop() #remove o equipamento antigo da lista "equipamentos da cabeça"
              bequi+=5 #faz a soma dos bonus que o item oferece
              fadiga=5 #faz a soma do bonus que o item oferece
              bequip=bequi+fzbequi(nivel,fbequi) #refaz o calculo de quanto é o bonus total do personagem
              c1+=1 #define que vc comprou o item chapeu da loja
              print("Parabéns! Você comprou",loja[0][0]) #mensagem de confirmação de ação foi realizada

            elif(c1==1): #verificacao se caso já possui o item
              print("Você já possui esse item...") #mensagem informando que jogador ja possui o item

            elif(dinheiro<=loja[0][1]): #verificacao se o dinheiro é suficiente pra realizar a compra
              print("Você não possui dinheiro suficiente") #mensagem informando que dinheiro atual é insuficiente

          elif(opcao==2): #comprando a roupa da loja
            if(dinheiro>=loja[1][1] and c2==0): #verificacao se dinheiro é maior que preço e se nao possui o item
              dinheiro-=loja[1][1] #subtracao do dinheiro pelo preço do item
              echest.insert(0,loja[1][0]) #insere o item comprado na tabela de itens equipados
              echest.pop() #remove o item antigo da lista de equipamentos equipados
              bequi+=5 #recebendo o bonus oferecido pelo equipamento
              bequip=bequi+fzbequi(nivel,fbequi) #att total bonus personagem apos compra
              c2+=1 #define que vc comprou o item roupa
              print("Parabéns!! você comprou",loja[1][0]) #mensagem de confirmação que ação foi realizada

            elif(c2==1): #verificacao caso ja possui o item
              print("Você já possui esse item...") #mensagem informativa dizendo que já possui o item

            elif(c2==2):
              print("-MEU DEUS!! ONDE CONSEGUIU ESSE MACACÃO? ISSO É UMA EDIÇÃO EXTREMAMENTE RARA! SÓ OS MELHORES PESCADORES DA ILHA POSSUEM UM DESSE!")

            elif(dinheiro<=loja[1][1]): #verificação se possui dinheiro necessario pra efetuar a compra
              print("Você não possui dinheiro suficiente") #mensagem informando que nao possui dinheiro necessario pra realizar a compra

          elif(opcao==3): #comprando a ferramenta da loja
            if(dinheiro>=loja[2][1] and c3==0): #verificando se dinheiro é maior que o preço e se ainda nao possui o item
              dinheiro-=loja[2][1] #subtraindo dinheiro menos o preço do item
              etool.insert(0,loja[2][0]) #inserindo item comprado na lista de itens equipados
              etool.pop() #removendo o item antigo da lista de equipamentos equipados
              bequi+=12 #recebendo bonus pelo item comprado
              bequip=bequi+fzbequi(nivel,fbequi) #att total bonus personagem apos compra
              c3+=1 #define que vc comprou a ferramenta da loja
              print("Parabéns!! você comprou",loja[2][0]) #mensagem de confirmação que ação foi realizada

            elif(c3==1): #verificação se ja possui o item
              print("Você já possui esse item...") #mensagem informando que já possui o item

            elif(dinheiro<=loja[2][1]): #verificando se possui dinheiro suficiente pra compra do item
              print("Você não possui dinheiro suficiente") #mensagem informando que nao possui dinheiro pra realizar a ação

          elif(opcao==4): #comprando a bota da loja
            if(dinheiro>=loja[3][1] and c4==0):#verificando se possui dinheiro suficiente e se ainda nao possui o item
              dinheiro-=loja[3][1] #subtraindo o dinheiro pelo valor do item
              eboot.insert(0,loja[3][0]) #adicionado item comprado a lista de itens equipados
              eboot.pop() #excluindo o item antigo da lista de itens equipados
              bequi+=10 #recebendo o bonus pelo item comprado
              bequip=bequi+fzbequi(nivel,fbequi) #att total bonus personagem apos compra
              c4+=1 #define que vc omcprou a bota da loja
              print("Parabéns!! você comprou",loja[3][0]) #mensagem de confirmação que a ação foi realizada

            elif(c4==1): #verificação se ja possui o item
              print("Você já possui esse item...") #mensagem informando que ja possui o item

            elif(c4==2):
              print("-UAAAAAU! ONDE CONSEGUIU ESSE PAR DE BOTAS LENDÁRIAS? SEMPRE ACHEI QUE FOSSEM APENAS UMA LENDA!..")

            elif(dinheiro<=loja[3][1]): #verificando se possui dinheiro suficiente
              print("Você não possui dinheiro suficiente") #mensagem informando que nao possui dinheiro suficiente

          elif(opcao==5): #comprando a bolsa da loja
            if(dinheiro>=loja[4][1] and c5==0): #verificando se possui dinheiro suficiente e se ainda nao possui o item
              dinheiro-=loja[4][1] #subtraindo do dinheiro o valor do item
              ebag.insert(0,loja[4][0]) #adicionando o equipamento comprado a lista de equipamentos equipados
              ebag.pop() #removendo da lista equipamentos equipados o item antigo
              limite+=5 #recebendo o bonus do item comprado
              c5+=1 #define que vc comprou a bolsa da loja
              print("Parabéns!! você comprou",loja[4][0]) #mensagem de confirmação que a ação foi realizada

            elif(c5==1): #verificação se ja possui o item
              print("Você já possui esse item...") #mensagem informando que ja possui o item

            elif(dinheiro<=loja[4][1]): #verificando se o dinheiro é menor que o preço
              print("Você não possui dinheiro suficiente") #informando que nao possui dinheiro suficiente pra realizar a compra

          elif(opcao==9): #printa status player
            pstatus() #chama funcao status player que printa tudo do personagem

          elif(opcao==0): #funcao padrão pra retornar/sair
            break #da fim ao while

          else: #verificacao de erro
            print("OPÇÃO INVÁLIDA!")

      elif(opcao==2): #opcao de venda na loja
        if(len(bolsa)<1): #verifica se possui algo para vender
          print("Você não possui nada para vender..") #se bolsa estiver vazia, imprime mensagem que nao há nada a vender

        while (len(bolsa)>0): #verifica se existe algo na bolsa
          for l in range(len(bolsa)): #repeticao baseada nos elementos presentes da bolsa
            print(f"opcao {l+1} Vender {bolsa[l]} por {valorvenda(bolsa[l])} moedas.") #printando numero do item, nome, preço
          print("9 = Vender tudo") #print da opcao padrao player status
          print("0 = Voltar") #print da opcao padrao sair/voltar
          opcao=int(input("")) #input para ler opção

          if(opcao==0):
            break

          elif(opcao==9): #aqui opcao de vender tudo da bolsa
            print(f"Valor total da venda de todos os itens é: {vvtotal()} moedas") #print que mostra o a soma do valor de todos peixes presentes na bolsa
            print("Tem certeza que deseja vender tudo da bolsa?") #pergunta de verificacao se o jogador realmente deseja vender tudo
            print("1 = SIM") #print opcao sim
            print("2 = NÃO") #print opcao nao
            opcao=int(input("")) #input, recebe opcao selecionada
            if(opcao==1): #se escolhido sim para vender tudo, entao...
              dinheiro+=vvtotal() #dinheiro recebe o valor total de todos itens presentes na bolsa
              for l in range(len(bolsa)): #gira uma strutura de repeticao pra excluir todos itens da bolsa
                bolsa.pop(0) #pop para apagar os itens da bolsa

            elif(opcao==2): #se opcao de vender tudo for nao, entao...
              print("Venda total cancelada") #print mensagem que ação foi cancelada

            else: #verificacao de erro
              print("OPÇÃO INVÁLIDA!")

          else:
            if(opcao>len(bolsa)):
              print("OPÇÃO INVÁLIDA!")

            else:
              dinheiro+=valorvenda(bolsa[opcao-1])
              removeritem(opcao,bolsa,valorvenda(bolsa[opcao-1]))


      elif(opcao==3):
        while True:
          for l in range(len(loja)):
            print(f"opcao {l+1} - {loja[l][0]}")

          print(f"9 - Player Status")
          print(f"0 - Sair")
          opcao=int(input(""))

          if(opcao==1):
            print(srtajuliana[2])

          elif(opcao==2):
            print(srtajuliana[3])

          elif(opcao==3):
            print(srtajuliana[4])

          elif(opcao==4):
            print(srtajuliana[5])

          elif(opcao==5):
            print(srtajuliana[6])
            print(srtajuliana[7])

          elif(opcao==9): #opcao padrao player status
            pstatus()

          elif(opcao==0): #opcao padrao sair/voltar
            break

          else: #verificacao de erro
            print("OPÇÃO INVÁLIDA!")

      elif(opcao==4):#inserção das piadas do npc Juliana
        if(0<stnum<=20):
          print(piadinhasjuli[1])
          print(piadinhasjuli[2])

        elif(20<stnum<=40):
          print(piadinhasjuli[4])
          print(piadinhasjuli[5])

        elif(40<stnum<=60):
          print(piadinhasjuli[7])
          print(piadinhasjuli[8])

        elif(60<stnum<=80):
          print(piadinhasjuli[10])
          print(piadinhasjuli[11])

        else:
          print(piadinhasjuli[13])
          print(piadinhasjuli[14])

      elif(opcao==9): #opcao padrão de printar o player status
        pstatus()

      elif(opcao==0): #opcao padrao de voltar/sair
        print(srtajuliana[8])
        break

      else: #verificacao de erro
        print("OPÇÃO INVÁLIDA!")

  elif(opcao==3):#opcoes do rio
    while True:
      menuriver=fmenuplacefish(jnam,namejinidk) #aqui para sempre atualizar o nome do npc--------------------------------------------------------------------------
      print("")
      print("---RIO---") #printa local que vc esta
      displaymenu(menuriver,"Player Status","Voltar a vila") #printa as opcoes do rio
      opcao=int(input("")) #input da decisao

      if(opcao==1): #se opcao for pescar
        if(energia>=10): #verifica se energia é suficiente pra fazer a acao
          energia-=fadiga #subtrai da energia o valor da acao
          stnum=prob() #gira o dado pra gerar o numero

          if((fr[0]-bequip)<stnum<=(fr[1]-bequip)): #se o numero sorteado pelo dado de 1 a 100 for dentro do intervalor 1~55, entao jogador falhou em pescar um peixe
            print("Poxa... Comeram a isca ") #mensagem do resultado da acao
            exp=subxp(1,exp) #calculo de ganho de experiencia pela falha, falha = +1exp
            nivel=fnivel(exp,nivel) #roda funcao pra verificar nivel
            bequip=bequi+fzbequi(nivel,fbequi) #foda funcao pra verificar bonus
            print(stnum) #printa o numero sorteado pelo dado

          elif((sr[0]-bequip)<stnum<=sr[1]): #se numero sorteado pelo dado estiver dentro do intervalo 56~85, entao jogador pegou peixe pequeno rio
            print("Peguei um lambarizinho") #printa mensagem resultado acao
            print(stnum) #printa numero gerado pelo dado
            exp=subxp(2,exp) #soma +2 de exp pelo peixe pequeno
            nivel=fnivel(exp,nivel) #refaz o calculo de verificacao/definicao de nivel player
            bequip=bequi+fzbequi(nivel,fbequi) #refaz o calculo de verificacao/definicao do bonus total do player
            bolsa=increaseinv(bolsa,limite,"Lambari") #adiciona a bolsa o peixe adquirido

          elif((mr[0]-bequip)<stnum<=(mr[1]-bequip)): #se numero sorteado pelo dado estiver dentro do intervalo 86~95, entao jogador pegou peixe medio rio
            print("Opa!! Peguei uma Tilápia") #mensagem resultado da acao
            print(stnum) #printa numero gerado pelo dado
            exp=subxp(5,exp) #soma +5 exp pelo peixe medio
            nivel=fnivel(exp,nivel) #refaz calculo de verificacao/definicao nivel
            bequip=bequi+fzbequi(nivel,fbequi) #refaz calculo de verificacao/definicao bonus total
            bolsa=increaseinv(bolsa,limite,"Tilápia") #adiciona o peixe adquirido a bolsa

          elif((lr[0]-bequip)<stnum<=lr[1]): #se numero sorteado pelo dado estiver dentro do intervalo 96~100, jogador pegou peixe grande rio
            stnum=prob() #rola o dado mais uma vez pra ver se vai entrar na tabela do peixe raro
            if(98<=stnum<=100): #se numero sorteado pela segunda vez for 98~100 (peixe raro = 2% dentro dos 5% do peixe grande)
              print("UMA CARPA LENDÁRIA!!!") #printa resultado da acao
              print(stnum) #printa numero gerado pelo segundo giro do dado
              exp=subxp(100,exp) #calcula exp
              nivel=fnivel(exp,nivel) #recalcula/verifica nivel
              bequip=bequi+fzbequi(nivel,fbequi) #recalcula/verifica bonus total
              if((cpyi and cpya)==0): #verificacao se ja obteve algum peixe raro, se cpyi ou cpya = 0 player nunca pegou um peixe raro do rio
                stnum=prob() #gira o dado pra definir qual peixe raro vai receber
                if(0<stnum<=50): #se o terceiro giro do dado der numero entre 1~50, entao player recebe carpa ying
                  bolsa=increaseinv(bolsa,limite,"Carpa Ying") #adiciona carpa ying na mochila
                  cpyi=1 #define que capa ying foi obtido
                  cpya=0 #define que carpa yang nao foi obtido
                else: #se numero gerado pelo 3 giro do dado for 51~100, player recebe a carpa yang
                  bolsa=increaseinv(bolsa,limite,"Carpa Yang") #adiciona carpa yang na mochila
                  cpya=1 #define que carpa yang foi obtida
                  cpyi=0 #define que carpa ying nao foi obtida
              elif(cpya==1): #se carpa yang foi obtida
                bolsa=increaseinv(bolsa,limite,"Carpa Ying") #entao dessa vez vc recebe a ying
                cpyi=1 #define que a carpa ying foi obtida
                cpya=0 #define que a carpa yang nao foi obtida
              else: #se condicao foi inversa da anterior
                bolsa=increaseinv(bolsa,limite,"Carpa Yang") #recebe a carpa yang
                cpya=1 #define que carpa yang foi obtida
                cpyi=0 #define que carpa ying nao foi obtida
            else: #se condicao dos 2% dentro dos 5% nao for atendida, entao player recebe um peixe grande normal
              print("IHUUUUUL!! PEGUEI UM PEIXÃO!!!") #mensagem de resultado da acao
              print(stnum) #printa valor gerado pelo dado
              exp=subxp(15,exp) #calcula exp
              nivel=fnivel(exp,nivel) #recalcula/verifica nivel
              bequip=bequi+fzbequi(nivel,fbequi) #recalcula/verifica bonus total
              bolsa=increaseinv(bolsa,limite,"Traira") #adiciona item peixe grande rio a bolsa

        else: #se personagem nao tiver energia >=10
          print("~Estou cansado... Preciso descansar...") #printa que personagem nao pode realizar a acao

      elif(opcao==2): #opcao de nadar no rio e recuperar 5 de energia
        if((tedio<3) and (energia <= 95)): #verifica se tedio e energia sao menores que 95
          energia=energia+5 #se condicao atendida, energia recebe +5
          tedio+=1 #tedio aumenta em +1, tedio=3 impossibilidade em continuar recuperando energia ao nadar
          print("~Estou me sentindo um pouco mais disposto!") #mensagem de realizacao da acao
        elif(tedio==3): #se tedio for =3
          print("~Ah! Enjoei de nadar...") #mensagem imprimindo que personagem nao fará a acao

        elif(energia>95): #se energia for maior que 95
          print("~Estou cheio de energia!! preciso fazer algo produtivo!") #mensagem informando que player nao fará acao

      elif(opcao==3 and namejinidk in menuriver): #dialogo com npc jin no rio
        while True:
          if(jnam==0): #verifica se vc ja interagiu/se apresentou
            print("")
            print(f"[{namejinidk}]")
            print(srjin[0]) #printa fala do npc
            print("")
            print(f"1 = {asknpcr[0]}") #printa opcao de se apresentar ao npc
            print(f"0 = Voltar outra hora") #printa opcao de abandonar dialogo com npc
            opcao=int(input(""))

            if(opcao==1): #se opcao selecionada foi se apresentar ao npc
              print(f"~{asknpcr[0]}")
              print(srjin[1]) #printa mensagem do npc se apresentando a voce
              jnam=1 #define que vc conheceu e agora sabe o nome do npc
              namejinidk=namenpc(0) #chama a funcao pra alterar o nome do npc


            elif(opcao==0): #se opcao do dialogo do npc for zero, entao abandona o dialogo
              break

            else: #verificacao de erro
              print("OPÇÃO INVÁLIDA!")

          elif((jnam==1) and (inforareriver==0) or (not(("Carpa Ying" and "Carpa Yang") in bolsa))): #se vc ja conhece o npc, entao
            print("")
            print(f"[{namejinidk}]")
            displaymenu(menujin,"Player status","Voltar") #mostra o menu com as opcoes extras
            opcao=int(input(""))
            if(opcao==1): #selecionando opcao de perguntar dica ao npc jin
              print(f"~{asknpcr[1]}") #player pergunta ao npc se npc possui dica a oferecer
              print(srjin[2]) #resposta dica npc river
              print(srjin[3]) #resposta dica2 npc river


            elif(opcao==2): #selecionando a opcao conversar com npc jin
              print(asknpcr[2]) #player decide conversar
              for l in range(5): #estrutura de repeticao pra printar o dialogo do npc jin
                print(srjin[l+4])
              inforareriver=1

            elif(opcao==0): #opcao padrao voltar/sair
              break

            else: #verificacao de erro
              print("OPÇÃO INVÁLIDA!")

          elif(inforareriver==1 and ("Carpa Ying" and "Carpa Yang" in bolsa) and jnam==1):
            print("")
            print(f"[{namejinidk}]")
            displaymenu(menujin2,"Player status","Voltar")
            opcao=int(input(""))
            if(opcao==1): #selecionando opcao de perguntar dica ao npc jin
              print(f"~{asknpcr[1]}") #player pergunta ao npc se npc possui dica a oferecer
              print(srjin[2]) #resposta dica npc river
              print(srjin[3]) #resposta dica2 npc river

            elif(opcao==2): #selecionando a opcao conversar com npc jin
              print(asknpcr[2]) #player decide conversar
              for l in range(5): #estrutura de repeticao pra printar o dialogo do npc jin
                print(srjin[l+4])
              inforareriver=1



            elif(opcao==3):
              print(srjin[9])
              print("")
              print("Deseja dar o casal de carpas?")
              print("1 = SIM")
              print("2 = NÃO")
              opcao=int(input(""))
              if(opcao==1):
                bolsa.remove("Carpa Ying")
                bolsa.remove("Carpa Yang")
                if("RubberGalocha" in eboot):
                  bequi+=10
                else:
                  bequi+=20
                eboot.insert(0,"RootsBoots")
                eboot.pop()
                bequip=bequi+fzbequi(nivel,fbequi)
                c4=2
                print(srjin[10])
                print("")
                print("Senhor Jin se despede com um sorriso alegre...")#pensamentos, nao precisa de ~ ou -
                print("...Sinto que nunca mais verei o senhor Jin...")#pensamentos, nao precisa de ~ ou -
                jnam=2
                break
                #menuriver.
              elif(opcao==2):
                print("~Talvez depois...")#resposta ao npc manter ~

              elif(opcao==9):
                pstatus()

              else:
                print("OPÇÃO INVÁLIDA!")

      elif(opcao==9):
        pstatus()

      elif(opcao==0): #opcao padrao voltar/sair
        break

      else: #verificacao de erro
        print("OPÇÃO INVÁLIDA!")

  elif(opcao==4):#opções da praia
    while True:
      menubeach=fmenuplacefish(tnam,nametoruidk)
      print("")
      print("---PRAIA---") #printa local presente
      displaymenu(menubeach,"Player Status","Voltar a vila") #printa menu mar
      opcao=int(input(""))
      if(opcao==1): #se opcao pescar for selecionada
        if(energia>=10): #verifica se possui energia suficiente pra executar a acao
          energia-=fadiga #subtrai da energia a quantia para realizar acao
          stnum=prob() #gira o dado pra definir o sucesso
          if((fs[0]-bequip)<stnum<=(fs[1]-bequip)): #se numero do dado estiver entre 1~80, entao falhou
            print("~Poxa... Comeu a isca =/") #mensagem informando resultado da acao
            exp=subxp(1,exp) #soma xp
            nivel=fnivel(exp,nivel) #recalcula/verifica nivel
            bequip=bequi+fzbequi(nivel,fbequi) #recalcula/verifica bonus
            print(stnum) #printa numero sorteado pelo dado

          elif((ss[0]-bequip)<stnum<=(ss[1]-bequip)): #se numero do dado estiver entre 80~90, entao player recebe peixe pequeno mar
            print("~Peguei uma Anchova!") #imprime resultado da acao
            print(stnum) #printa resultado do dado
            exp=subxp(10,exp) #soma exp
            nivel=fnivel(exp,nivel) #recalcula/verifica nivel
            bequip=bequi+fzbequi(nivel,fbequi) #recalcula/verifica bonus total
            bolsa=increaseinv(bolsa,limite,"Anchova") #adiciona o peixe obtido na bolsa

          elif((ms[0]-bequip)<stnum<(ms[1]-bequip)): #se numero do dado estiver entre 90~98, entao player recebe peixe medio mar
            print("~Opa!! Pesquei uma Corvina!") #imprime resultado da acao
            print(stnum) #printa resultado do dado
            exp=subxp(30,exp) #soma xp
            nivel=fnivel(exp,nivel) #recalcula/verifica nivel
            bequip=bequi+fzbequi(nivel,fbequi) #recalcula/verifica bonus total
            bolsa=increaseinv(bolsa,limite,"Corvina") #adiciona peixe obtido na bolsa

          elif((ls[0]-bequip)<stnum<=ls[1]): #se numero do dado estiver 98~100, entao...
            print(stnum)
            stnum=prob() #gira o dado mais uma vez pra verificar se vai entrar na tabela do peixe raro mar
            if(98<=stnum<=100): #se na segunda rolagem de dados numero der entre 98~100
              print("~Eita... Peguei... Um... Polvo azul?!??") #imprime resultado da acao
              print(stnum) #printa numero gerado pela segunda rolagem de dado
              exp=subxp(100,exp) #soma xp
              nivel=fnivel(exp,nivel) #recalcula/verifica nivel
              bequip=bequi+fzbequi(nivel,fbequi) #recalcula/verifica bonus total
              bolsa=increaseinv(bolsa,limite,"Kralamor") #adiciona peixe obtido na bolsa
            else: #se na segunda rolagem de dado nao acessar tabela de peixe raro, entao player recebe peixe grande normal
              print("~EITAAA!! PEGUEI UM TUBARÃO!!") #mensagem de resultado da acao
              print(stnum) #printa numero gerado pela segunda rolagem do dado
              exp=subxp(100,exp) #soma xp
              nivel=fnivel(exp,nivel) #recalcula/verifica nivel
              bequip=bequi+fzbequi(nivel,fbequi) #recalcula/verifica bonus total
              bolsa=increaseinv(bolsa,limite,"Tubarão") #adiciona peixe obtido na bolsa


        else: #caso nao atenda a condicao de ter energia >=10
          print("~Estou cansado... Preciso descansar...") #mensagem informando que acao nao sera executada

      elif(opcao==2): #se opcao de nadar for selecionada
        if((tedio<3) and (energia <= 95)): #verifica se o tedio nao foi atingido e energia é menor que 95
          energia=energia+5 #se condicao atendida, recupera 5 de energia
          tedio=tedio+1 #aumenta em 1 o tedio
          print("~Estou me sentindo um pouco mais disposto!") #mensagem de resultado da acao
        elif(tedio==3): #se o tedio for 3, acao nao sera executada
          print("~Ah! Enjoei de nadar...") #mensagem resultado da acao

        elif(energia>=95): #se energia for maior que 95, personagem se recusa em executar a acao
          print("~Estou cheio de energia!! preciso fazer algo produtivo!") #imprime resultado da acao

      elif(opcao==3 and nametoruidk in menubeach):
        while True:
          if(tnam==0): #verifica se vc ja interagiu/se apresentou
            print("[Senhor desconhecido da praia]")
            print(srtorufin[0]) #printa fala do npc
            print(f"1 = {asknpcs[0]}") #printa opcao de se apresentar ao npc
            print(f"0 = Voltar outra hora") #printa opcao de abandonar dialogo com npc
            opcao=int(input(""))

            if(opcao==1): #se opcao selecionada foi se apresentar ao npc
              print(f"~{asknpcs[0]}")
              print(srtorufin[1]) #printa mensagem do npc se apresentando a voce
              tnam+=1 #define que vc conheceu e agora sabe o nome do npc
              nametoruidk=namenpc(1) #chama a funcao pra alterar o nome do npc


            elif(opcao==0): #se opcao do dialogo do npc for zero, entao abandona o dialogo
              break

            else: #verificacao de erro
              print("OPÇÃO INVÁLIDA!")

          elif(tnam==1 and (inforaresea==0) or (not("Kralamor" in bolsa))): #se vc ja conhece o npc, entao
            print("[Senhor Torufin]")
            displaymenu(menutorufin,"Player status","Voltar") #mostra o menu com as opcoes extras
            opcao=int(input(""))
            if(opcao==1): #selecionando opcao de perguntar dica ao npc torufin
              print(f"~{asknpcs[1]}") #player pergunta ao npc se npc possui dica a oferecer
              print(srtorufin[2]) #resposta dica npc mar
              print("")

            elif(opcao==2): #selecionando a opcao conversar com npc torufin
              print(f"~{asknpcs[2]}") #player decide conversar
              for l in range(6): #estrutura de repeticao pra printar o dialogo do npc torufin
                print(srtorufin[l+3])
              print("")
              inforaresea=1

            elif(opcao==0): #opcao padrao voltar/sair
              break

            else: #verificacao de erro
              print("OPÇÃO INVÁLIDA!")

          elif(inforaresea==1 and ("Kralamor" in bolsa)):
            print(f"[{nametoruidk}]")
            displaymenu(menutorufin2,"Player status","Voltar")
            opcao=int(input(""))
            if(opcao==1): #selecionando opcao de perguntar dica ao npc jin
              print(f"~{asknpcs[1]}") #player pergunta ao npc se npc possui dica a oferecer
              print(srtorufin[2]) #resposta dica npc river
              print("")

            elif(opcao==2): #selecionando a opcao conversar com npc jin
              print(f"~{asknpcs[2]}") #player decide conversar
              for l in range(6): #estrutura de repeticao pra printar o dialogo do npc jin
                print(srtorufin[l+3])
              print("")
              inforaresea=1

            elif(opcao==3):
              print({srtorufin[9]})
              print("")
              print("Deseja dar o Polvo azul?")
              print("1 = SIM")
              print("2 = NÃO")
              opcao=int(input(""))
              if(opcao==1):
                bolsa.remove("Kralamor")
                if("FisherRobe" in echest):
                  bequi+=10
                else:
                  bequi+=15
                echest.insert(0,"ProFisherRobe")
                echest.pop()
                bequip=bequi+fzbequi(nivel,fbequi)
                c2=2
                print(srtorufin[10])
                print("")
                print("Senhor Torufin sorri satisfeito... E diz adeus..")
                print("...Talvez um dia eu faça uma visita...")
                tnam=2
                break
                #menuriver.
              elif(opcao==2):
                print("~Talvez depois...")

              else:
                print("OPÇÃO INVÁLIDA!")


      elif(opcao==9): #opcao padrao player status
        pstatus()

      elif(opcao==0): #opcao padrao sair/voltar
        break

      else: #verificacao de erro
        print("OPÇÃO INVÁLIDA!")

  elif(opcao==9):
    pstatus()

  elif(opcao==0):
    print("TEM CERTEZA QUE DESEJA SAIR DO JOGO?")
    print("1 - SIM")
    print("2 - NÃO")
    opcao=int(input(""))
    if(opcao==1):
      print("GAME ENCERRADO!")
      print("")
      break
    elif(opcao==2):
      print("RETORNANDO AO GAME")
      print("")
    else:
      print("OPÇÃO INVÁLIDA!")

  else: #verificacao de erro
    print("OPÇÃO INVÁLIDA!")

#creditos
print("----------FISHVILLAGE------------")
print("-------------BETA----------------")
print("---------------------------------")
print("------------CRÉDITOS-------------")
print("---------------------------------")
print("---------DESENVOLVEDORES---------")
print("------------HFelipe--------------")
print("------------RSepulcri------------")
print("------------CYasmim--------------")
print("---------------------------------")
print("  ⓒ 2023 白狼-しろおおかみ Studio ")