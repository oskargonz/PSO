import matplotlib.pyplot as plt
import numpy as np
import math

from scipy.io import wavfile
from scipy.io.wavfile import write
samplerate, data = wavfile.read('Struna 6 - E.wav') #Plik mono!!!!!


print ("Częstotliwość próbkowania ......... " + str(samplerate) + " Hz")
print ("Liczba próbek ..................... " + str(len(data)))

okres_probkowania = 1 / samplerate

print ("Okres próbkowania ................. " + str(okres_probkowania) + " s")

czas_trwania_nagrania = len(data) * okres_probkowania

print ("Czas trwania nagrania ............. " + str(czas_trwania_nagrania) + " s")

amplituda = data.max()
minimum = data.min()
print ("Amplituda ......................... " + str(amplituda))
print ("Minimum ........................... " + str(minimum))



ile_przesunac = float(input("O ile czasu przesunąć sygnał? [s]"))

liczba_probek = int(ile_przesunac/okres_probkowania)

ile_wzmocnic = float(input("O ile wzmocnic drugi sygnał?"))

print("Aby przesunąć sygnał o czas: " + str(ile_przesunac) + " należy wstawić " + str(liczba_probek) + " próbek")

data_wzmocnione = np.int16(data * ile_wzmocnic)
data_mix = []

liczba_probek_wzmocnione = len(data) + liczba_probek

energia_wzmocniona = 0.0
energia_poczatkowa = 0.0
power_wzmocnione = 0.0
power_poczatkowe = 0.0

for i in range(liczba_probek_wzmocnione):
    if i < liczba_probek:
        data_mix.append(data[i])
        energia_wzmocniona = energia_wzmocniona + (abs(data[i]) ** 2) / 2 ** 15
        energia_poczatkowa = energia_poczatkowa + (abs(data[i]) ** 2) / 2 ** 15
    elif i >= len(data):
        data_mix.append(data_wzmocnione[i - liczba_probek])
        energia_wzmocniona = energia_wzmocniona + (abs(data_wzmocnione[i - liczba_probek]) ** 2) / 2 ** 15
    else:
        data_mix.append(np.int16(data[i] + data_wzmocnione[i - liczba_probek]))
        energia_wzmocniona = energia_wzmocniona + ((abs(data[i]) + abs(data_wzmocnione[i - liczba_probek])) ** 2) / 2 ** 15
        energia_poczatkowa = energia_poczatkowa + (abs(data[i]) ** 2) / 2 ** 15

power_wzmocnione = energia_wzmocniona / liczba_probek_wzmocnione
power_poczatkowe = energia_poczatkowa / len(data)
data_mix = np.array(data_mix)
     
data_x = range(len(data_mix))

plt.plot(data_x, data_mix)

plt.show()

decybele_wzmocnione = 10 * math.log10(power_wzmocnione)
decybele_poczatkowe = 10 * math.log10(power_poczatkowe)

print("\nEnergia sygnału poczatkowego: " + str(energia_poczatkowa))
print("Energia sygnału wzmocnionego: " + str(energia_wzmocniona))
print("\nMoc sygnału poczatkowego: " + str(power_poczatkowe))
print("Moc sygnału wzmocnionego: " + str(power_wzmocnione))

print("\nPoziom sygnału przed efektem .................... " + str(decybele_poczatkowe) + " dB")
print("Poziom sygnału po efekcie ....................... " + str(decybele_wzmocnione) + " dB")



write("oskar_gasior.wav", samplerate, data_mix)


        







