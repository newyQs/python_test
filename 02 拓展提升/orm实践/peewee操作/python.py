from .model import Member, Facility, Booking
from peewee import Case, fn, JOIN, SQL, Select
from datetime import datetime

# (1)
query = Facility.select()

# (2)
query = Facility.select(Facility.name, Facility.membercost)

# To iterate:
for facility in query:
    print(facility.name)

# (3)
query = Facility.select().where(Facility.membercost > 0)

# (4)
query = (
    Facility.select(
        Facility.facid, Facility.name, Facility.membercost, Facility.monthlymaintenance
    ).where(
        (Facility.membercost > 0) & (Facility.membercost < (Facility.monthlymaintenance / 50))
    )

)

# (5)
query = Facility.select().where(Facility.name.contains('tennis'))
# 或者
query = Facility.select().where(Facility.name ** '%tennis%')

# (6)
query = Facility.select().where(Facility.facid.in_([1, 5]))
# 或者
query = Facility.select().where((Facility.facid == 1) | (Facility.facid == 5))

# (7)
cost = Case(None, [(Facility.monthlymaintenance > 100, 'expensive')], 'cheap')
query = Facility.select(Facility.name, cost.alias('cost'))

# (8)
query = (
    Member.select(
        Member.memid, Member.surname, Member.firstname, Member.joindate
    ).where(
        Member.joindate >= datetime.date(2012, 9, 1)
    )

)

# (9)
query = (
    Member
        .select(Member.surname)
        .order_by(Member.surname)
        .limit(10)
        .distinct()
)

# (10)
lhs = Member.select(Member.surname)
rhs = Facility.select(Facility.name)
query = lhs | rhs

# 注：
# | - UNION
# + - UNION ALL
# & - INTERSECT
# - - EXCEPT

# (11)
query = Member.select(fn.MAX(Member.joindate))

# (12)
MemberAlias = Member.alias()
subq = MemberAlias.select(fn.MAX(MemberAlias.joindate))
query = (
    Member
        .select(Member.firstname, Member.surname, Member.joindate)
        .where(Member.joindate == subq)
)

# (13)
query = (
    Booking
        .select(Booking.starttime)
        .join(Member)
        .where((Member.surname == 'Farrell') & (Member.firstname == 'David'))
)

# (14)
query = (
    Booking
        .select(Booking.starttime, Facility.name)
        .join(Facility)
        .where(
        (fn.date_trunc('day', Booking.starttime) == datetime.date(2012, 9, 21)) &
        Facility.name.startswith('Tennis'))
        .order_by(Booking.starttime, Facility.name)
)

# To retrieve the joined facility's name when iterating:
for booking in query:
    print(booking.starttime, booking.facility.name)

# (15)
MA = Member.alias()
query = (
    Member
        .select(Member.firstname, Member.surname)
        .join(MA, on=(MA.recommendedby == Member.memid))
        .order_by(Member.surname, Member.firstname)
)

# (16)
MA = Member.alias()
query = (
    Member
        .select(Member.firstname, Member.surname, MA.firstname, MA.surname)
        .join(MA, JOIN.LEFT_OUTER, on=(Member.recommendedby == MA.memid))
        .order_by(Member.surname, Member.firstname)
)

for m in query:
    print(m.firstname, m.surname)
    if m.recommendedby:
        print('  ', m.recommendedby.firstname, m.recommendedby.surname)

# (17)
fullname = Member.firstname + ' ' + Member.surname
query = (Member
         .select(fullname.alias('member'), Facility.name.alias('facility'))
         .join(Booking)
         .join(Facility)
         .where(Facility.name.startswith('Tennis'))
         .order_by(fullname, Facility.name)
         .distinct())

# (18)
cost = Case(Member.memid, (
    (0, Booking.slots * Facility.guestcost),
), (Booking.slots * Facility.membercost))
fullname = Member.firstname + ' ' + Member.surname

query = (
    Member
        .select(fullname.alias('member'), Facility.name.alias('facility'),
                cost.alias('cost'))
        .join(Booking)
        .join(Facility)
        .where(
        (fn.date_trunc('day', Booking.starttime) == datetime.date(2012, 9, 14)) &
        (cost > 30))
        .order_by(SQL('cost').desc())
)

# To iterate over the results, it might be easiest to use namedtuples:
for row in query.namedtuples():
    print(row.member, row.facility, row.cost)

# (19)
MA = Member.alias()
subq = (
    MA
        .select(MA.firstname + ' ' + MA.surname)
        .where(Member.recommendedby == MA.memid)
)
query = (
    Member
        .select(fullname.alias('member'), subq.alias('recommended'))
        .order_by(fullname)
)

# (20)
cost = Case(Member.memid, (
    (0, Booking.slots * Facility.guestcost),
), (Booking.slots * Facility.membercost))

iq = (
    Member
        .select(fullname.alias('member'), Facility.name.alias('facility'),
                cost.alias('cost'))
        .join(Booking)
        .join(Facility)
        .where(fn.date_trunc('day', Booking.starttime) == datetime.date(2012, 9, 14))
)

query = (
    Member
        .select(iq.c.member, iq.c.facility, iq.c.cost)
        .from_(iq)
        .where(iq.c.cost > 30)
        .order_by(SQL('cost').desc())
)

# To iterate, try using dicts:
for row in query.dicts():
    print(row['member'], row['facility'], row['cost'])

# (21)
res = Facility.insert({
    Facility.facid: 9,
    Facility.name: 'Spa',
    Facility.membercost: 20,
    Facility.guestcost: 30,
    Facility.initialoutlay: 100000,
    Facility.monthlymaintenance: 800}).execute()

# OR:
res = (Facility
       .insert(facid=9, name='Spa', membercost=20, guestcost=30,
               initialoutlay=100000, monthlymaintenance=800)
       .execute())

# 插入多条数据
data = [
    {'facid': 9, 'name': 'Spa', 'membercost': 20, 'guestcost': 30,
     'initialoutlay': 100000, 'monthlymaintenance': 800},
    {'facid': 10, 'name': 'Squash Court 2', 'membercost': 3.5,
     'guestcost': 17.5, 'initialoutlay': 5000, 'monthlymaintenance': 80}]
res = Facility.insert_many(data).execute()

# (22)
maxq = Facility.select(fn.MAX(Facility.facid) + 1)
subq = Select(columns=(maxq, 'Spa', 20, 30, 100000, 800))
res = Facility.insert_from(subq, Facility._meta.sorted_fields).execute()

# (23)
res = (Facility
       .update({Facility.initialoutlay: 10000})
       .where(Facility.name == 'Tennis Court 2')
       .execute())

# 或者
res = (Facility
       .update(initialoutlay=10000)
       .where(Facility.name == 'Tennis Court 2')
       .execute())

# (24)
nrows = (Facility
         .update(membercost=6, guestcost=30)
         .where(Facility.name.startswith('Tennis'))
         .execute())

# (25)
sq1 = Facility.select(Facility.membercost * 1.1).where(Facility.facid == 0)
sq2 = Facility.select(Facility.guestcost * 1.1).where(Facility.facid == 0)

res = (Facility
       .update(membercost=sq1, guestcost=sq2)
       .where(Facility.facid == 1)
       .execute())

# 或者
cte = (Facility
       .select(Facility.membercost * 1.1, Facility.guestcost * 1.1)
       .where(Facility.name == 'Tennis Court 1')
       .cte('new_prices', columns=('nmc', 'ngc')))
res = (Facility
       .update(membercost=SQL('new_prices.nmc'), guestcost=SQL('new_prices.ngc'))
       .with_cte(cte)
       .from_(cte)
       .where(Facility.name == 'Tennis Court 2')
       .execute())

# (26)
nrows = Booking.delete().execute()

# (27)
nrows = Member.delete().where(Member.memid == 37).execute()

# (28)
subq = Booking.select().where(Booking.member == Member.memid)
nrows = Member.delete().where(~fn.EXISTS(subq)).execute()

# (29)
query = Facility.select(fn.COUNT(Facility.facid))
count = query.scalar()
# 或者
count = Facility.select().count()


# (30)
query = Facility.select(fn.COUNT(Facility.facid)).where(Facility.guestcost >= 10)
count = query.scalar()
# 或者
count = Facility.select().where(Facility.guestcost >= 10).count()