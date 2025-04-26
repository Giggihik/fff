import sqlite3
con = sqlite3.Connection('../data/gnom.db')
cur = con.cursor()
quary = '''
    CREATE TABLE clients (
      id INTEGER PRIMARY KEY,
     full_name VARCHAR(100) NOT NULL,
     flight_number TEXT NOT NULL,
     passport_data TEXT NOT NULL,
     phone_number TEXT NOT NULL,
     email TEXT NOT NULL
    );
'''
cur.execute(quary)

quary = '''INSERT INTO clients("id", "full_name", "flight_number", "passport_data", "phone_number", "email") VALUES ('3', 'Barack Hussein Obama II', 'AA2001', '6729 593467', '+7(999) 123-456 70', 'obama58cool@mail.ru'), ('4', 'Jason Michael Statham', 'BA2490 ', '5955 789043', '+7(992) 567-892 11', 'jason.boss.kfc44@mail.ru'), ('5', 'Kylie Kardashian Jenner', 'CC7902', '8903 657489', '+7(994) 789-356 33', 'kylie.beauty.queen44@gmai.com'), ('6', 'Sultanova Jumagul Baktiyarovna', 'A4444', '6972 546789', '+7(777) 444-555 66', 'giggihik@gmail.com'), ('7', 'Myrtle Wade', 'C3039', '3546 477894', '+7(999)455-788 78', 'ksoejdido@mail.ru'), ('8', 'Fred Michael', 'H19199', '5555 778888', '+7(994)677-825 90', 'huegofg@gmail.com'), ('9', 'Georgina Rodriguez ', 'A7777', '1456 098345', '+996(355)-777 77 77', 'kulerdaddy@mail.ru'), ('10', 'Sedrik Louis ', 'D5435', '6789 234567', '+996(678)-666 12 22', 'sedrikhuoi@gmail.com'), ('11', 'Dior Chanel', 'S5454', '6666 666666', '+7(234)-678 99 00', 'diorcompany@mail.ru'), ('12', 'Louis Viton ', 'M9878', '8976 234567', '+523(123)-777 88 11', 'clownguess@mail.ru'), ('13', 'Victoria Secret', 'J1551', '1551 672355', '+322(777)-999 00 00', 'giggikik@gmail.com'), ('14', 'Katie Mur', 'K67680', '8909 765577', '+7(992)-366 77 99', 'kojmina@gmail.com'), ('15', 'Samuel Frank', 'Z6788', '4356 890657', '+7(999)-555 14 99', 'gurem33@gmail.com'), ('16', 'Khabib Nurmagomedov', 'D5457', '5749 895632', '+7(999)-999 44 55', 'khabibufcboss@mail.ru'), ('17', 'Islam Makhachev', 'D5458', '5799 123456', '+7(999)-222 33 33', 'yasamyisexualnuy@gmail.com'), ('18', 'Khamzat Chimaev', 'D5459', '5788 769843', '+7(932)-445 32 45', 'khamzatgigant95@gmail.com'), ('19', ' Rodtang Jitmuangnon', 'F3245', '6666 777777', '+32(435)-982 77 66', 'ironman@mail.ru'), ('20', 'Gigi Hadid', 'C456', '8787 989897', '+45(726)-888 99 11', 'gigihadidmodel@mail.com'), ('21', 'John Johnson', 'A1324', '9876 432567', '+12(111)-666 90 76', 'justjohn00@mail.ru'), ('22', 'Mc Lovin', 'Y628', '9909 435367', '+25(767)-848 24 33', 'traxerlove@gmail.com'), ('23', 'Akpeil Supreme', 'S2132', '5768 345677', '+7(995)-324 77 98', 'akpejilllll2@mail.ru'), ('24', 'Mike Tyson', 'G2446', '5467 233590', '+32(436)-132 89 77', 'mikeboxertysongav@gmail.com'), ('25', 'Michael B. Jordan', 'W444', '4234 567890', '+66(789)-324 55 11', 'samuraiblack@mail.ru'); '''
cur.execute(quary)

quary = '''
CREATE TABLE airlines(
id INTEGER PRIMARY KEY,
name VARCHAR(100) NOT NULL,
country VARCHAR(100) NOT NULL,
iata_code TEXT NOT NULL
);
'''
cur.execute(quary)
quary = '''INSERT INTO airlines("id", "name", "country", "iata_code") VALUES ('1', 'S7', 'USA', 'ATL'), ('2', 'Emirates', 'United Arab Emirates', 'DXB'), ('3', 'All Nippon Airways', 'Japan', 'ANA'), ('4', 'China Southern Airlines', 'China', 'CSA'), ('5', 'Turkish airlines ', 'Turkey', 'TKY'), ('6', 'Austrian Airlines', 'Austria', 'AUS'), ('7', 'Kazakh Air', 'Kazakhstan ', 'KZA'), ('8', 'Value Jet', ' Vietnam', 'VLJ'), ('9', 'Virgin Australia', 'Australia', 'VAS'), ('10', 'Jetysuu', 'Kyrgyzstan', 'JTS'), ('11', 'Air India', 'India', 'AI 098'), ('12', 'Adria Airways', 'Slovenia', 'ADR'), ('13', 'Adro Servicios Aereos', 'Mexico', 'DRO'), ('14', 'Advance Air Charters', 'Canada', 'ADV'), ('15', 'Asian Air', 'Kyrgyzstan', 'AAZ'), ('16', 'Air Nigeria', 'Nigeria', 'NGP'), ('17', 'Baltic Jet Aircompany', 'Latvia', 'BJC'), ('18', 'Berkut Air', 'Kazakhstan', 'BEK'), ('19', 'Belgorod Air Enterprise', 'Russia', 'BED
'), ('20', 'Buffalo Airways', 'Canada', 'BFL'), ('21', 'Blue Bird Aviation', 'Sudan', 'BLB'), ('22', 'Coral Sun Airways', 'Kiribati', 'CSK'), ('23', 'Challenge Airlines IL', 'Israel', 'ICL'), ('24', 'Dagestan Airlines', 'Russia', 'DAG'), ('25', 'Danish Navy', 'Denmark', 'DNY'); '''
cur.execute(quary)

quary = '''
CREATE TABLE airports(
id INTEGER PRIMARY KEY,
name VARCHAR(100) NOT NULL,
country VARCHAR(100) NOT NULL,
city VARCHAR(100) NOT NULL,
iata_code TEXT NOT NULL
);
'''
cur.execute(quary)

quary = '''INSERT INTO airports("id", "name", "city", "country", "iata_code") VALUES ('1', 'Domodedovo', 'Moskow', 'Russia', 'DDV'), ('2', 'Westchase Houston', 'Houston', 'USA', 'JWH'), ('3', 'Chizhou Jiuhuashan Airport', 'Chizhou', 'China', 'JUH'), ('4', 'Fukuoka Airport', 'Fukuoka', 'Japan', 'FUK'), ('5', 'Houari Boumediene Airport', 'Algiers', 'Algeria', 'ALG'), ('6', 'Khartoum International Airport', 'Khartoum', 'Sudan', 'KRT'), ('7', 'Murtala Muhammed International Airport', 'Lagos', 'Nigeria', 'LOS'), ('8', 'Akanu Ibiam International Airport', 'Enugu', 'Nigeria', 'ENU'), ('9', 'Billy Bishop Toronto City Airport', 'Toronto', 'Canada', 'YTZ'), ('10', 'Saint John Airport', 'St. John', 'Canada', 'YSJ'), ('11', 'Hermosillo International Airport', 'Hermosillo', 'Mexico', 'HMO'), ('12', 'Villahermosa International Airport', 'Villahermosa ', 'Mexico', 'VSA'), ('13', 'Hartsfield–Jackson Atlanta International Airport', 'Atlanta', 'USA', 'ATL'), ('14', 'Midway International Airport', 'Chicago', 'USA', 'MDW'), ('15', 'Harry Reid International Airport', 'Las Vegas', 'USA', 'LAS'), ('16', 'Aktau International Airport', 'Aktau', 'Kazakhstan', 'SCO'), ('17', 'Manas International Airport', 'Bishkek', 'Kyrgyzstan', 'FRU'), ('18', 'Issyk-Kul International Airport', 'Issyk-Kul', 'Kyrgyzstan', 'IKU'), ('19', 'Lijiang Sanyi International Airport', 'Lijiang', 'China', 'LJG'), ('20', 'Lijiang Sanyi International Airport', 'Lijiang', 'China', 'LJG'), ('21', 'Gaya Airport', 'Gaya', 'India', 'GAY'), ('22', 'Phuket International Airport', 'Phuket', 'Thailand', 'HKT'), ('23', 'Can Tho International Airport', 'Can Tho', 'Vietnam', 'VCA'), ('24', 'Zayed International Airport', 'Abu-Dhabi', 'United Arab Emirate', 'AUH'), ('25', 'Graz Airport', 'Graz', 'Austria', 'GRZ'); '''
cur.execute(quary)

quary = '''
CREATE TABLE class_of_services(
id INTEGER PRIMARY KEY,
name VARCHAR(100) NOT NULL,
price FLOAT
);
'''
cur.execute(quary)

quary = '''INSERT INTO class_of_services("id", "name", "price") VALUES ('1', 'Economy', '3000'), ('2', ' Premium Economy', '3500'), ('3', 'Business', '5000'), ('4', 'First Class', '8000'); '''
cur.execute(quary)

quary = '''
CREATE TABLE flights(
id INTEGER PRIMARY KEY,
number_of_flight TEXT NOT NULL,
departure_date TIMESTAMP NOT NULL,
departure_airports_id INT,
arrival_airports_id INT,
planes_id INT,
airlines_id INT
);
'''
cur.execute(quary)

quary = '''INSERT INTO flights("id", "number_of_flight", "departure_date", "departure_airports_id", "arrival_airports_id", "planes_id", "airlines_id") VALUES ('3', 'AA2001 ', '2025-02-01 01:30:00+00', '1', '2', '1', '1'), ('4', 'BA2490 ', '2025-03-15 18:00:00+00', '2', '1', '2', '2'), ('5', 'A4444', '6222-05-04 01:06:00+00', '4', '3', '4', '3'), ('6', 'CC5678', '4566-06-02 13:00:00+00', '2', '4', '3', '4'), ('7', 'Z183', '4656-03-11 02:08:07+00', '12', '21', '9', '5'), ('8', 'J788', '3433-02-11 00:34:54+00', '13', '20', '7', '22'), ('9', 'S4544', '7877-02-21 22:43:43+00', '5', '16', '12', '7'), ('10', 'D345', '6788-05-11 02:08:59+00', '3', '25', '11', '19'), ('11', 'C536', '5533-05-05 00:44:04+00', '15', '17', '13', '16'), ('12', 'V4738', '3344-12-10 23:54:59+00', '14', '22', '20', '1'), ('13', 'F347', '3434-03-24 01:56:57+00', '6', '23', '6', '6'), ('14', 'G278', '5567-04-04 00:06:57+00', '7', '24', '14', '2'), ('15', 'L326', '2030-09-17 22:22:59+00', '14', '10', '18', '20'); '''
cur.execute(quary)

quary = '''
CREATE TABLE planes(
id INTEGER PRIMARY KEY,
model TEXT NOT NULL,
capacity INT,
airlines_id INT
);
'''
cur.execute(quary)

quary = '''INSERT INTO planes("id", "model", "capacity", "airlines_id") VALUES ('1', 'Boeing 777-300', '550', '2'), ('2', 'Boeing 747-400.', '660', '7'), ('3', 'Boeing 747-8', '700', '11'), ('4', 'Airbus A380-800', '853', '4'), ('5', 'Airbus A380-900', '900', '10'), ('6', 'Boeing 777-300ER', '550', '1'), ('7', 'Airbus A350-1000', '480', '20'), ('8', 'Airbus A340-600/300', '440', '9'), ('9', 'Boeing 787-10', '440', '6'), ('10', 'Airbus A350-900', '440', '25'), ('11', 'Ту-214 ', '210', '10'), ('12', 'Mitsubishi Regional Jet', '90', '3'), ('13', 'Bombardier Cseries A220-300 ', '150', '12'), ('14', 'Boeing 777-300', '550', '5'), ('15', 'Boeing 747-8', '700', '8'), ('16', 'Airbus A380-800', '853', '14'), ('17', 'Airbus A350-1000', '480', '15'), ('18', 'Airbus A340-600/300', '440', '16'), ('19', 'Airbus A340-600/300', '440', '17'), ('20', 'Airbus A380-900', '900', '18'), ('21', 'Airbus A380-900', '900', '19'), ('22', 'Boeing 747-400.', '660', '21'), ('23', 'Ту-214 ', '210', '22'), ('24', 'Mitsubishi Regional Jet', '90', '23'), ('25', 'Bombardier Cseries A220-300 ', '150', '24'); '''
cur.execute(quary)

quary = '''
CREATE TABLE seats(
id INTEGER PRIMARY KEY,
number_of_the_seat INT,
row INT,
class_of_services_id INT
);
'''
cur.execute(quary)

quary = '''INSERT INTO seats("id", "number_of_the_seat", "row", "class_of_services_id") VALUES ('1', '100', '3', '4'), ('2', '500', '8', '2'), ('3', '300', '5', '3'), ('4', '5', '1', '2'), ('5', '444', '4', '2'), ('6', '456', '4', '1'), ('7', '1', '1', '4'), ('8', '44', '5', '2'), ('9', '222', '9', '3'), ('10', '15', '1', '4'), ('11', '666', '20', '3'), ('12', '312', '5', '2'), ('13', '7', '1', '1'), ('14', '45', '5', '2'), ('15', '2', '1', '4'); '''
cur.execute(quary)

quary = '''
CREATE TABLE tickets(
id INTEGER PRIMARY KEY,
number TEXT NOT NULL,
date_of_purchase TIMESTAMP,
price FLOAT,
clients_id INT,
flights_id INT,
seats_id INT,
class_of_services_id INT
);
'''
cur.execute(quary)

quary = '''INSERT INTO "tickets" ("id", "number", "date_of_purchase", "price", "clients_id", "flights_id", "seats_id", "class_of_services_id") VALUES ('1', 'F333', '2024-03-01 02:44:05+00', '5000', '5', '5', '3', '3'), ('2', 'K90', '2030-12-12 12:45:59+00', '3000', '3', '6', '6', '1'), ('3', 'L522', '2024-10-28 22:30:44+00', '8000', '6', '5', '1', '4'), ('4', 'S123', '2046-11-30 01:34:55+00', '5000', '4', '3', '3', '3'), ('5', 'H777', '2000-12-31 23:01:01+00', '4000', '5', '6', '4', '2'), ('7', 'W444', '7777-12-11 05:07:59+00', '3500', '25', '6', '4', '1'), ('8', 'S2132', '3243-02-21 22:42:04+00', '5000', '23', '15', '13', '3'), ('9', 'Y628', '4542-05-22 22:22:53+00', '7000', '22', '3', '6', '3'), ('10', 'A1324', '3424-02-03 23:24:23+00', '3000', '21', '14', '11', '1'), ('11', 'K67680', '2212-04-03 22:23:23+00', '8080', '14', '13', '2', '4'), ('12', 'A7777', '6796-05-30 22:57:04+00', '8000', '9', '8', '7', '4'), ('13', 'S5454', '4343-04-22 22:43:43+00', '6000', '11', '10', '8', '3'); '''
cur.execute(quary)

# print(cur.fetchall())

con.commit()
con.close()
