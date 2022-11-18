import functions_framework
import sys
import datetime
import mysql.connector
import re
from google.cloud import storage

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
       request (flask.Request): The request object.
       <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
       The response text, or any set of values that can be turned into a
       Response object using `make_response`
       <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'bucket' and 'object' in request_json:
      bucket = request_json['bucket']
      b_object = request_json['object']

    elif request_args and 'bucket' and 'object' in request_args:
      bucket = request_args['bucket']
      b_object = request_args['object']

    else:
      return 'Nenhum bucket e/ou objeto definidos'

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket)
    blob = bucket.blob(b_object)
    file_str = blob.download_as_text()

    
    now = datetime.datetime.now()

    now = now.strftime('%Y_%m_%d')

    try:
      mydb = mysql.connector.connect(
      host="YOUR_HOST",
      user="YOUR_USER",
      password="YOUR_PASSWORD",
      database="YOUR_DATABASE"
      )
    except:
      return 'Não foi possível conectar ao banco'

    mycursor = mydb.cursor()

    query = f'CREATE TABLE {now} ('

    for field in file_str.splitlines()[0].split(';'):
        query = query + '{}'.format(re.sub('[\s/*&%$#@!().]','_',field.strip())) + ' VARCHAR(100), '

    query = query.strip()[0:-1]
    query = query + ')'
    #print(query)

    try:
      mycursor.execute(query)
    except:
      return 'Não foi possível criar a tabela. Verifique se ela já existe'

    try:
      for x in range(1, len(file_str.splitlines()) - 1):
        query = f'INSERT INTO {now} VALUES('
        for y in file_str.splitlines()[x].split(';'):
          if re.search('\d{2}/\d{2}/\d{4}', y) != None:
            y = "{}-{}-{}".format(y.split('/')[2], y.split('/')[1], y.split('/')[0])
          query = query + f'"{y}", '
        query = query.strip()[0:-1] + ')'
        #print(query)
        mycursor.execute(query)
    except:
      return f'Não foi possível inserir os valores na tabela {now}'
      
    return 'Sucesso!!'