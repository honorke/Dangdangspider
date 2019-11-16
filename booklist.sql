/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50520
Source Host           : localhost:3306
Source Database       : bookstore

Target Server Type    : MYSQL
Target Server Version : 50520
File Encoding         : 65001

Date: 2019-11-16 15:26:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `booklist`
-- ----------------------------
DROP TABLE IF EXISTS `booklist`;
CREATE TABLE `booklist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` char(100) DEFAULT NULL,
  `price` char(10) DEFAULT NULL,
  `pic` char(30) DEFAULT NULL,
  `author` char(30) DEFAULT NULL,
  `publish` char(30) DEFAULT NULL,
  `time` char(20) DEFAULT NULL,
  `no` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of booklist
-- ----------------------------

