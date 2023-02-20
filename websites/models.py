import firebase_admin
from firebase_admin import credentials, firestore, storage, db
import random
import string
# import credentials file
cred = credentials.Certificate(
        {
            "type": "service_account",
            "project_id": "web-pdam-4834f",
            "private_key_id": "a730cb49767938bacf712488945a83c535a42781",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC88OgYXUaDCmqY\nbE/8ghYqessx7LqX8kc9Q1UD3lVE4A0nu9bbVtiV+4XDs+rECMzCM1gRRjiPyNyl\nKhj8NtR4DL86LlbJhksnlWXhWRRegJtm3hZ10BzRLinGqm8g0jnoe953zyo7bCIx\nzJFWy+fQ0W4kfTPqz+no3YBk4XbKdWBqF3thBcUs9x14TraxH3CBMMB8VTaN8xfB\nyOSIWs4yx2bEs2rbbdeP/FDSyMGlkRbGj64/sAdR5b84SgwQyHmndbMISfpVJYCH\n0EnOvuxaINMPd1YAilSxvXcGpbm9BFHBvLS5/XeMXjlr4A96mY7F4qSnJ+sp2EwR\n6CSwF4zBAgMBAAECggEAPbPk8BQCE4hi0F1K79kh2QSZ+DdppnaaWkDzchx5N1F+\nKlQ3MhFWEQD/qa5HhHalO+SdpaKLlTVRDWVGnJNhZsUu7Ba3BAAl6grppyK6urQA\nTCNKLXZl+tA7F2SQfyT4gVp2iCTxE0/YiO/YJQLZNUI32JXEzzHQH1q68/cHns0O\nC/aUAsLJjdIPnozY2pFlNZ0QWMZreRdKKrumkTSxUAqHuw/kvhtbm2tBppfzh/H5\nJzeuuGr7awbKAOwswkPVSdicvLqbWVhQ5O2hhnMR6U18uoim1I2C/+v0aoFmxS4S\no6hHKhz1ZLap+BwaWG02sGY9ASYsaHAGKAvzLnwQcwKBgQD/VG11KnmiUnkmqzxl\nxyebKx0OtmWJ8VRaa1Iqr1HA0juXStIq0Dfrh6qVis8VLR5YeM/ona4XTjoVsZb7\nkI0uzZwOCPAODZ94Jj4ec18Mo9FzuvUxrn9n8faFXrGZbpncSmjsgQiF6hpf7iYj\nzFeKIMzLyr6R8YBVBe4ob9qnAwKBgQC9b95CXKuUE7ywfd7oa/czumR1AZJZkJ6t\nPNhTcANDRw8EC2eSLnWKig1iYx0z+XMtxJ2eE21qxCj0o91hjoxPoiFJBgiRW1RR\nrTOTGgLjls+3RMx5+/pEpyZG3kcV/qkKyAAuahqfJCg/MzgNXn5osXEwq22eNIE/\ngEMgH5e/6wKBgG+gjaonw72/qM/LFUC57Qrdsnp4K7Q/Gc3eFbIrq+ZNA1iFkZS+\nK3SBf4aZhSeQ7i9nwh3EshPmU2agmY2qCM9pfMx2A91g/1McBRRzBB8Wj7+1APWT\ngIgFNO3iFGsr+4Bf17duQjepvZYrG+mSsMLmzCJcpSxRFPYW/aQYItPZAoGBALO4\nENVGk6TdALM0ByjbXN/fYnS68/wyvsc9pUGrT/0gyfcdVroRh4PSqxX/T/JCIup1\n0M7qQXD7/prxZxKpqSXXe9qKddBpI9qFBhv1nm4KYq/M/mxwCKPfK+op8KjGO9s1\nmS5vjSgTpncnAXN1hVmPlgIFcO6Zg1EaPxSXxGDXAoGARemRWe0PLwA5lbq2l1vA\nBHpPwsKlcnFL2iJ0H50MCvuq/3zdWMnulESlZgwSEG8w0DJfg4q0PZTkIQHP/Tkb\nG/Wmij2YtMICiSBKnAF+RQ1b1EbTUH6kK4hvBPzFp/qku6YKKxiOQpali2Um2PEt\nRmcvMu6EIptEcWgtozR/ab4=\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-zk59n@web-pdam-4834f.iam.gserviceaccount.com",
            "client_id": "111821251321717113701",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-zk59n%40web-pdam-4834f.iam.gserviceaccount.com"
        }
)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://web-pdam-4834f-default-rtdb.asia-southeast1.firebasedatabase.app'
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
    