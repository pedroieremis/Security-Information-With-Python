import phonenumbers
from phonenumbers import geocoder

telefone = input('\nDigite o número de telefone para verificação da localização:\nFormato de exemplo: +5584996669204\n')
res = phonenumbers.parse(telefone)

print('\n'+geocoder.country_name_for_number(res, 'pt')+f' é o País de: {telefone}')
print(geocoder.description_for_number(res, 'pt')+f' é o estado de: {telefone}')
print(f'{telefone} é validado em: '+geocoder.description_for_valid_number(res, 'pt'))
