from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy import Table,Column,Integer,String,Metadata
metadata= Metadata()
engine = create_engine('sqlite:///:my_users:', echo=True)