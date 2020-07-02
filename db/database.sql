-- Table: public."crimeCategories"

-- DROP TABLE public."crimeCategories";

CREATE TABLE public."crimeCategories"
(
    id integer NOT NULL DEFAULT nextval('"crimeCategories_id_seq"'::regclass),
    name character(200) COLLATE pg_catalog."default",
    CONSTRAINT "crimeCategories_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public."crimeCategories"
    OWNER to postgres;


-- Table: public."outcomesCount"

-- DROP TABLE public."outcomesCount";

CREATE TABLE public."outcomesCount"
(
    id integer NOT NULL DEFAULT nextval('"outcomesCount_id_seq"'::regclass),
    persistent_id character(200) COLLATE pg_catalog."default",
    CONSTRAINT "outcomesCount_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public."outcomesCount"
    OWNER to postgres;


-- Table: public."outcomesCrimes"

-- DROP TABLE public."outcomesCrimes";

CREATE TABLE public."outcomesCrimes"
(
    id integer NOT NULL DEFAULT nextval('"outcomesCrimes_id_seq"'::regclass),
    persistent_id character(200) COLLATE pg_catalog."default",
    category character(200) COLLATE pg_catalog."default",
    date_1 character(200) COLLATE pg_catalog."default",
    person_id character(200) COLLATE pg_catalog."default",
    CONSTRAINT "outcomesCrimes_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public."outcomesCrimes"
    OWNER to postgres;


-- Table: public."streetLevelCrimes"

-- DROP TABLE public."streetLevelCrimes";

CREATE TABLE public."streetLevelCrimes"
(
    id integer NOT NULL,
    category_id character(200) COLLATE pg_catalog."default",
    location_type character(200) COLLATE pg_catalog."default",
    latitude character(200) COLLATE pg_catalog."default",
    longitude character(200) COLLATE pg_catalog."default",
    street_id character(200) COLLATE pg_catalog."default",
    street_name character(200) COLLATE pg_catalog."default",
    context character(200) COLLATE pg_catalog."default",
    outcome_status character(200) COLLATE pg_catalog."default",
    persistent_id character(200) COLLATE pg_catalog."default",
    location_subtype character(200) COLLATE pg_catalog."default",
    month character(200) COLLATE pg_catalog."default",
    CONSTRAINT "streetLevelCrimes_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public."streetLevelCrimes"
    OWNER to postgres;


-- Table: public.users

-- DROP TABLE public.users;

CREATE TABLE public.users
(
    id integer NOT NULL DEFAULT nextval('users_id_seq'::regclass),
    name character(200) COLLATE pg_catalog."default",
    lastname character(200) COLLATE pg_catalog."default",
    email character(200) COLLATE pg_catalog."default",
    username character(200) COLLATE pg_catalog."default",
    password character(200) COLLATE pg_catalog."default",
    date character(200) COLLATE pg_catalog."default",
    CONSTRAINT users_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.users
    OWNER to postgres;