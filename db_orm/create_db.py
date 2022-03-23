import random
from main import engine, Users,sessionmaker ,Base
from barnum import gen_data

Base.metadata.create_all(engine)
sessionmaker_ = sessionmaker(bind=engine)
#myfirstuser = Users(name='Ruven1', lastname='Milshtein1', age=33, company='Nokia')
session = sessionmaker_()
#session.add(myfirstuser)
#session.commit()
'''

userlist = []

for i in range(200):

    userlist.append(Users(name=gen_data.create_name()[0], lastname=gen_data.create_name()[1], age=random.randint(20,70), company=gen_data.create_company_name()))

for u in userlist:
   print(u)

session.bulk_save_objects(userlist)
session.commit()

session.query(Users).filter(Users.name == 'Ruven').delete(synchronize_session=False)

session.commit()
'''
tmp = session.query(Users).filter_by(id='1').one()
tmp.age = 50
session.add(tmp)
session.commit()
