CREATE DATABASE eg;
USE eg;

CREATE TABLE Doctor(Doctor_id VARCHAR(50) PRIMARY KEY,
                    Doctor_name VARCHAR(50) not null,
                    Doctor_address VARCHAR(150),
                    Doctor_Phone_no BIGINT CHECK (Doctor_Phone_no BETWEEN 1000000000 AND 9999999999)
                   );

CREATE TABLE Donor(Donor_id VARCHAR(50) PRIMARY KEY,
                   Donor_name VARCHAR(50),
                   Donor_Phone_no BIGINT check(Donor_Phone_no between 1000000000 and 9999999999),
                   DOB DATE,
                   Gender CHAR(10),
                   Donor_address VARCHAR(50),
                   Weight INT,
                   Blood_pressure INT,
                   Iron_content INT,
                   Doctor_id VARCHAR(50),
                   FOREIGN KEY(Doctor_id) REFERENCES Doctor(Doctor_id) ON DELETE CASCADE ON UPDATE CASCADE
                   );

CREATE TABLE Blood_bank(Blood_id INT PRIMARY KEY,
                        Blood_bank_name VARCHAR(50),
                        Blood_Bank_address VARCHAR(50)
                        );
       
CREATE TABLE Blood(Blood_group VARCHAR(20),
                   Donor_id VARCHAR(50),
                   Blood_bank_id INT,
                   PRIMARY KEY(Donor_id,Blood_bank_id),
                   FOREIGN KEY(Donor_id) REFERENCES Donor(Donor_id) ON DELETE CASCADE ON UPDATE CASCADE,
                   FOREIGN KEY(Blood_bank_id) REFERENCES Blood_bank(Blood_id) ON DELETE CASCADE ON UPDATE CASCADE
                   );

CREATE TABLE Patient(Patient_id VARCHAR(50) PRIMARY KEY,
                     Patient_name VARCHAR(20),
                     Patient_phone_no  BIGINT check(Patient_Phone_no between 1000000000 and 9999999999),
                     Patient_address VARCHAR(100),
                     Hospital_address VARCHAR(100)
                     );

CREATE TABLE Blood_delivery(Blood_bank_id INT,
                            Patient_id VARCHAR(50),
                            PRIMARY KEY(Blood_bank_id,Patient_id),
                            FOREIGN KEY(Blood_bank_id) REFERENCES Blood_bank(Blood_id) ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY(Patient_id) REFERENCES Patient(Patient_id) ON DELETE CASCADE ON UPDATE CASCADE
                            );
