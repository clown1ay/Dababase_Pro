-- MySQL dump 10.13  Distrib 5.6.28, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: HR_Manage
-- ------------------------------------------------------
-- Server version	5.6.28-0ubuntu0.15.04.1

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

--
-- Table structure for table `admin_table`
--

DROP TABLE IF EXISTS `admin_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_table` (
  `user` varchar(20) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_table`
--

LOCK TABLES `admin_table` WRITE;
/*!40000 ALTER TABLE `admin_table` DISABLE KEYS */;
INSERT INTO `admin_table` VALUES ('admin','admin');
/*!40000 ALTER TABLE `admin_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bm_bm`
--

DROP TABLE IF EXISTS `bm_bm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bm_bm` (
  `bmbm` varchar(4) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `bmm` varchar(60) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`bmbm`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bm_bm`
--

LOCK TABLES `bm_bm` WRITE;
/*!40000 ALTER TABLE `bm_bm` DISABLE KEYS */;
INSERT INTO `bm_bm` VALUES ('CWB','财务部'),('PXB','培训部'),('RSB','人事部'),('WLB','外联部'),('XMB','项目部');
/*!40000 ALTER TABLE `bm_bm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bm_wh`
--

DROP TABLE IF EXISTS `bm_wh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bm_wh` (
  `whbm` varchar(10) CHARACTER SET utf8 NOT NULL,
  `whcd` varchar(16) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`whbm`),
  UNIQUE KEY `whbm_UNIQUE` (`whbm`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bm_wh`
--

LOCK TABLES `bm_wh` WRITE;
/*!40000 ALTER TABLE `bm_wh` DISABLE KEYS */;
INSERT INTO `bm_wh` VALUES ('BK','本科'),('BS','博士'),('BSH','博士后'),('DZ','大专'),('SS','硕士'),('ZK','专科');
/*!40000 ALTER TABLE `bm_wh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bm_zc`
--

DROP TABLE IF EXISTS `bm_zc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bm_zc` (
  `zcbm` varchar(10) CHARACTER SET utf8 NOT NULL,
  `zcmc` varchar(60) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`zcbm`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bm_zc`
--

LOCK TABLES `bm_zc` WRITE;
/*!40000 ALTER TABLE `bm_zc` DISABLE KEYS */;
INSERT INTO `bm_zc` VALUES ('CZ','处级'),('JZ','局级'),('KY','科员'),('KZ','科级'),('SX','实习');
/*!40000 ALTER TABLE `bm_zc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cygx`
--

DROP TABLE IF EXISTS `cygx`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cygx` (
  `autoid` int(6) NOT NULL AUTO_INCREMENT,
  `zgbm` int(6) NOT NULL,
  `Brgx` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `xm` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `job` varchar(60) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`autoid`,`zgbm`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cygx`
--

LOCK TABLES `cygx` WRITE;
/*!40000 ALTER TABLE `cygx` DISABLE KEYS */;
INSERT INTO `cygx` VALUES (3,2,'父女','李大山','医生'),(4,2,'母女','王华华','医生'),(5,6,'父子','林大波','个体经营'),(6,6,'母子','王大波','个体经营'),(7,7,'父女','张大海','教师'),(8,7,'母女','李丽','教师'),(9,7,'父女','张大山','教师'),(10,7,'母女','李丽','教师'),(11,9,'夫妻','王丽丽','医生'),(12,1,'父子','张大大','老师'),(13,1,'母子','李花花','老师'),(14,1,'兄弟','张二','运动员');
/*!40000 ALTER TABLE `cygx` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `m_dadj`
--

DROP TABLE IF EXISTS `m_dadj`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `m_dadj` (
  `zgbm` int(6) NOT NULL,
  `xm` varchar(12) CHARACTER SET utf8 NOT NULL,
  `xb` varchar(5) CHARACTER SET utf8 DEFAULT NULL,
  `mz` varchar(18) CHARACTER SET utf8 DEFAULT NULL,
  `csny` varchar(20) DEFAULT NULL,
  `hyzk` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `whcd` varchar(30) CHARACTER SET utf8 DEFAULT NULL,
  `jkzk` varchar(30) CHARACTER SET utf8 DEFAULT NULL,
  `zzmm` varchar(30) CHARACTER SET utf8 DEFAULT NULL,
  `zcbm` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `jg` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `sfzh` varchar(25) CHARACTER SET utf8 DEFAULT NULL,
  `byxx` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `zytc` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `hkszd` varchar(60) CHARACTER SET utf8 DEFAULT NULL,
  `hkxz` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `xzz` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `zw` varchar(50) CHARACTER SET utf8mb4 DEFAULT NULL,
  `gzm` varchar(30) CHARACTER SET utf8 DEFAULT NULL,
  `jspx` varchar(400) CHARACTER SET utf8 DEFAULT NULL,
  `jlcf` varchar(400) CHARACTER SET utf8 DEFAULT NULL,
  `smwt` varchar(200) CHARACTER SET utf8 DEFAULT NULL,
  `tbrqm` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `tbrq` varchar(30) DEFAULT NULL,
  `gsyj` varchar(200) CHARACTER SET utf8 DEFAULT NULL,
  `scrq` varchar(30) DEFAULT NULL,
  `ryxz` varchar(30) CHARACTER SET utf8 DEFAULT NULL,
  `rcsj` varchar(20) DEFAULT NULL,
  `ryzt` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `bz` varchar(200) CHARACTER SET utf8 DEFAULT NULL,
  `bmbm` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`zgbm`),
  KEY `wh_m_dadj` (`whcd`),
  KEY `bm_m_dadj` (`bmbm`),
  KEY `zc_m_dadj_` (`zcbm`),
  CONSTRAINT `bm_m_dadj` FOREIGN KEY (`bmbm`) REFERENCES `bm_bm` (`bmbm`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `wh_m_dadj` FOREIGN KEY (`whcd`) REFERENCES `bm_wh` (`whbm`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `zc_m_dadj_` FOREIGN KEY (`zcbm`) REFERENCES `bm_zc` (`zcbm`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `m_dadj`
--

LOCK TABLES `m_dadj` WRITE;
/*!40000 ALTER TABLE `m_dadj` DISABLE KEYS */;
INSERT INTO `m_dadj` VALUES (1,'张三','男','汉族','1993-03-03','未婚','BK','良好','群众','SX','山东省','3333333333333','哈工大','歌唱','山东省威海市','城镇','威海市文化西路2号','组长','程序员','去年培训','无','无','张三','2017-06-05','合格！','2017-06-05','实习生','2016-01-01','正常工作','无','PXB'),(2,'李四','女','汉族','1993-01-01','未婚','BS','良好','群众','SX','陕西省','22222222222','山东大学','书法','山东省威海市','城镇','烟台市××路','组长','开发人员','去年培训','无','无','李四','2017-06-04','合格！','2017-06-04','实习生','2015-01-01','正常工作','无','PXB'),(3,'王小小','女','汉族','1996-03-05','未婚','BK','良好','党员','SX','江苏省南京市','636633523665236','苏州大学','舞蹈','江苏省南京市','城镇','山东省威海市','无','技术人员','2015-01-06培训一月','无','无','王小小','2017-06-01','合格','2017-06-05','终生员工','2014-01-01','在岗','无','WLB'),(4,'曲小五','女','汉族','1990-06','未婚','SS','良好','党员','KZ','广西省南宁市','263589622522336522','广西大学','舞蹈','广西省南宁市','城镇','山东省济南市','组长','技术人员','2014-01 培训一年','2015-03二等奖励','无','曲小五','2017-05-06','合格','2017-06-06','终生员工','2013-001-01','在岗','已休假三次','XMB'),(5,'王山','男','汉族','1996-01-01','未婚','BK','良好','团员','KY','山西省太原市','6545236653314556','山东大学','跑步','山东省济南市','城镇','山东省济南市','无','技术人员','2014-09培训三个月','无','无','王山','2017-06-01','合格','2017-06-05','终生员工','2014-01-01','在岗','无','XMB'),(6,'林波波','男','汉族','1996-01-01','未婚','BK','良好','群众','KY','浙江省杭州市','4648794654897994','浙江理工大学','跑步','浙江省杭州市','城镇','山东省济南市','无','技术人员','无','无','无','林波波','2017-06-01','合格','2017-06-05','终生员工','2014-01-01','在岗','无','RSB'),(7,'张小小','女','汉族','1996-03-04','未婚','BK','良好','团员','KY','江苏省南京市','565646118797615459','南京理工大学','舞蹈','江苏省南京市','城镇','山东省济南市','无','行政人员','2014-06-03培训一年','2015优秀员工','无','张小小','2017-06-01','合格','2017-06-06','终生员工','2013-01-01','在岗','无','CWB'),(8,'薛华','男','汉族','1996-01-07','未婚','BK','良好','党员','KY','河南省郑州市','565484615613879','郑州大学','跆拳道','河南省郑州市','城镇','山东省济南市','组长','技术人员','2013-09培训三个月','2015优秀员工','无','薛华','2016-01-01','合格','2016-01-05','终生员工','2013-01-01','在岗','无','XMB'),(9,'许力','男','汉族','1990-03-01','已婚','SS','良好','党员','KZ','甘肃省兰州市','625148216548415','兰州大学','拳击','山东省济南市','城镇','山东省济南市','组长','技术人员','2013-01-01培训五个月','2014优秀员工','无','许力','2017-01-01','合格','2017-01-06','终生员工','2012-01-01','在岗','未曾休假','PXB');
/*!40000 ALTER TABLE `m_dadj` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-06-13  9:10:51
