
CREATE TABLE peliculas (
    id INTEGER PRIMARY KEY,
    titulo VARCHAR(10),
    duracion SMALLINT,
    fecha_estreno DATE
);


INSERT INTO peliculas (id, titulo, duracion, fecha_estreno) VALUES
(1, 'Parasite', 97, '2019-12-03'),
(2, 'Enemigo al acecho', 130, '2009-04-25'),
(3, 'American Paradise', 141, '2002-12-01'),
(4, 'Antes que anochezca', 102, '2007-11-04'),
(5, 'Inglorious Bastards', 105, '2009-08-13'),
(6, 'Training Day', 135, '2001-01-18'),
(7, 'Pedro Navaja', 114, '1984-10-03'),
(8, 'Gladiator', 215, '2000-04-10'),
(9, 'The Patriot', 182, '1995-06-21');

SELECT * FROM peliculas;