import os
import shutil
import pandas as pd
from dbfread import DBF

def convert_dbf_to_csv(input_file, output_file, encoding='latin1'):
    table = DBF(input_file, encoding=encoding)
    df = pd.DataFrame(iter(table))
    if not df.empty:
        df.to_csv(output_file, index=False)
        return True
    return False

def scan_and_convert(base_directory, output_directory, data_output_directory, encoding='latin1'):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    if not os.path.exists(data_output_directory):
        os.makedirs(data_output_directory)
    
    for root, dirs, files in os.walk(base_directory):
        print(f"Visiting directory: {root}")
        for file in files:
            print(f"Found file: {file}")
            if file.lower().endswith('.dbf'):
                input_file = os.path.join(root, file)
                output_file = os.path.join(output_directory, os.path.splitext(file)[0] + '.csv')
                data_output_file = os.path.join(data_output_directory, os.path.splitext(file)[0] + '.csv')
                print(f"Converting {input_file} to {output_file}")
                try:
                    if convert_dbf_to_csv(input_file, output_file, encoding):
                        shutil.move(output_file, data_output_file)
                        print(f"Successfully converted {input_file} to {data_output_file}")
                    else:
                        print(f"No data in {input_file}, skipping conversion")
                except UnicodeDecodeError as e:
                    print(f"Error converting {input_file}: {e}")
                except Exception as e:
                    print(f"Unexpected error converting {input_file}: {e}")

# Execute o script no diretório base
base_directory = '.'
output_directory = os.path.join(base_directory, 'converted_csv_files')
data_output_directory = os.path.join(base_directory, 'data_converted_csv_files')
scan_and_convert(base_directory, output_directory, data_output_directory)