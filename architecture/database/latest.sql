-- mu
-- database v0.10

BEGIN;

CREATE TABLE "User" (
  user_id            serial,
  uuid            varchar(100) NOT NULL,
  email            text NOT NULL,
  username        text NOT NULL,
  password_hash    char(60) NOT NULL,
  first_name        varchar(100),
  last_name        varchar(100),
  gender            char(1),
  date_of_birth    date,
  summary            text,
  created            timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (user_id),
  UNIQUE (uuid),
  UNIQUE (email),
  UNIQUE (username)
);

-- e.g. Remixer, Group/Band, Artist, Songwriter, Producer, Guitarist, etc.
CREATE TABLE "AgentType" (
  agent_type_id    serial,
  name            varchar(50) NOT NULL,
  PRIMARY KEY (agent_type_id),
  UNIQUE (name)
);

CREATE TABLE "Agent" (
  agent_id            serial,
  agent_type_id       integer NOT NULL,
  musicbrainz_mbid    char(36),
  name                text NOT NULL,
  sort_name            varchar(50),
  created                timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (agent_id),
  UNIQUE (name),
  FOREIGN KEY (agent_type_id) REFERENCES "AgentType"
);

-- NOTE: Agent groupings won't be used yet.
CREATE TABLE "AgentAgent" (
  agent_agent_id  serial,
  parent_agent_id integer NOT NULL,
  child_agent_id  integer NOT NULL,
  start_date      timestamp,
  end_date        timestamp,
  PRIMARY KEY (agent_agent_id),
  FOREIGN KEY (parent_agent_id) REFERENCES "Agent" (agent_id),
  FOREIGN KEY (child_agent_id) REFERENCES "Agent" (agent_id)
);

-- e.g. User is following an artist.
CREATE TABLE "UserAgent" (
  user_agent_id    serial,
  user_id            integer NOT NULL,
  agent_id        integer NOT NULL,
  created            timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (user_agent_id),
  FOREIGN KEY (user_id) REFERENCES "User",
  FOREIGN KEY (agent_id) REFERENCES "Agent"
);

-- @todo: A nicer way of storing fuzzy temporal data?
CREATE TABLE "Event" (
  event_id                        serial,
  predicted_start_release_date    timestamp,
  predicted_end_release_date      timestamp,
  predicted_textual_release_date    bytea,
  certainty                       integer,
  PRIMARY KEY (event_id)
);

-- e.g. Digital, CD, DVD, Cassette, Vinyl.
CREATE TABLE "ProductMedium" (
  product_medium_id    serial,
  name                varchar(50) NOT NULL,
  PRIMARY KEY (product_medium_id),
  UNIQUE (name)
);

-- e.g. Album, EP, Single.
CREATE TABLE "ProductType" (
  product_type_id    serial,
  name            varchar(50) NOT NULL,
  PRIMARY KEY (product_type_id),
  UNIQUE (name)
);

-- e.g. Official, Promotional, Bootleg.
CREATE TABLE "ProductStatus" (
  product_status_id    serial,
  name                varchar(50) NOT NULL,
  PRIMARY KEY (product_status_id),
  UNIQUE (name)
);

-- e.g. Boxset, US Tour, etc.
CREATE TABLE "Work" (
  work_id  serial,
  title             text NOT NULL,
  sort_title        varchar(50),
  created           timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (work_id)
);

-- e.g. Album, etc.
CREATE TABLE "Product" (
  product_id            serial,
  work_id             integer,
  product_type_id        integer NOT NULL,
  product_status_id    integer NOT NULL,
  product_medium_id    integer,
  event_id            integer NOT NULL,
  title                text NOT NULL,
  sort_title            varchar(50),
  created                timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (product_id),
  FOREIGN KEY (work_id) REFERENCES "Work",
  FOREIGN KEY (product_type_id) REFERENCES "ProductType",
  FOREIGN KEY (product_status_id) REFERENCES "ProductStatus",
  FOREIGN KEY (product_medium_id) REFERENCES "ProductMedium",
  FOREIGN KEY (event_id) REFERENCES "Event"
);

-- e.g. Live Performance.
CREATE TABLE "ServiceType" (
  service_type_id    serial,
  name            varchar(50) NOT NULL,
  PRIMARY KEY (service_type_id),
  UNIQUE (name)
);

CREATE TABLE "Service" (
  service_id          serial,
  work_id             integer,
  service_type_id     integer,
  event_id            integer NOT NULL,
  title               text NOT NULL,
  sort_title          varchar(50),
  created             timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (service_id),
  FOREIGN KEY (work_id) REFERENCES "Work",
  FOREIGN KEY (service_type_id) REFERENCES "ServiceType",
  FOREIGN KEY (event_id) REFERENCES "Event"
);

-- NOTE: Both ProductAgent and ServiceAgent show participation:
-- NOTE: agent_order is used to assign some 'order' to a list
-- of agents against an event. E.g. an importance. It is used on
-- addition to agent_type_id to help distinguish agents.
-- ProductAgent contains the artists against a product...
CREATE TABLE "ProductAgent" (
  product_agent_id    serial,
  product_id          integer NOT NULL,
  agent_id            integer NOT NULL,
  agent_order         integer,
  agent_type_id         integer,
  created                timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (product_agent_id),
  FOREIGN KEY (product_id) REFERENCES "Product",
  FOREIGN KEY (agent_id) REFERENCES "Agent",
  FOREIGN KEY (agent_type_id) REFERENCES "AgentType"
);

-- ServiceAgent contains the artists against a service (performance, etc.)
CREATE TABLE "ServiceAgent" (
  service_agent_id    serial,
  service_id          integer NOT NULL,
  agent_id            integer NOT NULL,
  agent_order         integer,
  agent_type_id         integer,
  created                timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (service_agent_id),
  FOREIGN KEY (service_id) REFERENCES "Service",
  FOREIGN KEY (agent_id) REFERENCES "Agent",
  FOREIGN KEY (agent_type_id) REFERENCES "AgentType"
);

CREATE TABLE "UserEvent" (
  user_event_id           serial,
  user_id                 integer NOT NULL,
  event_id                integer NOT NULL,
  start_release_date      timestamp,
  end_release_date        timestamp,
  textual_release_date    bytea,
  created                 timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (user_event_id),
  FOREIGN KEY (user_id) REFERENCES "User",
  FOREIGN KEY (event_id) REFERENCES "Event"
);

CREATE TABLE "UserProduct" (
  user_product_id            serial,
  user_id                    integer NOT NULL,
  product_id                integer NOT NULL,
  weight                  integer NOT NULL DEFAULT 50,
  created                    timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (user_product_id),
  FOREIGN KEY (user_id) REFERENCES "User",
  FOREIGN KEY (product_id) REFERENCES "Product"
);

CREATE TABLE "UserService" (
  user_service_id            serial,
  user_id                    integer NOT NULL,
  service_id                integer NOT NULL,
  weight                  integer NOT NULL DEFAULT 50,
  created                    timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (user_service_id),
  FOREIGN KEY (user_id) REFERENCES "User",
  FOREIGN KEY (service_id) REFERENCES "Service"
);

CREATE TABLE "ContentOwner" (
  content_owner_id    serial,
  name                text NOT NULL,
  sort_name            varchar(50),
  start_date            date,
  end_date            date,
  created                timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (content_owner_id),
  UNIQUE (name, start_date, end_date)
);

-- e.g. Label, Distributor, Holding, Original Production, Bootleg Production, etc.
CREATE TABLE "ContentOwnerProductType" (
  content_owner_product_type_id    serial,
  name                            varchar(50),
  PRIMARY KEY (content_owner_product_type_id),
  UNIQUE (name)
);

CREATE TABLE "ContentOwnerProduct" (
  content_owner_product_id        serial,
  content_owner_id                integer NOT NULL,
  product_id                         integer NOT NULL,
  content_owner_product_type_id    integer,
  created                            timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (content_owner_product_id),
  FOREIGN KEY (content_owner_id) REFERENCES "ContentOwner",
  FOREIGN KEY (product_id) REFERENCES "Product",
  FOREIGN KEY (content_owner_product_type_id) REFERENCES "ContentOwnerProductType"
);

COMMIT;
