# schema helps to serialize and also convert mongo db format json to our ui needed json

def studentEntity(db_item)->dict:
    return {
        "id":str(db_item["_id"]),
        "name":str(db_item["student_name"]),
        "email": str(db_item["student_email"]),
        "phone": str(db_item["student_phone"]),
    }

def listOfStudentEntity(db_item_list)->list:
    list_student_entity=[]
    for item in db_item_list:
        list_student_entity.append(studentEntity(item))

    return list_student_entity
