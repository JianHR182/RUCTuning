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
-- Name: sbtest21; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest21 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest21 OWNER TO tianjikun;

--
-- Name: sbtest22; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest22 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest22 OWNER TO tianjikun;

--
-- Name: sbtest23; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest23 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest23 OWNER TO tianjikun;

--
-- Name: sbtest24; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest24 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest24 OWNER TO tianjikun;

--
-- Name: sbtest25; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest25 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest25 OWNER TO tianjikun;

--
-- Name: sbtest26; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest26 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest26 OWNER TO tianjikun;

--
-- Name: sbtest27; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest27 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest27 OWNER TO tianjikun;

--
-- Name: sbtest28; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest28 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest28 OWNER TO tianjikun;

--
-- Name: sbtest29; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest29 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest29 OWNER TO tianjikun;

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
-- Name: sbtest30; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest30 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest30 OWNER TO tianjikun;

--
-- Name: sbtest31; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest31 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest31 OWNER TO tianjikun;

--
-- Name: sbtest32; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest32 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest32 OWNER TO tianjikun;

--
-- Name: sbtest33; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest33 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest33 OWNER TO tianjikun;

--
-- Name: sbtest34; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest34 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest34 OWNER TO tianjikun;

--
-- Name: sbtest35; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest35 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest35 OWNER TO tianjikun;

--
-- Name: sbtest36; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest36 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest36 OWNER TO tianjikun;

--
-- Name: sbtest37; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest37 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest37 OWNER TO tianjikun;

--
-- Name: sbtest38; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest38 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest38 OWNER TO tianjikun;

--
-- Name: sbtest39; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest39 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest39 OWNER TO tianjikun;

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
-- Name: sbtest40; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest40 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest40 OWNER TO tianjikun;

--
-- Name: sbtest41; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest41 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest41 OWNER TO tianjikun;

--
-- Name: sbtest42; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest42 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest42 OWNER TO tianjikun;

--
-- Name: sbtest43; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest43 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest43 OWNER TO tianjikun;

--
-- Name: sbtest44; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest44 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest44 OWNER TO tianjikun;

--
-- Name: sbtest45; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest45 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest45 OWNER TO tianjikun;

--
-- Name: sbtest46; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest46 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest46 OWNER TO tianjikun;

--
-- Name: sbtest47; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest47 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest47 OWNER TO tianjikun;

--
-- Name: sbtest48; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest48 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest48 OWNER TO tianjikun;

--
-- Name: sbtest49; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest49 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest49 OWNER TO tianjikun;

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
-- Name: sbtest50; Type: TABLE; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE TABLE sbtest50 (
    id integer NOT NULL,
    k integer DEFAULT 0 NOT NULL,
    c character(120) DEFAULT NULL::bpchar NOT NULL,
    pad character(60) DEFAULT NULL::bpchar NOT NULL
)
WITH (orientation=row, compression=no);


ALTER TABLE public.sbtest50 OWNER TO tianjikun;

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
-- Name: sbtest21_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest21_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest21_id_seq OWNER TO tianjikun;

--
-- Name: sbtest21_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest21_id_seq OWNED BY sbtest21.id;


--
-- Name: sbtest22_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest22_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest22_id_seq OWNER TO tianjikun;

--
-- Name: sbtest22_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest22_id_seq OWNED BY sbtest22.id;


--
-- Name: sbtest23_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest23_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest23_id_seq OWNER TO tianjikun;

--
-- Name: sbtest23_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest23_id_seq OWNED BY sbtest23.id;


--
-- Name: sbtest24_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest24_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest24_id_seq OWNER TO tianjikun;

--
-- Name: sbtest24_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest24_id_seq OWNED BY sbtest24.id;


--
-- Name: sbtest25_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest25_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest25_id_seq OWNER TO tianjikun;

--
-- Name: sbtest25_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest25_id_seq OWNED BY sbtest25.id;


--
-- Name: sbtest26_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest26_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest26_id_seq OWNER TO tianjikun;

--
-- Name: sbtest26_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest26_id_seq OWNED BY sbtest26.id;


--
-- Name: sbtest27_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest27_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest27_id_seq OWNER TO tianjikun;

--
-- Name: sbtest27_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest27_id_seq OWNED BY sbtest27.id;


--
-- Name: sbtest28_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest28_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest28_id_seq OWNER TO tianjikun;

--
-- Name: sbtest28_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest28_id_seq OWNED BY sbtest28.id;


--
-- Name: sbtest29_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest29_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest29_id_seq OWNER TO tianjikun;

--
-- Name: sbtest29_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest29_id_seq OWNED BY sbtest29.id;


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
-- Name: sbtest30_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest30_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest30_id_seq OWNER TO tianjikun;

--
-- Name: sbtest30_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest30_id_seq OWNED BY sbtest30.id;


--
-- Name: sbtest31_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest31_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest31_id_seq OWNER TO tianjikun;

--
-- Name: sbtest31_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest31_id_seq OWNED BY sbtest31.id;


--
-- Name: sbtest32_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest32_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest32_id_seq OWNER TO tianjikun;

--
-- Name: sbtest32_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest32_id_seq OWNED BY sbtest32.id;


--
-- Name: sbtest33_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest33_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest33_id_seq OWNER TO tianjikun;

--
-- Name: sbtest33_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest33_id_seq OWNED BY sbtest33.id;


--
-- Name: sbtest34_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest34_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest34_id_seq OWNER TO tianjikun;

--
-- Name: sbtest34_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest34_id_seq OWNED BY sbtest34.id;


--
-- Name: sbtest35_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest35_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest35_id_seq OWNER TO tianjikun;

--
-- Name: sbtest35_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest35_id_seq OWNED BY sbtest35.id;


--
-- Name: sbtest36_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest36_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest36_id_seq OWNER TO tianjikun;

--
-- Name: sbtest36_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest36_id_seq OWNED BY sbtest36.id;


--
-- Name: sbtest37_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest37_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest37_id_seq OWNER TO tianjikun;

--
-- Name: sbtest37_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest37_id_seq OWNED BY sbtest37.id;


--
-- Name: sbtest38_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest38_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest38_id_seq OWNER TO tianjikun;

--
-- Name: sbtest38_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest38_id_seq OWNED BY sbtest38.id;


--
-- Name: sbtest39_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest39_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest39_id_seq OWNER TO tianjikun;

--
-- Name: sbtest39_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest39_id_seq OWNED BY sbtest39.id;


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
-- Name: sbtest40_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest40_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest40_id_seq OWNER TO tianjikun;

--
-- Name: sbtest40_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest40_id_seq OWNED BY sbtest40.id;


--
-- Name: sbtest41_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest41_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest41_id_seq OWNER TO tianjikun;

--
-- Name: sbtest41_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest41_id_seq OWNED BY sbtest41.id;


--
-- Name: sbtest42_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest42_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest42_id_seq OWNER TO tianjikun;

--
-- Name: sbtest42_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest42_id_seq OWNED BY sbtest42.id;


--
-- Name: sbtest43_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest43_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest43_id_seq OWNER TO tianjikun;

--
-- Name: sbtest43_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest43_id_seq OWNED BY sbtest43.id;


--
-- Name: sbtest44_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest44_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest44_id_seq OWNER TO tianjikun;

--
-- Name: sbtest44_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest44_id_seq OWNED BY sbtest44.id;


--
-- Name: sbtest45_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest45_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest45_id_seq OWNER TO tianjikun;

--
-- Name: sbtest45_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest45_id_seq OWNED BY sbtest45.id;


--
-- Name: sbtest46_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest46_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest46_id_seq OWNER TO tianjikun;

--
-- Name: sbtest46_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest46_id_seq OWNED BY sbtest46.id;


--
-- Name: sbtest47_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest47_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest47_id_seq OWNER TO tianjikun;

--
-- Name: sbtest47_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest47_id_seq OWNED BY sbtest47.id;


--
-- Name: sbtest48_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest48_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest48_id_seq OWNER TO tianjikun;

--
-- Name: sbtest48_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest48_id_seq OWNED BY sbtest48.id;


--
-- Name: sbtest49_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest49_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest49_id_seq OWNER TO tianjikun;

--
-- Name: sbtest49_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest49_id_seq OWNED BY sbtest49.id;


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
-- Name: sbtest50_id_seq; Type: SEQUENCE; Schema: public; Owner: tianjikun
--

CREATE  SEQUENCE sbtest50_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sbtest50_id_seq OWNER TO tianjikun;

--
-- Name: sbtest50_id_seq; Type: LARGE SEQUENCE OWNED BY; Schema: public; Owner: tianjikun
--

ALTER  SEQUENCE sbtest50_id_seq OWNED BY sbtest50.id;


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

ALTER TABLE sbtest21 ALTER COLUMN id SET DEFAULT nextval('sbtest21_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest22 ALTER COLUMN id SET DEFAULT nextval('sbtest22_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest23 ALTER COLUMN id SET DEFAULT nextval('sbtest23_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest24 ALTER COLUMN id SET DEFAULT nextval('sbtest24_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest25 ALTER COLUMN id SET DEFAULT nextval('sbtest25_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest26 ALTER COLUMN id SET DEFAULT nextval('sbtest26_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest27 ALTER COLUMN id SET DEFAULT nextval('sbtest27_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest28 ALTER COLUMN id SET DEFAULT nextval('sbtest28_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest29 ALTER COLUMN id SET DEFAULT nextval('sbtest29_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest3 ALTER COLUMN id SET DEFAULT nextval('sbtest3_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest30 ALTER COLUMN id SET DEFAULT nextval('sbtest30_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest31 ALTER COLUMN id SET DEFAULT nextval('sbtest31_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest32 ALTER COLUMN id SET DEFAULT nextval('sbtest32_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest33 ALTER COLUMN id SET DEFAULT nextval('sbtest33_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest34 ALTER COLUMN id SET DEFAULT nextval('sbtest34_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest35 ALTER COLUMN id SET DEFAULT nextval('sbtest35_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest36 ALTER COLUMN id SET DEFAULT nextval('sbtest36_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest37 ALTER COLUMN id SET DEFAULT nextval('sbtest37_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest38 ALTER COLUMN id SET DEFAULT nextval('sbtest38_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest39 ALTER COLUMN id SET DEFAULT nextval('sbtest39_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest4 ALTER COLUMN id SET DEFAULT nextval('sbtest4_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest40 ALTER COLUMN id SET DEFAULT nextval('sbtest40_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest41 ALTER COLUMN id SET DEFAULT nextval('sbtest41_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest42 ALTER COLUMN id SET DEFAULT nextval('sbtest42_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest43 ALTER COLUMN id SET DEFAULT nextval('sbtest43_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest44 ALTER COLUMN id SET DEFAULT nextval('sbtest44_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest45 ALTER COLUMN id SET DEFAULT nextval('sbtest45_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest46 ALTER COLUMN id SET DEFAULT nextval('sbtest46_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest47 ALTER COLUMN id SET DEFAULT nextval('sbtest47_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest48 ALTER COLUMN id SET DEFAULT nextval('sbtest48_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest49 ALTER COLUMN id SET DEFAULT nextval('sbtest49_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest5 ALTER COLUMN id SET DEFAULT nextval('sbtest5_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tianjikun
--

ALTER TABLE sbtest50 ALTER COLUMN id SET DEFAULT nextval('sbtest50_id_seq'::regclass);


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
-- Name: sbtest21_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest21
    ADD CONSTRAINT sbtest21_pkey PRIMARY KEY  (id);


--
-- Name: sbtest22_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest22
    ADD CONSTRAINT sbtest22_pkey PRIMARY KEY  (id);


--
-- Name: sbtest23_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest23
    ADD CONSTRAINT sbtest23_pkey PRIMARY KEY  (id);


--
-- Name: sbtest24_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest24
    ADD CONSTRAINT sbtest24_pkey PRIMARY KEY  (id);


--
-- Name: sbtest25_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest25
    ADD CONSTRAINT sbtest25_pkey PRIMARY KEY  (id);


--
-- Name: sbtest26_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest26
    ADD CONSTRAINT sbtest26_pkey PRIMARY KEY  (id);


--
-- Name: sbtest27_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest27
    ADD CONSTRAINT sbtest27_pkey PRIMARY KEY  (id);


--
-- Name: sbtest28_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest28
    ADD CONSTRAINT sbtest28_pkey PRIMARY KEY  (id);


--
-- Name: sbtest29_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest29
    ADD CONSTRAINT sbtest29_pkey PRIMARY KEY  (id);


--
-- Name: sbtest2_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest2
    ADD CONSTRAINT sbtest2_pkey PRIMARY KEY  (id);


--
-- Name: sbtest30_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest30
    ADD CONSTRAINT sbtest30_pkey PRIMARY KEY  (id);


--
-- Name: sbtest31_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest31
    ADD CONSTRAINT sbtest31_pkey PRIMARY KEY  (id);


--
-- Name: sbtest32_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest32
    ADD CONSTRAINT sbtest32_pkey PRIMARY KEY  (id);


--
-- Name: sbtest33_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest33
    ADD CONSTRAINT sbtest33_pkey PRIMARY KEY  (id);


--
-- Name: sbtest34_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest34
    ADD CONSTRAINT sbtest34_pkey PRIMARY KEY  (id);


--
-- Name: sbtest35_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest35
    ADD CONSTRAINT sbtest35_pkey PRIMARY KEY  (id);


--
-- Name: sbtest36_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest36
    ADD CONSTRAINT sbtest36_pkey PRIMARY KEY  (id);


--
-- Name: sbtest37_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest37
    ADD CONSTRAINT sbtest37_pkey PRIMARY KEY  (id);


--
-- Name: sbtest38_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest38
    ADD CONSTRAINT sbtest38_pkey PRIMARY KEY  (id);


--
-- Name: sbtest39_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest39
    ADD CONSTRAINT sbtest39_pkey PRIMARY KEY  (id);


--
-- Name: sbtest3_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest3
    ADD CONSTRAINT sbtest3_pkey PRIMARY KEY  (id);


--
-- Name: sbtest40_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest40
    ADD CONSTRAINT sbtest40_pkey PRIMARY KEY  (id);


--
-- Name: sbtest41_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest41
    ADD CONSTRAINT sbtest41_pkey PRIMARY KEY  (id);


--
-- Name: sbtest42_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest42
    ADD CONSTRAINT sbtest42_pkey PRIMARY KEY  (id);


--
-- Name: sbtest43_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest43
    ADD CONSTRAINT sbtest43_pkey PRIMARY KEY  (id);


--
-- Name: sbtest44_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest44
    ADD CONSTRAINT sbtest44_pkey PRIMARY KEY  (id);


--
-- Name: sbtest45_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest45
    ADD CONSTRAINT sbtest45_pkey PRIMARY KEY  (id);


--
-- Name: sbtest46_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest46
    ADD CONSTRAINT sbtest46_pkey PRIMARY KEY  (id);


--
-- Name: sbtest47_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest47
    ADD CONSTRAINT sbtest47_pkey PRIMARY KEY  (id);


--
-- Name: sbtest48_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest48
    ADD CONSTRAINT sbtest48_pkey PRIMARY KEY  (id);


--
-- Name: sbtest49_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest49
    ADD CONSTRAINT sbtest49_pkey PRIMARY KEY  (id);


--
-- Name: sbtest4_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest4
    ADD CONSTRAINT sbtest4_pkey PRIMARY KEY  (id);


--
-- Name: sbtest50_pkey; Type: CONSTRAINT; Schema: public; Owner: tianjikun; Tablespace: 
--

ALTER TABLE sbtest50
    ADD CONSTRAINT sbtest50_pkey PRIMARY KEY  (id);


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
-- Name: k_21; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_21 ON sbtest21 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_22; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_22 ON sbtest22 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_23; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_23 ON sbtest23 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_24; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_24 ON sbtest24 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_25; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_25 ON sbtest25 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_26; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_26 ON sbtest26 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_27; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_27 ON sbtest27 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_28; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_28 ON sbtest28 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_29; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_29 ON sbtest29 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_3; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_3 ON sbtest3 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_30; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_30 ON sbtest30 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_31; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_31 ON sbtest31 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_32; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_32 ON sbtest32 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_33; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_33 ON sbtest33 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_34; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_34 ON sbtest34 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_35; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_35 ON sbtest35 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_36; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_36 ON sbtest36 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_37; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_37 ON sbtest37 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_38; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_38 ON sbtest38 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_39; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_39 ON sbtest39 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_4; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_4 ON sbtest4 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_40; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_40 ON sbtest40 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_41; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_41 ON sbtest41 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_42; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_42 ON sbtest42 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_43; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_43 ON sbtest43 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_44; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_44 ON sbtest44 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_45; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_45 ON sbtest45 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_46; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_46 ON sbtest46 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_47; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_47 ON sbtest47 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_48; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_48 ON sbtest48 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_49; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_49 ON sbtest49 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_5; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_5 ON sbtest5 USING btree (k) TABLESPACE pg_default;


--
-- Name: k_50; Type: INDEX; Schema: public; Owner: tianjikun; Tablespace: 
--

CREATE INDEX k_50 ON sbtest50 USING btree (k) TABLESPACE pg_default;


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

