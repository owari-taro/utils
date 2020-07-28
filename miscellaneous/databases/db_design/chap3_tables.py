from sqlalchemy.ext.hybrid import hybrid_method  # ,hybrid_property
from sqlalchemy import Column, Integer, Numeric, String, DateTime,\
    ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from datetime import datetime, timedelta
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase


# https://pypi.org/project/sqlalchemy-repr/
# 各テーブルはこのクラスを継承する必要がある
Base = declarative_base(cls=RepresentableBase)


class Branch(Base):
    __tablename__ = "branch"
    id = Column(Integer(), primary_key=True)
    name = Column(String(256), unique=True)
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow,
                        onupdate=datetime.utcnow)
    # slack通知用。nullの場合は通知がとばないです！
   # slack_token = Column(String(512))
   # webhook_url = Column(String(512))
   # channel_id = Column(String(256))
   ## slack_notified_at = Column(DateTime())


class Store(Base):
    __tablename__ = "store"
    id=Clumn(Integer(),primary_key=True)
    store_id = Column(Integer(),ForeignKey("store.id"))
    # ex:fuel,jqueryなど
    branch_id = Column(Integer(), ForeignKey("branch.id"),
                       nullable=False)
    name = Column(String(256), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    # githubのurlの一部分
    #url_path = Column(String(512), nullable=False, unique=True)


class Product(Base):
    __tablename__ = "product"
    store_id = Column(Integer(), primary_key=True)
    # ex:fuel,jqueryなど
    name = Column(String(256), nullable=False, unique=True)
    category_id = Column(Integer(), nullable=False, ForeignKey("category.id"))
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow,
                        onupdate=datetime.utcnow)


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer(), nullable=False, primary_key=True)
    name = Column(String(256), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow,
                        onupdate=datetime.utcnow)


class BranchProduct(Base):
    __tablename__ = "branch_product"
    id=Column(Integer(),primary_key=True)
    branch_id = Column(Integer(), nullable=False, ForeignKey("branch.id"))
    store_id = Column(Integer(), nullable=False, ForeignKey("store.id"))
    product_id = Column(Integer(), nullable=False, ForeignKey("product.id"))
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow,
                        onupdate=datetime.utcnow)
    #TODO:write constraing