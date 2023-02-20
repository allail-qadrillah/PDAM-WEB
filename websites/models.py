import firebase_admin
from firebase_admin import credentials, firestore, storage, db
import random
import string
# import credentials file
cred = credentials.Certificate(
    {
        "type": "service_account",
        "project_id": "web-pdam",
        "private_key_id": "2be6fc49a20a6701b3c13728e173861168713227",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQD3VKKOUgZv9VoZ\nCUZ7eBSh/4CXxH3rOxEoPZmni1Dh5hvEMP1qBGOWQ8wbqab6vZ+HPd7Pq8IAyEGu\nxBbwM3FQrCbQnxOZhHCpRG+0LvgTllh/7GS46our0ewfySRxU6yJjwvy5lMLxIEK\nxyeU2bFgQVxbkcZgnihkaMzg5us8vpEisazoCFj70lGiYxerh5XA1BqqXGwwktHX\nbi/fMEw2cbWLGLtUkPCzPc+uXuB2uRwMQeDy+Ds8qD4/kNMdGS4mCTENIeYnMq4g\nkIu9F7RPG/3WDQPRknyQlR+d+aZV++vT9dVWV5Q5SdPrStzlDomIBi0Buh0FpJsH\nIIJ916HfAgMBAAECggEAHitT6YIGPf7oKW37tnuMd2xICSXolC/az7/1L75Aifr8\nf78tZ5K3JnEJAzDRE6cwv+74mvgLt0u2KLV2SiuEPX/E+6VZNIc2tOG1ByjEOE4a\nZ9RJPv3WjAlpwOt+B1gvuiyERnH48aexHpmcxufns+Lqe1L5/KFzh41PEc9Tz3n+\nrRXUUzQ8rwT1pPo2krfarWys3Bm7Y7LovzzvTwCR9qxrrI+YSxaxLUakuW8eh7mn\neCtifxt77/xjdSuCY7AQ04m74t5IsIqoFAm+jxVNYFbMFltve0bFLVa3nXo1+2iR\nmn58tbnZE5VWlxuYTCXUfiLTUysffSIplIVs/LWwSQKBgQD8u1ippbx/96FqTflm\nAzdGBUl/Fio1j13KGxK/CJoElqgoGQKBHucqpUUs6wZGfG1yqwrhMfFpJw/8+gc7\n1GPZQ+MZzZQiPWzrd/GZ3yo5kDPYQH2lzmQnQcIT5EBxEQ7J3XoVR4VliEBqmkke\nH7Eqbhg/1sdFKZVIJH/KZJKa6QKBgQD6h2iCcwXtpw1HGlkx6yS4aHIQOysVS63h\n+xnjMhTlV4/2odzFf/7ECyB9JNHLhHnKVmEt3NAXX4gUY5epzv0vqeHABMpymyu4\nCWVSLWSIbQR+w6mJFRcJqPEFaSBTFv9zG6TCoQLXxY5ICQSKI119YAdscdxTZGOb\nk+XxU0/JhwKBgFZ0dEEcfB4+hM5LvDwkb30Zg+ngmDHYSFpB5qjI9X8KVp3Y6F1p\nR+TzwnU6NNxZ5krqrf8ZSZ8SCMsecOkLn9iL+50xETKhVqg6UMC1ccldRg79CL52\nmxY+zXhmhZDoJ+nwRLoQzFZORNLy0n5mkwGTxeHYxDQppHKYYcrHmss5AoGAVMqh\nl40gk4e3mboUOC3ytqs6971e3o1Ho7Vd1KRtqBWTtxCfbQTeEDIH4/MjQnNq2Q2V\nRHV4xIBjySrP+PwCezBPJLM6ZcGY8WfUsBSG8xmarODCL5BAxNc2A/PJqfWdrbLM\nd8cQ9EB74GuU6r//c2CeApkizeKrR8utxpjA518CgYAI+AnWWeasfoUv+Su+IBUW\nfVRtYvDSXBYaJqslLziRzmCD5Tx3qH6hwYPySjm3CMY9xR9hzPIRENGn0stvTZtV\n/193Dy9uvNxVf42Y3nnzmGBaIj/1Bp6P4YrUATDMfXfMDFwhR5PQUFMp4cfbEyrt\nYdvf/aJ+Qm2yxvZp49dUgw==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-y66gk@web-pdam.iam.gserviceaccount.com",
        "client_id": "118209172272680803745",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-y66gk%40web-pdam.iam.gserviceaccount.com"
    }
)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://web-pdam-default-rtdb.asia-southeast1.firebasedatabase.app'
})

firestore = firestore.client()


class Firebase:

    def add_collection(self, collection, document, data):
        return firestore.collection(collection).document(document).set(data)

class User(Firebase):
    def __init__(self):
        self.user = 'user'
        self.username = str()
        self.golongan = str()
        self.bulan = int()


    def random_string(self, string_length=5):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(string_length))


    def add_user(self):
        kode_pelanggan = self.random_string().upper()
        return self.add_collection(self.user, kode_pelanggan, {
            'nama': self.username,
            'golongan': self.golongan,
            'bulan': self.bulan,
            'foto_profile': f"https://mdbootstrap.com/img/new/avatars/{random.randint(0, 25)}.jpg",
            "id_pelanggan": kode_pelanggan,
            'debit_pdam': 0,
            'pembayaran_pdam': 0,
            'debit_pelanggan': 0,
            'pembayaran_pelanggan': 0
        })


    def get_user(self, kode_pelangan=''):
        if kode_pelangan != '':
            data = firestore.collection(
                self.user).document(kode_pelangan).get()
            return data.to_dict()

        data = firestore.collection(self.user).get()
        return [each.to_dict() for each in data]
    

    def update_user(self, kode_pelanggan, data):
        firestore.collection(self.user).document(kode_pelanggan).update(data)


    def get_golongan(self, kode_pelanggan):
        user = self.get_user(kode_pelanggan)
        return user['golongan']


    def delete_user(self, id):
        return firestore.collection(self.user).document(id).delete()


    def get_pdam(self):
        return db.reference('/pdam').get()


    def get_pelanggan(self):
        return db.reference('/pelanggan').get()


    def get_pembayaran_pdam(self, kode_pelanggan):
        volume_air = self.get_pdam()
        golongan = self.get_golongan(kode_pelanggan)

        return "{:.3f}".format(self.count_pembayaran(golongan, volume_air))
    

    def get_pembayaran_pelanggan(self, kode_pelanggan):
        volume_air = self.get_pelanggan()
        golongan = self.get_golongan(kode_pelanggan)

        return "{:.3f}".format(self.count_pembayaran(golongan, volume_air))


    def count_pembayaran(self, golongan, volume_air):
        if golongan == "Rumah Tangga A":
            if volume_air >= 0 and volume_air <= 10:
                return (volume_air * 2.500) + 4.500 + 3.000
            else:
                return (volume_air * 3.500) + 4.500 + 3.000

        elif golongan == "Rumah Tangga B":
            if volume_air >= 0 and volume_air <= 10:
                return (volume_air * 3.000 ) + 4.500 + 3.000
            else:
                return (volume_air * 3.850) + 4.500 + 3.000

        elif golongan == "Rumah Tangga C":
            if volume_air >= 0 and volume_air <= 10:
                return (volume_air * 3.250 ) + 4.500 + 3.000
            else:
                return (volume_air * 4.200) + 4.500 + 3.000

        elif golongan == "Rumah Tangga D":
            if volume_air >= 0 and volume_air <= 10:
                return (volume_air * 3.500 ) + 4.500 + 3.000
            else:
                return (volume_air * 4.550) + 4.500 + 3.000

        elif golongan == "Niaga Kecil":
            if volume_air >= 0 and volume_air <= 10:
                return (volume_air * 3.500 ) + 4.500 + 3.000
            else:
                return (volume_air * 6.300) + 4.500 + 3.000

        elif golongan == "Niaga Menengah":
            if volume_air >= 0 and volume_air <= 10:
                return (volume_air * 3.850 ) + 4.500 + 3.000
            else:
                return (volume_air * 6.650) + 4.500 + 3.000

        elif golongan == "Niaga Besar":
            if volume_air >= 0 and volume_air <= 10:
                return (volume_air * 4.200 ) + 4.500 + 3.000
            else:
                return (volume_air * 7.000) + 4.500 + 3.000


    def __str__(self) -> str:
        return f'{self.username} {self.golongan} {self.bulan}'