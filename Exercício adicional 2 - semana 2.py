segundos_str = input('Por favor, entre com o número de segundos que deseja conveter:')
total_segs = int(segundos_str)

dia = total_segs / 86400
horas = total_segs / 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dia, 'dias',horas, 'horas,', minutos, 'minutos e',segs_restantes_final, 'segundos.')






