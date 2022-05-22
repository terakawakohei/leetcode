class Solution:
    def defangIPaddr(self, address: str) -> str:
        return str.replace(".", "[.]")


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))
