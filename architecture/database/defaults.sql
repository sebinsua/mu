-- mu
-- database defaults v0.10

-- default AgentTypes
-- NOTE: It is possible for a content author to be a songwriter for one product, and the lead singer for another.
INSERT INTO "AgentType" (name) VALUES ('Artist');

-- default ContentOwnerProductTypes
-- NOTE: It is possible for a content owner to be a distributor for one product, but something else for another.
INSERT INTO "ContentOwnerProductType" (name) VALUES ('Original Production'), ('Bootleg Production'), ('Reissue Production'), ('Distributor'), ('Holding'), ('Unknown');

-- default ProductTypes
INSERT INTO "ProductType" (name) VALUES ('Album'), ('EP'), ('Single');

-- default ProductStatuses
INSERT INTO "ProductStatus" (name) VALUES ('Official'), ('Promotional'), ('Bootleg');

-- default ProductMediums
INSERT INTO "ProductMedium" (name) VALUES ('Digital'), ('CD'), ('DVD'), ('Vinyl'), ('Cassette');

-- default ServiceTypes
INSERT INTO "ServiceType" (name) VALUES ('Live Performance');
