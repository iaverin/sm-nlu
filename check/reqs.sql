

select m.message_id, m."timestamp", m.content->>'text' from message m, sender s 
where 

m.timestamp >='2021-08-15 00:00:00' and m.timestamp <='2021-08-15 23:59:59' and  
m.sender_id  = s.sender_id and s.type_id = 0

order by m.timestamp desc 
 



select * from message m  where "content" ->>'text'='������ , �������� ����� ��� ����� �������� +79271660870 �������. ��� ����� �������� ����� ������ ��������� �� ���� � �� ��������'

select * from message m  where "content" ->>'text'='� ����� �����, ���� ��� ����� ������, ������ �� ������ � ����� �� ����� ������� ����� ��� ������. ��� � ���� �������� ���������� � ��� ��� ��� �����?'

select * from message m  where "content" ->>'text'='ZZV500011658'
ZZV500011658

select * from message m  where m.timestamp >='2021-08-15 00:00:00' and m.timestamp <='2021-08-15 23:59:59' and "content" ->>'text'='��� ����� ������� ����� �� �� ����� ������ ������. ��� �� � ���� �������� � ��� �� �������������?'   

select * from message m where dialog_id = 951214 order by m."timestamp" asc

select * from message m where sender_id = 950630 order by m."timestamp" asc