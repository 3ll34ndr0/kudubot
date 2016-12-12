destinos = {'villaguay': """
SALIDA LLEGADA EMPRESA
23:55  01:55   *FLECHA BUS* 
00:35  02:35   *RAPIDO TATA*
00:35  02:35   *RAPIDO TATA* _salvo sabados_
03:10  05:00   *ZENIT* _lunes a viernes_
06:35  09:00   *SAN JOSE* _lunes a viernes_
09:30  11:30   *ZENIT*
11:05  13:00   *FLECHA BUS* _lunes a sabados_
14:10  16:05   *FLECHA BUS*
16:50  19:00   *21 AUTOTRANSPORTE*
18:30  20:25   *NUEVO EXPRESO*
20:00  22:35   *SAN JOSE* _lunes a sabados_
21:43  23:45   *ZENIT*
""" ,'villa clara': """SALIDA LLEGADA EMPRESA
23:55  01:05   *FLECHA BUS*
03:10  04:30   *ZENIT*
06:35  08:30   *SAN JOSE*
09:30  11:15   *ZENIT*
11:05  12:35   *FLECHA BUS*
14:10  15:40   *FLECHA BUS*
16:50  18:30   *21 AUTOTRANSPORTE*
18:30  20:05   *NUEVO EXPRESO*
20:00  22:05   *SAN JOSE* _lunes a sabados_
""" , 'victoria': """SALIDA LLEGADA EMPRESA
23:25  05:35   *RIO URUGUAY* _salvo sabados_
00:35  05:40   *RAPIDO TATA* _salvo sabados_
07:00  13:00   *RIO URUGUAY*
12:20  18:20   *RAPIDO TATA*
""" , 'viale': """SALIDA LLEGADA EMPRESA
04:50  08:00   *E.T.A*
18:20  21:30   *no definido* 
""" , 'ubajay': """SALIDA LLEGADA EMPRESA
07:00  07:45   *RIO URUGUAY* _solo lunes-miercoles-jueves-viernes_
""" , 'santa fe': """SALIDA LLEGADA EMPRESA
21:43  02:50   *ZENIT*
23:20  04:00   *MERCOBUS*
23:55  04:45   *FLECHA BUS*
01:00  05:00   *TIGRE IGUAZU*
01:30  05:30   *SINGER*
02:15  06:30   *SAN JOSE*
""" , 'san salvador': """SALIDA LLEGADA EMPRESA
23:00  00:20   *PALMARES*
23:55  00:40   *FLECHA BUS*
00:35  01:35   *RAPIDO TATA* _salvo sabados_
00:35  01:35   *RAPIDO TATA*
02:15  03:05   *SAN JOSE*
03:10  04:10   *ZENIT* _lunes a viernes_
06:35  08:05   *SAN JOSE* _salvo domingos_
08:15  09:30   *PALMARES* _sabados, domingos y feriados_
09:30  10:30   *ZENIT*
11:05  12:15   *FLECHA BUS*
12:30  13:45   *PALMARES* _lunes a sabados_
14:10  15:10   *FLECHA BUS*
16:50  18:10   *21 AUTOTRANSPORTE* 
18:30  19:30   *NUEVO EXPRESO* 
18:30  19:45   *PALMARES* _lunes a sabados_
20:00  21:20   *SAN JOSE* 
21:00  22:15   *PALMARES* _lunes a viernes_
21:43  22:35   *ZENIT* 
22:20  23:30   *PALMARES*
""", 'san jose': """SALIDA LLEGADA EMPRESA
23:10  00:55   *JOVI BUS*
23:25  01:05   *RIO URUGUAY*
23:25  01:05   *RIO URUGUAY* _salvo sabados_
23:40  01:20   *RAPIDO TATA*
05:25  07:00   *NUEVO EXPRESO*
07:00  08:45   *RIO URUGUAY*
07:00  08:45   *RIO URUGUAY*
08:00  09:45   *NUEVO EXPRESO*
08:25  10:00   *JOVI BUS*
10:25  12:00   *NUEVO EXPRESO*
12:20  13:55   *RAPIDO TATA*
12:20  13:55   *RAPIDO TATA*
12:40  14:15   *RAPIDO TATA*
13:00  15:00   *JOVI BUS*
16:25  18:00   *NUEVO EXPRESO*
17:45  19:25   *RAPIDO TATA*
18:00  20:00   *JOVI BUS*
19:00  21:00   *JOVI BUS*
""", 'salto': """SALIDA LLEGADA EMPRESA 
07:05  08:10   *FLECHA BUS* 	
11:15  12:15   *CHADRE* 	
18:00  19:00   *CHADRE* 	
19:15  20:15   *FLECHA BUS* 	
""", 'rosario del tala': """SALIDA LLEGADA EMPRESA 
07:00  11:15   *RIO URUGUAY* 
12:20  16:25   *RAPIDO TATA* 
23:25  03:50   *RIO URUGUAY* _salvo sabados_
""", 'rosario': """SALIDA LLEGADA EMPRESA 
01:15  01:15   *TIGRE IGUAZU* 
23:25  06:30   *RIO URUGUAY* _salvo sabados_
00:35  06:50   *RAPIDO TATA* _salvo sabados_
23:55  07:00   *FLECHA BUS* 
07:00  14:00   *RIO URUGUAY* 
12:20  19:20   *RAPIDO TATA* 
""", 'retiro': """SALIDA LLEGADA EMPRESA 
17:45  01:20   *RAPIDO TATA* 
23:50  05:30   *FLECHA BUS* 
00:10  06:00   *NUEVO EXPRESO* 
00:15  06:00   *SINGER* 
00:55  06:00   *RAPIDO TATA* 
00:45  06:30   *RAPIDO TATA* 
01:00  06:30   *FLECHA BUS* 
01:15  06:45   *FLECHA BUS* 
01:20  07:15   *FLECHA BUS* 
02:10  07:30   *FLECHA BUS* 
02:35  08:25   *RAPIDO ARGENTINO* 
06:25  13:00   *SINGER* 
05:45  13:10   *CRUCERO NORTE* 
09:10  15:00   *FLECHA BUS* 
12:15  18:30   *FLECHA BUS* 
13:15  19:40   *RAPIDO TATA* 
12:40  20:30   *RAPIDO TATA* 
15:30  21:30   *FLECHA BUS* 
16:30  22:30   *FLECHA BUS* 
17:15  23:15   *NUEVO EXPRESO* 
""", 'resistencia': """SALIDA LLEGADA EMPRESA 
21:30  04:40   *NUEVO EXPRESO* 
23:15  08:00   *NUEVO EXPRESO* 
00:40  08:20   *FLECHA BUS* 
13:15  21:00   *NUEVO EXPRESO* 
""", 'puerto yerua': """SALIDA LLEGADA EMPRESA 
05:45  07:00   *LUCERITO* _lunes a sabados_
07:00  08:00   *LUCERITO* _domingos y feriados_
10:45  11:25   *LUCERITO* _lunes a viernes_
11:00  12:00   *LUCERITO* _domingos y feriados_
12:00  12:45   *LUCERITO* _lunes a sabados_
18:30  19:15   *LUCERITO* _lunes a sabados_
18:30  19:30   *LUCERITO* _domingos y feriados_
21:30  22:30   *LUCERITO* _lunes a sabados_
""", 'puerto iguazu': """SALIDA LLEGADA EMPRESA 
19:15  07:00   *SINGER* 
19:45  08:00   *TIGRE IGUAZU* 
21:30  09:00   *CRUCERO NORTE* 
21:00  09:30   *RAPIDO ARGENTINO* 
""", 'posadas': """SALIDA LLEGADA EMPRESA 
19:15  04:00   *SINGER* 
19:45  04:00   *TIGRE IGUAZU* 
21:00  05:30   *RAPIDO ARGENTINO* 
21:30  06:00   *CRUCERO NORTE* 
01:20  08:30   *TIGRE IGUAZU* 
08:40  17:00   *MERCOBUS* _jueves y sabados_
""", 'paso de los libres': """SALIDA LLEGADA EMPRESA 
21:00  03:00   *RAPIDO ARGENTINO* 
03:30  06:55   *FLECHA BUS* 
02:45  07:10   *RAPIDO TATA* 
08:45  15:00   *MERCOBUS* 
14:50  19:05   *FLECHA BUS* 
""", 'parana': """SALIDA LLEGADA EMPRESA 
21:43  02:08   *ZENIT* 
22:20  02:40   *MERCOBUS* 
23:55  04:05   *FLECHA BUS* 
01:30  05:00   *TIGRE IGUAZU* 
02:15  05:50   *SAN JOSE* 
23:15  06:00   *LUCERITO* 
03:10  07:10   *ZENIT* _lunes a viernes_
04:50  08:55   *E.T.A* _solo lunes_
06:35  11:30   *SAN JOSE* 
09:30  14:00   *ZENIT* 
10:30  15:45   *21 AUTOTRANSPORTE* 
11:05  18:20   *FLECHA BUS* _salvo domingos_
14:10  18:25   *FLECHA BUS* 
12:30  19:30   *LUCERITO* 
16:50  21:05   *21 AUTOTRANSPORTE* 
""", 'nueva escocia': """SALIDA LLEGADA EMPRESA 
07:00  08:30   *LUCERITO* _domingos y feriados_
10:45  12:15   *LUCERITO* _lunes a viernes_
12:00  13:30   *LUCERITO* _lunes a sabados_
18:30  20:00   *LUCERITO* _lunes a sabados_
18:30  20:00   *LUCERITO* _domingos y feriados_
""", 'nogoya': """SALIDA LLEGADA EMPRESA 
00:35  05:00   *RAPIDO TATA* _salvo sabados_
07:00  12:15   *RIO URUGUAY* 
12:20  17:35   *RAPIDO TATA* 
23:25  04:50   *RIO URUGUAY* _salvo sabados_
""", 'monte caseros': """SALIDA LLEGADA EMPRESA 
01:45  04:50   *FLECHA BUS* 
04:05  07:00   *FLECHA BUS* 
05:15  08:25   *FLECHA BUS* 
06:10  09:30   *ZENIT* 
08:00  11:00   *NUEVO EXPRESO* 
15:50  19:10   *MERCOBUS* 
19:00  22:40   *RAPIDO TATA* 
""", 'mocoreta': """SALIDA LLEGADA EMPRESA 
23:15  01:00   *NUEVO EXPRESO* 
01:45  03:40   *FLECHA BUS* 
03:30  04:55   *FLECHA BUS* 
05:15  07:25   *FLECHA BUS* 
06:10  08:30   *ZENIT* 
08:00  10:00   *NUEVO EXPRESO* 
09:50  11:30   *MERCOBUS* 
12:30  14:50   *RAPIDO TATA* 
15:50  18:00   *FLECHA BUS*
19:00  21:30   *NUEVO EXPRESO*
""", 'mercedes': """SALIDA LLEGADA EMPRESA 
21:30  00:30   *NUEVO EXPRESO* 
23:15  03:50   *NUEVO EXPRESO* 
00:40  04:10   *FLECHA BUS* 
02:30  07:00   *NUEVO EXPRESO* 
08:00  13:30   *NUEVO EXPRESO* 
13:15  17:00   *NUEVO EXPRESO* 
12:30  17:50   *RAPIDO TATA*
""", 'mar del plata': """SALIDA LLEGADA EMPRESA 
01:20  00:45   *TIGRE IGUAZU* _miercoles y sabados_
00:15  11:15   *FLECHA BUS*
""", 'manteros': """SALIDA LLEGADA EMPRESA 
23:25  03:05   *RIO URUGUAY* _salvo sabados_
07:00  10:20   *RIO URUGUAY* __solo lunes_ - miercoles - jueves - viernes_ 
""", 'macia': """SALIDA LLEGADA EMPRESA 
00:35  03:50   *RAPIDO TATA* _salvo sabados_
23:25  04:10   *RIO URUGUAY* _salvo sabados_ - 
07:00  11:35   *RIO URUGUAY* __solo lunes_ - miercoles - jueves - viernes_ 
""", 'lucas gonzalez': """SALIDA LLEGADA EMPRESA 
07:00  11:45   *RIO URUGUAY* 
23:25  04:20   *RIO URUGUAY* _salvo sabados_ - 
00:35  04:30   *RAPIDO TATA* _salvo sabados_ - 
""", 'los charruas': """SALIDA LLEGADA EMPRESA 
23:00  00:00   *EXP. CHARRUAS* _lunes a viernes_
06:00  07:00   *EXP. CHARRUAS* 
12:00  13:00   *EXP. CHARRUAS* 
19:00  20:30   *EXP. CHARRUAS* 
""", 'liniers': """SALIDA LLEGADA EMPRESA 
00:10  07:00   *NUEVO EXPRESO* 
23:40  08:40   *RAPIDO TATA* 
02:35  15:00   *RAPIDO ARGENTINO*
""", 'la plata': """SALIDA LLEGADA EMPRESA 
02:10  09:00   *FLECHA BUS*
""", 'la criolla': """SALIDA LLEGADA EMPRESA 
06:15  07:30   *MICRO o. AYUI* _lunes a sabados_
08:00  09:00   *MICRO o. AYUI* _domingos y feriados_
10:50  11:20   *MICRO o. AYUI* _salvo domingos_
12:15  12:45   *MICRO o. AYUI* 
15:30  16:00   *MICRO o. AYUI* _salvo verano_
19:00  19:30   *MICRO o. AYUI* 
""", 'gualeguaychu': """SALIDA LLEGADA EMPRESA 
18:30  00:25   *NUEVO EXPRESO* 
23:10  03:30   *JOVI BUS* 
23:40  03:55   *RAPIDO TATA* 
01:25  05:00   *NUEVO EXPRESO* 
05:30  09:35   *NUEVO EXPRESO* 
08:00  12:20   *NUEVO EXPRESO* 
08:25  12:35   *JOVI BUS* 
10:25  15:00   *NUEVO EXPRESO* 
12:40  17:15   *RAPIDO TATA* 
13:00  17:30   *JOVI BUS* 
17:15  20:30   *NUEVO EXPRESO* 
16:25  21:00   *NUEVO EXPRESO* 
17:45  21:55   *RAPIDO TATA* 
18:00  22:30   *JOVI BUS* 
19:00  23:40   *JOVI BUS* 
""", 'gualeguay': """SALIDA LLEGADA EMPRESA 
18:00  00:00   *JOVI BUS* 
08:25  14:00   *JOVI BUS* 
""", 'general campos': """SALIDA LLEGADA EMPRESA 
23:00  00:00   *17 DE MAYO* _salvo verano_
23:55  00:10   *FLECHA BUS* 
03:10  03:50   *ZENIT* 
06:35  07:45   *SAN JOSE* 
08:15  09:15   *17 DE MAYO* _domingos y feriados_
09:30  10:20   *ZENIT* 
11:05  11:50   *FLECHA BUS* 
12:30  13:30   *17 DE MAYO* _lunes a sabados_
14:10  14:55   *FLECHA BUS* 
16:50  17:40   **21 TOURS* 
18:30  19:15   *NUEVO EXPRESO* 
18:30  19:30   *17 DE MAYO* _lunes a sabados_
20:00  20:55   *SAN JOSE* _lunes a sabados_
21:00  22:00   *17 DE MAYO* _lunes a viernes_
21:43  22:45   *ZENIT* 
22:20  23:20   *17 DE MAYO* sabados
""", 'feliciano': """SALIDA LLEGADA EMPRESA 
21:00  00:20   *EXP. FELICIANO*
23:15  03:30   *LUCERITO* 
12:30  15:30   *LUCERITO* 
14:20  18:00   *EXP. FELICIANO*
""", 'federal': """SALIDA LLEGADA EMPRESA 
06:50  08:30   *21 TOURS* _lunes a sabados_
10:40  11:40   *21 TOURS* _lunes a domingos_
13:00  14:40   *21 TOURS* 
13:00  14:40   *21 TOURS* _lunes a domingos_
17:30  18:30   *21 TOURS* _lunes a sabados_
20:30  22:10   *21 TOURS* 
20:30  22:10   *21 TOURS* _lunes a domingos_
""", 'federación': """SALIDA LLEGADA EMPRESA 
00:20  01:30   *SAN JOSE* _lunes a viernes_
05:15  06:15   *FLECHA BUS* 
05:50  06:50   *FLECHA BUS* 
06:10  07:15   *ZENIT* 
06:20  07:15   *FLECHA BUS* 
06:45  07:55   *RAPIDO TATA* 
08:00  09:20   *RAPIDO TATA* 
09:05  10:10   *RAPIDO TATA* 
12:30  13:30   *RAPIDO TATA* 
12:35  13:35   *21 TOURS* 
15:30  16:30   *ZENIT* 
18:35  19:20   *RAPIDO TATA* 
19:00  20:00   *NUEVO EXPRESO* 
20:20  21:30   *ZENIT* 
21:55  23:00   *FLECHA BUS* 
""", 'curuzu cuatia': """SALIDA LLEGADA EMPRESA 
21:30  00:45   *NUEVO EXPRESO* 
23:15  20:20   *NUEVO EXPRESO* 
00:40  03:25   *FLECHA BUS* 
02:45  05:45   *RAPIDO TATA* 
02:30  06:20   *NUEVO EXPRESO* 
03:10  06:30   *SINGER* 
08:00  12:30   *NUEVO EXPRESO* 
08:40  13:20   *MERCOBUS* 
13:15  15:50   *NUEVO EXPRESO* 
12:30  16:30   *RAPIDO TATA* 
""", 'corrientes': """SALIDA LLEGADA EMPRESA 
21:30  05:30   *NUEVO EXPRESO* 
23:15  07:00   *NUEVO EXPRESO* 
00:40  07:40   *FLECHA BUS* 
08:00  17:00   *NUEVO EXPRESO* 
13:15  20:00   *NUEVO EXPRESO* 
""", 'cordoba': """SALIDA LLEGADA EMPRESA 
21:43  07:20   *ZENIT* 
22:20  08:00   *MERCOBUS*-PLUS ULTRA _viernes y domingos_
""", 'concepción del uruguay': """SALIDA LLEGADA EMPRESA 
23:10  02:25   *JOVI BUS* 
23:25  02:25   *RIO URUGUAY* 
23:40  02:30   *RAPIDO TATA* 
05:25  08:30   *NUEVO EXPRESO* 
07:00  09:45   *RIO URUGUAY* 
07:00  09:45   *RIO URUGUAY* 
08:30  10:30   *RAPIDO TATA* 
08:00  11:00   *NUEVO EXPRESO* 
08:25  11:15   *JOVI BUS* 
10:25  13:30   *NUEVO EXPRESO* 
12:15  14:15   *FLECHA BUS* 
12:20  14:55   *RAPIDO TATA* 
12:40  15:30   *RAPIDO TATA* 
13:00  16:25   *JOVI BUS* 
16:25  19:40   *NUEVO EXPRESO* 
17:45  20:40   *RAPIDO TATA* 
18:00  21:15   *JOVI BUS* 
19:00  22:15   *JOVI BUS* 
18:30  23:10   *NUEVO EXPRESO* 
""", 'colonia ayui': """SALIDA LLEGADA EMPRESA 
06:15  06:45   *CHAMUSSY* 
07:30  08:15   *no definido* _domingos y feriados_
10:30  11:00   *CHAMUSSY* _lunes a viernes_
11:45  13:00   *S.C. SERVICIOS* _lunes a sabados_
12:15  13:00   *CHAMUSSY* 
15:30  16:15   *CHAMUSSY* 
19:00  19:40   *CHAMUSSY* 
20:00  21:00   *S.C. SERVICIOS* _lunes a sabados_
""", 'colon': """SALIDA LLEGADA EMPRESA 
23:25  01:20   *RIO URUGUAY* _salvo sabados_
23:10  01:25   *JOVI BUS* 
23:25  01:25   *RIO URUGUAY* 
23:40  01:45   *RAPIDO TATA* 
01:25  03:15   *NUEVO EXPRESO* 
05:25  07:25   *NUEVO EXPRESO* 
07:00  09:00   *RIO URUGUAY* 
07:00  09:00   *RIO URUGUAY* 
08:00  10:00   *NUEVO EXPRESO* 
08:25  10:20   *JOVI BUS* 
10:25  12:25   *NUEVO EXPRESO* 
12:20  14:10   *RAPIDO TATA* 
12:20  14:10   *RAPIDO TATA* 
12:40  14:30   *RAPIDO TATA* 
13:15  14:50   *RAPIDO TATA* 
13:00  15:20   *JOVI BUS* 
16:25  18:25   *NUEVO EXPRESO* 
17:45  19:45   *RAPIDO TATA* 
18:00  20:20   *JOVI BUS* 
19:00  21:20   *JOVI BUS* 
""", 'chajari': """SALIDA LLEGADA EMPRESA 
22:45  00:00   *RAPIDO TATA* _solo viernes_
23:00  00:10   *FLECHA BUS* 
23:15  00:35   *NUEVO EXPRESO* 
23:15  00:40   *LUCERITO* 
00:15  01:30   *JOVI BUS* 
00:40  02:00   *FLECHA BUS* 
01:45  02:55   *FLECHA BUS* 
02:45  04:00   *RAPIDO TATA* 
04:05  05:15   *FLECHA BUS* 
05:15  06:45   *FLECHA BUS* 
06:10  08:05   *ZENIT* _pasa por federacion_
08:00  09:10   *NUEVO EXPRESO* 
09:15  10:25   *JOVI BUS* 
09:05  11:00   *RAPIDO TATA* _pasa por federacion_
10:20  11:30   *FLECHA BUS* _lunes a sabados_
12:30  13:40   *LUCERITO* 
13:15  14:10   *JOVI BUS* 
12:30  14:25   *RAPIDO TATA* _pasa por federacion_
13:40  15:10   *NUEVO EXPRESO* 
14:20  15:30   *EXP. FELICIANO*
14:50  16:00   *FLECHA BUS* 
15:30  16:40   *JOVI BUS* 
15:50  17:00   *FLECHA BUS* 
17:30  18:50   *SAN JOSE* 
19:00  21:00   *NUEVO EXPRESO* _pasa por federacion_
20:05  21:30   *NUEVO EXPRESO* 
20:15  21:30   *JOVI BUS* 
21:30  22:50   *NUEVO EXPRESO* 
""", 'calabacilla': """SALIDA LLEGADA EMPRESA 
05:45  06:25   *LUCERITO* _lunes a sabados_
07:00  07:40   *LUCERITO* 
10:45  11:25   *LUCERITO* _lunes a viernes_
11:00  11:40   *LUCERITO* 
12:00  12:40   *LUCERITO* _lunes a sabados_
18:30  19:10   *LUCERITO* _lunes a sabados_
18:30  19:10   *LUCERITO* 
21:30  22:10   *LUCERITO* _lunes a sabados_
""", 'basavilbaso': """SALIDA LLEGADA EMPRESA 
23:25  03:25   *RIO URUGUAY* _salvo sabados_
07:00  10:50   *RIO URUGUAY* 
12:20  15:55   *RAPIDO TATA* 
""", '#retiro-concordia': """SALIDA LLEGADA EMPRESA
00:15 06:45    *RÁPIDO SAN JOSÉ* _Semi Cama_
00:50 06:20    *FLECHA BUS* _Semi Cama_
01:15 09:05    *RÁPIDO SAN JOSÉ* _Semi Cama_
05:00 12:30    *RÁPIDO SAN JOSÉ* _Comun con aire_
06:30 13:15    *NUEVO EXPRESO-FLECHA BUS* _Semi Cama_
08:30 14:50    *FLECHA BUS* _Cama_
08:30 14:50    *FLECHA BUS* _Semi Cama_
10:00 15:50    *FLECHA BUS* _Semi Cama_
10:00 15:50    *FLECHA BUS* _Cama_
12:15 18:35    *RÁPIDO SAN JOSÉ* _Semi Cama_
12:15 18:35    *RÁPIDO SAN JOSÉ* _Cama_
14:15 19:45    *VÍA BARILOCHE* _Cama_
14:30 20:25    *FLECHA BUS* _Semi Cama_
15:00 21:00    *EL RÁPIDO ARGENTINO* _Coche Cama_
15:30 21:30    *CRUCERO DEL NORTE* _Cama Ejecutivo_
15:30 21:30    *NUEVO EXPRESO - FLECHA BUS* _Cama_
16:00 21:55    *FLECHA BUS* _Cama Ejecutivo_
16:00 21:55    *FLECHA BUS* _Semi _Cama_
18:30 00:40    *FLECHA BUS* _Semi Cama_
18:35 00:30    *RÁPIDO SAN JOSÉ* _Semi Cama_
18:35 00:30    *RÁPIDO SAN JOSÉ* _Cama Ejecutivo_
20:00 01:45    *FLECHA BUS* _Semi Cama_
20:00 01:45    *FLECHA BUS* _Cama_
21:15 03:00    *EXPRESO SINGER* _Semi Plus_
21:15 03:00    *EXPRESO SINGER* _Semi Cama_
21:30 03:00    *TIGRE IGUAZU* _Semi Cama_
21:30 03:00    *TIGRE IGUAZU* _Cama_
23:30 05:15    *FLECHA BUS* _Semi Cama_
23:30 05:15    *FLECHA BUS* _Cama Ejecutivo_
""", '#parana-concordia': """SALIDA LLEGADA EMPRESA
05:45	10:20	   *FLECHA BUS*
08:15	12:35	   *FLECHA BUS*
11:15	15:30	   *ZENIT*
13:30	17:30	   *RAPIDO TATA*
15:30	20:20	   *ZENIT*
15:35	19:40	   *RAPIDO* _Solo Viernes_
18:45	23:00	   *FLECHA BUZ*
18:55	23:00    *RAPIDO* _Solo Viernes_
20:10	00:20	   *RAPIDO TATA* _Excepto Sabado y Domingo_
23:55	04:05	   *FLECHA BUS* _Solo Lunes_
""", '#santa fe-concordia': """SALIDA LLEGADA EMPRESA
01:20	06:10	   *ZENIT* _Excepto Domingo_
12:40	17:30	   *RAPIDO TATA*
21:15	01:30	   *EXPRESO SINGER* _Excepto Sabado_
23:10	04:05	   *FLECHA BUS* _Excepto Sabado_
""",}