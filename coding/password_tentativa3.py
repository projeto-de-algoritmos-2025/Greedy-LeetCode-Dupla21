import re


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        missing_types = 0
        if not re.search(r'[a-z]', password):
            missing_types += 1
        if not re.search(r'[A-Z]', password):
            missing_types += 1
        if not re.search(r'[0-9]', password):
            missing_types += 1

        replaces = 0

        one_seq = 0
        two_seq = 0

        i = 0
        while i < n:
            length = 1
            j = i + 1
            while j < n and password[j] == password[i]:
                length += 1
                j += 1

            if length >= 3:
                replaces += length // 3

                if length % 3 == 0:
                    one_seq += 1
                elif length % 3 == 1:
                    two_seq += 1

            i = j

        if n < 6:
            return max(6 - n, missing_types)

        elif n <= 20:
            return max(replaces, missing_types)

        else:
            deletes = n - 20

            can_delete = min(one_seq, deletes)
            replaces -= can_delete
            deletes -= can_delete

            can_delete = min(two_seq * 2, deletes)
            replaces -= can_delete // 2
            deletes -= can_delete

            replaces -= deletes // 3

            return (n - 20) + max(replaces, missing_types)