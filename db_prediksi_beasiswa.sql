-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 31, 2025 at 12:48 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_prediksi_beasiswa`
--

-- --------------------------------------------------------

--
-- Table structure for table `data_akademik`
--

CREATE TABLE `data_akademik` (
  `id` int(11) NOT NULL,
  `nis` varchar(20) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `total_nilai_uts` int(11) NOT NULL,
  `total_nilai_uas` int(11) NOT NULL,
  `semester` enum('Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6') NOT NULL,
  `kelas` varchar(20) DEFAULT NULL,
  `unggah_rapor_1` varchar(255) DEFAULT NULL,
  `unggah_rapor_2` varchar(255) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data_akademik`
--

INSERT INTO `data_akademik` (`id`, `nis`, `nama`, `total_nilai_uts`, `total_nilai_uas`, `semester`, `kelas`, `unggah_rapor_1`, `unggah_rapor_2`, `timestamp`) VALUES
(27, '2324.10.132', 'Abiyyu Osa Aqillan', 870, 954, 'Semester 2', 'X TKR', 'Rapot Abiyyu Osa Aqillan smt 1.pdf', 'Rapot Abiyyu Osa Aqillan smt 2.pdf', '2025-01-31 11:04:32'),
(28, '2324.10.133', 'Achmad Fadillah ', 954, 956, 'Semester 2', 'X TKR', 'Rapot Achmad Fadillah smt 1.pdf', 'Rapot Achmad Fadillah smt 2.pdf', '2024-12-25 17:27:44'),
(29, '2324.10.134', 'Adrian Bassyah', 862, 888, 'Semester 2', 'X TKR', 'Rapot Adrian Bassyah smt 1.pdf', 'Rapot Adrian Bassyah smt 2.pdf', '2025-01-01 05:31:26'),
(30, '2324.10.135', 'Al\'Imam Syafei', 939, 988, 'Semester 2', 'X TKR', 'Rapot Al ‘Imam Syafei smt 1.pdf', 'Rapot Al’imam Syafei smt 1.pdf', '2024-12-25 17:27:44'),
(31, '2324.10.136', 'Andrew Dixa Cakrawala Yasin', 955, 962, 'Semester 2', 'X TKR', 'Rapot Andrew Dixa Cakrawala Yasin smt 1.pdf', 'Rapot Andrew Dixa Cakrawala Yasin smt 2.pdf', '2024-12-25 17:27:44'),
(32, '2324.10.144', 'Mustofa Akmal Hidayat', 988, 984, 'Semester 2', 'X TKR', 'Rapot Mustofa Akmal Hidayat smt 1.pdf', 'Rapot Mustofa Akmal Hidayat smt 2.pdf', '2024-12-25 17:27:44'),
(33, '2324.10.137', 'Arif Rahman', 782, 847, 'Semester 2', 'X TKR', 'Rapot Arif Rahman smt 1.pdf', 'Rapot Arif Rahman smt 2.pdf', '2024-12-25 17:27:44'),
(34, '2324.10.138', 'Fajri Wijayanto', 960, 983, 'Semester 2', 'X TKR', 'Rapot Fajri Wijayanto smt 1.pdf', 'Rapot Fajri Wijayanto smt 2.pdf', '2024-12-25 17:27:44'),
(35, '2324.10.139', 'Gian Luigi Farrel', 983, 1026, 'Semester 2', 'X TKR', 'Rapot Gian Luigi Farrel smt 1.pdf', 'Rapot Gian Luigi Farrel smt 2.pdf', '2024-12-25 17:27:44'),
(36, '2324.10.140', 'Jeremia Farel Lusikooy', 901, 652, 'Semester 2', 'X TKR', 'Rapot Jeremia Farel Lusikooy smt 1.pdf', 'Rapot Jeremia Farel Lusikooy smt 2.pdf', '2024-12-27 09:18:24'),
(37, '2324.10.096', 'Achmad Ghifari Adhitya', 953, 984, 'Semester 2', 'X TKJ', 'Rapot Achmad Ghifari Adhitya smt 1.pdf', 'Rapot Achmad Ghifari Adhitya smt 2.pdf', '2024-12-25 17:27:44'),
(38, '2324.10.097', 'Andri Adithia', 880, 949, 'Semester 2', 'X TKJ', 'Rapot Andri Adithia_smt 1.pdf', 'Rapot Andri Adithia_smt 2.pdf', '2025-01-28 10:41:40'),
(39, '2324.10.098', 'Anugerah Defa Putra Akbar', 964, 984, 'Semester 2', 'X TKJ', 'Rapot Anugerah Defa Putra Akbar smt 1.pdf', 'Rapot Anugerah Defa Putra Akbar smt 2.pdf', '2024-12-25 17:27:44'),
(40, '2324.10.099', 'Arka Sandi Aqillah', 1034, 1081, 'Semester 2', 'X TKJ', 'Rapot Arka Sandi Aqillah smt 1.pdf', 'Rapot Arka Sandi Aqillah smt 2.pdf', '2024-12-25 17:27:44'),
(41, '2324.10.100', 'Dadung Divi Catur Syahputra', 943, 967, 'Semester 2', 'X TKJ', 'Rapot Dadung Divi Catur Syahputra smt 1.pdf', 'Rapot Dadung Divi Catur Syahputra smt 2.pdf', '2024-12-25 17:27:44'),
(42, '2324.10.101', 'Diva Dinda Faprilia', 970, 948, 'Semester 2', 'X TKJ', 'Rapot Diva Dinda Faprilia smt 1.pdf', 'Rapot Diva Dinda Faprilia smt 2.pdf', '2024-12-25 17:27:44'),
(43, '2324.10.102', 'Farhan S', 941, 923, 'Semester 2', 'X TKJ', 'Rapot Farhan S. smt 1.pdf', 'Rapot Farhan S. smt 2.pdf', '2025-01-01 05:50:48'),
(44, '2324.10.103', 'Farhan Wahyudiantoro', 976, 986, 'Semester 2', 'X TKJ', 'Rapot Farhan Wahyudiantoro smt 1.pdf', 'Rapot Farhan Wahyudiantoro smt 2.pdf', '2024-12-25 17:27:44'),
(45, '2324.10.104', 'Fatih Aly Nugroho', 969, 966, 'Semester 2', 'X TKJ', 'Rapot Fatih Aly Nugroho smt 1.pdf', 'Rapot Fatih Aly Nugroho smt 2.pdf', '2024-12-25 17:27:44'),
(46, '2324.10.105', 'Febriano Christian Viditama R. Leo', 960, 994, 'Semester 2', 'X TKJ', 'Rapot Febriano Christian Viditama R. Leo smt 1.pdf', 'Rapot Febriano Christian Viditama R. Leo smt 2.pdf', '2024-12-25 17:27:44'),
(47, '2324.10.061', 'Ade Zazkya Fitryanti', 1022, 1052, 'Semester 2', 'X MP', 'Rapot  Ade Zazkya Fitriyanti smt 1.pdf', 'Rapot Ade Zazkya Fitryanti smt 2.pdf', '2024-12-25 17:27:44'),
(48, '2324.10.062', 'Alifia Efalina Rahmadani', 969, 1002, 'Semester 2', 'X MP', 'Rapot Alifia Efalina Rahmadani smt 1.pdf', 'Rapot Alifia Efalina Rahmadani smt 2.pdf', '2024-12-25 17:27:44'),
(49, '2324.10.063', 'Anisa Nafa Azzahra', 980, 996, 'Semester 2', 'X MP', 'Rapot Anisa Nafa Azzahra smt 1.pdf', 'Rapot Anisa Nafa Azzahra smt 2.pdf', '2024-12-25 17:27:44'),
(50, '2324.10.064', 'Arrasylah Putri Melayu', 957, 974, 'Semester 2', 'X MP', 'Rapot Arrasylah Putri Melayu smt 1.pdf', 'Rapot arrasylah putri melayu smt 2.pdf', '2024-12-25 17:27:44'),
(51, '2324.10.065', 'Caecil Shanie Gwenn', 930, 920, 'Semester 2', 'X MP', 'Rapot Caecil Shanie Gwenn smt 1.pdf', 'Rapot Caecil Shanie Gwenn smt 2.pdf', '2025-01-01 05:52:48'),
(52, '2324.10.066', 'Claudia Laeticia Abigail Rambing', 999, 1016, 'Semester 2', 'X MP', 'Rapot Claudia Laeticia Abigail Rambing smt 1.pdf', 'Rapot Claudia Laeticia Abigail Rambing smt 2.pdf', '2024-12-25 17:27:44'),
(53, '2324.10.067', 'Glory Pamela Sekar Kinanti', 1011, 1026, 'Semester 2', 'X MP', 'Rapot Glory Pamela Sekar Kinanti smt 1.pdf', 'Rapot Glory Pamela Sekar Kinanti smt 2.pdf', '2024-12-25 17:27:44'),
(54, '2324.10.068', 'Khalishah Salsabila', 1036, 1057, 'Semester 2', 'X MP', 'Rapot Khalishah Salsabila smt 1.pdf', 'Rapot Khalishah Salsabila smt 2.pdf', '2024-12-25 17:27:44'),
(55, '2324.10.069', 'Nanda Raudhatul Jannah', 1003, 1015, 'Semester 2', 'X MP', 'Rapot Nanda Raudhatul Jannah smt 1.pdf', 'Rapot Nanda Raudhatul Jannah smt 2.pdf', '2024-12-25 17:27:44'),
(56, '2324.10.070', 'Nazwa Zahiyyah', 944, 972, 'Semester 2', 'X MP', 'Rapot Nazwa Zahiyyah smt 1.pdf', 'Rapot Nazwa Zahiyyah smt 2.pdf', '2024-12-25 17:27:44'),
(57, '2324.10.035', 'Cahya Wilujeng', 995, 1014, 'Semester 2', 'X BC', 'Rapot Cahya Wilujeng smt 1.pdf', 'Rapot cahya wilujeng smt 2.pdf', '2024-12-25 17:27:44'),
(58, '2324.10.036', 'Ghaalib Permana', 942, 950, 'Semester 2', 'X BC', 'Rapot Ghaalib Permana smt 1.pdf', 'Rapot Ghaalib Permana smt 2.pdf', '2024-12-25 17:27:44'),
(60, '2324.10.037', 'Iman Syafi\'i Rachman', 958, 965, 'Semester 2', 'X BC', 'Rapot Iman Syafi’I Rachman smt 1.pdf', 'Rapot Iman Syafi’I Rachman smt 2.pdf', '2024-12-25 17:27:44'),
(61, '2324.10.038', 'Johanes Roland Putra', 902, 951, 'Semester 2', 'X BC', 'Rapot Johanes Roland Putra smt 1.pdf', 'Rapot Johanes Roland Putra smt 2.pdf', '2024-12-25 17:27:44'),
(62, '2324.10.039', 'Mariska Nur Pratama', 973, 996, 'Semester 2', 'X BC', 'Rapot Mariska Nur Pratama smt 1.pdf', 'Rapot Mariska Nur Pratama smt 2.pdf', '2024-12-25 17:27:44'),
(63, '2324.10.040', 'Rakha Faisa Ramadhan Athallah Rustandi', 952, 970, 'Semester 2', 'X BC', 'Rapot Rakha Faisa Ramadhan A.R. smt 1.pdf', 'Rapot Rakha Faisa Ramadhan A.R. smt 2.pdf', '2024-12-25 17:27:44'),
(64, '2324.10.041', 'Rizka Wulan Putri', 1001, 1029, 'Semester 2', 'X BC', 'Rapot Rizka Wulan Putri smt 1.pdf', 'Rapot Rizka Wulan Putri smt 2.pdf', '2024-12-25 17:27:44'),
(65, '2324.10.042', 'Selvi Mawarny', 981, 998, 'Semester 2', 'X BC', 'Rapot Selvi Mawarny smt 1.pdf', 'Rapot Selvi Mawarny smt 2.pdf', '2024-12-25 17:27:44'),
(66, '2324.10.043', 'Siti Soleha', 960, 993, 'Semester 2', 'X BC', 'Rapot Siti Soleha smt 1.pdf', 'Rapot Siti Soleha smt 2.pdf', '2024-12-25 17:27:44'),
(67, '2324.10.001', 'Alindra Fatih Khairunnisa', 955, 1042, 'Semester 2', 'X AK', 'Rapot Alindra Fatih Khairunnisa smt 1.pdf', 'Rapot Alindra Fatih Khairunnisa smt 2.pdf', '2024-12-25 17:27:44'),
(68, '2324.10.002', 'Anna Zasqya', 980, 1009, 'Semester 2', 'X AK', 'Rapot Anna Zasqya smt 1.pdf', 'Rapot Ana Zasqya smt 2.pdf', '2025-01-30 10:31:18'),
(69, '2324.10.003', 'Chelsy Syevyna Sirait', 981, 1012, 'Semester 2', 'X AK', 'Rapot Chelsy Stevyna Sirait smt 1.pdf', 'Rapot Chelsy Stevyna Sirait smt 2.pdf', '2024-12-25 17:27:44'),
(70, '2324.10.004', 'Cinta Is Nuraini', 994, 1020, 'Semester 2', 'X AK', 'Rapot Cinta Is Nuraini smt 1.pdf', 'Rapot Cinta Is Nuraini smt 2.pdf', '2024-12-25 17:27:44'),
(71, '2324.10.005', 'Kartika Dewi', 988, 1029, 'Semester 2', 'X AK', 'Rapot Kartika Dewi smt 1.pdf', 'Rapot Kartika Dewi smt 2.pdf', '2024-12-25 17:27:44'),
(72, '2324.10.006', 'Muthia Nur Arifin', 1005, 1030, 'Semester 2', 'X AK', 'Rapot Muthia Nur Arifin smt 1.pdf', 'Rapot Muthia Nur Arifin smt 2.pdf', '2024-12-25 17:27:44'),
(73, '2324.10.007', 'Putri Amanda Fauziyah', 969, 1013, 'Semester 2', 'X AK', 'Rapot Putri Amanda Fauziyah smt 1.pdf', 'Rapot Putri Amanda Fauziyah smt 2.pdf', '2024-12-25 17:27:44'),
(74, '2324.10.008', 'Rahmawati Bancin', 964, 1010, 'Semester 2', 'X AK', 'Rapot Rahmawati Bancin  smt 1.pdf', 'Rapot Rahmawati Bancin smt 2.pdf', '2024-12-25 17:27:44'),
(75, '2324.10.009', 'Rossy Febriani', 1008, 1018, 'Semester 2', 'X AK', 'Rapot Rossy Febriani smt 1.pdf', 'Rapot Rossy Febriani smt 2.pdf', '2024-12-25 17:27:44'),
(76, '2324.10.012', 'Win Jauza Hanifah', 1015, 1045, 'Semester 2', 'X AK', 'Rapot Win Jauza Hanifah smt 1.pdf', 'Rapot Win Jauza Hanifah smt 2.pdf', '2024-12-25 17:27:44'),
(77, '2223.10.127', 'Adian Noer Ananto', 879, 866, 'Semester 4', 'XI TKR', 'Rapot Adian Noer Ananto smt 3.pdf', 'Rapot Adian Noer Ananto smt 4.pdf', '2024-12-25 17:27:44'),
(78, '2223.10.128', 'Ahmad Al Amar Harland', 835, 865, 'Semester 4', 'XI TKR', 'Rapot Ahmad Al Amar Harland smt 3.pdf', 'Rapot Ahmad Al Amar Harland smt 4.pdf', '2024-12-25 17:27:44'),
(79, '2223.10.129', 'Ahmad Muhhazir', 576, 579, 'Semester 4', 'XI TKR', 'Rapot Ahmad Muhhazir smt 3.pdf', 'Rapot Ahmad Muhhazir smt 4.pdf', '2024-12-25 17:27:44'),
(80, '2223.10.130', 'Aldo Algadri', 925, 940, 'Semester 4', 'XI TKR', 'Rapot Aldo Algadri smt 4.pdf', 'Rapot Aldo Algadri_smt 3.pdf', '2025-01-01 05:56:32'),
(81, '2223.10.131', 'Alif Maulana', 846, 863, 'Semester 4', 'XI TKR', 'Rapot Alif Maulana smt 3.pdf', 'Rapot Alif Maulana_smt 4.pdf', '2024-12-25 17:27:44'),
(82, '2223.10.132', 'Ar Rafi', 884, 883, 'Semester 4', 'XI TKR', 'Rapot Ar Rafi smt 3.pdf', 'Rapot Ar Rafi smt 4.pdf', '2024-12-25 17:27:44'),
(83, '2223.10.133', 'Dwi Septian Al Ghifari', 828, 865, 'Semester 4', 'XI TKR', 'Rapot Dwi Septian Al Ghifari smt 3.pdf', 'Rapot Dwi Septian Al Ghifari smt 4.pdf', '2024-12-25 17:27:44'),
(84, '2223.10.134', 'Fadlan Ramadhan', 854, 875, 'Semester 4', 'XI TKR', 'Rapot Fadlan Ramadhan smt 3.pdf', 'Rapot Fadlan Ramadhan smt 4.pdf', '2024-12-25 17:27:44'),
(85, '2223.10.135', 'Farel Amartya Putra Pratama', 880, 891, 'Semester 4', 'XI TKR', 'Rapot Farel Amartya Putra Pratama smt 3.pdf', 'Rapot Farel Amartya Putra Pratama smt 4.pdf', '2024-12-25 17:27:44'),
(86, '2223.10.136', 'Ihsan Hafidh', 949, 934, 'Semester 4', 'XI TKR', 'Rapot Ihsan Hafidh smt 3.pdf', 'Rapot Ihsan Hafidh smt 4.pdf', '2024-12-27 03:13:57'),
(88, '2223.10.094', 'Abdul Muis', 829, 879, 'Semester 4', 'XI TKJ', 'Rapot Abdul Muis smt 3.pdf', 'Rapot Abdul Muis smt 4.pdf', '2024-12-25 17:27:44'),
(89, '2223.10.095', 'Ach Mycaldo Mayorga', 866, 879, 'Semester 4', 'XI TKJ', 'Rapot Ach Mycaldo Mayorga smt 3.pdf', 'Rapot Ach Mycaldo Mayorga_smt 4.pdf', '2024-12-25 17:27:44'),
(90, '2223.10.096', 'Adrian Gusti Pangestu', 830, 883, 'Semester 4', 'XI TKJ', 'Rapot Adrian Gusti Pangestu smt 3.pdf', 'Rapot Adrian Gusti Pangestu smt 4.pdf', '2024-12-25 17:27:44'),
(91, '2223.10.097', 'Ahmad Zidan', 925, 958, 'Semester 4', 'XI TKJ', 'Rapot Ahmad Zidan smt 3.pdf', 'Rapot Ahmad Zidan smt 4.pdf', '2025-01-01 05:58:24'),
(92, '2223.10.098', 'Aksa Mulla', 863, 881, 'Semester 4', 'XI TKJ', 'Rapot Aksa Mulla smt 3.pdf', 'Rapot Aksa Mulla smt 4.pdf', '2024-12-25 17:27:44'),
(93, '2223.10.099', 'Aldian Garin Sukma', 845, 866, 'Semester 4', 'XI TKJ', 'Rapot Aldian Garin Sukma smt 3.pdf', 'Rapot Aldian Garin Sukma smt 4.pdf', '2024-12-25 17:27:44'),
(94, '2223.10.100', 'Andhika Maulana Wijayadi', 842, 896, 'Semester 4', 'XI TKJ', 'Rapot Andhika Maulana Wijayadi smt 3.pdf', 'Rapot Andhika Maulana Wijayadi smt 4.pdf', '2024-12-25 17:27:44'),
(95, '2223.10.101', 'Bima Satria Bregas', 866, 889, 'Semester 4', 'XI TKJ', 'Rapot Bima Satria Bregas smt 3.pdf', 'Rapot Bima Satria Bregas smt 4.pdf', '2024-12-25 17:27:44'),
(96, '2223.10.102', 'Daniel Juan Pedor Da Silva', 904, 897, 'Semester 4', 'XI TKJ', 'Rapot Daniel Juan Pedor Da Silva smt 3.pdf', 'Rapot Daniel Juan Pedor Da Silva smt 4.pdf', '2024-12-25 17:27:44'),
(97, '2223.10.108', 'Indriani Komala Sari', 947, 954, 'Semester 4', 'XI TKJ', 'Rapot Indriani Komala Sari smt 3.pdf', 'Rapot Indriani Komala Sari smt 4.pdf', '2024-12-25 17:27:44'),
(99, '2223.10.060', 'Dwi Ferawati', 916, 964, 'Semester 4', 'XI MP', 'Rapot Dwi Ferawati_smt 3.pdf', 'Rapot Dwi Ferawati_smt 4.pdf', '2025-01-01 06:00:13'),
(100, '2223.10.061', 'Nadiatul Fadilah', 923, 902, 'Semester 4', 'XI MP', 'Rapot Nadiatul Fadilah smt 3.pdf', 'Rapot Nadiatul Fadilah smt 4.pdf', '2024-12-25 17:27:44'),
(101, '2223.10.062', 'Nazwha Ridha Nursimah', 912, 897, 'Semester 4', 'XI MP', 'Rapot Nazhwa Ridha Nursimah smt 3.pdf', 'Rapot Nazwha Ridha Nursimah smt 4.pdf', '2024-12-25 17:27:44'),
(102, '2223.10.063', 'Sasa Rahmalia', 936, 939, 'Semester 4', 'XI MP', 'Rapot Sasa Rahmalia smt 3.pdf', 'Rapot Sasa Rahmalia smt 4.pdf', '2024-12-25 17:27:44'),
(103, '2223.10.064', 'Shafira Mariana Lestari', 903, 909, 'Semester 4', 'XI MP', 'Rapot Shafira Mariana Lestari smt 3.pdf', 'Rapot Shafira Mariana Lestari smt 4.pdf', '2024-12-25 17:27:44'),
(104, '2223.10.065', 'Siti Ramona Setiadi', 957, 962, 'Semester 4', 'XI MP', 'Rapot Siti Ramona Setiadi smt 3.pdf', 'Rapot Siti Ramona Setiadi smt 4.pdf', '2024-12-25 17:27:44'),
(105, '2223.10.066', 'Vanesa Candra Wirawan', 895, 905, 'Semester 4', 'XI MP', 'Rapot Vanesa Candra Wirawan smt 3.pdf', 'Rapot Vanesa Candra Wirawan smt 4.pdf', '2024-12-25 17:27:44'),
(106, '2223.10.067', 'Widtantri Tirtamurti', 904, 902, 'Semester 4', 'XI MP', 'Rapot Widtantri Tirtamurti smt 3.pdf', 'Rapot Widtantri Tirtamurti smt 4.pdf', '2024-12-25 17:27:44'),
(107, '2223.10.068', 'Yla Sabrina Zhocy', 904, 914, 'Semester 4', 'XI MP', 'Rapot Yla Sabrina Zhocy smt 3.pdf', 'Rapot Yla Sabrina Zhocy smt 4.pdf', '2024-12-25 17:27:44'),
(108, '2223.10.025', 'Adjeng Ardhia Regita Putri', 949, 978, 'Semester 4', 'XI BC', 'Rapot Adjeng Ardhia Regita Putri smt 3.pdf', 'Rapot Adjeng Ardhia Regita Putri smt 4.pdf', '2024-12-25 17:27:44'),
(109, '2223.10.026', 'Davina Putri Syahwa', 879, 879, 'Semester 4', 'XI BC', 'Rapot Davina Putri Syahwa smt 3.pdf', 'Rapot Davina Putri Syahwa smt 4.pdf', '2024-12-25 17:27:44'),
(110, '2223.10.027', 'Du\'a Abdah', 880, 896, 'Semester 4', 'XI BC', 'Rapot Du’a Abdah smt 3.pdf', 'Rapot Du’a Abdah smt 4.pdf', '2024-12-25 17:27:44'),
(111, '2223.10.028', 'Ega Yuli Febrianto', 846, 879, 'Semester 4', 'XI BC', 'Rapot Ega Yuli Febrianto smt 3.pdf', 'Rapot Ega Yuli Febrianto smt 4.pdf', '2024-12-25 17:27:44'),
(112, '2223.10.029', 'Helena Angie', 923, 934, 'Semester 4', 'XI BC', 'Rapot Helena Angie smt 3.pdf', 'Rapot Helena Angie smt 4.pdf', '2024-12-25 17:27:44'),
(113, '2223.10.030', 'Hypolitus Marihot Neonbanu', 878, 896, 'Semester 4', 'XI BC', 'Rapot Hypolitus Marihot Neonbanu smt 3.pdf', 'Rapot Hypolitus Marihot Neonbanu smt 4.pdf', '2024-12-25 17:27:44'),
(114, '2223.10.031', 'Keyzia Ratu Topan Divani', 908, 938, 'Semester 4', 'XI BC', 'Rapot Keyzia Ratu Topan Divani smt 3.pdf', 'Rapot Keyzia Ratu Topan Divani smt 4.pdf', '2024-12-25 17:27:44'),
(115, '2223.10.032', 'Muhammad Fadhil Lubis', 884, 898, 'Semester 4', 'XI BC', 'Rapot Muhammad Fadhil Lubis smt 3.pdf', 'Rapot Muhammad Fadhil Lubis smt 4.pdf', '2024-12-25 17:27:44'),
(116, '2223.10.033', 'Muhammad Faiq Ramzi', 876, 905, 'Semester 4', 'XI BC', 'Rapot Muhammad Faiq Ramzi smt 3.pdf', 'Rapot Muhammad Faiq Ramzi smt 4.pdf', '2024-12-25 17:27:44'),
(117, '2223.10.034', 'Muhammad Febrian Bagaskara', 851, 891, 'Semester 4', 'XI BC', 'Rapot Muhammad Febrian Bagaskara smt 3.pdf', 'Rapot Muhammad Febrian Bagaskara smt 4.pdf', '2024-12-25 17:27:44'),
(118, '2223.10.036', 'Ratu Tania Efendy', 922, 942, 'Semester 4', 'XI BC', 'Rapot Ratu Tania Effendy smt 3.pdf', 'Rapot Ratu Tania Effendy smt 4.pdf', '2025-01-01 06:02:44'),
(119, '2223.10.001', 'Alif Vanop Khoirunnisyam', 927, 920, 'Semester 4', 'XI AK', 'Rapot Alif Vanop smt 3.pdf', 'Rapot Alif Vanop smt 4.pdf', '2024-12-25 17:27:44'),
(120, '2223.10.002', 'Atshilah Syahla\'Nufa', 940, 951, 'Semester 4', 'XI AK', 'Rapot Atshiilah Syahlaa\'nufa smt 3.pdf', 'Rapot Atshiilah syahla\'nufa smt 4.pdf', '2025-01-01 06:26:39'),
(123, '2223.10.004', 'Gandhi Agung Prasetyo', 939, 927, 'Semester 4', 'XI AK', 'Rapot Gandhi Agung Prasetyo smt 3.pdf', 'Rapot Gandhi Agung Prasetyo smt 4.pdf', '2024-12-25 17:27:44'),
(124, '2223.10.005', 'Hany Fatimatuz Zahra', 966, 953, 'Semester 4', 'XI AK', 'Rapot Hany Fatimatuz Zahra smt 3.pdf', 'Rapot Hany Fatimatuz Zahra smt 4.pdf', '2024-12-25 17:27:44'),
(125, '2223.10.006', 'Mohammad Farrel', 918, 912, 'Semester 4', 'XI AK', 'Rapot Mohammad Farrel smt 3.pdf', 'Rapot Mohammad Farrel smt 4.pdf', '2024-12-25 17:27:44'),
(126, '2223.10.007', 'Najwa Syifa', 921, 914, 'Semester 4', 'XI AK', 'Rapot Najwa Syifa smt 3.pdf', 'Rapot Najwa Syifa smt 4.pdf', '2024-12-25 17:27:44'),
(127, '2223.10.008', 'Nathan Bagus Setiaji', 920, 922, 'Semester 4', 'XI AK', 'Rapot Nathan Bagus Setiaji smt 3.pdf', 'Rapot Nathan Bagus Setiaji smt 4.pdf', '2024-12-25 17:27:44'),
(128, '2223.10.009', 'Putri Aulia', 928, 918, 'Semester 4', 'XI AK', 'Rapot Putri Aulia smt 3.pdf', 'Rapot Putri Aulia smt 4.pdf', '2024-12-25 17:27:44'),
(129, '2223.10.012', 'Saskia Klodiyah', 967, 957, 'Semester 4', 'XI AK', 'Rapot Saskia Klodiyah smt 3.pdf', 'Rapot Saskia Klodiyah smt 4.pdf', '2024-12-25 17:27:44'),
(130, '2223.10.003', 'Christina', 901, 905, 'Semester 4', 'XI AK', 'Rapot christina smt 3.pdf', 'Rapot christina smt 4.pdf', '2024-12-25 17:27:44'),
(131, '2223.10.059', 'Alivia Ramadani', 907, 911, 'Semester 4', 'XI MP', 'Rapot Alivia Ramadani smt 3.pdf', 'Rapot Alivia Ramadani smt 4.pdf', '2024-12-25 17:27:44');

-- --------------------------------------------------------

--
-- Table structure for table `data_non_akademik`
--

CREATE TABLE `data_non_akademik` (
  `id` int(11) NOT NULL,
  `nis` varchar(20) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `alfa_uts` int(11) NOT NULL,
  `alfa_uas` int(11) NOT NULL,
  `ekstrakurikuler_uts` int(11) NOT NULL,
  `ekstrakurikuler_uas` int(11) NOT NULL,
  `kepribadian_uts` int(11) NOT NULL,
  `kepribadian_uas` int(11) NOT NULL,
  `unggah_sertifikat` varchar(255) DEFAULT NULL,
  `semester` enum('Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6') NOT NULL,
  `kelas` varchar(20) DEFAULT NULL,
  `skor_sertifikat` int(11) NOT NULL DEFAULT 0,
  `skor_alfa` int(11) DEFAULT NULL,
  `skor_ekstrakurikuler` int(11) DEFAULT NULL,
  `skor_kepribadian` int(11) DEFAULT NULL,
  `total_score` float DEFAULT 0,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `lain_lain` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data_non_akademik`
--

INSERT INTO `data_non_akademik` (`id`, `nis`, `nama`, `alfa_uts`, `alfa_uas`, `ekstrakurikuler_uts`, `ekstrakurikuler_uas`, `kepribadian_uts`, `kepribadian_uas`, `unggah_sertifikat`, `semester`, `kelas`, `skor_sertifikat`, `skor_alfa`, `skor_ekstrakurikuler`, `skor_kepribadian`, `total_score`, `timestamp`, `lain_lain`) VALUES
(137, '2324.10.132', 'Abiyyu Osa Aqillan', 18, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X TKR', 0, 0, 80, 80, 24, '2024-12-25 17:25:08', NULL),
(139, '2324.10.133', 'Achmad Fadillah', 3, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X TKR', 0, 3, 80, 80, 25.2, '2024-12-30 14:34:17', NULL),
(140, '2324.10.134', 'Adrian Bassyah', 33, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X TKR', 0, 0, 80, 80, 24, '2024-12-30 18:07:34', NULL),
(141, '2324.10.135', 'Al\' Imam Syafei', 0, 0, 2, 2, 2, 2, 'Pemain bola 11 (2).png', 'Semester 2', 'X TKR', 61, 5, 80, 80, 44.3, '2024-12-25 17:25:08', NULL),
(142, '2324.10.136', 'Andrew Dixa Cakrawala', 0, 0, 3, 3, 2, 2, '3 orang.png', 'Semester 2', 'X TKR', 61, 5, 95, 80, 46.55, '2024-12-25 17:25:08', NULL),
(143, '2324.10.137', 'Arif Rahman', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X TKR', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(144, '2324.10.138', 'Fajri Wijayanto', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X TKR', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(145, '2324.10.139', 'Gian Luigi Farrel', 6, 0, 2, 2, 2, 2, 'Pemain bola 11 (2).png', 'Semester 2', 'X TKR', 61, 0, 80, 80, 42.3, '2024-12-25 17:25:08', NULL),
(146, '2324.10.140', 'Jeremia Farel Lusikooy', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X TKR', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(147, '2324.10.144', 'Mustofa Akmal Hidayat', 0, 0, 3, 3, 2, 2, NULL, 'Semester 2', 'X TKR', 0, 5, 95, 80, 28.25, '2024-12-25 17:25:08', NULL),
(148, '2324.10.096', 'Achmad Ghifari Adhitya', 0, 0, 2, 2, 2, 2, 'Lomba paskibra (12 orang)_1.png', 'Semester 2', 'X TKJ', 59, 5, 80, 80, 43.7, '2024-12-25 17:25:08', NULL),
(149, '2324.10.097', 'Andri Adithia', 3, 3, 2, 2, 2, 2, NULL, 'Semester 2', 'X TKJ', 0, 0, 80, 80, 24, '2024-12-25 17:25:08', NULL),
(150, '2324.10.098', 'Anugerah Defa Putra Akbar', 0, 0, 2, 2, 2, 2, 'Pemain bola 11 (2).png', 'Semester 2', 'X TKJ', 54, 5, 80, 80, 42.2, '2024-12-25 17:25:08', NULL),
(151, '2324.10.099', 'Arka Sandi Aqillah', 0, 0, 2, 2, 2, 2, 'Arka_sandi_aqillah.png', 'Semester 2', 'X TKJ', 92, 5, 80, 80, 53.6, '2024-12-25 17:25:08', NULL),
(152, '2324.10.100', 'Dadung Divi Catur Syahputra', 0, 1, 2, 2, 2, 2, NULL, 'Semester 2', 'X TKJ', 0, 3, 80, 80, 25.2, '2024-12-25 17:25:08', NULL),
(153, '2324.10.101', 'Diva Dinda Faprilila', 1, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X TKJ', 0, 3, 80, 80, 25.2, '2024-12-25 17:25:08', NULL),
(154, '2324.10.102', 'Farhan S', 0, 1, 2, 2, 2, 2, NULL, 'Semester 2', 'X TKJ', 0, 3, 80, 80, 25.2, '2024-12-25 17:25:08', NULL),
(155, '2324.10.103', 'Farhan Wahyudiantoro', 0, 0, 3, 3, 2, 2, '8 orang.png', 'Semester 2', 'X TKJ', 33, 5, 95, 80, 38.15, '2024-12-25 17:25:08', NULL),
(156, '2324.10.104', 'Fatih Aly Nugroho', 1, 1, 2, 1, 2, 2, NULL, 'Semester 2', 'X TKJ', 0, 3, 75, 80, 24.45, '2024-12-25 17:25:08', NULL),
(157, '2324.10.105', 'Febriano Christian Viditama R. Leo', 0, 0, 2, 2, 2, 2, 'FEBRIANO CHRISTIAN VIDITAMA R. LEO.png', 'Semester 2', 'X TKJ', 68, 5, 80, 80, 46.4, '2024-12-25 17:25:08', NULL),
(158, '2324.10.061', 'Ade Zazkya Fitryanti', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X MP', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(159, '2324.10.062', 'Alifia Efalina Rahmadani', 0, 0, 2, 2, 2, 2, 'Lomba paskibra (12 orang)_1.png', 'Semester 2', 'X MP', 59, 5, 80, 80, 43.7, '2024-12-25 17:25:08', NULL),
(160, '2324.10.063', 'Anisa Nala Azzahra', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X MP', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(161, '2324.10.064', 'Arrasylah Putri Melayu', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X MP', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(162, '2324.10.065', 'Caecil Shanie Gwenn', 3, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X MP', 0, 3, 80, 80, 25.2, '2024-12-25 17:25:08', NULL),
(163, '2324.10.066', 'Claudia Laeticia Abigail Rambing', 0, 0, 2, 2, 2, 2, NULL, 'Semester 1', 'X MP', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(164, '2324.10.067', 'Glory Pamela Sekar Kinanti', 0, 0, 2, 2, 2, 2, NULL, 'Semester 1', 'X MP', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(165, '2324.10.068', 'Khalishah Salsabila', 0, 0, 2, 2, 2, 2, 'Lomba paskibra (12 orang)_1.png', 'Semester 2', 'X MP', 59, 5, 80, 80, 43.7, '2024-12-25 17:25:08', NULL),
(166, '2324.10.069', 'Nanda Raudhatul Jannah', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X MP', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(167, '2324.10.070', 'Nazwa Zahiyyah', 1, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X MP', 0, 3, 80, 80, 25.2, '2024-12-25 17:25:08', NULL),
(168, '2324.10.035', 'Cahya Wilujeng', 0, 0, 2, 3, 2, 2, NULL, 'Semester 2', 'X BC', 0, 5, 88, 80, 27.125, '2024-12-30 18:15:34', NULL),
(169, '2324.10.036', 'Ghaalib Permana', 0, 3, 2, 2, 2, 2, NULL, 'Semester 2', 'X BC', 0, 3, 80, 80, 25.2, '2024-12-25 17:25:08', NULL),
(170, '2324.10.037', 'Iman Syafi\'i Rachman', 0, 2, 3, 3, 2, 2, NULL, 'Semester 2', 'X BC', 0, 3, 95, 80, 27.45, '2024-12-25 17:25:08', NULL),
(171, '2324.10.038', 'Johanes Roland Putra', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X BC', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(172, '2324.10.039', 'Mariska Nur Pratama', 0, 0, 2, 2, 2, 2, 'Mariska Nur Pratama.png', 'Semester 2', 'X BC', 59, 5, 80, 80, 43.7, '2024-12-25 17:25:08', NULL),
(175, '2324.10.040', 'Rakha Ramadhan Athallah Rustandi', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X BC', 0, 5, 80, 80, 26, '2024-12-30 18:16:22', NULL),
(176, '2324.10.041', 'Rizka Wulan Putri', 0, 0, 3, 3, 2, 2, 'Lomba paskibra (12 orang)_1.png', 'Semester 2', 'X BC', 59, 5, 95, 80, 45.95, '2024-12-25 17:25:08', NULL),
(177, '2324.10.042', 'Selvi Mawarny', 0, 0, 2, 2, 2, 2, 'Selvy Mawarny_11zon.png', 'Semester 2', 'X BC', 61, 5, 80, 80, 44.3, '2024-12-25 17:25:08', NULL),
(178, '2324.10.043', 'Siti Soleha', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X BC', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(179, '2324.10.001', 'Alindra Fatih Khairunnisa', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X AK', 0, 5, 80, 80, 26, '2024-12-30 18:17:21', NULL),
(180, '2324.10.002', 'Anna Zasqya', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X AK', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(181, '2324.10.003', 'Chelsy Stevyna Sirait', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X AK', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(182, '2324.10.004', 'Cinta Is Nuraini', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X AK', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(184, '2324.10.005', 'Kartika Dewi', 0, 0, 2, 2, 2, 2, 'Lomba paskibra (12 orang)_1.png', 'Semester 2', 'X AK', 59, 5, 80, 80, 43.7, '2024-12-25 17:25:08', NULL),
(185, '2324.10.006', 'Muthia Nur Arifin', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X AK', 0, 5, 80, 80, 26, '2024-12-30 18:18:25', NULL),
(186, '2324.10.007', 'Putri Amanda Fauziyah', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X AK', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(187, '2324.10.008', 'Rahmawati Bancin', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X AK', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(188, '2324.10.009', 'Rossy Febriani', 0, 0, 2, 2, 2, 2, NULL, 'Semester 2', 'X AK', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(190, '2324.10.012', 'Win Jauza Hanifah', 0, 0, 2, 2, 2, 2, 'Lomba paskibra (12 orang)_1.png', 'Semester 2', 'X AK', 59, 5, 80, 80, 43.7, '2024-12-25 17:25:08', NULL),
(191, '2223.10.127', 'Adian Noer Ananto', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI TKR', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(192, '2223.10.128', 'Ahmad Al Amar Harland', 1, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI TKR', 0, 3, 80, 80, 25.2, '2024-12-25 17:25:08', NULL),
(193, '2223.10.129', 'Ahmad Muhhazir', 5, 0, 1, 1, 2, 2, NULL, 'Semester 4', 'XI TKR', 0, 0, 70, 80, 22.5, '2024-12-25 17:25:08', NULL),
(194, '2223.10.130', 'Aldo Algadri', 0, 0, 2, 2, 2, 2, 'Pemain bola 11 (2).png', 'Semester 4', 'XI TKR', 54, 5, 80, 80, 42.2, '2024-12-25 17:25:08', NULL),
(195, '2223.10.131', 'Alif Maulana', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI TKR', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(196, '2223.10.132', 'Ar Rafi', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI TKR', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(197, '2223.10.133', 'Dwi Septian Al Ghifari', 0, 5, 1, 1, 2, 2, NULL, 'Semester 4', 'XI TKR', 0, 0, 70, 80, 22.5, '2024-12-25 17:25:08', NULL),
(199, '2223.10.135', 'Farel Amartya Putra Pratama', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI TKR', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(200, '2223.10.136', 'Ihsan Hafidh', 0, 0, 3, 3, 2, 2, 'Ihsan Hafidh.png', 'Semester 4', 'XI TKR', 65, 5, 95, 80, 47.75, '2024-12-25 17:25:08', NULL),
(203, '2223.10.094', 'Abdul Muis', 24, 2, 2, 2, 2, 2, NULL, 'Semester 4', 'XI TKJ', 0, 0, 80, 80, 24, '2024-12-25 17:25:08', NULL),
(204, '2223.10.095', 'Ach Mycaldo Mayorga', 1, 1, 2, 2, 2, 2, 'Lomba paskibra (12 orang)_1.png', 'Semester 4', 'XI TKJ', 59, 3, 80, 80, 42.9, '2024-12-25 17:25:08', NULL),
(205, '2223.10.096', 'Adrian Gusti Pangestu', 3, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI TKJ', 0, 3, 80, 80, 25.2, '2024-12-25 17:25:08', NULL),
(206, '2223.10.097', 'Ahmad Zidan', 0, 0, 2, 2, 2, 2, 'TKJ (3 orang).png', 'Semester 4', 'XI TKJ', 59, 5, 80, 80, 43.7, '2024-12-25 17:25:08', NULL),
(207, '2223.10.098', 'Aksa Mulla', 1, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI TKJ', 0, 3, 80, 80, 25.2, '2024-12-25 17:25:08', NULL),
(208, '2223.10.099', 'Aldian Garin Sukma', 11, 1, 2, 2, 2, 2, NULL, 'Semester 4', 'XI TKJ', 0, 0, 80, 80, 24, '2024-12-25 17:25:08', NULL),
(209, '2223.10.100', 'Andhika Maulana Wijayadi', 6, 1, 2, 2, 2, 2, NULL, 'Semester 4', 'XI TKJ', 0, 0, 80, 80, 24, '2024-12-30 18:23:03', NULL),
(210, '2223.10.101', 'Bima Satria Bregas', 1, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI TKJ', 0, 3, 80, 80, 25.2, '2024-12-25 17:25:08', NULL),
(211, '2223.10.102', 'Daniel Juan Pedor Da Silva', 1, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI TKJ', 0, 3, 80, 80, 25.2, '2024-12-25 17:25:08', NULL),
(212, '2223.10.108', 'Indriani Komala Sari', 0, 0, 3, 3, 2, 2, 'TKJ (3 orang).png', 'Semester 4', 'XI TKJ', 59, 5, 95, 80, 45.95, '2024-12-25 17:25:08', NULL),
(213, '2223.10.059', 'Alivia Ramadani', 0, 1, 2, 3, 3, 2, NULL, 'Semester 4', 'XI MP', 0, 3, 88, 88, 27.45, '2024-12-25 17:25:08', NULL),
(214, '2223.10.060', 'Dwi Ferawati', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI MP', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(215, '2223.10.061', 'Nadiatul Fadilah', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI MP', 0, 5, 80, 80, 26, '2024-12-30 18:24:30', NULL),
(216, '2223.10.062', 'Nazwha Ridha Nursimah', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI MP', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(217, '2223.10.063', 'Sasa Rahmalia', 0, 0, 3, 3, 2, 2, NULL, 'Semester 4', 'XI MP', 0, 5, 95, 80, 28.25, '2024-12-25 17:25:08', NULL),
(218, '2223.10.064', 'Shafira Mariana Lestari', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI MP', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(219, '2223.10.065', 'Siti Ramona Setiadi', 0, 0, 2, 2, 2, 2, 'Lomba paskibra (12 orang)_1.png', 'Semester 4', 'XI MP', 59, 5, 80, 80, 43.7, '2024-12-25 17:25:08', NULL),
(220, '2223.10.066', 'Vanesa Candra Wirawan', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI MP', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(221, '2223.10.067', 'Widtantri Tirtamurti', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI MP', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(222, '2223.10.068', 'Yla Sabrina Zhocy ', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI MP', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(223, '2223.10.025', 'Adjeng Ardhia Regita Putri', 0, 0, 2, 2, 2, 2, 'Lomba paskibra (12 orang)_1.png', 'Semester 4', 'XI BC', 59, 5, 80, 80, 43.7, '2024-12-25 17:25:08', NULL),
(224, '2223.10.026', 'Davina Putri Syahwa', 8, 7, 2, 2, 2, 2, NULL, 'Semester 4', 'XI BC', 0, 0, 80, 80, 24, '2024-12-25 17:25:08', NULL),
(225, '2223.10.027', 'Du\'a Abdah', 5, 4, 2, 2, 2, 2, NULL, 'Semester 4', 'XI BC', 0, 0, 80, 80, 24, '2024-12-25 17:25:08', NULL),
(226, '2223.10.028', 'Ega Yuli Febrianto', 3, 2, 2, 2, 2, 2, 'Pemain bola 11 (2).png', 'Semester 4', 'XI BC', 54, 0, 80, 80, 40.2, '2024-12-25 17:25:08', NULL),
(228, '2223.10.030', 'Hypolitus Marihot Neonbanu', 1, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI BC', 0, 3, 80, 80, 25.2, '2024-12-25 17:25:08', NULL),
(229, '2223.10.031', 'Keyzia Ratu Topan Divani', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI BC', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(230, '2223.10.032', 'Muhammad Fadhil Lubis', 0, 1, 2, 2, 2, 2, NULL, 'Semester 4', 'XI BC', 0, 3, 80, 80, 25.2, '2024-12-25 17:25:08', NULL),
(231, '2223.10.033', 'Muhammad Faiq Ramzi', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI BC', 0, 5, 80, 80, 26, '2024-12-30 18:26:11', NULL),
(232, '2223.10.034', 'Muhammad Febrian Baguskara', 5, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI BC', 0, 0, 80, 80, 24, '2024-12-25 17:25:08', NULL),
(233, '2223.10.036', 'Ratu Tania Efendy', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI BC', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(234, '2223.10.001', 'Alif Vanop Khoirunnisyam', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI AK', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(235, '2223.10.002', 'Atsiilah Syahlaa\' Nufa', 0, 0, 2, 2, 2, 2, 'ATSILLAH SYAHLAA\'NUFA.png', 'Semester 4', 'XI AK', 72, 5, 80, 80, 47.6, '2024-12-25 17:25:08', NULL),
(236, '2223.10.003', 'Christina', 13, 0, 3, 3, 2, 2, NULL, 'Semester 4', 'XI AK', 0, 0, 95, 80, 26.25, '2024-12-25 17:25:08', NULL),
(237, '2223.10.004', 'Gandhi Agung Prasetyo', 0, 0, 3, 3, 2, 2, NULL, 'Semester 4', 'XI AK', 0, 5, 95, 80, 28.25, '2024-12-25 17:25:08', NULL),
(239, '2223.10.006', 'Mohammad Farrel', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI AK', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(240, '2223.10.007', 'Najwa Syifa', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI AK', 0, 5, 80, 80, 26, '2024-12-25 17:25:08', NULL),
(241, '2223.10.008', 'Nathan Bagus Setiaji', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI AK', 0, 5, 80, 80, 26, '2024-12-30 18:27:13', NULL),
(242, '2223.10.009', 'Putri Aulia ', 10, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI AK', 0, 0, 80, 80, 24, '2024-12-25 17:25:08', NULL),
(244, '2223.10.005', 'Hany Fatimatuz Zahra', 0, 0, 2, 2, 2, 2, 'Hany Fatimatuz Zahra.png', 'Semester 4', 'XI AK', 83, 5, 80, 80, 50.9, '2024-12-30 08:45:55', NULL),
(245, '2223.10.012', 'Saskia Klodiyah', 0, 0, 2, 2, 2, 2, 'Saskia Klodiyah_1.png', 'Semester 4', 'XI AK', 75, 5, 80, 80, 48.5, '2024-12-25 17:25:08', NULL),
(246, '2223.10.029', 'Helena Angie', 0, 0, 2, 2, 2, 2, 'HELENA ANGIE.png', 'Semester 4', 'XI BC', 59, 5, 80, 80, 43.7, '2024-12-25 17:25:08', NULL),
(248, '2223.10.134', 'Fadlan Ramadhan', 0, 0, 2, 2, 2, 2, NULL, 'Semester 4', 'XI TKR', 0, 5, 80, 80, 26, '2024-12-30 18:28:09', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `data_siswa`
--

CREATE TABLE `data_siswa` (
  `id` int(11) NOT NULL,
  `nis` varchar(20) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `jenis_kelamin` enum('Laki-laki','Perempuan') NOT NULL,
  `kelas` varchar(50) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data_siswa`
--

INSERT INTO `data_siswa` (`id`, `nis`, `nama`, `jenis_kelamin`, `kelas`, `timestamp`) VALUES
(1, '2324.10.132', 'Abiyyu Osa Aqillan	', 'Laki-laki', 'X TKR', '2024-12-25 17:18:19'),
(2, '2324.10.133', 'Achmad Fadillah', 'Laki-laki', 'X TKR', '2024-12-25 17:18:19'),
(5, '2324.10.134', 'Adrian', 'Laki-laki', 'X TKR', '2024-12-25 17:18:19'),
(6, '2324.10.135', 'Al\' Imam Syafei', 'Laki-laki', 'X TKR', '2024-12-25 17:18:19'),
(7, '2324.10.136', 'Andrew Dixa Cakrawala Yasin', 'Laki-laki', 'X TKR', '2024-12-25 17:18:19'),
(15, '2324.10.144', 'Mustofa Akmal Hidayat', 'Perempuan', 'X TKR', '2024-12-25 17:18:19'),
(26, '2324.10.096', 'Achmad Ghifari Adhitya', 'Laki-laki', 'X TKJ', '2024-12-25 17:18:19'),
(27, '2324.10.097', 'Andri Adithia', 'Laki-laki', 'X TKJ', '2024-12-25 17:18:19'),
(28, '2324.10.098', 'Anugerah Defa Putra Akbar', 'Laki-laki', 'X TKJ', '2024-12-25 17:18:19'),
(29, '2324.10.099', 'Arka Sandi Aqillah', 'Laki-laki', 'X TKJ', '2024-12-25 17:18:19'),
(30, '2324.10.100', 'Dadung Divi Catur Syahputra', 'Laki-laki', 'X TKJ', '2024-12-25 17:18:19'),
(31, '2324.10.101', 'Diva Dinda Faprilia', 'Laki-laki', 'X TKJ', '2024-12-25 17:18:19'),
(32, '2324.10.102', 'Farhan S', 'Laki-laki', 'X TKJ', '2024-12-25 17:18:19'),
(33, '2324.10.103', 'Farhan Wahyudiantoro', 'Laki-laki', 'X TKJ', '2024-12-25 17:18:19'),
(34, '2324.10.104', 'Fatih Aly Nugroho ', 'Laki-laki', 'X TKJ', '2024-12-25 17:18:19'),
(35, '2324.10.105', 'Febriano Christian Viditama R. Leo', 'Laki-laki', 'X TKJ', '2024-12-25 17:18:19'),
(50, '2324.10.061', 'Ade Zazkya Fitriyanti', 'Perempuan', 'X MP', '2024-12-25 17:18:19'),
(51, '2324.10.062', 'Alifia Efalina Rahmadani', 'Perempuan', 'X MP', '2024-12-25 17:18:19'),
(52, '2324.10.063', 'Anisa Nafa Azzahra', 'Perempuan', 'X MP', '2024-12-25 17:18:19'),
(53, '2324.10.064', 'Arrasylah Putri Melayu', 'Perempuan', 'X MP', '2024-12-25 17:18:19'),
(54, '2324.10.065', 'Caecil Shanie Gwenn', 'Perempuan', 'X MP', '2024-12-25 17:18:19'),
(55, '2324.10.066', 'Claudia Laeticia Abigail Rambing', 'Perempuan', 'X MP', '2024-12-25 17:18:19'),
(56, '2324.10.067', 'Glory Pamela Sekar Kinanti', 'Perempuan', 'X MP', '2024-12-25 17:18:19'),
(57, '2324.10.068', 'Khalishah Salsabila', 'Perempuan', 'X MP', '2024-12-25 17:18:19'),
(58, '2324.10.069', 'Nanda Raudhatul Jannah', 'Perempuan', 'X MP', '2024-12-25 17:18:19'),
(60, '2324.10.070', 'Nazwa Zahiyyah', 'Perempuan', 'X MP', '2024-12-25 17:18:19'),
(69, '2324.10.035', 'Cahya Wilujeng', 'Perempuan', 'X BC', '2024-12-25 17:18:19'),
(70, '2324.10.036', 'Ghaalib Permana', 'Laki-laki', 'X BC', '2024-12-25 17:18:19'),
(71, '2324.10.037', 'Iman Syafi\'i Rachman', 'Laki-laki', 'X BC', '2024-12-25 17:18:19'),
(72, '2324.10.038', 'Johanes Roland Putra', 'Laki-laki', 'X BC', '2024-12-25 17:18:19'),
(73, '2324.10.039', 'Mariska Nur Pratama', 'Perempuan', 'X BC', '2024-12-25 17:18:19'),
(84, '2324.10.040', 'Rakha Ramadhan Athallah Rustandi', 'Laki-laki', 'X BC', '2024-12-25 17:18:19'),
(85, '2324.10.041', 'Rizka Wulan Putri', 'Perempuan', 'X BC', '2024-12-25 17:18:19'),
(86, '2324.10.042', 'Selvi Mawarny', 'Perempuan', 'X BC', '2024-12-25 17:18:19'),
(87, '2324.10.043', 'Siti Soleha', 'Perempuan', 'X BC', '2024-12-25 17:18:19'),
(88, '2324.10.001', 'Alindra Fatih Khairunnisa', 'Perempuan', 'X AK', '2024-12-25 17:18:19'),
(89, '2324.10.002', 'Anna Zasqya', 'Perempuan', 'X AK', '2024-12-25 17:18:19'),
(90, '2324.10.003', 'Chelsy Stevyna Sirait', 'Perempuan', 'X AK', '2024-12-25 17:18:19'),
(91, '2324.10.004', 'Cinta Is Nuraini', 'Perempuan', 'X AK', '2024-12-25 17:18:19'),
(92, '2324.10.005', 'Kartika Dewi', 'Perempuan', 'X AK', '2024-12-25 17:18:19'),
(93, '2324.10.006', 'Muthia Nur Arifin', 'Perempuan', 'X AK', '2024-12-25 17:18:19'),
(94, '2324.10.007', 'Putri Amanda Fauziyah', 'Perempuan', 'X AK', '2024-12-25 17:18:19'),
(95, '2324.10.008', 'Rahmawati Bancin', 'Perempuan', 'X AK', '2024-12-25 17:18:19'),
(96, '2324.10.009', 'Rossy Febriani', 'Perempuan', 'X AK', '2024-12-25 17:18:19'),
(100, '2324.10.012', 'Win Jauza Hanifah', 'Perempuan', 'X AK', '2024-12-25 17:18:19'),
(101, '2223.10.127', 'Adian Noer Ananto', 'Laki-laki', 'XI TKR', '2024-12-25 17:18:19'),
(102, '2223.10.128', 'Ahmad Al Amar Harland', 'Laki-laki', 'XI TKR', '2024-12-25 17:18:19'),
(103, '2223.10.129', 'Ahmad Muhhazir', 'Laki-laki', 'XI TKR', '2024-12-25 17:18:19'),
(104, '2223.10.130', 'Aldo Algadri', 'Laki-laki', 'XI TKR', '2024-12-25 17:18:19'),
(105, '2223.10.131', 'Alif Maulana', 'Laki-laki', 'XI TKR', '2024-12-25 17:18:19'),
(106, '2223.10.132', 'Ar Rafi', 'Laki-laki', 'XI TKR', '2024-12-25 17:18:19'),
(107, '2223.10.133', 'Dwi Septian Al Ghifari', 'Laki-laki', 'XI TKR', '2024-12-25 17:18:19'),
(108, '2223.10.134', 'Fadlan Ramadhan', 'Laki-laki', 'XI TKR', '2024-12-25 17:18:19'),
(109, '2223.10.135', 'Farel Amartya Putra Pratama', 'Laki-laki', 'XI TKR', '2024-12-25 17:18:19'),
(110, '2223.10.136', 'Ihsan Hafidh', 'Laki-laki', 'XI TKR', '2024-12-25 17:18:19'),
(117, '2223.10.094', 'Abdul Muis', 'Laki-laki', 'XI TKJ', '2024-12-25 17:18:19'),
(118, '2223.10.095', 'Ach Mycaldo Mayorga', 'Laki-laki', 'XI TKJ', '2024-12-25 17:18:19'),
(119, '2223.10.096', 'Adrian Gusti Pangestu', 'Laki-laki', 'XI TKJ', '2024-12-25 17:18:19'),
(120, '2223.10.097', 'Ahmad Zidan ', 'Laki-laki', 'XI TKJ', '2024-12-25 17:18:19'),
(121, '2223.10.098', 'Aksa Mulla', 'Laki-laki', 'XI TKJ', '2024-12-25 17:18:19'),
(122, '2223.10.099', 'Aldian Garin Sukma', 'Laki-laki', 'XI TKJ', '2024-12-25 17:18:19'),
(123, '2223.10.100', 'Andhika Maulana Wijayadi', 'Laki-laki', 'XI TKJ', '2024-12-25 17:18:19'),
(124, '2223.10.101', 'Bima Satria Bregas', 'Laki-laki', 'XI TKJ', '2024-12-25 17:18:19'),
(125, '2223.10.102', 'Daniel Juan Pedor Da Silva', 'Laki-laki', 'XI TKJ', '2024-12-25 17:18:19'),
(131, '2223.10.108', 'Indriani Komala Sari', 'Laki-laki', 'XI TKJ', '2024-12-25 17:18:19'),
(152, '2223.10.059', 'Alivia Ramadani', 'Perempuan', 'XI MP', '2024-12-25 17:18:19'),
(153, '2223.10.060', 'Dwi Ferawati', 'Perempuan', 'XI MP', '2024-12-25 17:18:19'),
(154, '2223.10.061', 'Nadiatul Fadilah', 'Perempuan', 'XI MP', '2024-12-25 17:18:19'),
(155, '2223.10.062', 'Nazwha Ridha Nursimah', 'Perempuan', 'XI MP', '2024-12-25 17:18:19'),
(156, '2223.10.063', 'Sasa Rahmalia', 'Perempuan', 'XI MP', '2024-12-25 17:18:19'),
(157, '2223.10.064', 'Shafira Mariana Lestari', 'Perempuan', 'XI MP', '2024-12-25 17:18:19'),
(158, '2223.10.065', 'Siti Ramona Setiadi', 'Perempuan', 'XI MP', '2024-12-25 17:18:19'),
(159, '2223.10.066', 'Vanesa Candra Wirawan', 'Perempuan', 'XI MP', '2024-12-25 17:18:19'),
(160, '2223.10.067', 'Widtantri Tirtamurti', 'Perempuan', 'XI MP', '2024-12-25 17:18:19'),
(161, '2223.10.068', 'Yla Sabrina Zhocy', 'Perempuan', 'XI MP', '2024-12-25 17:18:19'),
(162, '2223.10.025', 'Adjeng Ardhia Regita Putri', 'Perempuan', 'XI BC', '2024-12-25 17:18:19'),
(163, '2223.10.026', 'Davina Putri Syahwa', 'Perempuan', 'XI BC', '2024-12-25 17:18:19'),
(164, '2223.10.027', 'Du\'a Abdah ', 'Laki-laki', 'XI BC', '2024-12-25 17:18:19'),
(165, '2223.10.028', 'Ega Yuli Febrianto', 'Laki-laki', 'XI BC', '2024-12-25 17:18:19'),
(166, '2223.10.029', 'Helena Angie', 'Perempuan', 'XI BC', '2024-12-25 17:18:19'),
(167, '2223.10.030', 'Hypolitus Marihot Neonbanu', 'Laki-laki', 'XI BC', '2024-12-25 17:18:19'),
(168, '2223.10.031', 'Keyzia Ratu Topan Divani', 'Perempuan', 'XI BC', '2024-12-25 17:18:19'),
(169, '2223.10.032', 'Muhammad Fadhil Lubis', 'Laki-laki', 'XI BC', '2024-12-25 17:18:19'),
(170, '2223.10.033', 'Muhammad Faiq Ramzi', 'Laki-laki', 'XI BC', '2024-12-25 17:18:19'),
(171, '2223.10.034', 'Muhammad Febrian Bagaskara', 'Laki-laki', 'XI BC', '2024-12-25 17:18:19'),
(176, '2223.10.036', 'Ratu Tania Efendy', 'Perempuan', 'XI BC', '2024-12-25 17:18:19'),
(178, '2223.10.001', 'Alif Vanop Khoirunnisyam', 'Laki-laki', 'XI AK', '2024-12-25 17:18:19'),
(179, '2223.10.002', 'Atsilah Syahlaa\'Nufa', 'Perempuan', 'XI AK', '2024-12-25 17:18:19'),
(180, '2223.10.003', 'Christina', 'Perempuan', 'XI AK', '2024-12-25 17:18:19'),
(181, '2223.10.004', 'Gandhi Agung Prasetyo', 'Laki-laki', 'XI AK', '2024-12-25 17:18:19'),
(182, '2223.10.005', 'Hany Fatimatuz Zahra', 'Perempuan', 'XI AK', '2024-12-25 17:18:19'),
(183, '2223.10.006', 'Mohammad Farrel', 'Laki-laki', 'XI AK', '2024-12-25 17:18:19'),
(184, '2223.10.007', 'Najwa Syifa', 'Perempuan', 'XI AK', '2024-12-25 17:18:19'),
(185, '2223.10.008', 'Nathan Bagus Setiaji', 'Laki-laki', 'XI AK', '2024-12-25 17:18:19'),
(186, '2223.10.009', 'Putri Aulia', 'Perempuan', 'XI AK', '2024-12-25 17:18:19'),
(189, '2223.10.012', 'Saskia Klodiyah', 'Perempuan', 'XI AK', '2024-12-25 17:18:19'),
(193, '2324.10.137', 'Arif Rahman', 'Laki-laki', 'X TKR', '2024-12-25 17:18:19'),
(194, '2324.10.138', 'Fajri Wijayanto', 'Laki-laki', 'X TKR', '2024-12-25 17:18:19'),
(195, '2324.10.139', 'Gian Luigi Farrel', 'Laki-laki', 'X TKR', '2024-12-25 17:18:19'),
(196, '2324.10.140', 'Jeremia Farel Lusikooy', 'Laki-laki', 'X TKR', '2024-12-25 17:18:19');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `role` enum('Admin','Guru','Siswa') NOT NULL,
  `kelas_tertuju` varchar(50) DEFAULT NULL,
  `nama` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role`, `kelas_tertuju`, `nama`) VALUES
(1, 'admin', 'admin123', 'Admin', '-', NULL),
(3, 'siswa1', 'siswa123', 'Siswa', NULL, NULL),
(4, 'suwardi', 'password123', 'Guru', 'X TKR', 'suwardi Albiansyah'),
(5, 'isnaeni_fiqriyah', 'password123', 'Guru', 'X TKJ', 'isnaeni fiqriyah'),
(6, 'siti_amanda', 'password123', 'Guru', 'X MP', 'siti amanda'),
(7, 'sarah_rizki', 'password123', 'Guru', 'X BC', 'sarah rizki'),
(8, 'nunung_rustika', 'password123', 'Guru', 'X AK', 'nunung rustika'),
(9, 'septianingsih', 'password123', 'Guru', 'XI TKR', 'septianingsih'),
(10, 'afi_faturrohmah', 'password123', 'Guru', 'XI TKJ', 'afi faturrohmah'),
(11, 'sustri_karniasih', 'password123', 'Guru', 'XI MP', 'sustri karniasih'),
(12, 'lutfia_rahmawati', 'password123', 'Guru', 'XI BC', 'lutfia rahmawati'),
(13, 'diah_rachmyati', 'password123', 'Guru', 'XI AK', 'diah rachmyati');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data_akademik`
--
ALTER TABLE `data_akademik`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_data_akademik` (`nis`);

--
-- Indexes for table `data_non_akademik`
--
ALTER TABLE `data_non_akademik`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_data_non_akademik` (`nis`);

--
-- Indexes for table `data_siswa`
--
ALTER TABLE `data_siswa`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nis` (`nis`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data_akademik`
--
ALTER TABLE `data_akademik`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=139;

--
-- AUTO_INCREMENT for table `data_non_akademik`
--
ALTER TABLE `data_non_akademik`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=253;

--
-- AUTO_INCREMENT for table `data_siswa`
--
ALTER TABLE `data_siswa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=205;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `data_akademik`
--
ALTER TABLE `data_akademik`
  ADD CONSTRAINT `data_akademik_ibfk_1` FOREIGN KEY (`nis`) REFERENCES `data_siswa` (`nis`),
  ADD CONSTRAINT `fk_data_akademik` FOREIGN KEY (`nis`) REFERENCES `data_siswa` (`nis`) ON DELETE CASCADE;

--
-- Constraints for table `data_non_akademik`
--
ALTER TABLE `data_non_akademik`
  ADD CONSTRAINT `data_non_akademik_ibfk_1` FOREIGN KEY (`nis`) REFERENCES `data_siswa` (`nis`),
  ADD CONSTRAINT `fk_data_non_akademik` FOREIGN KEY (`nis`) REFERENCES `data_siswa` (`nis`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
