#coding=utf-8
"""
Database operation class
"""
import logging,sys,os,datetime
import re
from peewee import MySQLDatabase,BigIntegerField,Model,CharField,DoubleField,IntegerField,CharField,SqliteDatabase,FloatField,SmallIntegerField,DateTimeField
from peewee import OperationalError

__all__ = [
  'db',
  'User',
  'User_subscribe_list',
]

_current_path = os.path.dirname(os.path.realpath(__file__))

_path = '{}/.db'.format(_current_path)

# Local Execute sqlite writes
_connect = SqliteDatabase(_path)

_connect.is_closed() and _connect.connect()

class _Base(Model):
  # Connect the table to the database
  class Meta:
      database = _connect

class User(_Base):
  """用户数据表
  id chat_id create_time
  """
  chat_id = IntegerField(index=True,unique=True)
  create_time = DateTimeField('%Y-%m-%d %H:%M:%S',index=True)

  class Meta:
        indexes = (
          # (('Field1', 'Field2'), True), # Field1 and Field2 as a whole as an index, True for a unique index
          # (('field1', 'field2'), False), # field1 and field2 as a whole as an index, False means normal index
            # (('price','type','time'), False), # Joint index
        )

class User_subscribe_list(_Base):
  """
  User subscription form
  user_subscribe_list
  id user_id channel_name keywords status create_time
  """
  user_id = IntegerField(index=True)
  channel_name = CharField(50,null=False)# Channel Name
  
  # https://docs.telethon.dev/en/latest/concepts/chats-vs-channels.html#channels
  chat_id = CharField(50,null=False,default='')# Unofficial id of the channel. e.g. -1001630956637

  keywords = CharField(120,null=False)# 
  status = SmallIntegerField(default=0)# 0 Normal 1 Delete
  create_time = DateTimeField('%Y-%m-%d %H:%M:%S',null=True)
  

class _Db:
  def __init__(self):
    #Creating an instance class
    init_class = [
      User,
      User_subscribe_list
    ]
    for model_class in init_class:
      try:
        model = model_class()
        model.table_exists() or (model.create_table()) #Does not exist then create table
        
        # Execute a null query (detects errors for missing fields)
        model.get_or_none(0)

        setattr(self,model_class.__name__.lower(),model)
      except OperationalError as __e:
        _e = str(__e)

        # Handle error reporting for non-existent fields
        if 'no such column' in _e:
          find = re.search('no such column: (?:\w+\.)([a-z_0-9]+)$',_e)
          if find:
            field = find.group(1)
            if hasattr(model_class,field):
              self.add_column(model_class.__name__.lower(),getattr(model_class,field))
            else:
              raise __e

  def add_column(slef,table,field):
    '''
    Add fields dynamically

    https://stackoverflow.com/questions/35012012/peewee-adding-columns-on-demand

    Args:
        slef ([type]): [description]
        table ([type]): [description]
        field ([type]): [description]
    '''
    from playhouse.migrate import SqliteMigrator,migrate
    migrator = SqliteMigrator(_connect)
    migrate(
        migrator.add_column(table, field.name, field),
    )


  def __del__(self):
    # logger.debug('db connect close')
    # _connect.close()
    pass

db = _Db()
db.connect = _connect
