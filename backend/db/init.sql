create database devopsroles;
use devopsroles;

CREATE TABLE appointment (
  id INT AUTO_INCREMENT PRIMARY KEY,
  subject TEXT,
  locatie TEXT,
  data TEXT,
  prenume TEXT,
  nume TEXT,
  cnp TEXT,
  email TEXT,
  telefon TEXT,
  comment TEXT
);

