-- mu
-- database defaults v0.03

-- default AgentTypes
-- NOTE: It is possible for a content author to be a songwriter for one product, and the lead singer for another.
INSERT INTO "AgentType" (name) VALUES ('Artist');

-- default ContentAuthorTypes
-- TODO: There needs to be some way of (1) storing different people against one artist, or (2) featuring people against
--       another artist. The former is ephemeral and artist dependent, while the latter is product dependent.
-- NOTE: (1) can be eventually solved by adding multiple ContentAuthorContentAuthorTypes against a new ContentAuthorContentAuthors
--           table which would store the ephemeral nature, also. The types would be songwriter, guitarist, bassist, etc...
-- NOTE: (2) can be eventually solved by adding multiple ContentAuthorProductTypes, like: Remixer, Producer, Artist. See above.
-- INSERT INTO "ContentAuthorContentAuthorType" (name) VALUES ('Person'), ('Group'), ('Other'), ('Unknown');

-- default ContentOwnerProductTypes
-- NOTE: It is possible for a content owner to be a distributor for one product, but something else for another.
INSERT INTO "ContentOwnerProductType" (name) VALUES ('Original Production'), ('Bootleg Production'), ('Reissue Production'), ('Distributor'), ('Holding'), ('Unknown');

-- default EventTypes
-- NOTE: I don't think we need to do more than an implicit list of (type: Event) products against a work to symbolise a festival.
INSERT INTO "EventType" (name) VALUES ('Release'), ('Performance'), ('Other');

-- default ProductTypes
INSERT INTO "ProductType" (name) VALUES ('Event'), ('Album'), ('EP'), ('Single');

-- default ProductStatuses
INSERT INTO "ProductStatus" (name) VALUES ('Official'), ('Promotional'), ('Bootleg');

-- default ProductMediums
INSERT INTO "ProductMedium" (name) VALUES ('Live'), ('Digital'), ('CD'), ('DVD'), ('Vinyl'), ('Cassette');
