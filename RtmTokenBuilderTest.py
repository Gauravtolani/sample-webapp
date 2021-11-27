import sys
import unittest
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RtmTokenBuilder import RtmTokenBuilder, Role_Rtm_User
from AccessToken import AccessToken, kRtmLogin

appID = "645930a984ae45c5831d9ecc05e5e675"
appCertificate = "cd34943caaf94047b61dd018de702a72"
userAccount = "test_user"
expireTimestamp = 1446455471
salt = 1
ts = 1111111


def test():
    token = RtmTokenBuilder.buildToken(appID, appCertificate, userAccount, Role_Rtm_User, expireTimestamp, channel)
    parser = AccessToken()
    parser.fromString(token)
    print(parser.messages[kRtmLogin])
    return parser.messages[kRtmLogin]
    # self.assertEqual(parser.messages[kRtmLogin], expireTimestamp)


# if __name__ == "__main__":
#     # unittest.main()
#     test()