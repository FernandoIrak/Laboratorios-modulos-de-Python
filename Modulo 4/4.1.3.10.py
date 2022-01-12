def l100kmtompg(litros):
    millas = 100 * 1000 / 1609.344
    galones = litros / 3.785411784
    return millas / galones

def mpgtol100km(millas):
    litros = 3.785411784
    kilometros = millas * 1609.344 / 1000
    km100 = kilometros / 100
    return litros / km100

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))