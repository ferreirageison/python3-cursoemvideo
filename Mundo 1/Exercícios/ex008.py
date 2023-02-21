# conversor de medidas
medida = int(input('Digite uma medida em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {}metros equivale a \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(
medida, km, hm, dam, dm, cm, mm))
