tc = float(input('Qual a temperatura (°C) '))
tk = tc + 273.15
tf = (tc * 1.8) + 32
# 'ou tf = (9 * tc) /5 + 32'
# 'ou tf = 9 * tc / 5 + 32'
print('A temperatura de {:.1f} °C equivale a {:.2f} °K e a {:.1f} °F'.format(tc, tk, tf))
