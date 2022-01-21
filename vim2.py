import imaplib
import email

################ IMAP SSL ##############################

with imaplib.IMAP4_SSL(host="imap.gmail.com", port=imaplib.IMAP4_SSL_PORT) as imap_ssl:
    print("Connection Object : {}".format(imap_ssl))

    ############### Login to Mailbox ######################
    print("Logging into mailbox...")
    resp_code, response = imap_ssl.login("yeboahd24@gmail.com", 'iwtdhqayqfpydlbw')
    print("Response Code : {}".format(resp_code))
    print("Response      : {}\n".format(response[0].decode()))

    ############### Set Mailbox #############
    resp_code, mail_count = imap_ssl.select(mailbox="[Gmail]/Spam", readonly=False)

    ############### Retrieve Mail IDs for given Directory #############
    resp_code, mails = imap_ssl.search(None, "ALL")
    print("Mail IDs : {}\n".format(mails[0].decode().split()))

    ################## Copy Messages to new mailbox ###################
    print("\nCopying few mails of spam to different directory....")
    mail_ids =  mails[0].decode().split()[-2:]
    mail_ids = ":".join(mail_ids)
    print(mail_ids)

    resp_code, response = imap_ssl.copy(mail_ids, "INBOX")
    print("Response Code : {}".format(resp_code))
    print("Response      : {}".format(response[0].decode()))

    ################## Copy Messages to new mailbox ###################
    print("\nCopying few mails of spam to different directory....")
    mail_ids =  mails[0].decode().split()[:2]

    for mail_id in mail_ids:
        resp_code, response = imap_ssl.copy(mail_id, "INBOX")
        print("Response Code : {}".format(resp_code))
        print("Response      : {}".format(response[0].decode()))

    ############# Close Selected Mailbox #######################
    print("\nClosing selected mailbox....")
    imap_ssl.close()
