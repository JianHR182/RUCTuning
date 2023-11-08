--
-- openGauss database dump
--

SET statement_timeout = 0;
SET xmloption = content;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: my_table; Type: TABLE; Schema: public; Owner: lzz; Tablespace: 
--

CREATE TABLE my_table (
    id integer NOT NULL,
    my_float double precision,
    my_double double precision,
    my_varchar character varying(255),
    my_timestamp timestamp without time zone,
    my_blob blob
)
WITH (orientation=row, compression=no);


ALTER TABLE public.my_table OWNER TO lzz;

--
-- Name: my_table3; Type: TABLE; Schema: public; Owner: lzz; Tablespace: 
--

CREATE TABLE my_table3 (
    id integer NOT NULL,
    my_float double precision,
    my_double double precision,
    my_varchar character varying(5),
    my_timestamp timestamp without time zone,
    my_blob blob
)
WITH (orientation=row, compression=no);


ALTER TABLE public.my_table3 OWNER TO lzz;

--
-- Name: my_table5; Type: TABLE; Schema: public; Owner: lzz; Tablespace: 
--

CREATE TABLE my_table5 (
    id integer NOT NULL,
    my_float double precision,
    my_double double precision,
    my_varchar2 character varying(5),
    my_timestamp timestamp without time zone,
    my_blob blob
)
WITH (orientation=row, compression=no);


ALTER TABLE public.my_table5 OWNER TO lzz;

--
-- Data for Name: my_table; Type: TABLE DATA; Schema: public; Owner: lzz
--

COPY my_table (id, my_float, my_double, my_varchar, my_timestamp, my_blob) FROM stdin;
\.
;

--
-- Data for Name: my_table3; Type: TABLE DATA; Schema: public; Owner: lzz
--

COPY my_table3 (id, my_float, my_double, my_varchar, my_timestamp, my_blob) FROM stdin;
\.
;

--
-- Data for Name: my_table5; Type: TABLE DATA; Schema: public; Owner: lzz
--

COPY my_table5 (id, my_float, my_double, my_varchar2, my_timestamp, my_blob) FROM stdin;
\.
;

--
-- Name: public; Type: ACL; Schema: -; Owner: omm
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM omm;
GRANT CREATE,USAGE ON SCHEMA public TO omm;
GRANT USAGE ON SCHEMA public TO PUBLIC;


--
-- openGauss database dump complete
--

