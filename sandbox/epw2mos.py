import sys

def epw_to_mos(epw_path, mos_path, location_name="MyWeather"):
    with open(epw_path, 'r', encoding='latin-1') as f:
        lines = f.readlines()

    header = lines[0].strip().split(",")
    location = header[1] if len(header) > 1 else location_name

    with open(mos_path, 'w', encoding='latin-1') as f:
        f.write(f'within;\n')
        f.write(f'block {location_name}\n')
        f.write(f'  extends Modelica.WeatherData.BaseClasses.WeatherDataFile;\n')
        f.write(f'end {location_name};\n')

        f.write('\n')

        f.write(f'annotation (experiment(StopTime=31536000));\n')
        f.write('\n')

        f.write('// Weather data converted from .epw\n')
        for line in lines[8:]:
            f.write(line)

    print(f"✅ Arquivo .mos gerado: {mos_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python epw2mos.py input.epw output.mos LocationName")
    else:
        epw_to_mos(sys.argv[1], sys.argv[2], sys.argv[3])