import re
import sys

from skpy import Skype


class SkypeApi:
    def __init__(self, login, passw):
        self.skype = Skype(login, passw)

    def get_chats(self):
        return self.skype.chats.recent()

    def get_chat_ID_by_topic(self, name):
        for chat in self.skype.chats.recent().values():
            if hasattr(chat, 'topic') and chat.topic == name: return chat

    def get_all_messages(self, name):
        messages = []
        chat = self.get_chat_ID_by_topic(name)
        self.__get_all_messages(chat, messages)
        return messages

    @staticmethod
    def __get_all_messages(chat, list_):
        last_len = 0
        while 1:
            list_.extend(chat.getMsgs())
            if last_len == len(list_):
                break
            else:
                last_len = len(list_)

    def get_links(self, name):
        links = []
        for msg in self.get_all_messages(name):
            match = re.search(r'href=[\'"]?([^\'" >]+)', msg.content)
            if match:
                links.append(match.group(1))
        return links


def write_to_file_no_duplicates(path, elements):
    with (open(path, 'a')) as f1, (open(path, 'r')) as f2:
        for ele in elements:
            in_file = [line.strip() for line in f2.readlines()]
            # print("if %s not in %s " %(ele,list))
            if ele not in in_file:
                f1.write(ele + '\n')
            f2.seek(0)


if __name__ == '__main__':
    # "Learning is an awesome journey"
    user = sys.argv[1]
    passw = sys.argv[2]
    chat = sys.argv[3]
    sa = SkypeApi(user, passw)
    links = sa.get_links(chat)
    write_to_file_no_duplicates("links.txt", links)
