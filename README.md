# Docker lab

Este é um repositórios de estudos utilizando docker.

##### Requesitos:

* [Docker] 
* [Docker-compose] 


```bash
git clone https://github.com/kssioalmeida/docker-lab.git
cd docker-lab
docker-compose up -d
```

Será criado 3 containers:
- Servidor Redis
- Servidor Mongo
- Aplicaçao Python

A escolha da linguagem é apenas para teste, não me atentando tanto a qualidade do código escrito, pois não era esse o intuíto. A aplicação acessa os servidores Redis e Mongo e exibe a quantidade de vezes que a página foi acessada.


Acesse a aplicação:

```bash
localhost:5000
```


[docker]: <https://www.docker.com/>
[docker-compose]: <https://docs.docker.com/compose/>

