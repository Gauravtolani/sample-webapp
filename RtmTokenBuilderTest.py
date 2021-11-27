import sys
import unittest
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RtmTokenBuilder import RtmTokenBuilder, Role_Rtm_User
from AccessToken import AccessToken, kRtmLogin

appID = "645930a984ae45c5831d9ecc05e5e675"
appCertificate = "cd34943caaf94047b61dd018de702a72"
# userAccount = "gaurav"
expireTimestamp = 1446455471
salt = 1
ts = 1111111


def test(userAccount):
    token = RtmTokenBuilder.buildToken(appID, appCertificate, userAccount, Role_Rtm_User, expireTimestamp)
    parser = AccessToken()
    parser.fromString(token)
    print(token)
    # print(parser.messages[kRtmLogin])
    return token
    # self.assertEqual(parser.messages[kRtmLogin], expireTimestamp)


# if __name__ == "__main__":
#     # unittest.main()
#     test('gaurav')