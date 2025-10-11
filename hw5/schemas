--
-- PostgreSQL database dump
--

\restrict cEyY7fh16e4RK7SHEsf27BIXP0w9r4AOh1PRCVAo94zFsCOEJ4wjdaTxVlH05WZ

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

-- Started on 2025-10-11 02:32:02

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 221 (class 1259 OID 16449)
-- Name: laptop; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.laptop (
    model integer NOT NULL,
    speed numeric(3,2) NOT NULL,
    ram integer NOT NULL,
    hd integer NOT NULL,
    screen numeric(4,1) NOT NULL,
    price integer NOT NULL
);


ALTER TABLE public.laptop OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16434)
-- Name: pc; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pc (
    model integer NOT NULL,
    speed numeric(3,2) NOT NULL,
    ram integer NOT NULL,
    hd integer NOT NULL,
    price integer NOT NULL
);


ALTER TABLE public.pc OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16465)
-- Name: printer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.printer (
    model integer NOT NULL,
    color boolean NOT NULL,
    type character varying(20) NOT NULL,
    price integer NOT NULL
);


ALTER TABLE public.printer OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16426)
-- Name: product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product (
    maker character(1) NOT NULL,
    model integer NOT NULL,
    type character varying(20) NOT NULL
);


ALTER TABLE public.product OWNER TO postgres;

--
-- TOC entry 4872 (class 2606 OID 16459)
-- Name: laptop laptop_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.laptop
    ADD CONSTRAINT laptop_pkey PRIMARY KEY (model);


--
-- TOC entry 4870 (class 2606 OID 16443)
-- Name: pc pc_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pc
    ADD CONSTRAINT pc_pkey PRIMARY KEY (model);


--
-- TOC entry 4874 (class 2606 OID 16473)
-- Name: printer printer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.printer
    ADD CONSTRAINT printer_pkey PRIMARY KEY (model);


--
-- TOC entry 4868 (class 2606 OID 16433)
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (model);


--
-- TOC entry 4876 (class 2606 OID 16460)
-- Name: laptop laptop_model_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.laptop
    ADD CONSTRAINT laptop_model_fkey FOREIGN KEY (model) REFERENCES public.product(model);


--
-- TOC entry 4875 (class 2606 OID 16444)
-- Name: pc pc_model_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pc
    ADD CONSTRAINT pc_model_fkey FOREIGN KEY (model) REFERENCES public.product(model);


--
-- TOC entry 4877 (class 2606 OID 16474)
-- Name: printer printer_model_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.printer
    ADD CONSTRAINT printer_model_fkey FOREIGN KEY (model) REFERENCES public.product(model);


-- Completed on 2025-10-11 02:32:02

--
-- PostgreSQL database dump complete
--

\unrestrict cEyY7fh16e4RK7SHEsf27BIXP0w9r4AOh1PRCVAo94zFsCOEJ4wjdaTxVlH05WZ

