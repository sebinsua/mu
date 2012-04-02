from helper.database import db, check_if_entity_exists

def add_content_owner(content_owner):
    # Test if the content owner already exists in the database.
    unique_content_owner = check_if_entity_exists(content_owner)
    if unique_content_owner:
        return unique_content_owner.content_owner_id

    db.session.add(content_owner)
    db.session.flush()
    return content_owner.content_owner_id


def link_product_to_content_owner(content_owner_id, product_id):
    from mu.model.entity.content_owner import ContentOwnerProduct

    content_owner_product = ContentOwnerProduct(content_owner_id, product_id)
    db.session.add(content_owner_product)
    db.session.flush()
    return content_owner_product.content_owner_product_id
