-- mu
-- database v0.03

BEGIN;

CREATE TABLE "Users" (
	user_id			serial,
	uuid			varchar(100) NOT NULL,
	email			text NOT NULL,
	username		text NOT NULL,
	password_hash	char(60) NOT NULL,
	first_name		varchar(100),
	last_name		varchar(100),
	gender			char(1),
	date_of_birth	date,
	summary			text,
	created			timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (user_id),
	UNIQUE (uuid),
  UNIQUE (email),
  UNIQUE (username)
);

CREATE TABLE "ContentAuthors" (
	content_author_id	serial,
	musicbrainz_mbid	char(36),
	name				text NOT NULL,
	sort_name			varchar(50),
	start_date		date,
	end_date			date,
	created				timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (content_author_id)
);

CREATE TABLE "UserContentAuthors" (
	user_content_author_id	serial,
	user_id					integer NOT NULL,
	content_author_id		integer NOT NULL,
	created					timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (user_content_author_id),
	FOREIGN KEY (user_id) REFERENCES "Users",
	FOREIGN KEY (content_author_id) REFERENCES "ContentAuthors"
);

CREATE TABLE "EventTypes" (
	event_type_id	serial,
	name		varchar(50),
	PRIMARY KEY (event_type_id),
	UNIQUE (name)
);

CREATE TABLE "Events" (
	event_id	serial,
	event_type_id	integer NOT NULL,
	predicted_release_date			timestamp,
	predicted_textual_release_date	text,
  created		timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (event_id),
	FOREIGN KEY (event_type_id) REFERENCES "EventTypes"
);

CREATE TABLE "ProductMediums" (
	product_medium_id	serial,
	name				varchar(50) NOT NULL,
	PRIMARY KEY (product_medium_id),
	UNIQUE (name)
);

CREATE TABLE "ProductTypes" (
	product_type_id	serial,
	name			varchar(50) NOT NULL,
	PRIMARY KEY (product_type_id),
	UNIQUE (name)
);

CREATE TABLE "ProductStatuses" (
	product_status_id	serial,
	name				varchar(50) NOT NULL,
	PRIMARY KEY (product_status_id),
	UNIQUE (name)
);

CREATE TABLE "Works" (
  work_id  serial,
  title             text NOT NULL,
  sort_title        varchar(50),
  created           timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (work_id)
);

CREATE TABLE "Products" (
	product_id			serial,
  work_id  integer,
	product_type_id		integer NOT NULL,
	product_status_id	integer NOT NULL,
	product_medium_id	integer,
  event_id          integer NOT NULL,
	title				text NOT NULL,
	sort_title			varchar(50),
	created				timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (product_id),
  FOREIGN KEY (work_id) REFERENCES "Works",
	FOREIGN KEY (product_type_id) REFERENCES "ProductTypes",
	FOREIGN KEY (product_status_id) REFERENCES "ProductStatuses",
	FOREIGN KEY (product_medium_id) REFERENCES "ProductMediums",
  FOREIGN KEY (event_id) REFERENCES "Events"
);

CREATE TABLE "ContentAuthorProductTypes" (
	content_author_product_type_id	serial,
	name							varchar(50) NOT NULL,
	PRIMARY KEY (content_author_product_type_id),
	UNIQUE (name)
);

CREATE TABLE "ContentAuthorProducts" (
	content_author_product_id		serial,
	content_author_id				integer NOT NULL,
	product_id						integer NOT NULL,
	content_author_product_type_id	integer,
	created							timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (content_author_product_id),
	FOREIGN KEY (content_author_id) REFERENCES "ContentAuthors",
	FOREIGN KEY (product_id)	REFERENCES "Products",
	FOREIGN KEY (content_author_product_type_id) REFERENCES "ContentAuthorProductTypes"
);

CREATE TABLE "UserEvents" (
	user_event_id			serial,
	user_id					integer NOT NULL,
	event_id				integer NOT NULL,
	certainty     	integer NOT NULL,
	created					timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (user_event_id),
	FOREIGN KEY (user_id) REFERENCES "Users",
	FOREIGN KEY (event_id) REFERENCES "Events"
);

CREATE TABLE "ContentOwners" (
	content_owner_id	serial,
	name				text NOT NULL,
	sort_name			varchar(50),
	start_date		date,
	end_date			date,
	created				timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (content_owner_id)
);

CREATE TABLE "ContentOwnerProductTypes" (
	content_owner_product_type_id	serial,
	name							varchar(50),
	PRIMARY KEY (content_owner_product_type_id),
	UNIQUE (name)
);

CREATE TABLE "ContentOwnerProducts" (
	content_owner_product_id		serial,
	content_owner_id				integer NOT NULL,
	product_id						integer NOT NULL,
	content_owner_product_type_id	integer,
	created							timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (content_owner_product_id),
	FOREIGN KEY (content_owner_id) REFERENCES "ContentOwners",
	FOREIGN KEY (product_id) REFERENCES "Products",
	FOREIGN KEY (content_owner_product_type_id) REFERENCES "ContentOwnerProductTypes"
);

COMMIT;
