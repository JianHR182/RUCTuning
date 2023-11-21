CREATE TABLE my_table (
    id integer NOT NULL,
    my_float double precision,
    my_num numeric(30,2),
    my_double double precision,
    my_varchar character varying(255),
    my_timestamp timestamp(3) without time zone,
    my_blob blob
)
WITH (orientation=row, compression=no);

CREATE TABLE my_table3 (
    id integer NOT NULL,
    my_float double precision,
    my_double double precision,
    my_varchar character varying(5),
    my_num numeric DEFAULT 0::numeric NOT NULL,
    my_timestamp timestamp without time zone,
    my_blob blob
)
WITH (orientation=row, compression=no);
CREATE TABLE my_table5 (
    id integer NOT NULL,
    my_float double precision,
    my_double double precision,
    my_varchar2 character varying(5),
    my_timestamp timestamp without time zone,
    my_blob blob
)
WITH (orientation=row, compression=no);
