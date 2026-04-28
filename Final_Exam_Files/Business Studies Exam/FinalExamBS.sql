create database finalproject;
use finalproject;

CREATE TABLE smart_meter (
    MeterID VARCHAR(10),
    Zone VARCHAR(20),
    ConsumerType VARCHAR(20),
    Date DATE,
    EnergyConsumed_kWh DECIMAL(10,2),
    PeakUsage_kWh DECIMAL(10,2),
    OutageMinutes INT,
    MeterStatus VARCHAR(10),
    TariffRate DECIMAL(5,2)
);

INSERT INTO smart_meter VALUES
('M1000','North','Residential','2024-01-05',40.12,4.50,5,'Active',6.20),
('M1001','South','Commercial','2024-01-06',75.30,7.80,0,'Active',7.10),
('M1002','Central','Industrial','2024-01-07',90.45,9.20,20,'Faulty',8.50),
('M1003','North','Residential','2024-01-08',35.60,3.20,10,'Active',5.90),
('M1004','South','Commercial','2024-01-09',60.10,6.40,0,'Active',6.80),
('M1005','Central','Industrial','2024-01-10',88.75,8.90,25,'Faulty',8.20),
('M1006','North','Residential','2024-01-11',42.33,4.80,0,'Active',6.00),
('M1007','South','Commercial','2024-01-12',70.25,7.10,5,'Active',7.00),
('M1008','Central','Industrial','2024-01-13',95.10,9.50,40,'Faulty',8.90),
('M1009','North','Residential','2024-01-14',38.22,3.90,0,'Active',5.80),

('M1010','South','Commercial','2024-01-15',65.44,6.70,10,'Active',6.90),
('M1011','Central','Industrial','2024-01-16',92.10,9.10,30,'Faulty',8.60),
('M1012','North','Residential','2024-01-17',36.55,3.40,0,'Active',5.70),
('M1013','South','Commercial','2024-01-18',77.20,7.90,0,'Active',7.30),
('M1014','Central','Industrial','2024-01-19',89.60,8.80,15,'Faulty',8.40),
('M1015','North','Residential','2024-01-20',41.10,4.20,5,'Active',6.10),
('M1016','South','Commercial','2024-01-21',68.30,6.90,0,'Active',7.00),
('M1017','Central','Industrial','2024-01-22',93.75,9.30,35,'Faulty',8.70),
('M1018','North','Residential','2024-01-23',39.90,4.00,0,'Active',5.90),
('M1019','South','Commercial','2024-01-24',72.80,7.40,0,'Active',7.20),

('M1020','Central','Industrial','2024-01-25',91.55,9.00,20,'Faulty',8.50),
('M1021','North','Residential','2024-01-26',37.20,3.60,5,'Active',5.80),
('M1022','South','Commercial','2024-01-27',74.10,7.60,0,'Active',7.10),
('M1023','Central','Industrial','2024-01-28',96.00,9.70,50,'Faulty',9.00),
('M1024','North','Residential','2024-01-29',34.75,3.10,0,'Active',5.60),
('M1025','South','Commercial','2024-01-30',69.90,7.00,10,'Active',7.00),
('M1026','Central','Industrial','2024-01-31',87.45,8.60,15,'Faulty',8.30),
('M1027','North','Residential','2024-02-01',43.60,4.90,0,'Active',6.20),
('M1028','South','Commercial','2024-02-02',76.80,7.80,0,'Active',7.20),
('M1029','Central','Industrial','2024-02-03',94.25,9.40,25,'Faulty',8.80),

-- continuing same pattern...

('M1139','North','Residential','2024-05-23',40.50,4.40,5,'Active',6.10),
('M1140','South','Commercial','2024-05-24',73.60,7.30,0,'Active',7.10),
('M1141','Central','Industrial','2024-05-25',92.80,9.20,30,'Faulty',8.70),
('M1142','North','Residential','2024-05-26',38.10,3.80,0,'Active',5.90),
('M1143','South','Commercial','2024-05-27',70.40,7.00,0,'Active',7.00),
('M1144','Central','Industrial','2024-05-28',95.60,9.60,40,'Faulty',8.90),
('M1145','North','Residential','2024-05-29',36.90,3.50,5,'Active',5.80),
('M1146','South','Commercial','2024-05-30',75.10,7.70,0,'Active',7.20),
('M1147','Central','Industrial','2024-05-31',90.20,9.00,20,'Faulty',8.50),
('M1148','North','Residential','2024-06-01',39.75,4.10,0,'Active',6.00),
('M1149','South','Commercial','2024-06-02',71.25,7.20,0,'Active',7.10);


-- Total & Average Daily Energy Consumption by Zone

SELECT 
    Zone,
    SUM(EnergyConsumed_kWh) AS Total_Energy,
    AVG(EnergyConsumed_kWh) AS Avg_Daily_Energy
FROM smart_meter
GROUP BY Zone;

-- Top 5 Highest Energy-Consuming Consumers by Type

SELECT 
    ConsumerType,
    MeterID,
    SUM(EnergyConsumed_kWh) AS Total_Consumption
FROM smart_meter
GROUP BY ConsumerType, MeterID
ORDER BY Total_Consumption DESC
LIMIT 5;

-- Monthly Consumption Trend Across Zones

SELECT 
    Zone,
    MONTH(Date) AS Month,
    SUM(EnergyConsumed_kWh) AS Monthly_Consumption
FROM smart_meter
GROUP BY Zone, MONTH(Date)
ORDER BY Month;

-- Average Cost per Zone

SELECT 
    Zone,
    AVG(EnergyConsumed_kWh * TariffRate) AS Avg_Cost
FROM smart_meter
GROUP BY Zone;

-- Meters with Highest Faults/Outages

SELECT 
    MeterID,
    COUNT(*) AS Fault_Count,
    SUM(OutageMinutes) AS Total_Outage
FROM smart_meter
WHERE MeterStatus = 'Faulty'
GROUP BY MeterID
ORDER BY Fault_Count DESC, Total_Outage DESC
LIMIT 5;

-- Zones with Lowest Energy Efficiency

SELECT 
    Zone,
    AVG(EnergyConsumed_kWh) AS Avg_Usage,
    AVG(OutageMinutes) AS Avg_Outage
FROM smart_meter
GROUP BY Zone
ORDER BY Avg_Usage DESC, Avg_Outage DESC;

-- Peak Usage: Weekday vs Weekend

SELECT 
    CASE 
        WHEN DAYOFWEEK(Date) IN (1,7) THEN 'Weekend'
        ELSE 'Weekday'
    END AS Day_Type,
    AVG(PeakUsage_kWh) AS Avg_Peak_Usage
FROM smart_meter
GROUP BY Day_Type;
