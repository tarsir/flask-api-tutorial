def query_model_for_fields(model_result, field_list):
    '''
    Return a dictionary of the object with the specified field list.

    Fields that don't exist in the object are ignored.
    '''
    model_fields = {}

    for field in field_list:
        if field in model_result:
            model_fields[field] = model_result[field]

    return model_fields

def query_full_model(model_result):
    '''
    Return a dictionary representation of the object as retrieved from the database.

    Null fields are represented as Python 'None'.
    '''
    model_fields = [f for f in model_result.__dict__ if not f.startswith('_')]
    return dict([( f, getattr(model_result, f, '') or None) for f in model_fields])

def query_full_models(model_list):
    '''
    Return a list of the dictionary representations of a list of objects from database.
    '''
    return [query_full_model(m) for m in model_list]
