CREATE EXTENSION pgcrypto;

CREATE TABLE users (
 	user_id uuid NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
 	fname VARCHAR (255) NOT NULL,
 	lname VARCHAR (255) NOT NULL,
 	phone VARCHAR (255) NOT NULL,
 	email VARCHAR (255) NOT NULL,
 	username VARCHAR (255) NOT NULL,
 	password TEXT NOT NULL,
	date_created TIMESTAMP NOT NULL,
	date_updated TIMESTAMP NOT NULL,
	user_admin BOOLEAN DEFAULT FALSE,
	user_super_user BOOLEAN DEFAULT FALSE,
	user_deleted BOOLEAN NOT NULL DEFAULT FALSE
);


CREATE TABLE files (
    file_id uuid NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
    file_sha1 VARCHAR (225) NOT NULL UNIQUE,
    file_name VARCHAR (225) NOT NULL,
    file_type VARCHAR (10),
    file_path VARCHAR (225) NOT NULL,
	file_size BIGINT,
    date_created TIMESTAMP NOT NULL,
    date_updated TIMESTAMP NOT NULL,
    attributes JSON
);
