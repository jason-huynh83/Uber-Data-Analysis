create database uber;
use uber;

create table apr14
(
    date DATE,
    lat dec(20,4),
    lon dec(20,5),
    base varchar(20)
);

describe apr14;

load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\uber-raw-data-apr14.csv'
into table apr14
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;

create table may14
(
    date DATE,
    lat dec(20,4),
    lon dec(20,5),
    base varchar(20)
);

load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\uber-raw-data-may14.csv'
into table may14
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;

create table jun14
(
    date DATE,
    lat dec(20,4),
    lon dec(20,5),
    base varchar(20)
);

load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\uber-raw-data-jun14.csv'
into table jun14
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;

create table jul14
(
    date DATE,
    lat dec(20,4),
    lon dec(20,5),
    base varchar(20)
);

load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\uber-raw-data-jul14.csv'
into table jul14
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;

create table aug14
(
    date DATE,
    lat dec(20,4),
    lon dec(20,5),
    base varchar(20)
);

load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\uber-raw-data-aug14.csv'
into table aug14
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;

select * from aug14;
select * from jul14;
select * from jun14;
select * from may14;
select * from apr14;

select date_apr, count(date_apr) from bigtable group by date_APR
union
select date_may, count(date_may) from bigtable group by date_may
union
select date_jun, count(date_jun) from bigtable group by date_jun
union
select date_jul, count(date_jul) from bigtable group by date_jul
union
select date_aug, count(date_aug) from bigtable group by date_aug;

describe may14;

create table bigtable
as
(
select apr14.date_apr, may14.date_may, jun14.date_jun, jul14.date_jul, aug14.date_aug
from apr14
join may14 on apr14.id = may14.id 
join jun14 on apr14.id = jun14.id 
join jul14 on apr14.id = jul14.id
join aug14 on apr14.id = aug14.id);

select * from bigtable;



