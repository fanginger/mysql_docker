-- CREATE DATABASE  `testdb` 

USE `testdb`;
DROP TABLE IF EXISTS `company`;
CREATE TABLE `company` (
  `company_id` varchar(120) COLLATE utf8_unicode_ci NOT NULL,
  `company_name` varchar(120) COLLATE utf8_unicode_ci DEFAULT NULL,
  `is_ddb_client` tinyint(4) DEFAULT NULL,
  `is_erp_client` tinyint(4) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL,
  `updated_time` datetime DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- 預設儲存空間
DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `uid` varchar(120) COLLATE utf8_unicode_ci NOT NULL,
  `country` varchar(120) COLLATE utf8_unicode_ci DEFAULT NULL,
  `role` varchar(120) COLLATE utf8_unicode_ci DEFAULT NULL,
  `is_invited` tinyint(4) DEFAULT NULL,
  `job_type` varchar(120) COLLATE utf8_unicode_ci DEFAULT NULL,
  `is_ddg_user` tinyint(4) DEFAULT NULL,
  `is_ddb_user` tinyint(4) DEFAULT NULL,
  `is_ddg_buy` tinyint(4) DEFAULT NULL,
  `company_id` varchar(120) COLLATE utf8_unicode_ci DEFAULT NULL,
  `register_time` datetime DEFAULT NULL,
  `created_time` datetime DEFAULT NULL,
  `updated_time` datetime DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `user_client`;

CREATE TABLE `user_client` (
  `uid` varchar(120) COLLATE utf8_unicode_ci NOT NULL,
  `cid` varchar(120) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_time` datetime DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8; 