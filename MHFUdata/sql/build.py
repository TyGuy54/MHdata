from .mappings import *
from MHFUdata.util.load import insert_df
from database.db_ops import DB_Ops


def build_database():
    db = DB_Ops("MHFU_Data.db")

    MonsterBase.create_table(db.conn)
    MonsterAilments.create_table(db.conn)
    MonsterBreaks.create_table(db.conn)
    MonsterHabitats.create_table(db.conn)

    insert_df(db)

    db.close()