from re import compile, finditer
import pathlib as Path
import sys
import os
import shutil

path = sys.argv[1]
# p = Path(root)
extensions = {
"images":['.jpeg', '.png', '.jpg', '.svg'],
"video":['.avi', '.mp4', '.mov', '.mkv'],
"documents":['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
"music":['.mp3', '.ogg', '.wav', '.amr'],
"archives":['.zip', '.gz', '.tar'],
"others":[]
}

def create_dirs(path):
    os.mkdir(f"{path}/images")
    os.mkdir(f"{path}/video")
    os.mkdir(f"{path}/documents")
    os.mkdir(f"{path}/music")
    os.mkdir(f"{path}/archives")
    os.mkdir(f"{path}/others")
try:
    create_dirs(path)
except FileExistsError:
    pass


        

def sorter(path):
    all = os.listdir(path)
    for x in all:
        name, ext = os.path.splitext(x)
        # ext = x.split(".")[-1]
        # name = x.split("\\")[-1]
        if x in all:
            if not os.path.isdir(x):
                for key, val in extensions.items():
                    if ext in val:
                        os.rename(f"{path}\\{x}", f"{path}\\{key}\\{x}")
                    else:
                        if x == "sort.py":
                            pass
            elif x in extensions.keys():
                pass
            elif os.path.isdir(x):
                os.rename(f"{path}\\{x}", f"{path}\\others\\{x}")
                
# def unpack_arch(path):
#     way = [i for i in os.listdir(f"{path}\\archives\\")]
#     for each in way:
#         name, ext = os.path.splitext(each)
#         shutil.unpack_archive(each, f"{path}\\archives\\{name}")
            
# unpack_arch(path)   




# sorter(path)   

def normalize(path):
    table = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g',
        'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh', 'з': 'z',
        'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k',
        'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
        'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
        'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ь': '', 'ю': 'iu', 'я': 'ia', 'А': 'A', 'Б': 'B',
        'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E',
        'Є': 'IE', 'Ж': 'ZH', 'З': 'Z', 'И': 'Y', 'І': 'I',
        'Ї': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
        'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S',
        'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS',
        'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ь': '', 'Ю': 'IU',
        'Я': 'IA', ' ': ' ', '/':'/', '~':'~', 'w':'w'
    }
    text = ''
    # directory, filename = os.path.split(path)
    for i in path:
        if i not in table.values():
            if i in table.keys():
                text+=table[i]
            elif '0'<=i<='9':
                text+=i
            else:
                text+='_'
        else:
            text+=i
    return os.rename(f'{path}', f'{text}')
    # trans = ''.join(table.get(i, i) for i in filename)
    # return os.path.join(directory, trans)
    # for i in path:
    #     if i in table:
    #         text += table[i]
    #         print(text)
    #     else:
    #         text += i +'/'
    # print(text)
normalize(path)
    





# def normalize(name):
#     full = ""
#     data = {
#         'а': 'a',
#         'б': 'b',
#         'в': 'v',
#         'г': 'h',
#         'ґ': 'g',
#         'д': 'd',
#         'е': 'e',
#         'є': 'ie',
#         'ж': 'zh',
#         'з': 'z',
#         'и': 'y',
#         'і': 'i',
#         'ї': 'i',
#         'й': 'i',
#         'к': 'k',
#         'л': 'l',
#         'м': 'm',
#         'н': 'n',
#         'о': 'o',
#         'п': 'p',
#         'р': 'r',
#         'с': 's',
#         'т': 't',
#         'у': 'u',
#         'ф': 'f',
#         'х': 'kh',
#         'ц': 'ts',
#         'ч': 'ch',
#         'ш': 'sh',
#         'щ': 'shch',
#         'ь': '',
#         'ў': 'u',
#         'ы': 'y',
#         'э': 'e',
#         'ю': 'iu',
#         'я': 'ia'
#     }
#     word = compile(r'[^a-zA-Z0-9]')
#     name = ''.join([data.get(i, i) for i in name])
#     name = word.sub('_', name)
#     return name
# a = input()       
# result = normalize(a)
# print(result)



# def read_files_and_folders(path):
#     for item in os.listdir(path):
#         item_path = os.path.join(path, item)
#         if os.path.isfile(item_path):
#             print(item_path)
#         elif os.path.isdir(item_path):
#             print(item_path)
#             read_files_and_folders(item_path)
# res = read_files_and_folders(path)
# print(res)




