-- mu
-- database v0.04

BEGIN;

CREATE TABLE "User" (
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

CREATE TABLE "AgentType" (
	agent_type_id	serial,
	name			varchar(50) NOT NULL,
	PRIMARY KEY (agent_type_id),
	UNIQUE (name)
);

CREATE TABLE "Agent" (
	agent_id	        serial,
	agent_type_id       integer NOT NULL,
	musicbrainz_mbid	char(36),
	name			    text NOT NULL,
	sort_name		    varchar(50),
	created			    timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (agent_id),
	FOREIGN KEY (agent_type_id) REFERENCES "AgentType"
);

-- TODO: Maybe at some point we could add a user_agent_type_id which
-- would allow us to define the difference between a user following other
-- agents and BEING one.
CREATE TABLE "UserAgent" (
	user_agent_id	serial,
	user_id			integer NOT NULL,
	agent_id	    integer NOT NULL,
	created			timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (user_agent_id),
	FOREIGN KEY (user_id) REFERENCES "User",
	FOREIGN KEY (agent_id) REFERENCES "Agent"
);

CREATE TABLE "EventType" (
	event_type_id	serial,
	name		    varchar(50),
	PRIMARY KEY (event_type_id),
	UNIQUE (name)
);

-- TODO: There is a nicer way of dealing with fuzzy temporal data which I shall
-- come up with.
CREATE TABLE "Event" (
	event_id                        serial,
	event_type_id	                integer NOT NULL,
	predicted_start_release_date	timestamp,
	predicted_end_release_date      timestamp,
	predicted_textual_release_date	bytea,
	certainty                       integer,
	created		                    timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (event_id),
	FOREIGN KEY (event_type_id) REFERENCES "EventType"
);

CREATE TABLE "ProductMedium" (
	product_medium_id	serial,
	name				varchar(50) NOT NULL,
	PRIMARY KEY (product_medium_id),
	UNIQUE (name)
);

CREATE TABLE "ProductType" (
	product_type_id	serial,
	name			varchar(50) NOT NULL,
	PRIMARY KEY (product_type_id),
	UNIQUE (name)
);

CREATE TABLE "ProductStatus" (
	product_status_id	serial,
	name				varchar(50) NOT NULL,
	PRIMARY KEY (product_status_id),
	UNIQUE (name)
);

CREATE TABLE "Work" (
	work_id  serial,
	title             text NOT NULL,
	sort_title        varchar(50),
	created           timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (work_id)
);

CREATE TABLE "Product" (
	product_id			serial,
	work_id             integer,
	product_type_id		integer NOT NULL,
	product_status_id	integer NOT NULL,
	product_medium_id	integer,
	event_id            integer NOT NULL,
	title				text NOT NULL,
	sort_title			varchar(50),
	created				timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (product_id),
	FOREIGN KEY (work_id) REFERENCES "Work",
	FOREIGN KEY (product_type_id) REFERENCES "ProductType",
	FOREIGN KEY (product_status_id) REFERENCES "ProductStatus",
	FOREIGN KEY (product_medium_id) REFERENCES "ProductMedium",
	FOREIGN KEY (event_id) REFERENCES "Event"
);

-- NOTE: agent_order is used to assign some 'order' to a list
-- of agents against an event. E.g. an importance. It is used on
-- addition to agent_type_id to help distinguish agents.
CREATE TABLE "AgentEvent" (
	agent_event_id		serial,
	agent_id			integer NOT NULL,
	agent_order         integer,
	agent_type_id     	integer,
	event_id            integer NOT NULL,
	certainty           integer NOT NULL DEFAULT '50',
	created				timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (agent_event_id),
	FOREIGN KEY (agent_id) REFERENCES "Agent",
	FOREIGN KEY (event_id)	REFERENCES "Event",
	FOREIGN KEY (agent_type_id) REFERENCES "AgentType"
);

CREATE TABLE "Action" (
	action_id   serial,
	agent_event_id    integer NOT NULL,
	description text  NOT NULL,
	PRIMARY KEY (action_id),
	FOREIGN KEY (agent_event_id) REFERENCES "AgentEvent"
);

CREATE TABLE "UserEvent" (
	user_event_id			serial,
	user_id					integer NOT NULL,
	event_id				integer NOT NULL,
	certainty     	        integer NOT NULL DEFAULT '100',
	created					timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (user_event_id),
	FOREIGN KEY (user_id) REFERENCES "User",
	FOREIGN KEY (event_id) REFERENCES "Event"
);

CREATE TABLE "ContentOwner" (
	content_owner_id	serial,
	name				text NOT NULL,
	sort_name			varchar(50),
	start_date		    date,
	end_date			date,
	created				timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (content_owner_id)
);

CREATE TABLE "ContentOwnerProductType" (
	content_owner_product_type_id	serial,
	name							varchar(50),
	PRIMARY KEY (content_owner_product_type_id),
	UNIQUE (name)
);

CREATE TABLE "ContentOwnerProduct" (
	content_owner_product_id		serial,
	content_owner_id				integer NOT NULL,
	product_id						integer NOT NULL,
	content_owner_product_type_id	integer,
	created							timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (content_owner_product_id),
	FOREIGN KEY (content_owner_id) REFERENCES "ContentOwner",
	FOREIGN KEY (product_id) REFERENCES "Product",
	FOREIGN KEY (content_owner_product_type_id) REFERENCES "ContentOwnerProductType"
);

COMMIT;
