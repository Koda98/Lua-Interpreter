
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "nonassocORnonassocANDnonassocLTGTLTEGTEEQUALSNEleftPLUSMINUSleftTIMESDIVIDEINTEGER_DIVIDErightUMINUSNOTAND BREAK DIVIDE DO ELSE END EQUALS FALSE GT GTE IDENTIFIER IF INTEGER_DIVIDE LT LTE MINUS NE NIL NOT NUMBER OR PLUS RETURN THEN TIMES TRUE WHILEchunk : blockblock : stat_liststat_list : stat stat_list\n                 | emptystat : ';'stat : BREAKstat : DO block ENDstat : WHILE exp DO block ENDstat : IF exp THEN block END\n            | IF exp THEN block ELSE block ENDstat : varlist '=' expliststat : RETURN\n            | RETURN explist\n            | RETURN ';'\n            | RETURN explist ';'varlist : var\n               | var ',' varlistvar : IDENTIFIERexplist : exp\n               | exp ',' explistexp : exp PLUS exp\n           | exp MINUS exp\n           | exp TIMES exp\n           | exp DIVIDE exp\n           | exp INTEGER_DIVIDE exp\n           | exp LT exp\n           | exp GT exp\n           | exp LTE exp\n           | exp GTE exp\n           | exp EQUALS exp\n           | exp NE exp\n           | exp AND exp\n           | exp OR expexp : '(' exp ')'exp : varexp : NUMBERexp : MINUS exp %prec UMINUS\n           | NOT expexp : FALSE\n           | TRUEexp : NILempty :"
    
_lr_action_items = {';':([0,4,6,7,8,12,14,20,21,23,24,25,28,29,30,32,33,47,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,76,],[6,6,-5,-6,6,29,-18,-35,-36,-39,-40,-41,52,-14,-19,-7,6,-37,-38,6,-11,-15,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-20,-8,-9,6,-10,]),'BREAK':([0,4,6,7,8,12,14,20,21,23,24,25,28,29,30,32,33,47,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,76,],[7,7,-5,-6,7,-12,-18,-35,-36,-39,-40,-41,-13,-14,-19,-7,7,-37,-38,7,-11,-15,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-20,-8,-9,7,-10,]),'DO':([0,4,6,7,8,12,14,17,20,21,23,24,25,28,29,30,32,33,47,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,76,],[8,8,-5,-6,8,-12,-18,33,-35,-36,-39,-40,-41,-13,-14,-19,-7,8,-37,-38,8,-11,-15,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-20,-8,-9,8,-10,]),'WHILE':([0,4,6,7,8,12,14,20,21,23,24,25,28,29,30,32,33,47,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,76,],[9,9,-5,-6,9,-12,-18,-35,-36,-39,-40,-41,-13,-14,-19,-7,9,-37,-38,9,-11,-15,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-20,-8,-9,9,-10,]),'IF':([0,4,6,7,8,12,14,20,21,23,24,25,28,29,30,32,33,47,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,76,],[10,10,-5,-6,10,-12,-18,-35,-36,-39,-40,-41,-13,-14,-19,-7,10,-37,-38,10,-11,-15,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-20,-8,-9,10,-10,]),'RETURN':([0,4,6,7,8,12,14,20,21,23,24,25,28,29,30,32,33,47,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,76,],[12,12,-5,-6,12,-12,-18,-35,-36,-39,-40,-41,-13,-14,-19,-7,12,-37,-38,12,-11,-15,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-20,-8,-9,12,-10,]),'$end':([0,1,2,3,4,5,6,7,12,14,15,20,21,23,24,25,28,29,30,32,47,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,76,],[-42,0,-1,-2,-42,-4,-5,-6,-12,-18,-3,-35,-36,-39,-40,-41,-13,-14,-19,-7,-37,-38,-11,-15,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-20,-8,-9,-10,]),'IDENTIFIER':([0,4,6,7,8,9,10,12,14,18,19,20,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,76,],[14,14,-5,-6,14,14,14,14,-18,14,14,-35,-36,14,-39,-40,-41,14,-13,-14,-19,14,-7,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-37,-38,14,-11,-15,14,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-20,-8,-9,14,-10,]),'END':([3,4,5,6,7,8,12,14,15,16,20,21,23,24,25,28,29,30,32,33,47,49,50,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,],[-2,-42,-4,-5,-6,-42,-12,-18,-3,32,-35,-36,-39,-40,-41,-13,-14,-19,-7,-42,-37,-38,-42,-11,-15,72,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,73,-20,-8,-9,-42,76,-10,]),'ELSE':([3,4,5,6,7,12,14,15,20,21,23,24,25,28,29,30,32,47,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,76,],[-2,-42,-4,-5,-6,-12,-18,-3,-35,-36,-39,-40,-41,-13,-14,-19,-7,-37,-38,-42,-11,-15,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,74,-20,-8,-9,-10,]),'(':([9,10,12,18,19,22,27,34,35,36,37,38,39,40,41,42,43,44,45,46,53,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'NUMBER':([9,10,12,18,19,22,27,34,35,36,37,38,39,40,41,42,43,44,45,46,53,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'MINUS':([9,10,12,14,17,18,19,20,21,22,23,24,25,26,27,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[18,18,18,-18,35,18,18,-35,-36,18,-39,-40,-41,35,18,35,18,18,18,18,18,18,18,18,18,18,18,18,18,-37,35,-38,18,-21,-22,-23,-24,-25,35,35,35,35,35,35,35,35,-34,]),'NOT':([9,10,12,18,19,22,27,34,35,36,37,38,39,40,41,42,43,44,45,46,53,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'FALSE':([9,10,12,18,19,22,27,34,35,36,37,38,39,40,41,42,43,44,45,46,53,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'TRUE':([9,10,12,18,19,22,27,34,35,36,37,38,39,40,41,42,43,44,45,46,53,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'NIL':([9,10,12,18,19,22,27,34,35,36,37,38,39,40,41,42,43,44,45,46,53,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'=':([11,13,14,54,],[27,-16,-18,-17,]),',':([13,14,20,21,23,24,25,30,47,49,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[31,-18,-35,-36,-39,-40,-41,53,-37,-38,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,]),'PLUS':([14,17,20,21,23,24,25,26,30,47,48,49,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[-18,34,-35,-36,-39,-40,-41,34,34,-37,34,-38,-21,-22,-23,-24,-25,34,34,34,34,34,34,34,34,-34,]),'TIMES':([14,17,20,21,23,24,25,26,30,47,48,49,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[-18,36,-35,-36,-39,-40,-41,36,36,-37,36,-38,36,36,-23,-24,-25,36,36,36,36,36,36,36,36,-34,]),'DIVIDE':([14,17,20,21,23,24,25,26,30,47,48,49,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[-18,37,-35,-36,-39,-40,-41,37,37,-37,37,-38,37,37,-23,-24,-25,37,37,37,37,37,37,37,37,-34,]),'INTEGER_DIVIDE':([14,17,20,21,23,24,25,26,30,47,48,49,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[-18,38,-35,-36,-39,-40,-41,38,38,-37,38,-38,38,38,-23,-24,-25,38,38,38,38,38,38,38,38,-34,]),'LT':([14,17,20,21,23,24,25,26,30,47,48,49,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[-18,39,-35,-36,-39,-40,-41,39,39,-37,39,-38,-21,-22,-23,-24,-25,None,None,None,None,None,None,39,39,-34,]),'GT':([14,17,20,21,23,24,25,26,30,47,48,49,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[-18,40,-35,-36,-39,-40,-41,40,40,-37,40,-38,-21,-22,-23,-24,-25,None,None,None,None,None,None,40,40,-34,]),'LTE':([14,17,20,21,23,24,25,26,30,47,48,49,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[-18,41,-35,-36,-39,-40,-41,41,41,-37,41,-38,-21,-22,-23,-24,-25,None,None,None,None,None,None,41,41,-34,]),'GTE':([14,17,20,21,23,24,25,26,30,47,48,49,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[-18,42,-35,-36,-39,-40,-41,42,42,-37,42,-38,-21,-22,-23,-24,-25,None,None,None,None,None,None,42,42,-34,]),'EQUALS':([14,17,20,21,23,24,25,26,30,47,48,49,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[-18,43,-35,-36,-39,-40,-41,43,43,-37,43,-38,-21,-22,-23,-24,-25,None,None,None,None,None,None,43,43,-34,]),'NE':([14,17,20,21,23,24,25,26,30,47,48,49,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[-18,44,-35,-36,-39,-40,-41,44,44,-37,44,-38,-21,-22,-23,-24,-25,None,None,None,None,None,None,44,44,-34,]),'AND':([14,17,20,21,23,24,25,26,30,47,48,49,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[-18,45,-35,-36,-39,-40,-41,45,45,-37,45,-38,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,None,45,-34,]),'OR':([14,17,20,21,23,24,25,26,30,47,48,49,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[-18,46,-35,-36,-39,-40,-41,46,46,-37,46,-38,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,None,-34,]),'THEN':([14,20,21,23,24,25,26,47,49,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[-18,-35,-36,-39,-40,-41,50,-37,-38,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,]),')':([14,20,21,23,24,25,47,48,49,56,57,58,59,60,61,62,63,64,65,66,67,68,69,],[-18,-35,-36,-39,-40,-41,-37,69,-38,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'chunk':([0,],[1,]),'block':([0,8,33,50,74,],[2,16,55,70,75,]),'stat_list':([0,4,8,33,50,74,],[3,15,3,3,3,3,]),'stat':([0,4,8,33,50,74,],[4,4,4,4,4,4,]),'empty':([0,4,8,33,50,74,],[5,5,5,5,5,5,]),'varlist':([0,4,8,31,33,50,74,],[11,11,11,54,11,11,11,]),'var':([0,4,8,9,10,12,18,19,22,27,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,50,53,74,],[13,13,13,20,20,20,20,20,20,20,13,13,20,20,20,20,20,20,20,20,20,20,20,20,20,13,20,13,]),'exp':([9,10,12,18,19,22,27,34,35,36,37,38,39,40,41,42,43,44,45,46,53,],[17,26,30,47,48,49,30,56,57,58,59,60,61,62,63,64,65,66,67,68,30,]),'explist':([12,27,53,],[28,51,71,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> chunk","S'",1,None,None,None),
  ('chunk -> block','chunk',1,'p_chunk','parser.py',20),
  ('block -> stat_list','block',1,'p_block','parser.py',25),
  ('stat_list -> stat stat_list','stat_list',2,'p_stat_list','parser.py',30),
  ('stat_list -> empty','stat_list',1,'p_stat_list','parser.py',31),
  ('stat -> ;','stat',1,'p_stat_semi','parser.py',39),
  ('stat -> BREAK','stat',1,'p_stat_break','parser.py',44),
  ('stat -> DO block END','stat',3,'p_stat_do','parser.py',49),
  ('stat -> WHILE exp DO block END','stat',5,'p_stat_while','parser.py',54),
  ('stat -> IF exp THEN block END','stat',5,'p_stat_if','parser.py',59),
  ('stat -> IF exp THEN block ELSE block END','stat',7,'p_stat_if','parser.py',60),
  ('stat -> varlist = explist','stat',3,'p_stat_assign','parser.py',68),
  ('stat -> RETURN','stat',1,'p_stat_return','parser.py',73),
  ('stat -> RETURN explist','stat',2,'p_stat_return','parser.py',74),
  ('stat -> RETURN ;','stat',2,'p_stat_return','parser.py',75),
  ('stat -> RETURN explist ;','stat',3,'p_stat_return','parser.py',76),
  ('varlist -> var','varlist',1,'p_varlist','parser.py',86),
  ('varlist -> var , varlist','varlist',3,'p_varlist','parser.py',87),
  ('var -> IDENTIFIER','var',1,'p_var','parser.py',95),
  ('explist -> exp','explist',1,'p_explist','parser.py',100),
  ('explist -> exp , explist','explist',3,'p_explist','parser.py',101),
  ('exp -> exp PLUS exp','exp',3,'p_exp_binop','parser.py',109),
  ('exp -> exp MINUS exp','exp',3,'p_exp_binop','parser.py',110),
  ('exp -> exp TIMES exp','exp',3,'p_exp_binop','parser.py',111),
  ('exp -> exp DIVIDE exp','exp',3,'p_exp_binop','parser.py',112),
  ('exp -> exp INTEGER_DIVIDE exp','exp',3,'p_exp_binop','parser.py',113),
  ('exp -> exp LT exp','exp',3,'p_exp_binop','parser.py',114),
  ('exp -> exp GT exp','exp',3,'p_exp_binop','parser.py',115),
  ('exp -> exp LTE exp','exp',3,'p_exp_binop','parser.py',116),
  ('exp -> exp GTE exp','exp',3,'p_exp_binop','parser.py',117),
  ('exp -> exp EQUALS exp','exp',3,'p_exp_binop','parser.py',118),
  ('exp -> exp NE exp','exp',3,'p_exp_binop','parser.py',119),
  ('exp -> exp AND exp','exp',3,'p_exp_binop','parser.py',120),
  ('exp -> exp OR exp','exp',3,'p_exp_binop','parser.py',121),
  ('exp -> ( exp )','exp',3,'p_exp_group','parser.py',126),
  ('exp -> var','exp',1,'p_exp_var','parser.py',131),
  ('exp -> NUMBER','exp',1,'p_exp_numeral','parser.py',136),
  ('exp -> MINUS exp','exp',2,'p_exp_unop','parser.py',141),
  ('exp -> NOT exp','exp',2,'p_exp_unop','parser.py',142),
  ('exp -> FALSE','exp',1,'p_exp_bool','parser.py',147),
  ('exp -> TRUE','exp',1,'p_exp_bool','parser.py',148),
  ('exp -> NIL','exp',1,'p_exp_nil','parser.py',153),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',158),
]
