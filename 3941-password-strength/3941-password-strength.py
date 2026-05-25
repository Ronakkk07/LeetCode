class Solution:
    def passwordStrength(self, password: str) -> int:
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        special_characters = ['!', '@', '#', '$']
        points = 0
        unique = "".join(dict.fromkeys(password))
        for passwd in unique:
            if ord(passwd) >= 97 and ord(passwd) <= 122:
                points += 1
            elif ord(passwd) >= 65 and ord(passwd) <= 90:
                points += 2
            elif passwd in digits:
                points += 3
            else:
                points += 5
        return points  