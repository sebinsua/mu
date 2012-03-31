from helper.database import db

def add_content_owner(content_owner):
    # todo: Test if content_owner already exists in the database by searching for the same
    #       unique constraints.
    # import pprint
    # print 'content_owner: '
    # for constraint in content_owner.__table__.constraints:
    #    pprint.pprint(constraint.columns)

    db.session.add(content_owner)
    db.session.flush()
    return content_owner.content_owner_id

def link_product_to_content_owner(content_owner_id, product_id):
    from mu.model.entity.content_owner import ContentOwnerProduct
    content_owner_product = ContentOwnerProduct(content_owner_id, product_id)
    db.session.add(content_owner_product)
    db.session.flush()
    return content_owner_product.content_owner_product_id
