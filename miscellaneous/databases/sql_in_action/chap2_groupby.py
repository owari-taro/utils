from sqlalchemy.ext.hybrid import hybrid_method  # ,hybrid_property
from sqlalchemy import Column, Integer, Numeric, String, DateTime,\
    ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from datetime import datetime,timedelta
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase


# https://pypi.org/project/sqlalchemy-repr/
# 各テーブルはこのクラスを継承する必要がある
Base = declarative_base(cls=RepresentableBase)
from sqlalchemy import Integer, Enum
import enum

class Sex(enum.Enum):
    MAN="man"
    WOMAN="woman"


class Person(Base):
    __tablename__="person"
    id=Column(Integer(),primary_key=True)
    name=Column(String(256),nullable=False)
    sex=Column(Enum(Sex),nullable=False)


if __name__ == "__main__":
    # 動作確認用
    import os
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import func
    # とりあえずsqliteでだめす
    test_db = "test.db"
    if os.path.exists(test_db):
        os.remove(test_db)
    engine = create_engine(f"sqlite:///{test_db}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    #https://carefree-se.hatenablog.com/entry/2017/12/20/000000
    persons=[Person(name="test",sex=Sex.MAN),Person(name="tes234t",sex=Sex.MAN),
        Person(name="testere",sex=Sex.WOMAN),Person(name="test4234",sex=Sex.WOMAN),Person(name="test231",sex=Sex.MAN)]
    for per in persons:
        session.add(per)
    session.commit()
    #session.query(Person.age, func.count(Person.age)).group_by(Person.age).all()
    res=session.query(Person.sex,func.count(Person.sex)).group_by(Person.sex).all()
    print(res)
