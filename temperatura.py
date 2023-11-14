def celcius_a_fahrenheit(celcius):
    return (celcius *9/5)+32

def mcelcius_a_kelvin(celcius):
    return celcius + 273.15

if __name__=='__main__':
    celcius=50
    fahrenheit=celcius_a_fahrenheit(celcius)
    print(f'{celcius} grados celcius son equivalentes a {fahrenheit} grados fahrenheit')