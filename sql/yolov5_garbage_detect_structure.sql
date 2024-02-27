/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80032
 Source Host           : localhost:3306
 Source Schema         : yolov5_garbage_detect

 Target Server Type    : MySQL
 Target Server Version : 80032
 File Encoding         : 65001

 Date: 20/05/2023 21:24:23
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for captcha
-- ----------------------------
DROP TABLE IF EXISTS `captcha`;
CREATE TABLE `captcha` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) DEFAULT NULL COMMENT '验证邮箱',
  `captcha` varchar(100) NOT NULL COMMENT '验证码',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `is_used` tinyint(1) DEFAULT NULL COMMENT '是否使用',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for dataset
-- ----------------------------
DROP TABLE IF EXISTS `dataset`;
CREATE TABLE `dataset` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '数据集id',
  `dataset_name` varchar(100) NOT NULL COMMENT '数据集名称',
  `class_num` int NOT NULL COMMENT '类别数量',
  `total_num` int NOT NULL COMMENT '总数量',
  `train_num` int NOT NULL COMMENT '训练集数量',
  `val_num` int NOT NULL COMMENT '验证集数量',
  `test_exist` tinyint(1) NOT NULL COMMENT '是否存在测试集',
  `test_num` int DEFAULT NULL COMMENT '测试集数量',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for detect_result
-- ----------------------------
DROP TABLE IF EXISTS `detect_result`;
CREATE TABLE `detect_result` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '检测结果id',
  `detect_result` text NOT NULL COMMENT '检测结果',
  `detect_result_image_name` varchar(100) NOT NULL COMMENT '检测结果图片名称',
  `detect_time` datetime DEFAULT NULL COMMENT '检测时间',
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `detect_result_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for image
-- ----------------------------
DROP TABLE IF EXISTS `image`;
CREATE TABLE `image` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '图片id',
  `image_name` varchar(100) NOT NULL COMMENT '图片名称',
  `image_absolute_path` text COMMENT '图片绝对路径',
  `image_relative_path` text COMMENT '图片相对路径',
  `image_type` varchar(100) NOT NULL COMMENT '图片类型',
  `dataset_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dataset_id` (`dataset_id`),
  CONSTRAINT `image_ibfk_1` FOREIGN KEY (`dataset_id`) REFERENCES `dataset` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for image_label_info
-- ----------------------------
DROP TABLE IF EXISTS `image_label_info`;
CREATE TABLE `image_label_info` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '图片标注信息id',
  `image_id` int DEFAULT NULL COMMENT '图片id',
  `label_id` int DEFAULT NULL COMMENT '标注id',
  PRIMARY KEY (`id`),
  KEY `image_id` (`image_id`),
  KEY `label_id` (`label_id`),
  CONSTRAINT `image_label_info_ibfk_1` FOREIGN KEY (`image_id`) REFERENCES `image` (`id`),
  CONSTRAINT `image_label_info_ibfk_2` FOREIGN KEY (`label_id`) REFERENCES `label` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for label
-- ----------------------------
DROP TABLE IF EXISTS `label`;
CREATE TABLE `label` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '标注id',
  `label_name` varchar(100) NOT NULL COMMENT '标注名称',
  `dataset_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dataset_id` (`dataset_id`),
  CONSTRAINT `label_ibfk_1` FOREIGN KEY (`dataset_id`) REFERENCES `dataset` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '角色id',
  `role_name` varchar(100) NOT NULL COMMENT '角色名称',
  `role_desc` varchar(100) NOT NULL COMMENT '角色描述',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `username` varchar(100) NOT NULL COMMENT '用户名',
  `password` varchar(500) NOT NULL COMMENT '密码',
  `email` varchar(100) NOT NULL COMMENT '邮箱',
  `join_time` datetime DEFAULT NULL COMMENT '加入时间',
  `status` tinyint(1) DEFAULT NULL COMMENT '是否启用',
  `role_id` int DEFAULT NULL COMMENT '用户角色',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2007 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for weights
-- ----------------------------
DROP TABLE IF EXISTS `weights`;
CREATE TABLE `weights` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '权重id',
  `weights_name` varchar(100) NOT NULL COMMENT '权重名称',
  `weights_relative_path` text NOT NULL COMMENT '权重相对路径',
  `weights_absolute_path` text COMMENT '权重绝对路径',
  `weights_version` varchar(100) NOT NULL COMMENT '权重版本',
  `enable` tinyint(1) NOT NULL COMMENT '是否启用',
  `dataset_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dataset_id` (`dataset_id`),
  CONSTRAINT `weights_ibfk_1` FOREIGN KEY (`dataset_id`) REFERENCES `dataset` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SET FOREIGN_KEY_CHECKS = 1;
