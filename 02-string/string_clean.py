'''
File: string_clean.py
Project: 02-string
===========
File Created: Wednesday, 22nd July 2020 10:35:04 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Wednesday, 22nd July 2020 10:35:08 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Description: 文本清理
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''

s = 'pýtĥöñ\fis\tawesome\r\n'

remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None,
    ord('\n') : None
}

a = s.translate(remap)
print(a)
