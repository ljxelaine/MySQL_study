-- 建立数据库university
CREATE SCHEMA `university` DEFAULT CHARACTER SET utf8 ;

-- 建立表department
CREATE TABLE `university`.`departemnt` (
  `dept_name` VARCHAR(20) NOT NULL,
  `building` VARCHAR(20) NULL,
  `budget` INT UNSIGNED NULL,
  PRIMARY KEY (`dept_name`));

-- 建立表student
CREATE TABLE `university`.`student` (
  `ID` INT NOT NULL,
  `name` VARCHAR(20) NULL,
  `sex` VARCHAR(20) NULL,
  `age` INT UNSIGNED NULL,
  `emtion_state` VARCHAR(45) NULL,
  `dept_name` VARCHAR(20) NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_student_1_idx` (`dept_name` ASC),
  CONSTRAINT `fk_student_1`
    FOREIGN KEY (`dept_name`)
    REFERENCES `university`.`departemnt` (`dept_name`)
    ON DELETE SET NULL
    ON UPDATE CASCADE);
    
-- 建立表exam
CREATE TABLE `university`.`exam` (
  `student_ID` INT NOT NULL,
  `exam_name` VARCHAR(45) NOT NULL,
  `grade` INT UNSIGNED NULL,
  PRIMARY KEY (`student_ID`, `exam_name`),
  CONSTRAINT `fk_exam_1`
    FOREIGN KEY (`student_ID`)
    REFERENCES `university`.`student` (`ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);
    
    