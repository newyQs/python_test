http://docs.peewee-orm.com/en/latest/peewee/query_examples.html

(1) 查询表中所有字段
```sql
SELECT * FROM facilities
```

(2) 查询name, membercost字段
```sql
SELECT name, membercost FROM facilities;
```

(3) 筛选where
```sql
SELECT * FROM facilities WHERE membercost > 0
```

(4) where and 多条件
```sql
SELECT facid, name, membercost, monthlymaintenance
FROM facilities
WHERE membercost > 0 AND membercost < (monthlymaintenance / 50)
```

(5) 模糊查询   name 
```sql
SELECT * FROM facilities WHERE name LIKE '%tennis%';
```

(6) in 筛选
```sql
SELECT * FROM facilities WHERE facid IN (1, 5);
```

(7) when then else end 
```sql
SELECT name,
CASE WHEN monthlymaintenance > 100 THEN 'expensive' ELSE 'cheap' END
FROM facilities;
```

(8) 时间
```sql
SELECT memid, surname, firstname, joindate FROM members
WHERE joindate >= '2012-09-01';
```

(9) 排序 order by
```sql
SELECT DISTINCT surname FROM members ORDER BY surname LIMIT 10;
```

(10) union连接
```sql
SELECT surname FROM members UNION SELECT name FROM facilities;
```

(11) 聚合函数max，最大值
```sql
SELECT MAX(join_date) FROM members;
```

(12) 子查询
```sql
SELECT firstname, surname, joindate FROM members
WHERE joindate = (SELECT MAX(joindate) FROM members);
```

(13) 多表内连接
```sql
SELECT starttime FROM bookings
INNER JOIN members ON (bookings.memid = members.memid)
WHERE surname = 'Farrell' AND firstname = 'David';
```

(14)
```sql
SELECT starttime, name
FROM bookings
INNER JOIN facilities ON (bookings.facid = facilities.facid)
WHERE date_trunc('day', starttime) = '2012-09-21':: date
  AND name LIKE 'tennis%'
ORDER BY starttime, name;
```

(15)
```sql
SELECT DISTINCT m.firstname, m.surname
FROM members AS m2
INNER JOIN members AS m ON (m.memid = m2.recommendedby)
ORDER BY m.surname, m.firstname;
```

(16)
```sql
SELECT m.firstname, m.surname, r.firstname, r.surname
FROM members AS m
LEFT OUTER JOIN members AS r ON (m.recommendedby = r.memid)
ORDER BY m.surname, m.firstname
```

(17)
```sql
SELECT DISTINCT m.firstname || ' ' || m.surname AS member, f.name AS facility
FROM members AS m
INNER JOIN bookings AS b ON (m.memid = b.memid)
INNER JOIN facilities AS f ON (b.facid = f.facid)
WHERE f.name LIKE 'Tennis%'
ORDER BY member, facility;
```

(18)
```sql
SELECT m.firstname || ' ' || m.surname AS member,
       f.name AS facility,
       (CASE WHEN m.memid = 0 THEN f.guestcost * b.slots
        ELSE f.membercost * b.slots END) AS cost
FROM members AS m
INNER JOIN bookings AS b ON (m.memid = b.memid)
INNER JOIN facilities AS f ON (b.facid = f.facid)
WHERE (date_trunc('day', b.starttime) = '2012-09-14') AND
 ((m.memid = 0 AND b.slots * f.guestcost > 30) OR
  (m.memid > 0 AND b.slots * f.membercost > 30))
ORDER BY cost DESC;
```

(19)
```sql
SELECT DISTINCT m.firstname || ' ' || m.surname AS member,
   (SELECT r.firstname || ' ' || r.surname
    FROM cd.members AS r
    WHERE m.recommendedby = r.memid) AS recommended
FROM members AS m ORDER BY member;
```

(20)
```sql
SELECT member, facility, cost from (
  SELECT
  m.firstname || ' ' || m.surname as member,
  f.name as facility,
  CASE WHEN m.memid = 0 THEN b.slots * f.guestcost
  ELSE b.slots * f.membercost END AS cost
  FROM members AS m
  INNER JOIN bookings AS b ON m.memid = b.memid
  INNER JOIN facilities AS f ON b.facid = f.facid
  WHERE date_trunc('day', b.starttime) = '2012-09-14'
) as bookings
WHERE cost > 30
ORDER BY cost DESC;
```

(21)
```sql
INSERT INTO "facilities" ("facid", "name", "membercost", "guestcost",
"initialoutlay", "monthlymaintenance") VALUES (9, 'Spa', 20, 30, 100000, 800)
```

(22)
```sql
INSERT INTO "facilities" ("facid", "name", "membercost", "guestcost",
  "initialoutlay", "monthlymaintenance")
SELECT (SELECT (MAX("facid") + 1) FROM "facilities") AS _,
        'Spa', 20, 30, 100000, 800;
```

(23)
```sql
UPDATE facilities SET initialoutlay = 10000 WHERE name = 'Tennis Court 2';
```

(24)
```sql
UPDATE facilities SET membercost=6, guestcost=30 WHERE name ILIKE 'Tennis%';
```

(25)
```sql
UPDATE facilities SET
membercost = (SELECT membercost * 1.1 FROM facilities WHERE facid = 0),
guestcost = (SELECT guestcost * 1.1 FROM facilities WHERE facid = 0)
WHERE facid = 1;

-- OR --
WITH new_prices (nmc, ngc) AS (
  SELECT membercost * 1.1, guestcost * 1.1
  FROM facilities WHERE name = 'Tennis Court 1')
UPDATE facilities
SET membercost = new_prices.nmc, guestcost = new_prices.ngc
FROM new_prices
WHERE name = 'Tennis Court 2'
```

(26)
```sql
DELETE FROM bookings;
```

(27)
```sql
DELETE FROM members WHERE memid = 37;
```

(28)
```sql
DELETE FROM members WHERE NOT EXISTS (
  SELECT * FROM bookings WHERE bookings.memid = members.memid);
```

(29)
```sql
SELECT COUNT(facid) FROM facilities;
```

(30)
```sql
SELECT COUNT(facid) FROM facilities WHERE guestcost >= 10
```