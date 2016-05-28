# keyperftest
Teste de performance da troca de chaves inteiras por uuids no postgres

Artigo completo no Blog: http://junglecoders.blogspot.be/2016/05/uso-de-uuids-como-chave-primaria-com.html

# Para testar em sua máquina:

1. Instale o postgresql 9.5
2. Crie um ambiente virtual. No Ubuntu 16.04 LTS:

  ```mkvirtualenv -p /usr/bin/python3.5 perftest```

3. Instale os pacotes necessários:

  ```pip install -r requiments.txt```

4. Migre:

  ```python manage.py migrate```

5. Execute os testes:

  ```python manage.py test```


Para mudar o número de registros criados, modifique a variável `N` em `settings.py`.
