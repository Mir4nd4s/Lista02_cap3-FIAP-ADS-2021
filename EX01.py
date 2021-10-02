qtd = 0
nPar = 0
nImpar = 0
contP = 0
contI = 0

print("Digite as notas dos 50 alunos: ")
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES!")
for i in range(2,50 + 1,2):
    contP = contP + 1
    nota = float(input("Por favor, insira a nota do aluno de número {}: ".format(i)))
    while nota < 0 or nota > 10:
        print("NOTA INVÁLIDA... TENTE NOVAMENTE!")
        nota = float(input("Por favor, insira a nota do aluno de número {}: ".format(i)))
    nPar = nPar + nota

print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES!")
for i in range(1,50 + 1,2):
    contI = contI + 1
    nota = float(input("Por favor, insira a nota do aluno de número {}: ".format(i)))
    while nota < 0 or nota > 10:
        print("NOTA INVÁLIDA... TENTE NOVAMENTE!")
        nota = float(input("Por favor, insira a nota do aluno de número {}: ".format(i)))
    nImpar = nImpar + nota

mPar = nPar/contP
mImpar = nImpar/contI

print("Os alunos de número par obtiveram uma média: {}".format(mPar))
print("Os alunos de número ìmpar obtiveram uma média: {}".format(mImpar))

if mPar == mImpar:
    print("*Houve empate entre os alunos pares e ímpares! Média: {}*".format(mPar))
elif mPar > mImpar:
    maior = mPar
    print("* Os alunos de número par, obtiveram a maior média! *")
else:
    maior = mImpar
    print("* Os alunos de número ímpar, obtiveram a maior média! *")

print("Quantidade de notas pares: {}\nQuantidade de notas impares: {}".format(contP,contI))


