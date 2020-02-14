import imapclient
import pyzmail
import pprint
import time
from datetime import datetime



def get_date(date_str: str):
    # Wed, 23 Oct 2019 05:56:53
    tmp = date_str.split(",")[-1]
    print(tmp)
    return datetime.strptime("23 Oct 2019 05:56:53", "%d %B %Y %H:%M:%S")


def get_unseen_mail(host: str, name: str, password: str) -> None:
    imap_obj = imapclient.IMAPClient(host, ssl=True)
    imap_obj.login(name, password)
    # show all foder ,each tuples's last element is  a full name
    # print(imap_obj.list_folders())
    imap_obj.select_folder("INBOX", readonly=True)
    ids = imap_obj.search(["SEEN"])
    raw_messages = imap_obj.fetch(ids, ["BODY[]"])
    # print(raw_messages[ids[0]])
    # time.sleep(3)
    # check each mail's content
    for _id in ids:
        message = pyzmail.PyzMessage.factory(raw_messages[_id][b"BODY[]"])
        if message.text_part != None:
            print(message.get_decoded_header("date", ""))
            time.sleep(3)
            #get_decoded_header('date', '')
            print("####################################################")
            content = message.text_part.get_payload().decode(message.text_part.charset)
            print(content)
            time.sleep(3)


if __name__ == "__main__":
    #get_unseen_mail(host, name, password)
    print(get_date("Wed, 23 Oct 2019 05:56:53"))
