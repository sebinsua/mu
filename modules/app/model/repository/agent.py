from helper.database import db

class ContentAuthorRepository:
    def add_content_author(self, content_author):
        db.session.add(content_author)
        db.session.commit()
        return content_author.content_author_id

    def link_product_to_content_author(self, content_author_id, product_id):
        from mu.model.entity.content_author import ContentAuthorProduct
        content_author_product = ContentAuthorProduct(content_author_id, product_id)
        # TODO: What about the content author product type!
        return content_author_product.content_author_product_id
