# Ceará 
SELECT DISTINCT municipio, COUNT(municipio), mes , ano, AVG(tempo_atracado), AVG(tempo_estadia) FROM Antaq.Atracacao_fato  WHERE regiao_geografica = 'Nordeste' GROUP BY municipio, mes, ano; 

# Nordeste 
SELECT DISTINCT municipio, COUNT(municipio), mes , ano, AVG(tempo_atracado), AVG(tempo_estadia) FROM Antaq.Atracacao_fato  WHERE regiao_geografica = 'Nordeste' GROUP BY municipio, mes, ano; 

# Brasil 
SELECT DISTINCT municipio, COUNT(municipio), mes , ano, AVG(tempo_atracado), AVG(tempo_estadia) FROM Antaq.Atracacao_fato  WHERE regiao_geografica = 'Nordeste' GROUP BY municipio, mes, ano; 

