-- MySQL Script generated by MySQL Workbench
-- Fri Dec 22 15:00:26 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `proj_DBPY` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `proj_DBPY` DEFAULT CHARACTER SET utf8 ;
USE `proj_DBPY` ;

-- -----------------------------------------------------
-- Table `mydb`.`Results`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `proj_DBPY`.`Results` ;

CREATE TABLE IF NOT EXISTS `proj_DBPY`.`Results` (
  `idResults` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `DateAndHour` DATETIME NULL,
  `time` TIME NULL,
  `nb_correct` INT NULL,
  `nb_total` INT NULL,
  `percent` FLOAT NULL,
  PRIMARY KEY (`idResults`),
  UNIQUE INDEX `idResults_UNIQUE` (`idResults` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `proj_DBPY`.`User` ;

CREATE TABLE IF NOT EXISTS `proj_DBPY`.`User` (
  `idUser` INT NOT NULL,
  `firstname` VARCHAR(45) NOT NULL,
  `lastname` VARCHAR(45) NOT NULL,
  `pseudo` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  PRIMARY KEY (`idUser`))
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
