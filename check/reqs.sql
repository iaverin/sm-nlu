

select m.message_id, m."timestamp", m.content->>'text' from message m, sender s 
where 

m.timestamp >='2021-08-15 00:00:00' and m.timestamp <='2021-08-15 23:59:59' and  
m.sender_id  = s.sender_id and s.type_id = 0

order by m.timestamp desc 
 



select * from message m  where "content" ->>'text'='Хорошо , запишите тогда мой номер телефона +79271660870 Евгений. Как будет обратная связь можете связаться со мной и мы заказжем'

select * from message m  where "content" ->>'text'='Я делал заказ, срок уже давно прошел, деталь не пришла и никто не может сказать когда она придет. Где я могу получить информацию о том где мой заказ?'

select * from message m  where "content" ->>'text'='ZZV500011658'
ZZV500011658

select * from message m  where m.timestamp >='2021-08-15 00:00:00' and m.timestamp <='2021-08-15 23:59:59' and "content" ->>'text'='мне нужно забрать заказ не из моего пункта выдачи. Как то я могу заказать в зал на Рокоссовского?'   

select * from message m where dialog_id = 951214 order by m."timestamp" asc

select * from message m where sender_id = 950630 order by m."timestamp" asc