DROP DATABASE IF EXISTS facto_projeto_arduino;
CREATE DATABASE facto_projeto_arduino;

CREATE TABLE IF NOT EXISTS facto_projeto_arduino.historico_operacoes (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_controle` varchar(100) DEFAULT NULL COMMENT 'campo para informar qual o item foi acionado',
  `acao_executada` varchar(200) DEFAULT NULL COMMENT 'campo para informar o tipo de ação realizada',
  `data_operacao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'data em que a operação foi realizada',
  PRIMARY KEY (`id`)
);