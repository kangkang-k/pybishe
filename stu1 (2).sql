-- MySQL dump 10.13  Distrib 5.7.32, for Win64 (x86_64)
--
-- Host: rm-8vb1z5e5731y5qj5wlo.mysql.zhangbei.rds.aliyuncs.com    Database: stu1
-- ------------------------------------------------------
-- Server version	5.7.28-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED='027217b6-7723-11eb-9778-00163e0d41fb:1-1661590';

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add test',7,'add_test'),(26,'Can change test',7,'change_test'),(27,'Can delete test',7,'delete_test'),(28,'Can view test',7,'view_test'),(29,'Can add student',8,'add_student'),(30,'Can change student',8,'change_student'),(31,'Can delete student',8,'delete_student'),(32,'Can view student',8,'view_student'),(33,'Can add teacher',9,'add_teacher'),(34,'Can change teacher',9,'change_teacher'),(35,'Can delete teacher',9,'delete_teacher'),(36,'Can view teacher',9,'view_teacher'),(37,'Can add task',10,'add_task'),(38,'Can change task',10,'change_task'),(39,'Can delete task',10,'delete_task'),(40,'Can view task',10,'view_task');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(8,'student','student'),(10,'task','task'),(9,'teacher','teacher'),(7,'TestModel','test');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-11-09 08:43:22.047809'),(2,'auth','0001_initial','2021-11-09 08:43:22.721328'),(3,'admin','0001_initial','2021-11-09 08:43:22.862449'),(4,'admin','0002_logentry_remove_auto_add','2021-11-09 08:43:22.870430'),(5,'admin','0003_logentry_add_action_flag_choices','2021-11-09 08:43:22.879449'),(6,'contenttypes','0002_remove_content_type_name','2021-11-09 08:43:22.983429'),(7,'auth','0002_alter_permission_name_max_length','2021-11-09 08:43:23.041050'),(8,'auth','0003_alter_user_email_max_length','2021-11-09 08:43:23.135429'),(9,'auth','0004_alter_user_username_opts','2021-11-09 08:43:23.143972'),(10,'auth','0005_alter_user_last_login_null','2021-11-09 08:43:23.194824'),(11,'auth','0006_require_contenttypes_0002','2021-11-09 08:43:23.198813'),(12,'auth','0007_alter_validators_add_error_messages','2021-11-09 08:43:23.207890'),(13,'auth','0008_alter_user_username_max_length','2021-11-09 08:43:23.261131'),(14,'auth','0009_alter_user_last_name_max_length','2021-11-09 08:43:23.322600'),(15,'auth','0010_alter_group_name_max_length','2021-11-09 08:43:23.380541'),(16,'auth','0011_update_proxy_permissions','2021-11-09 08:43:23.389555'),(17,'auth','0012_alter_user_first_name_max_length','2021-11-09 08:43:23.450303'),(18,'sessions','0001_initial','2021-11-09 08:43:23.506615'),(19,'TestModel','0001_initial','2021-11-09 08:44:18.470481'),(20,'student','0001_initial','2021-11-09 09:41:09.205219'),(21,'teacher','0001_initial','2021-11-09 12:01:38.430273'),(22,'student','0002_alter_student_id','2021-11-09 12:32:57.997521'),(23,'teacher','0002_teacher_clzz','2021-11-09 13:13:56.856424'),(24,'teacher','0003_auto_20211109_2113','2021-11-09 13:13:56.861375'),(25,'task','0001_initial','2021-11-09 13:31:22.855371'),(26,'student','0003_auto_20211110_1036','2021-11-10 02:36:47.741055'),(27,'student','0004_auto_20211110_1037','2021-11-10 02:37:58.314154'),(28,'student','0005_auto_20211110_1038','2021-11-10 02:38:42.600561'),(29,'student','0006_auto_20211110_1041','2021-11-10 02:41:39.482577'),(30,'student','0002_alter_student_stuid','2021-11-10 02:55:27.356654');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `upgrade_student`
--

DROP TABLE IF EXISTS `poor_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `poor_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `grade` varchar(100) DEFAULT NULL COMMENT '贫困等级',
  `poor_number` varchar(100) DEFAULT NULL COMMENT '贫困的数量',
  `student_id` int(11) DEFAULT NULL COMMENT '贫困学生id',
  `create_time` varchar(100) DEFAULT NULL COMMENT '创建时间',
  `update_time` varchar(100) DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COMMENT='贫困学生';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `upgrade_student`
--

LOCK TABLES `poor_student` WRITE;
/*!40000 ALTER TABLE `upgrade_student` DISABLE KEYS */;
INSERT INTO `poor_student` VALUES (1,'1级','10',19205250,'2021-12-10 23:33:20','2021-12-10 23:33:20'),(2,'1级','10',123123,'2021-12-10 23:34:06','2021-12-10 23:34:06'),(3,'1级','10',1234123,'2021-12-10 23:34:13','2021-12-10 23:34:13'),(4,'1级','10',123132123,'2021-12-10 23:34:21','2021-12-10 23:34:21'),(5,'1','121',1,'2021-12-11 13:28:02','2021-12-11 13:28:02');
/*!40000 ALTER TABLE `upgrade_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_admin`
--

DROP TABLE IF EXISTS `tb_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL COMMENT '帐号',
  `password` varchar(100) DEFAULT NULL COMMENT '密码',
  `email` char(100) DEFAULT NULL,
  `create_time` varchar(100) DEFAULT NULL COMMENT '创建时间',
  `update_time` varchar(100) DEFAULT NULL,
  `remarks` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='管理员表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_admin`
--

LOCK TABLES `tb_admin` WRITE;
/*!40000 ALTER TABLE `tb_admin` DISABLE KEYS */;
INSERT INTO `tb_admin` VALUES (1,'zhangxiaofei','e10adc3949ba59abbe56e057f20f883e','admin','2021-12-10 23:48:56','2021-12-11 14:14:29','111'),(3,'dsa111','a66abb5684c45962d887564f08346e8d','admin','2021-12-11 13:57:07','2021-12-11 14:00:06','dsa');
/*!40000 ALTER TABLE `tb_admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_attendance`
--

DROP TABLE IF EXISTS `tb_attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_attendance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(100) DEFAULT NULL COMMENT '课程名称',
  `late` varchar(100) DEFAULT NULL COMMENT '迟到人数',
  `late_time` varchar(100) DEFAULT NULL COMMENT '迟到时间',
  `create_time` varchar(100) DEFAULT NULL COMMENT '创建时间',
  `signIn` varchar(100) DEFAULT NULL COMMENT '签到人数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='签到统计表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_attendance`
--

LOCK TABLES `tb_attendance` WRITE;
/*!40000 ALTER TABLE `tb_attendance` DISABLE KEYS */;
INSERT INTO `tb_attendance` VALUES (1,'高数',NULL,'10','2021-12-10 23:58:18','111'),(2,'2','1','12','2021-12-11 13:41:27','100');
/*!40000 ALTER TABLE `tb_attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_student`
--

DROP TABLE IF EXISTS `tb_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stuId` varchar(20) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `s1` varchar(10) DEFAULT '0' COMMENT '已修学分',
  `s2` varchar(10) DEFAULT '0' COMMENT '未修学分',
  `s3` varchar(10) DEFAULT '0' COMMENT '必修学分',
  `college` varchar(200) DEFAULT '人工智能与大数据学院',
  `speciality` varchar(200) DEFAULT '软件技术',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8 COMMENT='学生表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_student`
--

LOCK TABLES `tb_student` WRITE;
/*!40000 ALTER TABLE `tb_student` DISABLE KEYS */;
INSERT INTO `tb_student` VALUES (2,'19205250','王飞','e10adc3949ba59abbe56e057f20f883e',NULL,'100','90','130','人工智能与大数据学院','软件技术'),(3,'123123','123123','4297f44b13955235245b2497399d7a93',NULL,'2','22','22','人工智能与大数据学院','软件技术'),(4,'1234123','123','202cb962ac59075b964b07152d234b70',NULL,'2','2','2','人工智能与大数据学院','软件技术'),(7,'123132123','王飞','4297f44b13955235245b2497399d7a93',NULL,'22','11','22','人工智能与大数据学院','软件技术'),(14,'123123123','李三','4297f44b13955235245b2497399d7a93',NULL,'','','','人工智能与大数据学院','软件技术'),(20,'123','张大富','4297f44b13955235245b2497399d7a93',NULL,'123','123','22','信息工程学院','软件技术'),(22,'121212','123123','202cb962ac59075b964b07152d234b70',NULL,'','','','',''),(23,'4343434','3434','14c879f3f5d8ed93a09f6090d77c2cc3',NULL,'','','','',''),(24,'32453245','3245234','66121d1f782d29b62a286909165517bc',NULL,'','','','',''),(25,'324324234','231231','4297f44b13955235245b2497399d7a93',NULL,'','','','','');
/*!40000 ALTER TABLE `tb_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_teacher`
--

DROP TABLE IF EXISTS `tb_teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `password` varchar(80) NOT NULL,
  `clzz` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COMMENT='教师表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_teacher`
--

LOCK TABLES `tb_teacher` WRITE;
/*!40000 ALTER TABLE `tb_teacher` DISABLE KEYS */;
INSERT INTO `tb_teacher` VALUES (1,'张启林','e10adc3949ba59abbe56e057f20f883e','1'),(2,'好老师','e10adc3949ba59abbe56e057f20f883e','1'),(3,'苏老师','e10adc3949ba59abbe56e057f20f883e','1'),(4,'张老师','e10adc3949ba59abbe56e057f20f883e','1'),(5,'王老师','e10adc3949ba59abbe56e057f20f883e','1'),(6,'小小张','e10adc3949ba59abbe56e057f20f883e',''),(7,'王飞1','4297f44b13955235245b2497399d7a93',''),(8,'张腾飞33','4297f44b13955235245b2497399d7a93',''),(9,'123','202cb962ac59075b964b07152d234b70',''),(10,'1234','81dc9bdb52d04dc20036dbd8313ed055',''),(11,'12345','827ccb0eea8a706c4c34a16891f84e7b','');
/*!40000 ALTER TABLE `tb_teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_topic`
--

DROP TABLE IF EXISTS `tb_topic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_topic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stuId` varchar(20) NOT NULL,
  `title` varchar(200) DEFAULT NULL,
  `content` longtext,
  `status` tinyint(1) DEFAULT '0' COMMENT '0 未提交,1已提交,待审核, 2审核通过 3 打回',
  `teacherId` int(11) NOT NULL,
  `notes` varchar(200) DEFAULT '' COMMENT '备注',
  `studentName` varchar(200) DEFAULT NULL COMMENT '学生名字',
  `teacherName` varchar(200) DEFAULT NULL,
  `topicFile` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COMMENT='选题';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_topic`
--

LOCK TABLES `tb_topic` WRITE;
/*!40000 ALTER TABLE `tb_topic` DISABLE KEYS */;
INSERT INTO `tb_topic` VALUES (5,'123123123','基于Django的毕业设计管理系统设计与实现','<div class=\"WordSection1\">\n\n<p class=\"MsoNormal\" align=\"center\"><span lang=\"EN-US\" times=\"\" new=\"\" roman\";=\"\" position:relative;top:-9.0pt;mso-text-raise:9.0pt\');
/*!40000 ALTER TABLE `tb_topic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testmodel_test`
--

DROP TABLE IF EXISTS `testmodel_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testmodel_test` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testmodel_test`
--

LOCK TABLES `testmodel_test` WRITE;
/*!40000 ALTER TABLE `testmodel_test` DISABLE KEYS */;
INSERT INTO `testmodel_test` VALUES (1,'zs'),(2,'zs');
/*!40000 ALTER TABLE `testmodel_test` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-11 23:08:05
