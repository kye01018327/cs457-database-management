--
-- PostgreSQL database dump
--

\restrict rCfdSnbqScy2CAOc9gf4rLFUz5Ryq0LYcSnzeAu94YdLGLWvbOdpOwhLqH2qDMK

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

-- Started on 2025-10-11 02:34:37

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

--
-- TOC entry 5025 (class 0 OID 16426)
-- Dependencies: 219
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.product (maker, model, type) FROM stdin;
A	1001	pc
A	1002	pc
A	1003	pc
A	2004	laptop
A	2005	laptop
A	2006	laptop
B	1004	pc
B	1005	pc
B	1006	pc
B	2007	laptop
C	1007	pc
D	1008	pc
D	1009	pc
D	1010	pc
D	3004	printer
D	3005	printer
E	1011	pc
E	1012	pc
E	1013	pc
E	2001	laptop
E	2002	laptop
E	2003	laptop
E	3001	printer
E	3002	printer
F	3003	printer
F	2008	laptop
F	2009	laptop
G	2010	laptop
H	3006	printer
H	3007	printer
\.


--
-- TOC entry 5027 (class 0 OID 16449)
-- Dependencies: 221
-- Data for Name: laptop; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.laptop (model, speed, ram, hd, screen, price) FROM stdin;
2001	2.00	2048	240	20.1	3673
2002	1.73	1024	80	17.0	949
2003	1.80	512	60	15.4	549
2004	2.00	512	60	13.3	1150
2005	2.16	1024	120	17.0	2500
2006	2.00	2048	80	15.4	1700
2007	1.83	1024	120	13.3	1429
2008	1.60	1024	100	15.4	900
2009	1.60	512	80	14.1	680
2010	2.00	2048	160	15.4	2300
\.


--
-- TOC entry 5026 (class 0 OID 16434)
-- Dependencies: 220
-- Data for Name: pc; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pc (model, speed, ram, hd, price) FROM stdin;
1001	2.66	1024	250	2114
1002	2.10	512	250	995
1003	1.42	512	80	478
1004	2.80	1024	250	649
1005	3.20	512	250	630
1006	3.20	1024	320	1049
1007	2.20	1024	200	510
1008	2.20	2048	250	770
1009	2.00	1024	250	650
1010	2.80	2048	300	770
1011	1.86	2048	160	959
1012	2.80	1024	180	649
1013	3.06	512	80	529
\.


--
-- TOC entry 5028 (class 0 OID 16465)
-- Dependencies: 222
-- Data for Name: printer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.printer (model, color, type, price) FROM stdin;
3001	t	ink-jet	99
3002	f	laser	239
3003	t	laser	899
3004	t	ink-jet	120
3005	f	laser	120
3006	t	ink-jet	100
3007	t	laser	200
\.


-- Completed on 2025-10-11 02:34:37

--
-- PostgreSQL database dump complete
--

\unrestrict rCfdSnbqScy2CAOc9gf4rLFUz5Ryq0LYcSnzeAu94YdLGLWvbOdpOwhLqH2qDMK

