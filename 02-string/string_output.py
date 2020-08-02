'''
File: string_output.py
Project: 02-string
===========
File Created: Wednesday, 22nd July 2020 10:55:31 pm
Author: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Last Modified: Wednesday, 22nd July 2020 10:55:37 pm
Modified By: <<LanLing>> (<<lanlingrock@gmail.com>>)
===========
Description: 指定宽度输出字符串
Copyright <<2020>> - 2020 Your Company, <<XDU>>
'''
import os
import textwrap


s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."


print(textwrap.fill(s, 40, initial_indent='    '))


# 按照终端的宽度进行输出
width = os.get_terminal_size().columns
print(textwrap.fill(s, width, initial_indent='    '))
