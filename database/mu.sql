-- mu
-- database v0.01

\connect root

SET client_encoding = 'UTF8';

CREATE DATABASE mu;

\connect mu root

BEGIN;

CREATE TABLE Users (
	userID		serial,
	UUID		varchar(100) NOT NULL,
	email		text NOT NULL,
	userName	text NOT NULL,
	passwordHash	char(60) NOT NULL,
	firstName	text,
	lastName	text,
	gender		char(1),
	birthdate	date,
	summary		text,
	created		timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (userID),
	UNIQUE (UUID, email, userName)
);

CREATE TABLE ContentAuthors (
	contentAuthorID	serial,
	musicBrainzMBID	char(36),
	name		text NOT NULL,
	sortName	varchar(50),
	startDate	timestamp,
	endDate		timestamp,
	created		timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (contentAuthorID)
);

CREATE TABLE UserContentAuthors (
	userContentAuthorID	serial,
	userID			integer NOT NULL,
	contentAuthorID		integer NOT NULL,
	created			timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (userContentAuthorID),
	FOREIGN KEY (userID) REFERENCES Users,
	FOREIGN KEY (contentAuthorID) REFERENCES ContentAuthors
);

CREATE TABLE ReleaseMediums (
	releaseMediumID	serial,
	name		varchar(50) NOT NULL,
	PRIMARY KEY (releaseMediumID),
	UNIQUE (name)
);

CREATE TABLE ReleaseTypes (
	releaseTypeID	serial,
	name		varchar(50) NOT NULL,
	PRIMARY KEY (releaseTypeID),
	UNIQUE (name)
);

CREATE TABLE ReleaseStatuses (
	releaseStatusID	serial,
	name		varchar(50) NOT NULL,
	PRIMARY KEY (releaseStatusID),
	UNIQUE (name)
);

CREATE TABLE Releases (
	releaseID	serial,
	releaseTypeID	integer NOT NULL,
	releaseStatusID	integer NOT NULL,
	releaseMediumID	integer NOT NULL,
	title		text NOT NULL,
	sortTitle	varchar(50),
	created		timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (releaseID),
	FOREIGN KEY (releaseTypeID) REFERENCES ReleaseTypes,
	FOREIGN KEY (releaseStatusID) REFERENCES ReleaseStatuses,
	FOREIGN KEY (releaseMediumID) REFERENCES ReleaseMediums
);

CREATE TABLE ContentAuthorReleaseTypes (
	contentAuthorReleaseTypeID	serial,
	name				varchar(50) NOT NULL,
	PRIMARY KEY (contentAuthorReleaseTypeID),
	UNIQUE (name)
);

CREATE TABLE ContentAuthorReleases (
	contentAuthorReleaseID		serial,
	contentAuthorID			integer NOT NULL,
	releaseID			integer NOT NULL,
	contentAuthorReleaseTypeID	integer NOT NULL,
	created				timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (contentAuthorReleaseID),
	FOREIGN KEY (contentAuthorID) REFERENCES ContentAuthors,
	FOREIGN KEY (releaseID)	REFERENCES Releases,
	FOREIGN KEY (contentAuthorReleaseTypeID) REFERENCES ContentAuthorReleaseTypes
);

CREATE TABLE EventTypes (
	eventTypeID	serial,
	name		varchar(50),
	PRIMARY KEY (eventTypeID),
	UNIQUE (name)
);

CREATE TABLE Events (
	eventID		serial,
	eventTypeID	integer NOT NULL,
	created		timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (eventID),
	FOREIGN KEY (eventTypeID) REFERENCES EventTypes
);

CREATE TABLE ReleaseEvents (
	releaseEventID			serial,
	releaseID			integer NOT NULL,
	eventID				integer NOT NULL,
	predictedReleaseDate		date,
	predictedTextualReleaseDate	text,
	created				timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (releaseEventID),
	FOREIGN KEY (releaseID) REFERENCES Releases,
	FOREIGN KEY (eventID) REFERENCES Events
);

CREATE TABLE UserEventStatuses (
	userEventStatusID	serial,
	name			varchar(50) NOT NULL,
	PRIMARY KEY (userEventStatusID),
	UNIQUE (name)
);

CREATE TABLE UserEvents (
	userEventID		serial,
	userID			integer NOT NULL,
	eventID			integer NOT NULL,
	userEventStatusID	integer NOT NULL,
	created			timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (userEventID),
	FOREIGN KEY (userID) REFERENCES Users,
	FOREIGN KEY (eventID) REFERENCES Events,
	FOREIGN KEY (userEventStatusID) REFERENCES UserEventStatuses
);

CREATE TABLE ContentOwners (
	contentOwnerID	serial,
	name		text NOT NULL,
	sortName	varchar(50),
	startDate	date,
	endDate		date,
	created		timestamp NOT NULL DEFAULT current_timestamp
);

CREATE TABLE ContentOwnerReleaseTypes (
	contentOwnerReleaseTypeID	serial,
	name				varchar(50),
	PRIMARY KEY (contentOwnerReleaseTypeID),
	UNIQUE (name)
);

CREATE TABLE ContentOwnerReleases (
	contentOwnerReleaseID		serial,
	contentOwnerID			integer NOT NULL,
	releaseID			integer NOT NULL,
	contentOwnerReleaseTypeID	integer NOT NULL,
	created				timestamp NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (contentOwnerReleaseID)
);

COMMIT;
