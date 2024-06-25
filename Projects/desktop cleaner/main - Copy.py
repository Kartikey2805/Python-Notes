from pathlib import Path
import os
from datetime import datetime


def desktop_clean():

    current_dir_path = Path(__file__).resolve().parent

    file_types_dict = {'json':'JSON','py':'Python','js':'JS','txt':'TXT'}

    # first time folder creation 
    if not Path.exists(Path.joinpath(current_dir_path,'JSON')):
        Path.mkdir('JSON')
    if not Path.exists(Path.joinpath(current_dir_path,'Python')):
        Path.mkdir('Python')
    if not Path.exists(Path.joinpath(current_dir_path,'JS')):
        Path.mkdir('JS')
    if not Path.exists(Path.joinpath(current_dir_path,'TXT')):
        Path.mkdir('TXT')
    
    for file in Path.iterdir(current_dir_path):
        if file.is_file() and file.name != 'main.py':
            filename = file.name
            filetype = filename.split('.')[1]
            # filename = file.suffix
            # filetype = file.stem

            start_date_time = datetime.now()       
            
            try: 
                if filetype in file_types_dict:
                    newPath = Path.joinpath(current_dir_path,file_types_dict[filetype],filename)
                    print(newPath)
                    print(f"[{start_date_time}] : Starting moving file {filename} to {file_types_dict[filetype]}")     
                    Path.rename(file,newPath)
                else:
                    print(f"[{start_date_time}] : Found a new file type: {filetype}, moving it to Unidentified Folder")
                    newPath = Path.joinpath(current_dir_path,'Unidentified',filename)
                    Path.rename(file,newPath)

                # calculating end time and total time elapsed 
                end_date_time = datetime.now()
                time_elapsed = (end_date_time - start_date_time).seconds
                print(f"File transmission ended, total time taken: {time_elapsed}")

            except Exception as err:
                print(err)


if __name__ == '__main__':
    desktop_clean()