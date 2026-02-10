import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from src.flat_file.user import User
from src.flat_file.flat_file_loader import Flat_file_loader

class Data_handler:
    users = []
    # En 16-byte nøgle til AES-128
    KEY = b'DetteErEnSikkerK' 

    def __init__(self, flat_file_name = "users.json"):
        self.flat_file_loader = Flat_file_loader(flat_file_name)
        self.users = self.flat_file_loader.load_memory_database_from_file()

    def _encrypt(self, text: str) -> str:
        """Hjælpefunktion til AES-128 kryptering."""
        cipher = AES.new(self.KEY, AES.MODE_ECB)
        ct_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
        return base64.b64encode(ct_bytes).decode()

    def _decrypt(self, s_encrypted: str) -> str:
        """Hjælpefunktion til AES-128 dekryptering."""
        try:
            cipher = AES.new(self.KEY, AES.MODE_ECB)
            decoded = base64.b64decode(s_encrypted)
            return unpad(cipher.decrypt(decoded), AES.block_size).decode()
        except:
            return s_encrypted # Returner original hvis den ikke er krypteret

    def _save(self):
        # Inden vi gemmer, krypteres de følsomme felter (GDPR)
        for u in self.users:
            u.first_name = self._encrypt(u.first_name)
            u.last_name = self._encrypt(u.last_name)
            u.address = self._encrypt(u.address)
        
        self.flat_file_loader.save_memory_database_to_file(self.users)
        
        # Efter gem, dekrypterer vi dem i RAM igen, så de kan bruges
        for u in self.users:
            u.first_name = self._decrypt(u.first_name)
            u.last_name = self._decrypt(u.last_name)
            u.address = self._decrypt(u.address)

    def get_number_of_users(self):
        return len(self.users)

    def get_user_by_id(self, user_id: int):
        for user in self.users:
            if user.person_id == user_id:
                return user
        return None
    
    def create_user(self, first_name, last_name, address, street_number, password):
        userId = len(self.users)
        hashed_pw = hashlib.sha256(password.encode()).hexdigest()
        user = User(userId, first_name, last_name, address, street_number, hashed_pw, True)
        self.users.append(user)
        self._save() # Krypterer og gemmer

    def disable_user(self, user_id:int):
        user = self.get_user_by_id(user_id)
        if user:
            user.enabled = False
            self._save()