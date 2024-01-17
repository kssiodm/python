create table funcionarios(
    idFuncionario integer PRIMARY KEY AUTO_INCREMENT,
    nome varchar(100),  
    email varchar(200),
    sexo varchar(10),
    departamento varchar(100),
    admissao varchar(10),
    salario integer,
    cargo varchar(100),
    idRegiao int
);

insert into funcionarios values (1,'Kelley','rkelley0@soundcloud.com','Feminino','Computadores','10/2/2009',67470,'Structural Engineer',2);
insert into funcionarios values (2,'Armstrong','sarmstrong1@infoseek.co.jp','Masculino','Esporte','3/31/2008',71869,'Financial Advisor',2);
insert into funcionarios values (3,'Carr','fcarr2@woothemes.com','Masculino','Automotivo','7/12/2009',101768,'Recruiting Manager',3);
insert into funcionarios values (4,'Murray','jmurray3@gov.uk','Feminino','Joalheria','12/25/2014',96897,'Desktop Support Technician',3);
insert into funcionarios values (5,'Ellis','jellis4@sciencedirect.com','Feminino','Alimentícios','9/19/2002',63702,'Software Engineer III',7);
insert into funcionarios values (6,'Phillips','bphillips5@time.com','Masculino','Ferramentas','8/21/2013',118497,'Executive Secretary',1);
insert into funcionarios values (7,'Williamson','rwilliamson6@ted.com','Masculino','Computadores','5/14/2006',65889,'Dental Hygienist',6);
insert into funcionarios values (8,'Harris','aharris7@ucoz.com','Feminino','Brinquedos','8/12/2003',84427,'Safety Technician I',4);
insert into funcionarios values (9,'James','rjames8@prnewswire.com','Masculino','Joalheria','9/7/2005',108657,'Sales Associate',2);
insert into funcionarios values (11,'Jacobs','jjacobsa@sbwire.com','Feminino','Joalheria','11/27/2003',121966,'Community Outreach Specialist',7);
insert into funcionarios values (12,'Black','mblackb@edublogs.org','Masculino','Roupas','2/4/2003',44179,'Data Coordiator',7);
insert into funcionarios values (13,'Schmidt','sschmidtc@state.gov','Masculino','Bebês','10/13/2002',85227,'Compensation Analyst',3);
insert into funcionarios values (14,'Webb','awebbd@baidu.com','Feminino','Computadores','10/22/2006',59763,'Software Test Engineer III',4);
insert into funcionarios values (15,'Jacobs','ajacobse@google.it','Feminino','Games','3/4/2007',141139,'Community Outreach Specialist',7);
insert into funcionarios values (16,'Medina','smedinaf@amazonaws.com','Feminino','Bebês','3/14/2008',106659,'Web Developer III',1);
insert into funcionarios values (17,'Morgan','dmorgang@123-reg.co.uk','Feminino','Crianças','5/4/2011',148952,'Programmer IV',6);
insert into funcionarios values (18,'Nguyen','jnguyenh@google.com','Masculino','Lar','11/3/2014',93804,'Geologist II',5);
insert into funcionarios values (19,'Day','rdayi@chronoengine.com','Masculino','Eletronicos','9/22/2004',109890,'VP Sales',3);

SELECT * from funcionarios;

SELECT nome,email from funcionarios WHERE sexo LIKE 'Feminino' AND departamento like 'lar';

SELECT idFuncionario,nome,email FROM funcionarios WHERE departamento LIKE 'Roupas';

SELECT nome FROM funcionarios WHERE sexo LIKE 'Masculino' AND departamento LIKE 'Jardim';


-- trabalhando com a database comercio
-- exercicio -1
SELECT 
    COUNT(sexo_cliente) AS 'Qtd.', sexo_cliente
FROM 
    cliente
GROUP 
    BY sexo_cliente;

-- exercicio -2
SELECT
    C.id_cliente AS registro,
    C.nome_cliente AS cliete,
    C.sexo_cliente AS sexo,
    C.email_cliente AS 'e-mail contato'
from
    cliente C
INNER JOIN
    endereco E
ON 
    C.id_cliente = E.idcliente
INNER JOIN
    telefone T
ON
    C.id_cliente = T.idcliente
WHERE
    sexo_cliente LIKE 'F'
AND
    E.bairro LIKE 'centro'
AND
    E.cidade LIKE 'RIO DE JANEIRO'
AND
    T.tipo_telefone <> 'CEL';

-- exercicio -3

SELECT 
    C.nome_cliente, C.email_cliente, T.numero_telefone
FROM
    cliente C
INNER JOIN
    endereco E
ON
    C.id_cliente = E.idcliente
INNER JOIN
    telefone T
ON
    C.id_cliente = T.idcliente
WHERE 
    T.tipo_telefone LIKE 'CEL'
AND 
    C.email_cliente <> 'NULL'
AND 
    E.estado LIKE 'RJ';

-- exercicio -4

SELECT 
    C.nome_cliente, C.email_cliente, T.numero_telefone
FROM
    cliente C
INNER JOIN
    endereco E
ON
    C.id_cliente = E.idcliente
INNER JOIN
    telefone T
ON
    C.id_cliente = T.idcliente
WHERE
    C.sexo_cliente LIKE 'F'
AND
    T.tipo_telefone LIKE 'CEL'
AND
    E.estado LIKE 'RJ'
AND 
    C.email_cliente <> 'NULL';