from mongoengine import Document, StringField, BooleanField, FloatField, DictField, ListField, DateTimeField

class Cases(Document):
    _id                         = StringField(primary_key=True, required=False)
    user_id                     = StringField()
    case_name                   = StringField(required=True)
    victim_images               = ListField()
    suspect_images              = ListField()

    meta                        = {'db_alias' : 'MARVEL'}

class Log(Document):
    username                    = StringField(required=True)
    password                    = StringField()
    user_id                     = StringField()
    case_id                     = StringField()
    status                      = BooleanField(default=True)
    created_at                  = FloatField()
    bookmarks                   = DictField()
    notes                       = ListField()
    role                        = StringField()

    meta                        = {'db_alias' : 'MARVEL'}

class Users(Document):
    _id                         = StringField(primary_key=True, required=False)
    username                    = StringField(required=True)
    hashed_pwd                  = StringField()
    status                      = StringField()

    meta                        = {'db_alias' : 'MARVEL'}

class SearchLogs(Document):
    keyword                     = StringField(required=True)
    result_count                = StringField()
    user_name                   = StringField()
    user_id                     = StringField()
    timestamp                   = DateTimeField()

    meta                        = {'db_alias' : 'MARVEL'}

class UserLog(Document):
    username                    = StringField(required=True)
    ip_address                  = StringField()
    endpoint                    = StringField()
    user_agent                  = StringField()
    timestamp                   = DateTimeField()

    meta                        = {'db_alias' : 'MARVEL'}