# teste_edesoft
Leitura de arquivo .csv no Google Cloud para inserção dos dados em um banco de dados SQL -> FORA DO CLOUD <-

############ PARA EXECUTAR ESTE CÓDIGO, VOCÊ PRECISA: #############

1 - criar uma conta no Google Cloud e ativá-la

2 -  no console do Google Cloud, você precisa criar um projeto e dentro deste projeto:

    A) você vai deve criar um bucket, liberar acesso público a este bucket e seus objetos (https://cloud.google.com/storage/docs/access-control/making-data-public) e subir um arquivo .csv de sua escolha

    ***ATENÇÃO***
    SALVAR O ARQUIVO .CSV COMO "CSV UTF-8" PARA A RENDERIZAÇÃO CORRETA DE CARACTERES ESPECIAIS
    #############################################################################################

    B) criar uma function (pode ser com configurações padrões)

    C) em runtime, você vai selecionar Python (este código foi feito usando Python 3.9)

    D) nesta function, você pode escolher copiar e colar o conteúdo de "index.py" no editor inline de código ou subir o arquivo zipado

    ***ATENÇÃO***
    O NOME DA FUNÇÃO PRINCIPAL DEVE SER O MESMO DO NOME DEFINIDO NO CAMPO "ENTRY POINT" AO LADO DO CAMPO "RUNTIME". NO CASO DE "INDEX.PY", O NOME DA FUNÇÃO É O MESMO NOME QUE VEM PRÉ-DEFINIDO POR PADRÃO AO CRIAR UMA FUNCTION
    #############################################################################################

    E) abaixo do arquivo, existe um outro chamado "requirements.txt" que define bibliotecas não embutidas do Python que PRECISAM ser chamadas para a execução do código. Abaixo de "functions-framework==3.*", você vai chamar mais duas bibliotecas e o arquivo vai ficar desta forma:

        functions-framework==3.*
        google-cloud-storage
        mysql-connector-python

    F) ao criar a função, ela gera um link para que você possa consumí-la. Para consumir a função corretamente você deve:

        1 - definir uma requisição HTTP com os seguintes campos "bucket" (nome do bucket onde está o objeto) e "object" (o caminho do objeto). Na plataforma do Cloud Functions existe uma aba chamada "testing", lá você pode simular requisições HTTP para a function

        OU

        2 - você pode passar o bucket e o object como parâmetros na url da function:

            https://YOUR_FUNCTION/?bucket=YOUR_BUCKET&object=YOUR_OBJECT

    ############## ATENÇÃO ###############
    NÃO ESQUECER DE MUDAR AS CONFIGURAÇÕES DE CONEXÃO AO BANCO DENTRO DE "INDEX.PY" PARA AS CONFIGURAÇÕES DO SEU BANCO

    ESTE CÓDIGO INSERE DADOS EM UM BANCO SQL QUE -> NÃO <- ESTEJAM NO CLOUD





    
