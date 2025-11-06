# REVISÃO DEDICADA A CONDICIONAIS

# Temperatura dos servidores
# Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

temperatura_atual = float(input('Digite a temperatura atual do servidor '));

if temperatura_atual > 25:
    print('ALERTA! - A temperatura está elevada');
elif temperatura_atual <= 25:
    print('OK! - A temperatura está normal');
else:
    print('ERRO')