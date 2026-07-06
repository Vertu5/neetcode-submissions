class MyHashSet:
    def __init__(self):
        # Utilisation d'un nombre premier pour minimiser les collisions
        self.taille = 2069 
        self.buckets = [[] for _ in range(self.taille)]

    def _hash(self, key: int) -> int:
        """La fonction de hachage qui convertit la clé en index de seau"""
        return key % self.taille

    def add(self, key: int) -> None:
        index_seau = self._hash(key)
        
        if key not in self.buckets[index_seau]:
            self.buckets[index_seau].append(key)

    def remove(self, key: int) -> None:
        index_seau = self._hash(key)
        
        if key in self.buckets[index_seau]:
            self.buckets[index_seau].remove(key)

    def contains(self, key: int) -> bool:
        index_seau = self._hash(key)
        return key in self.buckets[index_seau]