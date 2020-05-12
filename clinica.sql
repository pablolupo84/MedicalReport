-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-04-2020 a las 20:28:57
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `clinica`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `antecedentes`
--

CREATE DATABASE clinica;

use clinica;

DROP TABLE IF EXISTS `antecedentes`;
CREATE TABLE IF NOT EXISTS `antecedentes` (
  `id_paciente` int(10) NOT NULL,
  `Enfermedades` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `antecedentes`
--

INSERT INTO `antecedentes` (`id_paciente`, `Enfermedades`) VALUES
(1, 'Marcapasos'),
(4, 'Infarto'),
(7, 'Ligamentos rodilla derecha'),
(10, 'ACV');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--
DROP TABLE IF EXISTS `paciente`;
CREATE TABLE IF NOT EXISTS `paciente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `dni` varchar(9) NOT NULL,
  `telefono` int(9) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `Edad` int(3) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dni` (`dni`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `paciente`
--

INSERT INTO `paciente` (`nombre`, `apellidos`, `dni`, `telefono`, `direccion`, `Edad`) VALUES
('Pepe', 'Sanchez', '00000000T', 685658965, 'Piruleta 1', 25),
('Luis', 'Soro', '00000000J', 623621587, 'Piruleta 2', 32),
('Luis', 'Perales', '12345678T', 632589651, 'Caramelo, 1', 65),
('Luis', 'Peña', '87654321T', 62547895, 'Chicle, 1', 48),
('Luis', 'Japonés', '52645898T', 625897426, 'Golosina, 1', 16),
('Luis', 'Suarez', '12345678P', 658523687, 'Piruleta, 3', 16),
('Luis', 'Olmo', '12345678U', 658523654, 'Piruleta, 4', 15),
('Luis', 'Indio', '12345678A', 658523405, 'Algodon, 1', 63),
('Luis', 'Amperio', '12345678V', 655872354, 'Algodon, 2', 80),
('Luis', 'Batería', '12345678Z', 655851213, 'Algodon, 3', 55),
('Luis', 'Tata', '00000000R', 625484125, 'Algodon, 5', 32);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sesiones`
--
DROP TABLE IF EXISTS `sesiones`;
CREATE TABLE IF NOT EXISTS `sesiones` (
  `id_p` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `pagado` varchar(5) NOT NULL DEFAULT "NO"
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `sesiones`
--

INSERT INTO `sesiones` (`id_p`, `fecha`,`pagado`) VALUES
(1, '2020-04-27',"SI"),
(2, '2020-04-27',"SI"),
(1, '2020-04-27',"NO"),
(2, '2020-04-27',"NO");


--
-- Estructura de tabla para la tabla `volante`
--
DROP TABLE IF EXISTS `volante`;
CREATE TABLE IF NOT EXISTS `volante` (
  `id_paciente` int(11) NOT NULL,
  `tipo` enum('Particular','Sanitas','Mafre','DKV','AXA','MCmutual','Solimat','Antares','Mercadona') NOT NULL,
  `volante` int(11) NOT NULL,
  `patologia` varchar(200) NOT NULL,
  `tratamiento` varchar(200) NOT NULL,
  `total` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `volante`
--

INSERT INTO `volante` (`id_paciente`, `tipo`, `volante`, `patologia`, `tratamiento`, `total`) VALUES
(1, 'Particular', 20, '', '', 2),
(2, 'Mafre', 15, '', '', 2),
(5, 'Particular', 20, 'Esguince tobillo', 'Masaje y corrientes galvánicas', 0),
(7, 'DKV', 10, 'Dolor cervical', 'Masaje', 0),
(5, 'Particular', 20, 'Esguince tobillo', 'Masaje y corrientes galvánicas', 0),
(7, 'DKV', 10, 'Dolor cervical', 'Masaje', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `antecedentes`
--
ALTER TABLE `antecedentes` ADD KEY `id` (`id_paciente`);

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente` ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `sesiones`
--
ALTER TABLE `sesiones` ADD KEY `id_p` (`id_p`);

--
-- Indices de la tabla `volante`
--
ALTER TABLE `volante` ADD KEY `id_paciente` (`id_paciente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `paciente`
--
ALTER TABLE `paciente` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `antecedentes`
--
ALTER TABLE `antecedentes` ADD CONSTRAINT `id` FOREIGN KEY (`id_paciente`) REFERENCES `paciente` (`id`);

--
-- Filtros para la tabla `sesiones`
--
ALTER TABLE `sesiones` ADD CONSTRAINT `id_p` FOREIGN KEY (`id_p`) REFERENCES `paciente` (`id`);

--
-- Filtros para la tabla `volante`
--
ALTER TABLE `volante` ADD CONSTRAINT `id_paciente` FOREIGN KEY (`id_paciente`) REFERENCES `paciente` (`id`);

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
