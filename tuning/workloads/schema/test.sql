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
-- Name: sbtest1; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest1 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest1 OWNER TO tianjikun;

--
-- Name: sbtest10; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest10 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest10 OWNER TO tianjikun;

--
-- Name: sbtest11; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest11 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest11 OWNER TO tianjikun;

--
-- Name: sbtest12; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest12 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest12 OWNER TO tianjikun;

--
-- Name: sbtest13; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest13 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest13 OWNER TO tianjikun;

--
-- Name: sbtest14; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest14 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest14 OWNER TO tianjikun;

--
-- Name: sbtest15; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest15 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest15 OWNER TO tianjikun;

--
-- Name: sbtest16; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest16 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest16 OWNER TO tianjikun;

--
-- Name: sbtest17; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest17 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest17 OWNER TO tianjikun;

--
-- Name: sbtest18; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest18 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest18 OWNER TO tianjikun;

--
-- Name: sbtest19; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest19 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest19 OWNER TO tianjikun;

--
-- Name: sbtest2; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest2 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest2 OWNER TO tianjikun;

--
-- Name: sbtest20; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest20 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest20 OWNER TO tianjikun;

--
-- Name: sbtest3; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest3 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest3 OWNER TO tianjikun;

--
-- Name: sbtest4; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest4 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest4 OWNER TO tianjikun;

--
-- Name: sbtest5; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest5 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest5 OWNER TO tianjikun;

--
-- Name: sbtest6; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest6 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest6 OWNER TO tianjikun;

--
-- Name: sbtest7; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest7 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest7 OWNER TO tianjikun;

--
-- Name: sbtest8; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest8 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest8 OWNER TO tianjikun;

--
-- Name: sbtest9; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest9 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest9 OWNER TO tianjikun;

--
-- Name: sbtest10_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest10_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest10_id_seq OWNER TO tianjikun;

--
-- Name: sbtest10_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest10_id_seq OWNED BY sbtest10.id;


--
-- Name: sbtest11_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest11_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest11_id_seq OWNER TO tianjikun;

--
-- Name: sbtest11_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest11_id_seq OWNED BY sbtest11.id;


--
-- Name: sbtest12_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest12_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest12_id_seq OWNER TO tianjikun;

--
-- Name: sbtest12_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest12_id_seq OWNED BY sbtest12.id;


--
-- Name: sbtest13_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest13_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest13_id_seq OWNER TO tianjikun;

--
-- Name: sbtest13_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest13_id_seq OWNED BY sbtest13.id;


--
-- Name: sbtest14_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest14_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest14_id_seq OWNER TO tianjikun;

--
-- Name: sbtest14_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest14_id_seq OWNED BY sbtest14.id;


--
-- Name: sbtest15_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest15_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest15_id_seq OWNER TO tianjikun;

--
-- Name: sbtest15_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest15_id_seq OWNED BY sbtest15.id;


--
-- Name: sbtest16_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest16_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest16_id_seq OWNER TO tianjikun;

--
-- Name: sbtest16_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest16_id_seq OWNED BY sbtest16.id;


--
-- Name: sbtest17_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest17_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest17_id_seq OWNER TO tianjikun;

--
-- Name: sbtest17_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest17_id_seq OWNED BY sbtest17.id;


--
-- Name: sbtest18_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest18_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest18_id_seq OWNER TO tianjikun;

--
-- Name: sbtest18_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest18_id_seq OWNED BY sbtest18.id;


--
-- Name: sbtest19_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest19_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest19_id_seq OWNER TO tianjikun;

--
-- Name: sbtest19_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest19_id_seq OWNED BY sbtest19.id;


--
-- Name: sbtest1_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest1_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest1_id_seq OWNER TO tianjikun;

--
-- Name: sbtest1_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest1_id_seq OWNED BY sbtest1.id;


--
-- Name: sbtest20_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest20_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest20_id_seq OWNER TO tianjikun;

--
-- Name: sbtest20_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest20_id_seq OWNED BY sbtest20.id;


--
-- Name: sbtest2_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest2_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest2_id_seq OWNER TO tianjikun;

--
-- Name: sbtest2_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest2_id_seq OWNED BY sbtest2.id;


--
-- Name: sbtest3_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest3_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest3_id_seq OWNER TO tianjikun;

--
-- Name: sbtest3_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest3_id_seq OWNED BY sbtest3.id;


--
-- Name: sbtest4_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest4_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest4_id_seq OWNER TO tianjikun;

--
-- Name: sbtest4_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest4_id_seq OWNED BY sbtest4.id;


--
-- Name: sbtest5_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest5_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest5_id_seq OWNER TO tianjikun;

--
-- Name: sbtest5_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest5_id_seq OWNED BY sbtest5.id;


--
-- Name: sbtest6_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest6_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest6_id_seq OWNER TO tianjikun;

--
-- Name: sbtest6_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest6_id_seq OWNED BY sbtest6.id;


--
-- Name: sbtest7_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest7_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest7_id_seq OWNER TO tianjikun;

--
-- Name: sbtest7_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest7_id_seq OWNED BY sbtest7.id;


--
-- Name: sbtest8_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest8_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest8_id_seq OWNER TO tianjikun;

--
-- Name: sbtest8_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest8_id_seq OWNED BY sbtest8.id;


--
-- Name: sbtest9_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest9_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest9_id_seq OWNER TO tianjikun;

--
-- Name: sbtest9_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest9_id_seq OWNED BY sbtest9.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest1 ALTER COLUMN id SET DEFAULT nextval('sbtest1_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest10 ALTER COLUMN id SET DEFAULT nextval('sbtest10_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest11 ALTER COLUMN id SET DEFAULT nextval('sbtest11_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest12 ALTER COLUMN id SET DEFAULT nextval('sbtest12_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest13 ALTER COLUMN id SET DEFAULT nextval('sbtest13_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest14 ALTER COLUMN id SET DEFAULT nextval('sbtest14_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest15 ALTER COLUMN id SET DEFAULT nextval('sbtest15_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest16 ALTER COLUMN id SET DEFAULT nextval('sbtest16_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest17 ALTER COLUMN id SET DEFAULT nextval('sbtest17_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest18 ALTER COLUMN id SET DEFAULT nextval('sbtest18_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest19 ALTER COLUMN id SET DEFAULT nextval('sbtest19_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest2 ALTER COLUMN id SET DEFAULT nextval('sbtest2_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest20 ALTER COLUMN id SET DEFAULT nextval('sbtest20_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest3 ALTER COLUMN id SET DEFAULT nextval('sbtest3_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest4 ALTER COLUMN id SET DEFAULT nextval('sbtest4_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest5 ALTER COLUMN id SET DEFAULT nextval('sbtest5_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest6 ALTER COLUMN id SET DEFAULT nextval('sbtest6_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest7 ALTER COLUMN id SET DEFAULT nextval('sbtest7_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest8 ALTER COLUMN id SET DEFAULT nextval('sbtest8_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest9 ALTER COLUMN id SET DEFAULT nextval('sbtest9_id_seq'::regclass);


--
-- Name: sbtest10_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest10
    ADD CONSTRAINT sbtest10_pkey PRIMARY KEY  (id);


--
-- Name: sbtest11_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest11
    ADD CONSTRAINT sbtest11_pkey PRIMARY KEY  (id);


--
-- Name: sbtest12_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest12
    ADD CONSTRAINT sbtest12_pkey PRIMARY KEY  (id);


--
-- Name: sbtest13_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest13
    ADD CONSTRAINT sbtest13_pkey PRIMARY KEY  (id);


--
-- Name: sbtest14_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest14
    ADD CONSTRAINT sbtest14_pkey PRIMARY KEY  (id);


--
-- Name: sbtest15_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest15
    ADD CONSTRAINT sbtest15_pkey PRIMARY KEY  (id);


--
-- Name: sbtest16_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest16
    ADD CONSTRAINT sbtest16_pkey PRIMARY KEY  (id);


--
-- Name: sbtest17_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest17
    ADD CONSTRAINT sbtest17_pkey PRIMARY KEY  (id);


--
-- Name: sbtest18_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest18
    ADD CONSTRAINT sbtest18_pkey PRIMARY KEY  (id);


--
-- Name: sbtest19_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest19
    ADD CONSTRAINT sbtest19_pkey PRIMARY KEY  (id);


--
-- Name: sbtest1_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest1
    ADD CONSTRAINT sbtest1_pkey PRIMARY KEY  (id);


--
-- Name: sbtest20_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest20
    ADD CONSTRAINT sbtest20_pkey PRIMARY KEY  (id);


--
-- Name: sbtest2_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest2
    ADD CONSTRAINT sbtest2_pkey PRIMARY KEY  (id);


--
-- Name: sbtest3_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest3
    ADD CONSTRAINT sbtest3_pkey PRIMARY KEY  (id);


--
-- Name: sbtest4_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest4
    ADD CONSTRAINT sbtest4_pkey PRIMARY KEY  (id);


--
-- Name: sbtest5_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest5
    ADD CONSTRAINT sbtest5_pkey PRIMARY KEY  (id);


--
-- Name: sbtest6_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest6
    ADD CONSTRAINT sbtest6_pkey PRIMARY KEY  (id);


--
-- Name: sbtest7_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest7
    ADD CONSTRAINT sbtest7_pkey PRIMARY KEY  (id);


--
-- Name: sbtest8_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest8
    ADD CONSTRAINT sbtest8_pkey PRIMARY KEY  (id);


--
-- Name: sbtest9_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest9
    ADD CONSTRAINT sbtest9_pkey PRIMARY KEY  (id);


--
-- Name: k_1; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_1 ON sbtest1 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_10; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_10 ON sbtest10 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_11; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_11 ON sbtest11 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_12; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_12 ON sbtest12 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_13; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_13 ON sbtest13 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_14; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_14 ON sbtest14 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_15; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_15 ON sbtest15 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_16; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_16 ON sbtest16 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_17; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_17 ON sbtest17 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_18; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_18 ON sbtest18 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_19; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_19 ON sbtest19 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_2; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_2 ON sbtest2 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_20; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_20 ON sbtest20 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_3; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_3 ON sbtest3 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_4; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_4 ON sbtest4 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_5; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_5 ON sbtest5 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_6; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_6 ON sbtest6 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_7; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_7 ON sbtest7 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_8; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_8 ON sbtest8 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_9; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_9 ON sbtest9 USING btree (k) TABLESPACE pg_default;


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

