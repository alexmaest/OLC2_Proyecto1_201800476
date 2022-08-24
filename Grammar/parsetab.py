
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightADleftDIFIGUALIMENORIMAYORIMENORMAYORleftMASMENOSleftMULTIPLICACIONDIVISIONnonassocRPARLPARrightUMENOSAD AND ANDSINGLE ARROW ARROW2 BOOL BOOLEANO BREAK CADENA CAPACITY CHAR CLONE COMA CONTAINS CONTINUE DECIMAL DIF DIVISION DPUNTOS ELSE ENTERO F64 FN FOR I64 ID IF IGUAL IGUALI IN INSERT LCOR LEN LET LLLAV LOOP LPAR MAS MATCH MAYOR MAYORI MENOR MENORI MENOS MOD MULTIPLICACION MUT NEW OR ORSINGLE PCOMA PRINT PUB PUNTO PUSH RCOR REMOVE RETURN RLLAV RPAR STRING TOOWNED TOSTRING USIZE VEC WHILE WITHCAPACITY aMUT aSTRinit : instrucciones_ginstrucciones_g : instrucciones_g instruccion_g\n    | instruccion_ginstruccion_g : funcioninstrucciones_l : instrucciones_l instruccion_l\n    | instruccion_linstruccion_l : print PCOMA\n    | declaracion PCOMA\n    | asignacion PCOMA\n    | llamada PCOMA\n    | sentencia\n    | transferencia PCOMAfuncion : FN ID LPAR lista_parametros RPAR ARROW tipo_var statement\n    | FN ID LPAR lista_parametros RPAR statement\n    | FN ID LPAR RPAR ARROW tipo_var statement\n    | FN ID LPAR RPAR statementsentencia : if\n    | match\n    | loop\n    | while\n    | forif : IF exp statement elseelse : ELSE statement\n    | ELSE ifmatch : MATCH exp match_statementmatch_statement : LLLAV lista_brazos RLLAV\n    | LLLAV RLLAVlista_brazos : lista_brazos brazo\n    | brazobrazo : lista_exp_brazos ARROW2 instruccion_match COMA\n    | lista_exp_brazos ARROW2 statement COMA\n    | lista_exp_brazos ARROW2 statementlista_exp_brazos : lista_exp_brazos ORSINGLE exp\n    | expinstruccion_match : print\n    | llamada\n    | sentencia\n    | transferencialoop : LOOP statementwhile : WHILE exp statementfor : FOR ID IN exp statementtransferencia : BREAK\n    | RETURN\n    | RETURN exp\n    | CONTINUEstatement : LLLAV instrucciones_l RLLAV\n    | LLLAV RLLAVlista_parametros : lista_parametros COMA asignacion_simple\n    | asignacion_simpledeclaracion : LET asignacion_simple IGUAL exp\n    | LET MUT asignacion\n    | LET asignacionasignacion : ID IGUAL exp\n    | ID lista_arr IGUAL explista_arr : lista_arr LCOR exp RCOR\n    | LCOR exp RCORlista_exp : lista_exp COMA exp\n    | expasignacion_simple : ID DPUNTOS tipo_var\n    | MUT ID DPUNTOS tipo_var\n    | ID DPUNTOS ANDSINGLE tipo_var\n    | MUT ID DPUNTOS ANDSINGLE tipo_var\n    | ID DPUNTOS ANDSINGLE MUT tipo_var\n    | MUT ID DPUNTOS ANDSINGLE MUT tipo_varlista_arr2 : LCOR tipo_var PCOMA exp RCORexp : LPAR valores LPAR\n    | expmath\n    | expop\n    | exprel\n    | exparr\n    | expvec\n    | llamada\n    | ID\n    | valores\n    | exparam\n    | ID PUNTO exp_native\n    | valores PUNTO exp_nativeexpmath : exp MAS exp\n    | exp MENOS exp\n    | exp MULTIPLICACION exp\n    | exp DIVISION exp\n    | MENOS exp %prec UMENOSexpop : exp AND exp\n    | exp OR exp\n    | AD expexprel : exp IGUALI exp\n    | exp DIF exp\n    | exp MAYOR exp\n    | exp MENOR exp\n    | exp MAYORI exp\n    | exp MENORI expexparam : MUT ID\n    | ANDSINGLE MUT IDexparr : ID lista_arr\n    | newarrayexpvec : VEC AD newarraynewarray : LCOR lista_exp RCOR\n    | LCOR exp PCOMA exp RCORvalores : ENTERO\n    | DECIMAL\n    | CADENA\n    | BOOLEANOtipo_var : I64\n    | F64\n    | STRING\n    | ANDSINGLE aSTR\n    | BOOL\n    | CHAR\n    | USIZE\n    | ID\n    | lista_arr2\n    | LCOR tipo_var RCOR\n    | VEC MENOR lista_class MAYORlista_class : lista_class DPUNTOS tipo_var\n    | lista_class DPUNTOS llamada\n    | llamada\n    | tipo_varllamada : ID LPAR RPAR\n    | ID LPAR lista_exp RPARexp_native : TOSTRING LPAR RPAR\n    | TOOWNED LPAR RPAR\n    | CLONE LPAR RPAR\n    | LEN LPAR RPAR\n    | CAPACITY LPAR RPAR\n    | REMOVE LPAR exp RPAR\n    | CONTAINS LPAR exp RPAR\n    | PUSH LPAR exp RPAR\n    | INSERT LPAR lista_exp RPARprint : PRINT AD LPAR exp RPAR'
    
_lr_action_items = {'FN':([0,2,3,4,6,18,34,39,70,71,123,],[5,5,-3,-4,-2,-16,-14,-47,-15,-46,-13,]),'$end':([1,2,3,4,6,18,34,39,70,71,123,],[0,-1,-3,-4,-2,-16,-14,-47,-15,-46,-13,]),'ID':([5,8,13,14,16,17,19,23,31,33,38,39,40,45,48,50,51,52,53,54,56,58,59,61,62,63,65,68,71,72,73,74,75,76,77,80,83,85,86,98,99,106,108,111,115,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,155,159,160,161,162,163,167,173,202,203,205,206,207,224,225,226,227,229,230,231,232,233,234,235,247,258,259,],[7,9,20,21,9,21,49,21,21,21,49,-47,-6,-11,82,-17,-18,-19,-20,-21,96,96,96,96,113,21,21,122,-46,-5,-7,-8,-9,-10,-12,127,96,96,96,96,96,154,96,-39,21,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,200,-25,96,-40,96,21,215,96,96,-22,96,-27,-29,96,96,96,96,-23,-24,-26,-28,252,96,-41,-32,-30,-31,]),'LPAR':([7,39,49,56,58,59,61,71,78,83,85,86,96,98,99,102,103,104,105,108,118,122,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,147,160,162,173,189,190,191,192,193,194,195,196,197,202,205,207,215,224,225,226,227,232,234,247,252,258,259,],[8,-47,85,88,88,88,88,-46,124,88,88,88,85,88,88,-99,-100,-101,-102,88,88,85,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,187,88,88,88,219,220,221,222,223,224,225,226,227,88,88,-29,85,88,88,88,88,-28,88,-32,85,-30,-31,]),'RPAR':([8,10,12,21,22,24,25,26,27,28,29,30,35,64,66,85,89,90,91,92,93,94,95,96,97,100,102,103,104,105,114,116,117,131,132,133,150,151,152,154,164,166,168,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,211,212,217,218,219,220,221,222,223,236,237,238,239,240,241,242,243,244,245,254,255,256,257,],[11,15,-49,-110,-59,-103,-104,-105,-107,-108,-109,-111,-48,-61,-106,131,-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,-60,-63,-112,-118,172,-58,-94,-82,-85,-92,-62,-113,216,-119,-56,-78,-79,-80,-81,-83,-84,-86,-87,-88,-89,-90,-91,-66,-77,-76,-96,-93,-97,-64,-65,-55,-57,236,237,238,239,240,-120,-121,-122,-123,-124,254,255,256,257,-98,-125,-126,-127,-128,]),'MUT':([8,16,23,39,48,56,58,59,61,71,83,85,86,98,99,107,108,115,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,173,202,205,207,224,225,226,227,232,234,247,258,259,],[13,13,65,-47,80,106,106,106,106,-46,106,106,106,106,106,155,106,163,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,-29,106,106,106,106,-28,106,-32,-30,-31,]),'DPUNTOS':([9,20,24,25,26,27,28,29,30,66,82,117,119,120,121,122,127,131,166,172,212,213,214,215,],[14,63,-103,-104,-105,-107,-108,-109,-111,-106,14,-112,167,-117,-116,-110,63,-118,-113,-119,-65,-114,-115,-110,]),'COMA':([10,12,21,22,24,25,26,27,28,29,30,35,39,50,51,52,53,54,55,56,57,64,66,71,87,89,90,91,92,93,94,95,96,97,100,102,103,104,105,111,114,116,117,131,132,133,150,151,152,154,156,157,159,161,164,166,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,203,206,211,212,216,217,218,229,230,231,235,236,237,238,239,240,244,245,246,247,248,249,250,251,254,255,256,257,],[16,-49,-110,-59,-103,-104,-105,-107,-108,-109,-111,-48,-47,-17,-18,-19,-20,-21,-42,-43,-45,-61,-106,-46,-44,-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,-39,-60,-63,-112,-118,173,-58,-94,-82,-85,-92,173,-58,-25,-40,-62,-113,-119,-56,-78,-79,-80,-81,-83,-84,-86,-87,-88,-89,-90,-91,-66,-77,-76,-96,-93,-97,-22,-27,-64,-65,-129,-55,-57,-23,-24,-26,-41,-120,-121,-122,-123,-124,173,-98,258,259,-35,-36,-37,-38,-125,-126,-127,-128,]),'ARROW':([11,15,],[17,33,]),'LLLAV':([11,15,21,24,25,26,27,28,29,30,36,60,66,69,89,90,91,92,93,94,95,96,97,100,102,103,104,105,109,110,112,117,131,150,151,152,154,166,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,204,210,212,217,233,236,237,238,239,240,245,254,255,256,257,],[19,19,-110,-103,-104,-105,-107,-108,-109,-111,19,19,-106,19,-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,19,160,19,-112,-118,-94,-82,-85,-92,-113,-119,-56,-78,-79,-80,-81,-83,-84,-86,-87,-88,-89,-90,-91,-66,-77,-76,-96,-93,-97,19,19,-65,-55,19,-120,-121,-122,-123,-124,-98,-125,-126,-127,-128,]),'ANDSINGLE':([14,17,23,31,33,39,56,58,59,61,63,65,68,71,83,85,86,98,99,108,115,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,163,167,173,202,205,207,224,225,226,227,232,234,247,258,259,],[23,37,37,37,37,-47,107,107,107,107,115,37,37,-46,107,107,107,107,107,107,37,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,37,37,107,107,107,-29,107,107,107,107,-28,107,-32,-30,-31,]),'I64':([14,17,23,31,33,63,65,68,115,163,167,],[24,24,24,24,24,24,24,24,24,24,24,]),'F64':([14,17,23,31,33,63,65,68,115,163,167,],[25,25,25,25,25,25,25,25,25,25,25,]),'STRING':([14,17,23,31,33,63,65,68,115,163,167,],[26,26,26,26,26,26,26,26,26,26,26,]),'BOOL':([14,17,23,31,33,63,65,68,115,163,167,],[27,27,27,27,27,27,27,27,27,27,27,]),'CHAR':([14,17,23,31,33,63,65,68,115,163,167,],[28,28,28,28,28,28,28,28,28,28,28,]),'USIZE':([14,17,23,31,33,63,65,68,115,163,167,],[29,29,29,29,29,29,29,29,29,29,29,]),'LCOR':([14,17,23,31,33,39,49,56,58,59,61,63,65,68,71,82,83,84,85,86,96,98,99,108,115,118,124,125,127,129,130,135,136,137,138,139,140,141,142,143,144,145,146,150,153,160,162,163,167,173,174,202,205,207,217,224,225,226,227,232,234,247,258,259,],[31,31,31,31,31,-47,86,108,108,108,108,31,31,31,-46,86,108,130,108,108,86,108,108,108,31,108,108,108,86,108,108,108,108,108,108,108,108,108,108,108,108,108,108,130,108,108,108,31,31,108,-56,108,108,-29,-55,108,108,108,108,-28,108,-32,-30,-31,]),'VEC':([14,17,23,31,33,39,56,58,59,61,63,65,68,71,83,85,86,98,99,108,115,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,163,167,173,202,205,207,224,225,226,227,232,234,247,258,259,],[32,32,32,32,32,-47,101,101,101,101,32,32,32,-46,101,101,101,101,101,101,32,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,32,32,101,101,101,-29,101,101,101,101,-28,101,-32,-30,-31,]),'RLLAV':([19,38,39,40,45,50,51,52,53,54,71,72,73,74,75,76,77,111,159,160,161,203,205,206,207,229,230,231,232,235,247,258,259,],[39,71,-47,-6,-11,-17,-18,-19,-20,-21,-46,-5,-7,-8,-9,-10,-12,-39,-25,206,-40,-22,231,-27,-29,-23,-24,-26,-28,-41,-32,-30,-31,]),'PRINT':([19,38,39,40,45,50,51,52,53,54,71,72,73,74,75,76,77,111,159,161,203,206,229,230,231,233,235,],[47,47,-47,-6,-11,-17,-18,-19,-20,-21,-46,-5,-7,-8,-9,-10,-12,-39,-25,-40,-22,-27,-23,-24,-26,47,-41,]),'LET':([19,38,39,40,45,50,51,52,53,54,71,72,73,74,75,76,77,111,159,161,203,206,229,230,231,235,],[48,48,-47,-6,-11,-17,-18,-19,-20,-21,-46,-5,-7,-8,-9,-10,-12,-39,-25,-40,-22,-27,-23,-24,-26,-41,]),'BREAK':([19,38,39,40,45,50,51,52,53,54,71,72,73,74,75,76,77,111,159,161,203,206,229,230,231,233,235,],[55,55,-47,-6,-11,-17,-18,-19,-20,-21,-46,-5,-7,-8,-9,-10,-12,-39,-25,-40,-22,-27,-23,-24,-26,55,-41,]),'RETURN':([19,38,39,40,45,50,51,52,53,54,71,72,73,74,75,76,77,111,159,161,203,206,229,230,231,233,235,],[56,56,-47,-6,-11,-17,-18,-19,-20,-21,-46,-5,-7,-8,-9,-10,-12,-39,-25,-40,-22,-27,-23,-24,-26,56,-41,]),'CONTINUE':([19,38,39,40,45,50,51,52,53,54,71,72,73,74,75,76,77,111,159,161,203,206,229,230,231,233,235,],[57,57,-47,-6,-11,-17,-18,-19,-20,-21,-46,-5,-7,-8,-9,-10,-12,-39,-25,-40,-22,-27,-23,-24,-26,57,-41,]),'IF':([19,38,39,40,45,50,51,52,53,54,71,72,73,74,75,76,77,111,159,161,203,204,206,229,230,231,233,235,],[58,58,-47,-6,-11,-17,-18,-19,-20,-21,-46,-5,-7,-8,-9,-10,-12,-39,-25,-40,-22,58,-27,-23,-24,-26,58,-41,]),'MATCH':([19,38,39,40,45,50,51,52,53,54,71,72,73,74,75,76,77,111,159,161,203,206,229,230,231,233,235,],[59,59,-47,-6,-11,-17,-18,-19,-20,-21,-46,-5,-7,-8,-9,-10,-12,-39,-25,-40,-22,-27,-23,-24,-26,59,-41,]),'LOOP':([19,38,39,40,45,50,51,52,53,54,71,72,73,74,75,76,77,111,159,161,203,206,229,230,231,233,235,],[60,60,-47,-6,-11,-17,-18,-19,-20,-21,-46,-5,-7,-8,-9,-10,-12,-39,-25,-40,-22,-27,-23,-24,-26,60,-41,]),'WHILE':([19,38,39,40,45,50,51,52,53,54,71,72,73,74,75,76,77,111,159,161,203,206,229,230,231,233,235,],[61,61,-47,-6,-11,-17,-18,-19,-20,-21,-46,-5,-7,-8,-9,-10,-12,-39,-25,-40,-22,-27,-23,-24,-26,61,-41,]),'FOR':([19,38,39,40,45,50,51,52,53,54,71,72,73,74,75,76,77,111,159,161,203,206,229,230,231,233,235,],[62,62,-47,-6,-11,-17,-18,-19,-20,-21,-46,-5,-7,-8,-9,-10,-12,-39,-25,-40,-22,-27,-23,-24,-26,62,-41,]),'IGUAL':([21,22,24,25,26,27,28,29,30,49,64,66,79,82,84,114,116,117,127,164,166,174,211,212,217,],[-110,-59,-103,-104,-105,-107,-108,-109,-111,83,-61,-106,125,83,129,-60,-63,-112,83,-62,-113,-56,-64,-65,-55,]),'RCOR':([21,24,25,26,27,28,29,30,66,67,89,90,91,92,93,94,95,96,97,100,102,103,104,105,117,131,134,150,151,152,154,156,157,165,166,171,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,212,217,218,228,236,237,238,239,240,245,254,255,256,257,],[-110,-103,-104,-105,-107,-108,-109,-111,-106,117,-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,-112,-118,174,-94,-82,-85,-92,201,-58,212,-113,217,-119,-56,-78,-79,-80,-81,-83,-84,-86,-87,-88,-89,-90,-91,-66,-77,-76,-96,-93,-97,-65,-55,-57,245,-120,-121,-122,-123,-124,-98,-125,-126,-127,-128,]),'PCOMA':([21,24,25,26,27,28,29,30,41,42,43,44,46,55,56,57,66,67,81,87,89,90,91,92,93,94,95,96,97,100,102,103,104,105,117,126,128,131,150,151,152,154,157,166,169,170,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,212,216,217,236,237,238,239,240,245,254,255,256,257,],[-110,-103,-104,-105,-107,-108,-109,-111,73,74,75,76,77,-42,-43,-45,-106,118,-52,-44,-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,-112,-51,-53,-118,-94,-82,-85,-92,202,-113,-50,-54,-119,-56,-78,-79,-80,-81,-83,-84,-86,-87,-88,-89,-90,-91,-66,-77,-76,-96,-93,-97,-65,-129,-55,-120,-121,-122,-123,-124,-98,-125,-126,-127,-128,]),'aSTR':([23,37,115,],[66,66,66,]),'MAYOR':([24,25,26,27,28,29,30,66,87,89,90,91,92,93,94,95,96,97,100,102,103,104,105,109,110,112,117,119,120,121,122,128,131,133,134,150,151,152,154,157,165,166,168,169,170,171,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,209,210,212,213,214,215,217,218,228,236,237,238,239,240,241,242,243,245,253,254,255,256,257,],[-103,-104,-105,-107,-108,-109,-111,-106,143,-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,143,143,143,-112,166,-117,-116,-110,143,-118,143,143,-94,-82,143,-92,143,143,-113,143,143,143,143,-119,-56,-78,-79,-80,-81,143,143,-86,-87,-88,-89,-90,-91,-66,-77,-76,-96,-93,-97,143,143,-65,-114,-115,-110,-55,143,143,-120,-121,-122,-123,-124,143,143,143,-98,143,-125,-126,-127,-128,]),'MENOR':([32,87,89,90,91,92,93,94,95,96,97,100,102,103,104,105,109,110,112,128,131,133,134,150,151,152,154,157,165,168,169,170,171,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,209,210,217,218,228,236,237,238,239,240,241,242,243,245,253,254,255,256,257,],[68,144,-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,144,144,144,144,-118,144,144,-94,-82,144,-92,144,144,144,144,144,144,-119,-56,-78,-79,-80,-81,144,144,-86,-87,-88,-89,-90,-91,-66,-77,-76,-96,-93,-97,144,144,-55,144,144,-120,-121,-122,-123,-124,144,144,144,-98,144,-125,-126,-127,-128,]),'ELSE':([39,71,158,],[-47,-46,204,]),'MENOS':([39,56,58,59,61,71,83,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,105,108,109,110,112,118,124,125,128,129,130,131,133,134,135,136,137,138,139,140,141,142,143,144,145,146,150,151,152,154,157,160,162,165,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,202,205,207,209,210,217,218,224,225,226,227,228,232,234,236,237,238,239,240,241,242,243,245,247,253,254,255,256,257,258,259,],[-47,98,98,98,98,-46,98,98,98,136,-74,-67,-68,-69,-70,-71,-72,-73,-75,98,98,-95,-99,-100,-101,-102,98,136,136,136,98,98,98,136,98,98,-118,136,136,98,98,98,98,98,98,98,98,98,98,98,98,-94,-82,136,-92,136,98,98,136,136,136,136,136,-119,98,-56,-78,-79,-80,-81,136,136,136,136,136,136,136,136,-66,-77,-76,-96,-93,-97,98,98,-29,136,136,-55,136,98,98,98,98,136,-28,98,-120,-121,-122,-123,-124,136,136,136,-98,-32,136,-125,-126,-127,-128,-30,-31,]),'AD':([39,47,56,58,59,61,71,83,85,86,98,99,101,108,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,173,202,205,207,224,225,226,227,232,234,247,258,259,],[-47,78,99,99,99,99,-46,99,99,99,99,99,153,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,-29,99,99,99,99,-28,99,-32,-30,-31,]),'ENTERO':([39,56,58,59,61,71,83,85,86,88,98,99,108,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,173,202,205,207,224,225,226,227,232,234,247,258,259,],[-47,102,102,102,102,-46,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,-29,102,102,102,102,-28,102,-32,-30,-31,]),'DECIMAL':([39,56,58,59,61,71,83,85,86,88,98,99,108,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,173,202,205,207,224,225,226,227,232,234,247,258,259,],[-47,103,103,103,103,-46,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,-29,103,103,103,103,-28,103,-32,-30,-31,]),'CADENA':([39,56,58,59,61,71,83,85,86,88,98,99,108,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,173,202,205,207,224,225,226,227,232,234,247,258,259,],[-47,104,104,104,104,-46,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,-29,104,104,104,104,-28,104,-32,-30,-31,]),'BOOLEANO':([39,56,58,59,61,71,83,85,86,88,98,99,108,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,173,202,205,207,224,225,226,227,232,234,247,258,259,],[-47,105,105,105,105,-46,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,-29,105,105,105,105,-28,105,-32,-30,-31,]),'MAS':([87,89,90,91,92,93,94,95,96,97,100,102,103,104,105,109,110,112,128,131,133,134,150,151,152,154,157,165,168,169,170,171,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,209,210,217,218,228,236,237,238,239,240,241,242,243,245,253,254,255,256,257,],[135,-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,135,135,135,135,-118,135,135,-94,-82,135,-92,135,135,135,135,135,135,-119,-56,-78,-79,-80,-81,135,135,135,135,135,135,135,135,-66,-77,-76,-96,-93,-97,135,135,-55,135,135,-120,-121,-122,-123,-124,135,135,135,-98,135,-125,-126,-127,-128,]),'MULTIPLICACION':([87,89,90,91,92,93,94,95,96,97,100,102,103,104,105,109,110,112,128,131,133,134,150,151,152,154,157,165,168,169,170,171,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,209,210,217,218,228,236,237,238,239,240,241,242,243,245,253,254,255,256,257,],[137,-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,137,137,137,137,-118,137,137,-94,-82,137,-92,137,137,137,137,137,137,-119,-56,137,137,-80,-81,137,137,137,137,137,137,137,137,-66,-77,-76,-96,-93,-97,137,137,-55,137,137,-120,-121,-122,-123,-124,137,137,137,-98,137,-125,-126,-127,-128,]),'DIVISION':([87,89,90,91,92,93,94,95,96,97,100,102,103,104,105,109,110,112,128,131,133,134,150,151,152,154,157,165,168,169,170,171,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,209,210,217,218,228,236,237,238,239,240,241,242,243,245,253,254,255,256,257,],[138,-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,138,138,138,138,-118,138,138,-94,-82,138,-92,138,138,138,138,138,138,-119,-56,138,138,-80,-81,138,138,138,138,138,138,138,138,-66,-77,-76,-96,-93,-97,138,138,-55,138,138,-120,-121,-122,-123,-124,138,138,138,-98,138,-125,-126,-127,-128,]),'AND':([87,89,90,91,92,93,94,95,96,97,100,102,103,104,105,109,110,112,128,131,133,134,150,151,152,154,157,165,168,169,170,171,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,209,210,217,218,228,236,237,238,239,240,241,242,243,245,253,254,255,256,257,],[139,-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,139,139,139,139,-118,139,139,-94,-82,-85,-92,139,139,139,139,139,139,-119,-56,-78,-79,-80,-81,-83,139,-86,-87,-88,-89,-90,-91,-66,-77,-76,-96,-93,-97,139,139,-55,139,139,-120,-121,-122,-123,-124,139,139,139,-98,139,-125,-126,-127,-128,]),'OR':([87,89,90,91,92,93,94,95,96,97,100,102,103,104,105,109,110,112,128,131,133,134,150,151,152,154,157,165,168,169,170,171,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,209,210,217,218,228,236,237,238,239,240,241,242,243,245,253,254,255,256,257,],[140,-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,140,140,140,140,-118,140,140,-94,-82,-85,-92,140,140,140,140,140,140,-119,-56,-78,-79,-80,-81,-83,-84,-86,-87,-88,-89,-90,-91,-66,-77,-76,-96,-93,-97,140,140,-55,140,140,-120,-121,-122,-123,-124,140,140,140,-98,140,-125,-126,-127,-128,]),'IGUALI':([87,89,90,91,92,93,94,95,96,97,100,102,103,104,105,109,110,112,128,131,133,134,150,151,152,154,157,165,168,169,170,171,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,209,210,217,218,228,236,237,238,239,240,241,242,243,245,253,254,255,256,257,],[141,-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,141,141,141,141,-118,141,141,-94,-82,141,-92,141,141,141,141,141,141,-119,-56,-78,-79,-80,-81,141,141,-86,-87,-88,-89,-90,-91,-66,-77,-76,-96,-93,-97,141,141,-55,141,141,-120,-121,-122,-123,-124,141,141,141,-98,141,-125,-126,-127,-128,]),'DIF':([87,89,90,91,92,93,94,95,96,97,100,102,103,104,105,109,110,112,128,131,133,134,150,151,152,154,157,165,168,169,170,171,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,209,210,217,218,228,236,237,238,239,240,241,242,243,245,253,254,255,256,257,],[142,-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,142,142,142,142,-118,142,142,-94,-82,142,-92,142,142,142,142,142,142,-119,-56,-78,-79,-80,-81,142,142,-86,-87,-88,-89,-90,-91,-66,-77,-76,-96,-93,-97,142,142,-55,142,142,-120,-121,-122,-123,-124,142,142,142,-98,142,-125,-126,-127,-128,]),'MAYORI':([87,89,90,91,92,93,94,95,96,97,100,102,103,104,105,109,110,112,128,131,133,134,150,151,152,154,157,165,168,169,170,171,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,209,210,217,218,228,236,237,238,239,240,241,242,243,245,253,254,255,256,257,],[145,-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,145,145,145,145,-118,145,145,-94,-82,145,-92,145,145,145,145,145,145,-119,-56,-78,-79,-80,-81,145,145,-86,-87,-88,-89,-90,-91,-66,-77,-76,-96,-93,-97,145,145,-55,145,145,-120,-121,-122,-123,-124,145,145,145,-98,145,-125,-126,-127,-128,]),'MENORI':([87,89,90,91,92,93,94,95,96,97,100,102,103,104,105,109,110,112,128,131,133,134,150,151,152,154,157,165,168,169,170,171,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,209,210,217,218,228,236,237,238,239,240,241,242,243,245,253,254,255,256,257,],[146,-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,146,146,146,146,-118,146,146,-94,-82,146,-92,146,146,146,146,146,146,-119,-56,-78,-79,-80,-81,146,146,-86,-87,-88,-89,-90,-91,-66,-77,-76,-96,-93,-97,146,146,-55,146,146,-120,-121,-122,-123,-124,146,146,146,-98,146,-125,-126,-127,-128,]),'ARROW2':([89,90,91,92,93,94,95,96,97,100,102,103,104,105,131,150,151,152,154,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,208,209,217,236,237,238,239,240,245,253,254,255,256,257,],[-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,-118,-94,-82,-85,-92,-119,-56,-78,-79,-80,-81,-83,-84,-86,-87,-88,-89,-90,-91,-66,-77,-76,-96,-93,-97,233,-34,-55,-120,-121,-122,-123,-124,-98,-33,-125,-126,-127,-128,]),'ORSINGLE':([89,90,91,92,93,94,95,96,97,100,102,103,104,105,131,150,151,152,154,172,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,198,199,200,201,208,209,217,236,237,238,239,240,245,253,254,255,256,257,],[-74,-67,-68,-69,-70,-71,-72,-73,-75,-95,-99,-100,-101,-102,-118,-94,-82,-85,-92,-119,-56,-78,-79,-80,-81,-83,-84,-86,-87,-88,-89,-90,-91,-66,-77,-76,-96,-93,-97,234,-34,-55,-120,-121,-122,-123,-124,-98,-33,-125,-126,-127,-128,]),'PUNTO':([89,96,102,103,104,105,],[148,149,-99,-100,-101,-102,]),'IN':([113,],[162,]),'TOSTRING':([148,149,],[189,189,]),'TOOWNED':([148,149,],[190,190,]),'CLONE':([148,149,],[191,191,]),'LEN':([148,149,],[192,192,]),'CAPACITY':([148,149,],[193,193,]),'REMOVE':([148,149,],[194,194,]),'CONTAINS':([148,149,],[195,195,]),'PUSH':([148,149,],[196,196,]),'INSERT':([148,149,],[197,197,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones_g':([0,],[2,]),'instruccion_g':([0,2,],[3,6,]),'funcion':([0,2,],[4,4,]),'lista_parametros':([8,],[10,]),'asignacion_simple':([8,16,48,],[12,35,79,]),'statement':([11,15,36,60,69,109,112,204,210,233,],[18,34,70,111,123,158,161,229,235,247,]),'tipo_var':([14,17,23,31,33,63,65,68,115,163,167,],[22,36,64,67,69,114,116,120,164,211,213,]),'lista_arr2':([14,17,23,31,33,63,65,68,115,163,167,],[30,30,30,30,30,30,30,30,30,30,30,]),'instrucciones_l':([19,],[38,]),'instruccion_l':([19,38,],[40,72,]),'print':([19,38,233,],[41,41,248,]),'declaracion':([19,38,],[42,42,]),'asignacion':([19,38,48,80,],[43,43,81,126,]),'llamada':([19,38,56,58,59,61,68,83,85,86,98,99,108,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,167,173,202,205,224,225,226,227,233,234,],[44,44,95,95,95,95,121,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,95,214,95,95,95,95,95,95,95,249,95,]),'sentencia':([19,38,233,],[45,45,250,]),'transferencia':([19,38,233,],[46,46,251,]),'if':([19,38,204,233,],[50,50,230,50,]),'match':([19,38,233,],[51,51,51,]),'loop':([19,38,233,],[52,52,52,]),'while':([19,38,233,],[53,53,53,]),'for':([19,38,233,],[54,54,54,]),'lista_arr':([49,82,96,127,],[84,84,150,84,]),'exp':([56,58,59,61,83,85,86,98,99,108,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,173,202,205,224,225,226,227,234,],[87,109,110,112,128,133,134,151,152,157,165,168,169,170,171,175,176,177,178,179,180,181,182,183,184,185,186,209,210,218,228,209,241,242,243,133,253,]),'valores':([56,58,59,61,83,85,86,88,98,99,108,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,173,202,205,224,225,226,227,234,],[89,89,89,89,89,89,89,147,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,]),'expmath':([56,58,59,61,83,85,86,98,99,108,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,173,202,205,224,225,226,227,234,],[90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,]),'expop':([56,58,59,61,83,85,86,98,99,108,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,173,202,205,224,225,226,227,234,],[91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,]),'exprel':([56,58,59,61,83,85,86,98,99,108,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,173,202,205,224,225,226,227,234,],[92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,]),'exparr':([56,58,59,61,83,85,86,98,99,108,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,173,202,205,224,225,226,227,234,],[93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,]),'expvec':([56,58,59,61,83,85,86,98,99,108,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,173,202,205,224,225,226,227,234,],[94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,94,]),'exparam':([56,58,59,61,83,85,86,98,99,108,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,160,162,173,202,205,224,225,226,227,234,],[97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,]),'newarray':([56,58,59,61,83,85,86,98,99,108,118,124,125,129,130,135,136,137,138,139,140,141,142,143,144,145,146,153,160,162,173,202,205,224,225,226,227,234,],[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,199,100,100,100,100,100,100,100,100,100,100,]),'lista_class':([68,],[119,]),'lista_exp':([85,108,227,],[132,156,244,]),'match_statement':([110,],[159,]),'exp_native':([148,149,],[188,198,]),'else':([158,],[203,]),'lista_brazos':([160,],[205,]),'brazo':([160,205,],[207,232,]),'lista_exp_brazos':([160,205,],[208,208,]),'instruccion_match':([233,],[246,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones_g','init',1,'p_init','parser.py',52),
  ('instrucciones_g -> instrucciones_g instruccion_g','instrucciones_g',2,'p_instrucciones_g','parser.py',56),
  ('instrucciones_g -> instruccion_g','instrucciones_g',1,'p_instrucciones_g','parser.py',57),
  ('instruccion_g -> funcion','instruccion_g',1,'p_instruccion','parser.py',64),
  ('instrucciones_l -> instrucciones_l instruccion_l','instrucciones_l',2,'p_instrucciones_l','parser.py',68),
  ('instrucciones_l -> instruccion_l','instrucciones_l',1,'p_instrucciones_l','parser.py',69),
  ('instruccion_l -> print PCOMA','instruccion_l',2,'p_instruccion_l','parser.py',76),
  ('instruccion_l -> declaracion PCOMA','instruccion_l',2,'p_instruccion_l','parser.py',77),
  ('instruccion_l -> asignacion PCOMA','instruccion_l',2,'p_instruccion_l','parser.py',78),
  ('instruccion_l -> llamada PCOMA','instruccion_l',2,'p_instruccion_l','parser.py',79),
  ('instruccion_l -> sentencia','instruccion_l',1,'p_instruccion_l','parser.py',80),
  ('instruccion_l -> transferencia PCOMA','instruccion_l',2,'p_instruccion_l','parser.py',81),
  ('funcion -> FN ID LPAR lista_parametros RPAR ARROW tipo_var statement','funcion',8,'p_funcion','parser.py',85),
  ('funcion -> FN ID LPAR lista_parametros RPAR statement','funcion',6,'p_funcion','parser.py',86),
  ('funcion -> FN ID LPAR RPAR ARROW tipo_var statement','funcion',7,'p_funcion','parser.py',87),
  ('funcion -> FN ID LPAR RPAR statement','funcion',5,'p_funcion','parser.py',88),
  ('sentencia -> if','sentencia',1,'p_sentencia','parser.py',97),
  ('sentencia -> match','sentencia',1,'p_sentencia','parser.py',98),
  ('sentencia -> loop','sentencia',1,'p_sentencia','parser.py',99),
  ('sentencia -> while','sentencia',1,'p_sentencia','parser.py',100),
  ('sentencia -> for','sentencia',1,'p_sentencia','parser.py',101),
  ('if -> IF exp statement else','if',4,'p_if','parser.py',105),
  ('else -> ELSE statement','else',2,'p_else','parser.py',109),
  ('else -> ELSE if','else',2,'p_else','parser.py',110),
  ('match -> MATCH exp match_statement','match',3,'p_match','parser.py',115),
  ('match_statement -> LLLAV lista_brazos RLLAV','match_statement',3,'p_match_statement','parser.py',119),
  ('match_statement -> LLLAV RLLAV','match_statement',2,'p_match_statement','parser.py',120),
  ('lista_brazos -> lista_brazos brazo','lista_brazos',2,'p_lista_brazos','parser.py',125),
  ('lista_brazos -> brazo','lista_brazos',1,'p_lista_brazos','parser.py',126),
  ('brazo -> lista_exp_brazos ARROW2 instruccion_match COMA','brazo',4,'p_brazo','parser.py',133),
  ('brazo -> lista_exp_brazos ARROW2 statement COMA','brazo',4,'p_brazo','parser.py',134),
  ('brazo -> lista_exp_brazos ARROW2 statement','brazo',3,'p_brazo','parser.py',135),
  ('lista_exp_brazos -> lista_exp_brazos ORSINGLE exp','lista_exp_brazos',3,'p_lista_exp_brazos','parser.py',139),
  ('lista_exp_brazos -> exp','lista_exp_brazos',1,'p_lista_exp_brazos','parser.py',140),
  ('instruccion_match -> print','instruccion_match',1,'p_instruction_match','parser.py',147),
  ('instruccion_match -> llamada','instruccion_match',1,'p_instruction_match','parser.py',148),
  ('instruccion_match -> sentencia','instruccion_match',1,'p_instruction_match','parser.py',149),
  ('instruccion_match -> transferencia','instruccion_match',1,'p_instruction_match','parser.py',150),
  ('loop -> LOOP statement','loop',2,'p_loop','parser.py',154),
  ('while -> WHILE exp statement','while',3,'p_while','parser.py',158),
  ('for -> FOR ID IN exp statement','for',5,'p_for','parser.py',162),
  ('transferencia -> BREAK','transferencia',1,'p_transferencia','parser.py',166),
  ('transferencia -> RETURN','transferencia',1,'p_transferencia','parser.py',167),
  ('transferencia -> RETURN exp','transferencia',2,'p_transferencia','parser.py',168),
  ('transferencia -> CONTINUE','transferencia',1,'p_transferencia','parser.py',169),
  ('statement -> LLLAV instrucciones_l RLLAV','statement',3,'p_statement','parser.py',177),
  ('statement -> LLLAV RLLAV','statement',2,'p_statement','parser.py',178),
  ('lista_parametros -> lista_parametros COMA asignacion_simple','lista_parametros',3,'p_lista_parametros','parser.py',183),
  ('lista_parametros -> asignacion_simple','lista_parametros',1,'p_lista_parametros','parser.py',184),
  ('declaracion -> LET asignacion_simple IGUAL exp','declaracion',4,'p_declaracion','parser.py',191),
  ('declaracion -> LET MUT asignacion','declaracion',3,'p_declaracion','parser.py',192),
  ('declaracion -> LET asignacion','declaracion',2,'p_declaracion','parser.py',193),
  ('asignacion -> ID IGUAL exp','asignacion',3,'p_asignacion','parser.py',199),
  ('asignacion -> ID lista_arr IGUAL exp','asignacion',4,'p_asignacion','parser.py',200),
  ('lista_arr -> lista_arr LCOR exp RCOR','lista_arr',4,'p_lista_arr','parser.py',206),
  ('lista_arr -> LCOR exp RCOR','lista_arr',3,'p_lista_arr','parser.py',207),
  ('lista_exp -> lista_exp COMA exp','lista_exp',3,'p_lista_exp','parser.py',214),
  ('lista_exp -> exp','lista_exp',1,'p_lista_exp','parser.py',215),
  ('asignacion_simple -> ID DPUNTOS tipo_var','asignacion_simple',3,'p_asignacion_simple','parser.py',222),
  ('asignacion_simple -> MUT ID DPUNTOS tipo_var','asignacion_simple',4,'p_asignacion_simple','parser.py',223),
  ('asignacion_simple -> ID DPUNTOS ANDSINGLE tipo_var','asignacion_simple',4,'p_asignacion_simple','parser.py',224),
  ('asignacion_simple -> MUT ID DPUNTOS ANDSINGLE tipo_var','asignacion_simple',5,'p_asignacion_simple','parser.py',225),
  ('asignacion_simple -> ID DPUNTOS ANDSINGLE MUT tipo_var','asignacion_simple',5,'p_asignacion_simple','parser.py',226),
  ('asignacion_simple -> MUT ID DPUNTOS ANDSINGLE MUT tipo_var','asignacion_simple',6,'p_asignacion_simple','parser.py',227),
  ('lista_arr2 -> LCOR tipo_var PCOMA exp RCOR','lista_arr2',5,'p_lista_arr2','parser.py',238),
  ('exp -> LPAR valores LPAR','exp',3,'p_exp','parser.py',242),
  ('exp -> expmath','exp',1,'p_exp','parser.py',243),
  ('exp -> expop','exp',1,'p_exp','parser.py',244),
  ('exp -> exprel','exp',1,'p_exp','parser.py',245),
  ('exp -> exparr','exp',1,'p_exp','parser.py',246),
  ('exp -> expvec','exp',1,'p_exp','parser.py',247),
  ('exp -> llamada','exp',1,'p_exp','parser.py',248),
  ('exp -> ID','exp',1,'p_exp','parser.py',249),
  ('exp -> valores','exp',1,'p_exp','parser.py',250),
  ('exp -> exparam','exp',1,'p_exp','parser.py',251),
  ('exp -> ID PUNTO exp_native','exp',3,'p_exp','parser.py',252),
  ('exp -> valores PUNTO exp_native','exp',3,'p_exp','parser.py',253),
  ('expmath -> exp MAS exp','expmath',3,'p_expmath','parser.py',274),
  ('expmath -> exp MENOS exp','expmath',3,'p_expmath','parser.py',275),
  ('expmath -> exp MULTIPLICACION exp','expmath',3,'p_expmath','parser.py',276),
  ('expmath -> exp DIVISION exp','expmath',3,'p_expmath','parser.py',277),
  ('expmath -> MENOS exp','expmath',2,'p_expmath','parser.py',278),
  ('expop -> exp AND exp','expop',3,'p_explog','parser.py',287),
  ('expop -> exp OR exp','expop',3,'p_explog','parser.py',288),
  ('expop -> AD exp','expop',2,'p_explog','parser.py',289),
  ('exprel -> exp IGUALI exp','exprel',3,'p_exprel','parser.py',296),
  ('exprel -> exp DIF exp','exprel',3,'p_exprel','parser.py',297),
  ('exprel -> exp MAYOR exp','exprel',3,'p_exprel','parser.py',298),
  ('exprel -> exp MENOR exp','exprel',3,'p_exprel','parser.py',299),
  ('exprel -> exp MAYORI exp','exprel',3,'p_exprel','parser.py',300),
  ('exprel -> exp MENORI exp','exprel',3,'p_exprel','parser.py',301),
  ('exparam -> MUT ID','exparam',2,'p_exparam','parser.py',310),
  ('exparam -> ANDSINGLE MUT ID','exparam',3,'p_exparam','parser.py',311),
  ('exparr -> ID lista_arr','exparr',2,'p_exparr','parser.py',316),
  ('exparr -> newarray','exparr',1,'p_exparr','parser.py',317),
  ('expvec -> VEC AD newarray','expvec',3,'p_expvec','parser.py',322),
  ('newarray -> LCOR lista_exp RCOR','newarray',3,'p_newarray','parser.py',326),
  ('newarray -> LCOR exp PCOMA exp RCOR','newarray',5,'p_newarray','parser.py',327),
  ('valores -> ENTERO','valores',1,'p_valores','parser.py',332),
  ('valores -> DECIMAL','valores',1,'p_valores','parser.py',333),
  ('valores -> CADENA','valores',1,'p_valores','parser.py',334),
  ('valores -> BOOLEANO','valores',1,'p_valores','parser.py',335),
  ('tipo_var -> I64','tipo_var',1,'p_tipo_var','parser.py',342),
  ('tipo_var -> F64','tipo_var',1,'p_tipo_var','parser.py',343),
  ('tipo_var -> STRING','tipo_var',1,'p_tipo_var','parser.py',344),
  ('tipo_var -> ANDSINGLE aSTR','tipo_var',2,'p_tipo_var','parser.py',345),
  ('tipo_var -> BOOL','tipo_var',1,'p_tipo_var','parser.py',346),
  ('tipo_var -> CHAR','tipo_var',1,'p_tipo_var','parser.py',347),
  ('tipo_var -> USIZE','tipo_var',1,'p_tipo_var','parser.py',348),
  ('tipo_var -> ID','tipo_var',1,'p_tipo_var','parser.py',349),
  ('tipo_var -> lista_arr2','tipo_var',1,'p_tipo_var','parser.py',350),
  ('tipo_var -> LCOR tipo_var RCOR','tipo_var',3,'p_tipo_var','parser.py',351),
  ('tipo_var -> VEC MENOR lista_class MAYOR','tipo_var',4,'p_tipo_var','parser.py',352),
  ('lista_class -> lista_class DPUNTOS tipo_var','lista_class',3,'p_lista_class','parser.py',366),
  ('lista_class -> lista_class DPUNTOS llamada','lista_class',3,'p_lista_class','parser.py',367),
  ('lista_class -> llamada','lista_class',1,'p_lista_class','parser.py',368),
  ('lista_class -> tipo_var','lista_class',1,'p_lista_class','parser.py',369),
  ('llamada -> ID LPAR RPAR','llamada',3,'p_llamada','parser.py',378),
  ('llamada -> ID LPAR lista_exp RPAR','llamada',4,'p_llamada','parser.py',379),
  ('exp_native -> TOSTRING LPAR RPAR','exp_native',3,'p_exp_native','parser.py',384),
  ('exp_native -> TOOWNED LPAR RPAR','exp_native',3,'p_exp_native','parser.py',385),
  ('exp_native -> CLONE LPAR RPAR','exp_native',3,'p_exp_native','parser.py',386),
  ('exp_native -> LEN LPAR RPAR','exp_native',3,'p_exp_native','parser.py',387),
  ('exp_native -> CAPACITY LPAR RPAR','exp_native',3,'p_exp_native','parser.py',388),
  ('exp_native -> REMOVE LPAR exp RPAR','exp_native',4,'p_exp_native','parser.py',389),
  ('exp_native -> CONTAINS LPAR exp RPAR','exp_native',4,'p_exp_native','parser.py',390),
  ('exp_native -> PUSH LPAR exp RPAR','exp_native',4,'p_exp_native','parser.py',391),
  ('exp_native -> INSERT LPAR lista_exp RPAR','exp_native',4,'p_exp_native','parser.py',392),
  ('print -> PRINT AD LPAR exp RPAR','print',5,'p_print','parser.py',404),
]
