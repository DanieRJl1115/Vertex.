
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A_CORCHETE A_LLAVE A_PARENTESIS COMA COMENTARIO CONS C_CORCHETE C_LLAVE C_PARENTESIS DOS_P ENTONCES EXCEPTO FUNCION IDENTIFICADORES INTENTAR LITERALES METODO MIENTRAS OP_ARITMETICO OP_ASIGNACION OP_LOGICO OP_MULTIPLICATIVO OP_RELACIONAL OP_UNITARIO PARA PUNTO P_COMA REGRESAR SI VARprograma : sentencia_sentsentencia_sent : sent_linea P_COMA sentencia_sent\n                      | sentencia sentencia_sent\n                      | sent_linea : declarar_var\n                  | declarar_cons\n                  | asignacion\n                  | inst_fun\n                  | metodosentencia : sent_if\n                 | sent_for\n                 | sent_while\n                 | sent_fun\n                 | sent_trydeclarar_var : VAR IDENTIFICADORES\n                    | VAR IDENTIFICADORES OP_ASIGNACION valorvalor : expresion\n            | estructura_datos \n            | metodo\n            | IDENTIFICADORESexpresion : termino exp_etermino : factor term_extfactor : selec_dato\n             | A_PARENTESIS expresion C_PARENTESISselec_dato : IDENTIFICADORES\n                 | LITERALESterm_ext : OP_MULTIPLICATIVO factor term_ext\n               | exp_e : OP_ARITMETICO termino exp_e\n            | estructura_datos : lista\n                       | tupla\n                       | diccionariolista : A_CORCHETE dato dato_extra C_CORCHETE\n            | A_CORCHETE C_CORCHETEtupla : A_PARENTESIS dato dato_extra C_PARENTESISdato_extra : COMA dato dato_extra\n                 | diccionario : A_LLAVE LITERALES DOS_P dato element_ext C_LLAVE\n                  | A_LLAVE C_LLAVEelement_ext : COMA LITERALES DOS_P dato element_ext\n                 | dato : IDENTIFICADORES\n           | LITERALES\n           | expresionasignacion : IDENTIFICADORES OP_ASIGNACION valordeclarar_cons : CONS IDENTIFICADORES OP_ASIGNACION LITERALESinst_fun : IDENTIFICADORES A_PARENTESIS atributo C_PARENTESISatributo : IDENTIFICADORES atributo_dos\n                | LITERALES atributo_dos\n                | atributo_dos : COMA IDENTIFICADORES  atributo_dos\n                    | COMA LITERALES atributo_dos\n                    | metodo : PUNTO METODO A_PARENTESIS atributo C_PARENTESIS\n              | METODO A_PARENTESIS atributo C_PARENTESISsent_if : SI A_PARENTESIS exp_comparacion C_PARENTESIS A_LLAVE sentencia_sent C_LLAVE sent_elseexp_comparacion : dato OP_RELACIONAL dato exp_ext\n                       | LITERALESexp_ext : OP_LOGICO exp_comparacion \n               | sent_else : ENTONCES A_LLAVE sentencia_sent C_LLAVE \n                 | sent_for : PARA A_PARENTESIS declarar_var P_COMA expresion_comp P_COMA incremento C_PARENTESIS A_LLAVE sentencia_sent C_LLAVEexpresion_comp : IDENTIFICADORES OP_RELACIONAL datoincremento : op_incremento_simple\n                  | asignacion_exprop_incremento_simple : IDENTIFICADORES OP_UNITARIOasignacion_expr : IDENTIFICADORES OP_ASIGNACION expresionsent_while : MIENTRAS A_PARENTESIS exp_comparacion C_PARENTESIS A_LLAVE sentencia_sent C_LLAVEsent_fun : FUNCION A_PARENTESIS atributo C_PARENTESIS A_LLAVE sentencia_sent REGRESAR valor C_LLAVE\n                | FUNCION A_PARENTESIS atributo C_PARENTESIS A_LLAVE sentencia_sent C_LLAVEsent_try : INTENTAR A_LLAVE sentencia_sent C_LLAVE EXCEPTO A_LLAVE sentencia_sent C_LLAVE'
    
_lr_action_items = {'$end':([0,1,2,4,10,11,12,13,14,25,26,38,134,141,143,147,153,158,163,164,],[-4,0,-1,-4,-10,-11,-12,-13,-14,-4,-3,-2,-63,-70,-72,-57,-73,-71,-62,-64,]),'VAR':([0,4,10,11,12,13,14,25,34,37,108,112,113,130,134,141,143,147,153,155,156,158,163,164,],[15,15,-10,-11,-12,-13,-14,15,15,15,15,15,15,15,-63,-70,-72,-57,-73,15,15,-71,-62,-64,]),'CONS':([0,4,10,11,12,13,14,25,37,108,112,113,130,134,141,143,147,153,155,156,158,163,164,],[17,17,-10,-11,-12,-13,-14,17,17,17,17,17,17,-63,-70,-72,-57,-73,17,17,-71,-62,-64,]),'IDENTIFICADORES':([0,4,10,11,12,13,14,15,17,25,28,29,32,33,35,36,37,39,49,51,59,61,73,78,84,93,94,100,104,108,112,113,125,126,127,130,134,141,142,143,147,151,153,154,155,156,158,163,164,],[16,16,-10,-11,-12,-13,-14,27,30,16,40,55,55,65,65,55,16,40,65,65,55,91,91,91,105,65,111,65,65,16,16,16,65,139,65,16,-63,-70,40,-72,-57,91,-73,65,16,16,-71,-62,-64,]),'PUNTO':([0,4,10,11,12,13,14,25,28,37,39,108,112,113,130,134,141,142,143,147,153,155,156,158,163,164,],[18,18,-10,-11,-12,-13,-14,18,18,18,18,18,18,18,18,-63,-70,18,-72,-57,-73,18,18,-71,-62,-64,]),'METODO':([0,4,10,11,12,13,14,18,25,28,37,39,108,112,113,130,134,141,142,143,147,153,155,156,158,163,164,],[19,19,-10,-11,-12,-13,-14,31,19,19,19,19,19,19,19,19,-63,-70,19,-72,-57,-73,19,19,-71,-62,-64,]),'SI':([0,4,10,11,12,13,14,25,37,108,112,113,130,134,141,143,147,153,155,156,158,163,164,],[20,20,-10,-11,-12,-13,-14,20,20,20,20,20,20,-63,-70,-72,-57,-73,20,20,-71,-62,-64,]),'PARA':([0,4,10,11,12,13,14,25,37,108,112,113,130,134,141,143,147,153,155,156,158,163,164,],[21,21,-10,-11,-12,-13,-14,21,21,21,21,21,21,-63,-70,-72,-57,-73,21,21,-71,-62,-64,]),'MIENTRAS':([0,4,10,11,12,13,14,25,37,108,112,113,130,134,141,143,147,153,155,156,158,163,164,],[22,22,-10,-11,-12,-13,-14,22,22,22,22,22,22,-63,-70,-72,-57,-73,22,22,-71,-62,-64,]),'FUNCION':([0,4,10,11,12,13,14,25,37,108,112,113,130,134,141,143,147,153,155,156,158,163,164,],[23,23,-10,-11,-12,-13,-14,23,23,23,23,23,23,-63,-70,-72,-57,-73,23,23,-71,-62,-64,]),'INTENTAR':([0,4,10,11,12,13,14,25,37,108,112,113,130,134,141,143,147,153,155,156,158,163,164,],[24,24,-10,-11,-12,-13,-14,24,24,24,24,24,24,-63,-70,-72,-57,-73,24,24,-71,-62,-64,]),'P_COMA':([3,5,6,7,8,9,27,40,41,42,43,44,45,46,47,48,50,53,54,65,66,67,71,72,76,77,80,82,85,87,89,91,98,101,102,107,110,115,116,118,119,140,145,],[25,-5,-6,-7,-8,-9,-15,-20,-46,-17,-18,-19,-30,-31,-32,-33,-28,-26,-23,-25,-45,94,-16,-21,-26,-22,-35,-40,-48,-47,-56,-25,-30,-24,-28,-55,126,-29,-36,-27,-34,-65,-39,]),'C_LLAVE':([4,10,11,12,13,14,25,26,37,38,40,42,43,44,45,46,47,48,50,52,53,54,65,66,70,72,76,77,80,82,89,91,98,101,102,107,108,112,113,115,116,118,119,120,123,128,129,130,132,134,141,143,144,145,147,152,153,155,156,158,159,160,161,162,163,164,],[-4,-10,-11,-12,-13,-14,-4,-3,-4,-2,-20,-17,-18,-19,-30,-31,-32,-33,-28,82,-26,-23,-25,-45,97,-21,-26,-22,-35,-40,-56,-25,-30,-24,-28,-55,-4,-4,-4,-29,-36,-27,-34,-42,134,141,143,-4,145,-63,-70,-72,153,-39,-57,158,-73,-4,-4,-71,-42,163,164,-41,-62,-64,]),'REGRESAR':([4,10,11,12,13,14,25,26,38,113,129,134,141,143,147,153,158,163,164,],[-4,-10,-11,-12,-13,-14,-4,-3,-2,-4,142,-63,-70,-72,-57,-73,-71,-62,-64,]),'OP_ASIGNACION':([16,27,30,139,],[28,39,58,151,]),'A_PARENTESIS':([16,19,20,21,22,23,28,31,33,35,39,49,51,61,73,78,93,100,104,125,127,142,151,154,],[29,32,33,34,35,36,49,59,61,61,49,61,61,61,61,61,61,61,61,61,61,49,61,61,]),'A_LLAVE':([24,28,39,92,95,96,114,142,148,149,],[37,52,52,108,112,113,130,52,155,156,]),'A_CORCHETE':([28,39,142,],[51,51,51,]),'LITERALES':([28,29,32,33,35,36,39,49,51,52,58,59,61,73,78,84,93,100,104,125,127,133,142,151,154,],[53,57,57,64,64,57,53,76,76,81,87,57,53,53,53,106,76,76,76,64,76,146,53,53,76,]),'C_PARENTESIS':([29,32,36,45,50,53,54,55,56,57,59,60,62,64,65,66,68,69,72,74,75,76,77,83,86,88,90,91,98,99,101,102,105,106,109,115,117,118,121,122,124,131,135,136,137,138,150,157,],[-51,-51,-51,-30,-28,-26,-23,-54,85,-54,-51,89,92,-59,-25,-45,95,96,-21,-38,101,-26,-22,-49,-50,107,101,-25,-30,116,-24,-28,-54,-54,-61,-29,-38,-27,-52,-53,-58,-37,-60,149,-66,-67,-68,-69,]),'OP_MULTIPLICATIVO':([40,50,53,54,64,65,76,91,101,102,],[-25,78,-26,-23,-26,-25,-26,-25,-24,78,]),'OP_ARITMETICO':([40,45,50,53,54,64,65,76,77,91,98,101,102,118,],[-25,73,-28,-26,-23,-26,-25,-26,-22,-25,73,-24,-28,-27,]),'OP_RELACIONAL':([45,50,53,54,63,64,65,66,72,77,91,98,101,102,111,115,118,],[-30,-28,-26,-23,93,-26,-25,-45,-21,-22,-25,-30,-24,-28,127,-29,-27,]),'COMA':([45,50,53,54,55,57,65,66,72,74,75,76,77,79,91,98,101,102,105,106,115,117,118,120,159,],[-30,-28,-26,-23,84,84,-25,-45,-21,100,-45,-26,-22,100,-25,-30,-24,-28,84,84,-29,100,-27,133,133,]),'C_CORCHETE':([45,50,51,53,54,65,66,72,76,77,79,91,98,101,102,103,115,117,118,131,],[-30,-28,80,-26,-23,-25,-45,-21,-26,-22,-38,-25,-30,-24,-28,119,-29,-38,-27,-37,]),'OP_LOGICO':([45,50,53,54,65,66,72,76,77,91,98,101,102,109,115,118,],[-30,-28,-26,-23,-25,-45,-21,-26,-22,-25,-30,-24,-28,125,-29,-27,]),'DOS_P':([81,146,],[104,154,]),'EXCEPTO':([97,],[114,]),'ENTONCES':([134,],[148,]),'OP_UNITARIO':([139,],[150,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'sentencia_sent':([0,4,25,37,108,112,113,130,155,156,],[2,26,38,70,123,128,129,144,160,161,]),'sent_linea':([0,4,25,37,108,112,113,130,155,156,],[3,3,3,3,3,3,3,3,3,3,]),'sentencia':([0,4,25,37,108,112,113,130,155,156,],[4,4,4,4,4,4,4,4,4,4,]),'declarar_var':([0,4,25,34,37,108,112,113,130,155,156,],[5,5,5,67,5,5,5,5,5,5,5,]),'declarar_cons':([0,4,25,37,108,112,113,130,155,156,],[6,6,6,6,6,6,6,6,6,6,]),'asignacion':([0,4,25,37,108,112,113,130,155,156,],[7,7,7,7,7,7,7,7,7,7,]),'inst_fun':([0,4,25,37,108,112,113,130,155,156,],[8,8,8,8,8,8,8,8,8,8,]),'metodo':([0,4,25,28,37,39,108,112,113,130,142,155,156,],[9,9,9,44,9,44,9,9,9,9,44,9,9,]),'sent_if':([0,4,25,37,108,112,113,130,155,156,],[10,10,10,10,10,10,10,10,10,10,]),'sent_for':([0,4,25,37,108,112,113,130,155,156,],[11,11,11,11,11,11,11,11,11,11,]),'sent_while':([0,4,25,37,108,112,113,130,155,156,],[12,12,12,12,12,12,12,12,12,12,]),'sent_fun':([0,4,25,37,108,112,113,130,155,156,],[13,13,13,13,13,13,13,13,13,13,]),'sent_try':([0,4,25,37,108,112,113,130,155,156,],[14,14,14,14,14,14,14,14,14,14,]),'valor':([28,39,142,],[41,71,152,]),'expresion':([28,33,35,39,49,51,61,93,100,104,125,127,142,151,154,],[42,66,66,42,75,66,90,66,66,66,66,66,42,157,66,]),'estructura_datos':([28,39,142,],[43,43,43,]),'termino':([28,33,35,39,49,51,61,73,93,100,104,125,127,142,151,154,],[45,45,45,45,45,45,45,98,45,45,45,45,45,45,45,45,]),'lista':([28,39,142,],[46,46,46,]),'tupla':([28,39,142,],[47,47,47,]),'diccionario':([28,39,142,],[48,48,48,]),'factor':([28,33,35,39,49,51,61,73,78,93,100,104,125,127,142,151,154,],[50,50,50,50,50,50,50,50,102,50,50,50,50,50,50,50,50,]),'selec_dato':([28,33,35,39,49,51,61,73,78,93,100,104,125,127,142,151,154,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'atributo':([29,32,36,59,],[56,60,69,88,]),'exp_comparacion':([33,35,125,],[62,68,135,]),'dato':([33,35,49,51,93,100,104,125,127,154,],[63,63,74,79,109,117,120,63,140,159,]),'exp_e':([45,98,],[72,115,]),'term_ext':([50,102,],[77,118,]),'atributo_dos':([55,57,105,106,],[83,86,121,122,]),'dato_extra':([74,79,117,],[99,103,131,]),'expresion_comp':([94,],[110,]),'exp_ext':([109,],[124,]),'element_ext':([120,159,],[132,162,]),'incremento':([126,],[136,]),'op_incremento_simple':([126,],[137,]),'asignacion_expr':([126,],[138,]),'sent_else':([134,],[147,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> sentencia_sent','programa',1,'p_programa','analizador_sintactico.py',5),
  ('sentencia_sent -> sent_linea P_COMA sentencia_sent','sentencia_sent',3,'p_sentencia_sent','analizador_sintactico.py',9),
  ('sentencia_sent -> sentencia sentencia_sent','sentencia_sent',2,'p_sentencia_sent','analizador_sintactico.py',10),
  ('sentencia_sent -> <empty>','sentencia_sent',0,'p_sentencia_sent','analizador_sintactico.py',11),
  ('sent_linea -> declarar_var','sent_linea',1,'p_sent_linea','analizador_sintactico.py',20),
  ('sent_linea -> declarar_cons','sent_linea',1,'p_sent_linea','analizador_sintactico.py',21),
  ('sent_linea -> asignacion','sent_linea',1,'p_sent_linea','analizador_sintactico.py',22),
  ('sent_linea -> inst_fun','sent_linea',1,'p_sent_linea','analizador_sintactico.py',23),
  ('sent_linea -> metodo','sent_linea',1,'p_sent_linea','analizador_sintactico.py',24),
  ('sentencia -> sent_if','sentencia',1,'p_sentencia','analizador_sintactico.py',28),
  ('sentencia -> sent_for','sentencia',1,'p_sentencia','analizador_sintactico.py',29),
  ('sentencia -> sent_while','sentencia',1,'p_sentencia','analizador_sintactico.py',30),
  ('sentencia -> sent_fun','sentencia',1,'p_sentencia','analizador_sintactico.py',31),
  ('sentencia -> sent_try','sentencia',1,'p_sentencia','analizador_sintactico.py',32),
  ('declarar_var -> VAR IDENTIFICADORES','declarar_var',2,'p_declarar_var','analizador_sintactico.py',36),
  ('declarar_var -> VAR IDENTIFICADORES OP_ASIGNACION valor','declarar_var',4,'p_declarar_var','analizador_sintactico.py',37),
  ('valor -> expresion','valor',1,'p_valor','analizador_sintactico.py',44),
  ('valor -> estructura_datos','valor',1,'p_valor','analizador_sintactico.py',45),
  ('valor -> metodo','valor',1,'p_valor','analizador_sintactico.py',46),
  ('valor -> IDENTIFICADORES','valor',1,'p_valor','analizador_sintactico.py',47),
  ('expresion -> termino exp_e','expresion',2,'p_expresion','analizador_sintactico.py',50),
  ('termino -> factor term_ext','termino',2,'p_termino','analizador_sintactico.py',54),
  ('factor -> selec_dato','factor',1,'p_factor','analizador_sintactico.py',58),
  ('factor -> A_PARENTESIS expresion C_PARENTESIS','factor',3,'p_factor','analizador_sintactico.py',59),
  ('selec_dato -> IDENTIFICADORES','selec_dato',1,'p_selec_dato','analizador_sintactico.py',65),
  ('selec_dato -> LITERALES','selec_dato',1,'p_selec_dato','analizador_sintactico.py',66),
  ('term_ext -> OP_MULTIPLICATIVO factor term_ext','term_ext',3,'p_term_ext','analizador_sintactico.py',70),
  ('term_ext -> <empty>','term_ext',0,'p_term_ext','analizador_sintactico.py',71),
  ('exp_e -> OP_ARITMETICO termino exp_e','exp_e',3,'p_exp_e','analizador_sintactico.py',77),
  ('exp_e -> <empty>','exp_e',0,'p_exp_e','analizador_sintactico.py',78),
  ('estructura_datos -> lista','estructura_datos',1,'p_estructura_datos','analizador_sintactico.py',85),
  ('estructura_datos -> tupla','estructura_datos',1,'p_estructura_datos','analizador_sintactico.py',86),
  ('estructura_datos -> diccionario','estructura_datos',1,'p_estructura_datos','analizador_sintactico.py',87),
  ('lista -> A_CORCHETE dato dato_extra C_CORCHETE','lista',4,'p_lista','analizador_sintactico.py',91),
  ('lista -> A_CORCHETE C_CORCHETE','lista',2,'p_lista','analizador_sintactico.py',92),
  ('tupla -> A_PARENTESIS dato dato_extra C_PARENTESIS','tupla',4,'p_tupla','analizador_sintactico.py',99),
  ('dato_extra -> COMA dato dato_extra','dato_extra',3,'p_dato_extra','analizador_sintactico.py',103),
  ('dato_extra -> <empty>','dato_extra',0,'p_dato_extra','analizador_sintactico.py',104),
  ('diccionario -> A_LLAVE LITERALES DOS_P dato element_ext C_LLAVE','diccionario',6,'p_diccionario','analizador_sintactico.py',111),
  ('diccionario -> A_LLAVE C_LLAVE','diccionario',2,'p_diccionario','analizador_sintactico.py',112),
  ('element_ext -> COMA LITERALES DOS_P dato element_ext','element_ext',5,'p_element_ext','analizador_sintactico.py',119),
  ('element_ext -> <empty>','element_ext',0,'p_element_ext','analizador_sintactico.py',120),
  ('dato -> IDENTIFICADORES','dato',1,'p_dato','analizador_sintactico.py',127),
  ('dato -> LITERALES','dato',1,'p_dato','analizador_sintactico.py',128),
  ('dato -> expresion','dato',1,'p_dato','analizador_sintactico.py',129),
  ('asignacion -> IDENTIFICADORES OP_ASIGNACION valor','asignacion',3,'p_asignacion','analizador_sintactico.py',133),
  ('declarar_cons -> CONS IDENTIFICADORES OP_ASIGNACION LITERALES','declarar_cons',4,'p_declarar_cons','analizador_sintactico.py',137),
  ('inst_fun -> IDENTIFICADORES A_PARENTESIS atributo C_PARENTESIS','inst_fun',4,'p_inst_fun','analizador_sintactico.py',141),
  ('atributo -> IDENTIFICADORES atributo_dos','atributo',2,'p_atributo','analizador_sintactico.py',145),
  ('atributo -> LITERALES atributo_dos','atributo',2,'p_atributo','analizador_sintactico.py',146),
  ('atributo -> <empty>','atributo',0,'p_atributo','analizador_sintactico.py',147),
  ('atributo_dos -> COMA IDENTIFICADORES atributo_dos','atributo_dos',3,'p_atributo_dos','analizador_sintactico.py',154),
  ('atributo_dos -> COMA LITERALES atributo_dos','atributo_dos',3,'p_atributo_dos','analizador_sintactico.py',155),
  ('atributo_dos -> <empty>','atributo_dos',0,'p_atributo_dos','analizador_sintactico.py',156),
  ('metodo -> PUNTO METODO A_PARENTESIS atributo C_PARENTESIS','metodo',5,'p_metodo','analizador_sintactico.py',163),
  ('metodo -> METODO A_PARENTESIS atributo C_PARENTESIS','metodo',4,'p_metodo','analizador_sintactico.py',164),
  ('sent_if -> SI A_PARENTESIS exp_comparacion C_PARENTESIS A_LLAVE sentencia_sent C_LLAVE sent_else','sent_if',8,'p_sent_if','analizador_sintactico.py',171),
  ('exp_comparacion -> dato OP_RELACIONAL dato exp_ext','exp_comparacion',4,'p_exp_comparacion','analizador_sintactico.py',175),
  ('exp_comparacion -> LITERALES','exp_comparacion',1,'p_exp_comparacion','analizador_sintactico.py',176),
  ('exp_ext -> OP_LOGICO exp_comparacion','exp_ext',2,'p_exp_ext','analizador_sintactico.py',183),
  ('exp_ext -> <empty>','exp_ext',0,'p_exp_ext','analizador_sintactico.py',184),
  ('sent_else -> ENTONCES A_LLAVE sentencia_sent C_LLAVE','sent_else',4,'p_sent_else','analizador_sintactico.py',191),
  ('sent_else -> <empty>','sent_else',0,'p_sent_else','analizador_sintactico.py',192),
  ('sent_for -> PARA A_PARENTESIS declarar_var P_COMA expresion_comp P_COMA incremento C_PARENTESIS A_LLAVE sentencia_sent C_LLAVE','sent_for',11,'p_sent_for','analizador_sintactico.py',199),
  ('expresion_comp -> IDENTIFICADORES OP_RELACIONAL dato','expresion_comp',3,'p_expresion_comp','analizador_sintactico.py',203),
  ('incremento -> op_incremento_simple','incremento',1,'p_incremento','analizador_sintactico.py',207),
  ('incremento -> asignacion_expr','incremento',1,'p_incremento','analizador_sintactico.py',208),
  ('op_incremento_simple -> IDENTIFICADORES OP_UNITARIO','op_incremento_simple',2,'p_op_incremento_simple','analizador_sintactico.py',212),
  ('asignacion_expr -> IDENTIFICADORES OP_ASIGNACION expresion','asignacion_expr',3,'p_asignacion_expr','analizador_sintactico.py',216),
  ('sent_while -> MIENTRAS A_PARENTESIS exp_comparacion C_PARENTESIS A_LLAVE sentencia_sent C_LLAVE','sent_while',7,'p_sent_while','analizador_sintactico.py',220),
  ('sent_fun -> FUNCION A_PARENTESIS atributo C_PARENTESIS A_LLAVE sentencia_sent REGRESAR valor C_LLAVE','sent_fun',9,'p_sent_fun','analizador_sintactico.py',224),
  ('sent_fun -> FUNCION A_PARENTESIS atributo C_PARENTESIS A_LLAVE sentencia_sent C_LLAVE','sent_fun',7,'p_sent_fun','analizador_sintactico.py',225),
  ('sent_try -> INTENTAR A_LLAVE sentencia_sent C_LLAVE EXCEPTO A_LLAVE sentencia_sent C_LLAVE','sent_try',8,'p_sent_try','analizador_sintactico.py',232),
]
