/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - file_split
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`file_split` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `file_split`;

/*Table structure for table `cloudadata` */

DROP TABLE IF EXISTS `cloudadata`;

CREATE TABLE `cloudadata` (
  `filename` varchar(100) DEFAULT NULL,
  `owner` varchar(100) DEFAULT NULL,
  `f1` text,
  `skey` varchar(100) DEFAULT NULL,
  `f2` text,
  `skey1` varchar(100) DEFAULT NULL,
  `f3` varchar(100) DEFAULT NULL,
  `skey2` varchar(100) DEFAULT NULL,
  `data` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `cloudadata` */

insert  into `cloudadata`(`filename`,`owner`,`f1`,`skey`,`f2`,`skey1`,`f3`,`skey2`,`data`) values ('shiva.txt','shiva','Q60qX8qjFmcmnb74/Azwkw==','c9sEYaDZeyvimVpZjy3/jw==','udtujiZoifc=','whCM1mFn2tY=','1uy/imCJs0Wofp003P23Lg==','Fj/dGbjeDjr+bR5S/wyuhQ==','hi hello how are you');

/*Table structure for table `file` */

DROP TABLE IF EXISTS `file`;

CREATE TABLE `file` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `file` text,
  `filename` varchar(50) DEFAULT NULL,
  `CDate` varchar(20) DEFAULT NULL,
  `data` text,
  `owner` varchar(40) DEFAULT NULL,
  `pk` varchar(40) DEFAULT NULL,
  `mk` varchar(40) DEFAULT NULL,
  `privatekey` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `file` */

insert  into `file`(`id`,`file`,`filename`,`CDate`,`data`,`owner`,`pk`,`mk`,`privatekey`) values (4,'hi hello how are you','shiva.txt','2019-04-29','hi hello how are you\n','shiva','no','no',NULL);

/*Table structure for table `owner` */

DROP TABLE IF EXISTS `owner`;

CREATE TABLE `owner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(1000) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`,`username`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `owner` */

insert  into `owner`(`id`,`username`,`password`,`dob`,`email`,`city`,`contact`) values (3,'shiva','shiva','1994-05-11','shiva@gmai.com','hyd','78965412130');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `filename` varchar(40) NOT NULL,
  `data` text,
  `owner` varchar(40) DEFAULT NULL,
  `status` varchar(40) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `p1` varchar(40) DEFAULT 'no',
  `p2` varchar(40) DEFAULT 'no',
  `p3` blob,
  `s1` varchar(100) DEFAULT 'no',
  `s2` varchar(100) DEFAULT 'no',
  `s3` varchar(100) DEFAULT 'no',
  PRIMARY KEY (`filename`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`filename`,`data`,`owner`,`status`,`email`,`p1`,`p2`,`p3`,`s1`,`s2`,`s3`) values ('shiva.txt','hi hello how are you','shiva','yes','shiva.1000projects@gmail.com','Q60qX8qjFmcmnb74/Azwkw==','udtujiZoifc=','1uy/imCJs0Wofp003P23Lg==','c9sEYaDZeyvimVpZjy3/jw==','whCM1mFn2tY=','Fj/dGbjeDjr+bR5S/wyuhQ==');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(1000) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`,`username`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`id`,`username`,`password`,`dob`,`email`,`city`,`contact`) values (2,'krish','krish','1994-05-11','shiva.1000projects@gmail.com','hyd','9632587410');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
