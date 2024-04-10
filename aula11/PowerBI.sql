CREATE TABLE clientes (
    id SERIAL NOT NULL PRIMARY KEY,
    nome varchar(100) NOT NULL,
    sobrenome varchar(100) NOT NULL,
    email varchar(100) NOT NULL
);

CREATE TABLE pedidos (
    id SERIAL NOT NULL PRIMARY KEY,
    id_clientes INT,
    data_pedidio DATE,
    total numeric(7,2),
    status TEXT CHECK(STATUS IN ('Pendente', 'Finalizado', 'Cancelado')),
    FOREIGN KEY (id_clientes) REFERENCES clientes(id)
);

ALTER TABLE pedidos
ALTER COLUMN status SET DEFAULT 'Pendente';

-- Inserir pedidos
INSERT INTO pedidos(id_clientes, data_pedidio, total, status) VALUES
(1, '2024-04-01', 50.00, 'Pendente'),
(2, '2024-04-02', 75.20, 'Finalizado'),
(3, '2024-04-03', 30.50, 'Pendente'),
(4, '2024-04-04', 100.00, 'Finalizado'),
(5, '2024-04-05', 45.70, 'Cancelado'),
(6, '2024-04-06', 60.90, 'Finalizado'),
(7, '2024-04-07', 80.30, 'Pendente'),
(8, '2024-04-08', 25.00, 'Finalizado'),
(9, '2024-04-09', 90.10, 'Pendente'),
(10, '2024-04-10', 55.50, 'Finalizado');

INSERT INTO clientes(NOME, SOBRENOME, EMAIL) VALUES
('Iguinho', 'Job', 'iguinho@gmail.com'),
('Luigi', 'Boi Bandido', 'lulu@gmail.com'),
('Eduardo', 'Jujunior', 'edujujunior@gmail.com'),
('Maria', 'Silva', 'maria@gmail.com'),
('João', 'Santos', 'joao@gmail.com'),
('Ana', 'Ferreira', 'ana@gmail.com'),
('Pedro', 'Souza', 'pedro@gmail.com'),
('Juliana', 'Oliveira', 'juliana@gmail.com'),
('Lucas', 'Costa', 'lucas@gmail.com'),
('Carolina', 'Martins', 'carolina@gmail.com');