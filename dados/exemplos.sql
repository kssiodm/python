CREATE TABLE cliente (
  id BIGINT, 
  idade INT, 
  sexo CHAR, 
  dependentes INT, 
  escolaridade VARCHAR(20), 
  tipo_cartao VARCHAR(10), 
  limite_credito DOUBLE, 
  valor_transacoes_12m DOUBLE, 
  qtd_transacoes_12m BIGINT
);

show TABLES;
DESC cliente;

INSERT INTO cliente (
  id, 
  idade, 
  sexo, 
  dependentes, 
  escolaridade, 
  tipo_cartao, 
  limite_credito, 
  valor_transacoes_12m, 
  qtd_transacoes_12m);
  
INSERT INTO cliente VALUES (768805383, 45, 'M', 3, 'ensino medio', 'blue', 12691.51, 1144.90, 42);

INSERT INTO cliente VALUES (768805372, 40, 'F', 5, 'ensino fundamental', 'blue', 15691.51, 1024.90, 37);
INSERT INTO cliente VALUES (818770008, 49, 'F', 5, 'mestrado', 'blue', 8256.96, 1291.45, 33);
INSERT INTO cliente VALUES (713982108, 51, 'M', 3, 'mestrado', 'blue', 3418.56, 1887.72, 20);
                            
 SELECT * FROM cliente;
 
 SELECT id, escolaridade, sexo from cliente;
 
 SELECT id, escolaridade, sexo from cliente LIMIT 2;
 
 SELECT 10 + 20 +30 as SOMA;
 
 SELECT AVG(idade) as Media from cliente;
 
 CREATE TABLE transacao (
    id_transacao INT,
    id_cliente INT, 
    data_compra DATE,
    valor FLOAT 
);

show TABLES;

drop TABLE demo;

desc transacao;

ALTER TABLE transacao 
ADD id_loja VARCHAR(20);

after table transacao
MODIFY COLUMN valor DOUBLE;

SELECT * from transacao;

INSERT INTO transacao VALUES (1,768805383,'2021-06-10',50.74,'magalu'),
                  				(2,768805399,'2021-06-13',30.90,'giraffas'),
                  				(3,818770008,'2021-06-05',110.00,'postoshell'); 
                                
 delete from cliente WHERE id = 768805383;
 
 SELECT * from cliente WHERE id = 768805383;
 
 SELECT * from cliente WHERE id = 818770008;
 
 update transacao SET id_loja = 'magalu' WHERE id_transacao = 1;
 update transacao SET id_loja = 'giraffas' WHERE id_transacao = 2;
 update transacao SET id_loja = 'postoshell' WHERE id_transacao = 3;
 
  SELECT * from transacao;
  
  desc transacao;
   
  SELECT * FROM cliente WHERE sexo = 'F' OR escolaridade = 'mestrado';
  


SELECT 
    id as codigo, 
    dependentes as filhos,
    valor_transacoes_12m as gastos 
from 
    cliente 
WHERE 
    sexo = 'F'
ORDER by id DESC
limit 3;

SELECT * from transacao ORDER by id_transacao DESC;