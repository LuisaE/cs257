CREATE TABLE sales(
    id SERIAL,
    na integer,
    eu integer,
    jp integer,
    other integer,
    global_sales integer
);

CREATE TABLE platforms(
    id SERIAL,
    platform text
);

CREATE TABLE games_platforms(
    games_id integer,
    platforms_id integer,
    sales_id integer,
    user_score decimal,
    critic_score decimal
);

CREATE TABLE games(
    id SERIAL,
    name text,
    year integer,
    rating text,
    genre_id integer,
    publisher_id integer
);

CREATE TABLE publishers(
    id SERIAL,
    publisher text
);

CREATE TABLE genres(
    id SERIAL,
    genre text
);
