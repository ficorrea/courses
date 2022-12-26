create table nome_tabela(
					id int not null auto_increment, 
					dia date not null,
                    bairro varchar(50) not null,
                    quartos tinyint,
                    banheiros tinyint,
                    suites tinyint,
                    garagens tinyint,
                    area float,
                    valor bigint,
                    primary key(id)
                    ) default charset = utf8;
                    
					