from helper.database import db

class ContentOwnerRepository:
    def add_content_owner(self, content_owner):
        db.session.add(content_owner)
        db.session.commit()
        return content_owner.content_owner_id

    def link_product_to_content_owner(self, content_owner_id, product_id):
        from mu.model.entity.content_owner import ContentOwnerProduct
        content_owner_product = ContentOwnerProduct(content_owner_id, product_id)
        # TODO: What about the content owner product type!
        return content_owner_product.content_owner_product_id
