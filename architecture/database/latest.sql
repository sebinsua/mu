-- mu
-- database v0.01

SET client_encoding = 'UTF8';

BEGIN;

CREATE TABLE Users (
	user_id			serial,
	uuid			varchar(100) NOT NULL,
	email			text NOT NULL,
	username		text NOT NULL,
	password_hash	char(60) NOT NULL,
	first_name		text,
	last_name		text,
	gender			char(1),
	date_of_birth	date,
	summary			text,
	created			timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (user_id),
	UNIQUE (uuid),
  UNIQUE (email),
  UNIQUE (username)
);

CREATE INDEX users_email_index
  ON users
  USING btree
  (email );

CREATE INDEX users_username_index
  ON users
  USING btree
  (username );

CREATE INDEX users_uuid_index
  ON users
  USING btree
  (uuid );


CREATE TABLE ContentAuthors (
	content_author_id	serial,
	musicbrainz_mbid	char(36),
	name				text NOT NULL,
	sort_name			varchar(50),
	start_date			timestamp,
	end_date			timestamp,
	created				timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (content_author_id)
);

CREATE TABLE UserContentAuthors (
	usercontent_author_id	serial,
	user_id					integer NOT NULL,
	content_author_id		integer NOT NULL,
	created					timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (usercontent_author_id),
	FOREIGN KEY (user_id) REFERENCES Users,
	FOREIGN KEY (content_author_id) REFERENCES ContentAuthors
);

CREATE TABLE ReleaseMediums (
	release_medium_id	serial,
	name				varchar(50) NOT NULL,
	PRIMARY KEY (release_medium_id),
	UNIQUE (name)
);

CREATE TABLE ReleaseTypes (
	release_type_id	serial,
	name			varchar(50) NOT NULL,
	PRIMARY KEY (release_type_id),
	UNIQUE (name)
);

CREATE TABLE ReleaseStatuses (
	release_status_id	serial,
	name				varchar(50) NOT NULL,
	PRIMARY KEY (release_status_id),
	UNIQUE (name)
);

CREATE TABLE ReleaseGroups (
  release_group_id  serial,
  title             text NOT NULL,
  sort_title        varchar(50),
  created           timestamp NOT NULL DEFAULT current_timestamp,
  PRIMARY KEY (release_group_id)
);

CREATE TABLE Releases (
	release_id			serial,
  release_group_id  integer NOT NULL,
	release_type_id		integer NOT NULL,
	release_status_id	integer NOT NULL,
	release_medium_id	integer NOT NULL,
	title				text NOT NULL,
	sort_title			varchar(50),
	created				timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (release_id),
  FOREIGN KEY (release_group_id) REFERENCES ReleaseGroups,
	FOREIGN KEY (release_type_id) REFERENCES ReleaseTypes,
	FOREIGN KEY (release_status_id) REFERENCES ReleaseStatuses,
	FOREIGN KEY (release_medium_id) REFERENCES ReleaseMediums
);

CREATE TABLE ContentAuthorReleaseTypes (
	content_author_release_type_id	serial,
	name							varchar(50) NOT NULL,
	PRIMARY KEY (content_author_release_type_id),
	UNIQUE (name)
);

CREATE TABLE ContentAuthorReleases (
	content_author_release_id		serial,
	content_author_id				integer NOT NULL,
	release_id						integer NOT NULL,
	content_author_release_type_id	integer NOT NULL,
	created							timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (content_author_release_id),
	FOREIGN KEY (content_author_id) REFERENCES ContentAuthors,
	FOREIGN KEY (release_id)	REFERENCES Releases,
	FOREIGN KEY (content_author_release_type_id) REFERENCES ContentAuthorReleaseTypes
);

CREATE TABLE EventTypes (
	eventTypeID	serial,
	name		varchar(50),
	PRIMARY KEY (eventTypeID),
	UNIQUE (name)
);

CREATE TABLE Events (
	event_id	serial,
	eventTypeID	integer NOT NULL,
	created		timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (event_id),
	FOREIGN KEY (eventTypeID) REFERENCES EventTypes
);

CREATE TABLE ReleaseEvents (
	releaseevent_id					serial,
	release_id						integer NOT NULL,
	event_id						integer NOT NULL,
	predicted_release_date			date,
	predicted_textual_release_date	text,
	created							timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (releaseevent_id),
	FOREIGN KEY (release_id) REFERENCES Releases,
	FOREIGN KEY (event_id) REFERENCES Events
);

CREATE TABLE UserEventStatuses (
	user_event_status_id	serial,
	name					varchar(50) NOT NULL,
	PRIMARY KEY (user_event_status_id),
	UNIQUE (name)
);

CREATE TABLE UserEvents (
	user_event_id			serial,
	user_id					integer NOT NULL,
	event_id				integer NOT NULL,
	user_event_status_id	integer NOT NULL,
	created					timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (user_event_id),
	FOREIGN KEY (user_id) REFERENCES Users,
	FOREIGN KEY (event_id) REFERENCES Events,
	FOREIGN KEY (user_event_status_id) REFERENCES UserEventStatuses
);

CREATE TABLE ContentOwners (
	content_owner_id	serial,
	name				text NOT NULL,
	sort_name			varchar(50),
	start_date			date,
	end_date			date,
	created				timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (content_owner_id)
);

CREATE TABLE ContentOwnerReleaseTypes (
	content_owner_release_type_id	serial,
	name							varchar(50),
	PRIMARY KEY (content_owner_release_type_id),
	UNIQUE (name)
);

CREATE TABLE ContentOwnerReleases (
	content_owner_release_id		serial,
	content_owner_id				integer NOT NULL,
	release_id						integer NOT NULL,
	content_owner_release_type_id	integer NOT NULL,
	created							timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (content_owner_release_id),
	FOREIGN KEY (content_owner_id) REFERENCES ContentOwners,
	FOREIGN KEY (release_id) REFERENCES Releases,
	FOREIGN KEY (content_owner_release_type_id) REFERENCES ContentOwnerReleaseTypes
);

COMMIT;
