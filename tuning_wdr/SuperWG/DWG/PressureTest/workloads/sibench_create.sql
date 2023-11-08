CREATE TABLE public.sitest(
    id integer NOT NULL,
    value integer NOT NULL
);


ALTER TABLE public.sitest OWNER TO lzz;

ALTER TABLE ONLY public.sitest
    ADD CONSTRAINT sitest_pkey PRIMARY KEY (id);

