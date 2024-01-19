-- Creación de tablas
DROP DATABASE IF exists parcialbiblioteca;
CREATE DATABASE parcialbiblioteca;
USE parcialbiblioteca;

CREATE TABLE Usuario (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50),
    TipoUsuario VARCHAR(20),
    OtrosAtributos VARCHAR(255)
);

CREATE TABLE Sala (
    SalaID INT PRIMARY KEY AUTO_INCREMENT,
    NombreSala VARCHAR(50),
    OtrosAtributos VARCHAR(255)
);

CREATE TABLE Libro (
    LibroID INT PRIMARY KEY AUTO_INCREMENT,
    Titulo VARCHAR(100),
    Autor VARCHAR(50),
    Categoria VARCHAR(50),
    SalaID INT,
    OtrosAtributos VARCHAR(255),
    FOREIGN KEY (SalaID) REFERENCES Sala(SalaID)
);

CREATE TABLE Prestamo (
    PrestamoID INT PRIMARY KEY AUTO_INCREMENT,
    UsuarioID INT,
    LibroID INT,
    FechaPrestamo DATE,
    FechaDevolucion DATE,
    OtrosAtributos VARCHAR(255),
    FOREIGN KEY (UsuarioID) REFERENCES Usuario(UserID),
    FOREIGN KEY (LibroID) REFERENCES Libro(LibroID)
);

-- Inserciones 
INSERT INTO Usuario (Nombre, TipoUsuario, OtrosAtributos) VALUES
    ('Admin1', 'Administrador', 'Otros datos'),
    ('Visitante1', 'Visitante', 'Otros datos'),
    ('Admin2', 'Administrador', 'Otros datos');

INSERT INTO Sala (NombreSala, OtrosAtributos) VALUES
    ('Sala A', 'Otros datos'),
    ('Sala B', 'Otros datos'),
    ('Sala C', 'Otros datos');

INSERT INTO Libro (Titulo, Autor, Categoria, SalaID, OtrosAtributos) VALUES
    ('Libro1', 'Autor1', 'Ficción', 1, 'Otros datos'),
    ('Libro2', 'Autor2', 'No Ficción', 2, 'Otros datos'),
    ('Libro3', 'Autor3', 'Fantasía', 3, 'Otros datos');

INSERT INTO Prestamo (UsuarioID, LibroID, FechaPrestamo, FechaDevolucion, OtrosAtributos) VALUES
    (1, 1, '2024-01-18', '2024-02-01', 'Otros datos'),
    (2, 2, '2024-01-20', '2024-02-05', 'Otros datos'),
    (3, 3, '2024-01-22', '2024-02-10', 'Otros datos');