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

CREATE TABLE "AgentTypes" (
	agent_type_id	serial,
	name							varchar(50) NOT NULL,
	PRIMARY KEY (agent_type_id),
	UNIQUE (name)
);

CREATE TABLE "Agents" (
	agent_id	serial,
  agent_type_id integer NOT NULL,
	musicbrainz_mbid	char(36),
	name				text NOT NULL,
	sort_name			varchar(50),
	created				timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (agent_id),
  FOREIGN KEY (agent_type_id) REFERENCES "AgentTypes"
);

-- TODO: Maybe at some point we could add a user_agent_type_id which
-- would allow us to define the difference between a user following other
-- agents and BEING one.
CREATE TABLE "UserAgents" (
	user_agent_id	serial,
	user_id					integer NOT NULL,
	agent_id		integer NOT NULL,
	created					timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (user_agent_id),
	FOREIGN KEY (user_id) REFERENCES "Users",
	FOREIGN KEY (agent_id) REFERENCES "Agents"
);

CREATE TABLE "EventTypes" (
	event_type_id	serial,
	name		varchar(50),
	PRIMARY KEY (event_type_id),
	UNIQUE (name)
);

-- TODO: There is a nicer way of dealing with fuzzy temporal data which I shall
-- come up with.
CREATE TABLE "Events" (
	event_id	serial,
	event_type_id	integer NOT NULL,
	predicted_start_release_date			timestamp,
	predicted_end_release_date        timestamp,
  predicted_textual_release_date	text,
  certainty integer,
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

CREATE TABLE "Actions" (
  action_id   serial,
  event_id    integer NOT NULL,
  description text NOT NULL,
  PRIMARY KEY (action_id),
  FOREIGN KEY (event_id) REFERENCES "Events"
);

CREATE TABLE "AgentEvents" (
	agent_event_id		  serial,
	agent_id				    integer NOT NULL,
	event_id						integer NOT NULL,
	agent_type_id     	integer,
	created							timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (agent_event_id),
	FOREIGN KEY (agent_id) REFERENCES "Agents",
	FOREIGN KEY (event_id)	REFERENCES "Events",
	FOREIGN KEY (agent_type_id) REFERENCES "AgentTypes"
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
